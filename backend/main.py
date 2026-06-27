import os
import json
import random
from pathlib import Path
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai import OpenAI
from dotenv import load_dotenv

from knowledge_base import (
    RACES, CLASSES, MONSTERS, MAGIC_ITEMS, SPELLS,
    LOCATIONS, QUESTS, NPC_ROLES, PLOT_TWISTS,
    MORAL_DILEMMAS, FACTIONS, EVENTS,
)

load_dotenv()

API_BASE = os.getenv("API_BASE", "http://localhost:11434/v1")
API_MODEL = os.getenv("API_MODEL", "llama3.2")
API_KEY = os.getenv("API_KEY", "ollama")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

client = OpenAI(base_url=API_BASE, api_key=API_KEY)


class QuestRequest(BaseModel):
    genre: str
    difficulty: str


def _pick(d: dict, n: int) -> list:
    items = list(d.items())
    random.shuffle(items)
    return items[:n]


def _build_context(genre: str, difficulty: str) -> str:
    difficulty_mult = {"easy": 1, "medium": 2, "hard": 3}

    sample_races = _pick(RACES, 3)
    sample_classes = _pick(CLASSES, 3)
    sample_monsters = _pick(MONSTERS, 4 * difficulty_mult.get(difficulty, 2))
    sample_items = _pick(MAGIC_ITEMS, 3)
    sample_spells = _pick(SPELLS, 3)
    sample_locations = _pick(LOCATIONS, 4)
    sample_quests = random.sample(QUESTS, min(5, len(QUESTS)))
    sample_npcs = random.sample(NPC_ROLES, min(4, len(NPC_ROLES)))
    sample_twists = random.sample(PLOT_TWISTS, min(3, len(PLOT_TWISTS)))
    sample_dilemmas = random.sample(MORAL_DILEMMAS, min(2, len(MORAL_DILEMMAS)))
    sample_factions = random.sample(FACTIONS, min(3, len(FACTIONS)))
    sample_events = random.sample(EVENTS, min(2, len(EVENTS)))

    ctx = []

    ctx.append("=== D&D RACES (sample) ===")
    for name, data in sample_races:
        ctx.append(f"- {name.title()}: {data['description']} Traits: {', '.join(data['traits'])}")

    ctx.append("\n=== D&D CLASSES (sample) ===")
    for name, data in sample_classes:
        ctx.append(f"- {name.title()}: {data['description']} (HD: d{data['hit_die']}, Primary: {data['primary_ability']})")

    ctx.append("\n=== MONSTERS / ENEMIES (sample) ===")
    for name, data in sample_monsters:
        ctx.append(f"- {name.title()} — CR {data['cr']}, HP {data['hp']}, AC {data['armor_class']}. {data['description']}")

    ctx.append("\n=== MAGIC ITEMS (sample) ===")
    for name, data in sample_items:
        ctx.append(f"- {name.replace('_',' ').title()} ({data['rarity']}): {data['description']}")

    ctx.append("\n=== SPELLS (sample) ===")
    for name, data in sample_spells:
        ctx.append(f"- {name.replace('_',' ').title()} (Level {data['level']}, {data['school']}): {data['description']}")

    ctx.append("\n=== LOCATIONS (sample) ===")
    for name, desc in sample_locations:
        ctx.append(f"- {name.replace('_',' ').title()}: {desc}")

    ctx.append("\n=== QUEST HOOKS (sample) ===")
    for q in sample_quests:
        ctx.append(f"- {q}")

    ctx.append("\n=== NPC ROLES (sample) ===")
    for n in sample_npcs:
        ctx.append(f"- {n}")

    ctx.append("\n=== PLOT TWISTS (sample) ===")
    for t in sample_twists:
        ctx.append(f"- {t}")

    ctx.append("\n=== MORAL DILEMMAS (sample) ===")
    for d in sample_dilemmas:
        ctx.append(f"- {d}")

    ctx.append("\n=== FACTIONS (sample) ===")
    for f in sample_factions:
        ctx.append(f"- {f}")

    ctx.append("\n=== WORLD EVENTS (sample) ===")
    for e in sample_events:
        ctx.append(f"- {e}")

    return "\n".join(ctx)


@app.post("/generate-quest")
async def generate_quest(request: QuestRequest):
    context = _build_context(request.genre, request.difficulty)

    prompt = f"""You are a D&D game master. Generate a unique, deep quest scenario based on:
- Genre: {request.genre}
- Difficulty: {request.difficulty}

Use the reference data below for inspiration (races, monsters, items, spells, locations, plot twists, factions, events, moral dilemmas).

REFERENCE DATA:
{context}

Create a quest with layers: a surface objective hiding a deeper conflict, a moral gray area, and a twist that changes how the party sees the situation.

Return JSON with exactly these fields:
- title: string (quest name, evocative)
- map: string (short description of the area layout)
- story: string (4-6 sentences setting up the quest, including the hook and the hidden conflict)
- locations: array of strings (3-5 key locations)
- npcs: array of objects with name, role, and motivation
- enemies: array of objects with name, hp, ac, and a short description
- factions: array of strings (factions involved and their stance)
- plot_twist: string (the hidden truth the party will uncover)
- moral_dilemma: string (a hard choice the party must face)
- reward: string (what players get, can be unusual or story-driven)
- suggested_level: integer (recommended character level)
"""

    try:
        response = client.chat.completions.create(
            model=API_MODEL,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.8,
        )
        raw = response.choices[0].message.content
        if raw.startswith("```json"):
            raw = raw[7:-3]
        elif raw.startswith("```"):
            raw = raw[3:-3]
        data = json.loads(raw)
        return data
    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/races")
async def get_races():
    return {k: v["description"] for k, v in RACES.items()}


@app.get("/api/classes")
async def get_classes():
    return {k: v["description"] for k, v in CLASSES.items()}


@app.get("/api/monsters")
async def get_monsters():
    return {k: {"cr": v["cr"], "hp": v["hp"], "ac": v["armor_class"]} for k, v in MONSTERS.items()}


@app.get("/api/items")
async def get_items():
    return {k.replace("_", " ").title(): v["description"] for k, v in MAGIC_ITEMS.items()}


FRONTEND_DIR = Path(__file__).resolve().parent.parent / "frontend"
FRONTEND_FILE = FRONTEND_DIR / "dndai.html"


@app.get("/")
async def serve_frontend():
    if FRONTEND_FILE.exists():
        return FileResponse(str(FRONTEND_FILE))
    return {"error": "Frontend not found"}





if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
