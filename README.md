# D&D Quest Generator

AI-powered quest generator for Dungeons & Dragons. Generates unique quests with locations, NPCs, enemies, and rewards using OpenAI GPT.

## Features

- Generates D&D-style quests with story, locations, NPCs, enemies, and rewards
- Built-in knowledge base: 10 races, 12 classes, 18 monsters, magic items, spells, locations
- Adjustable difficulty (easy / medium / hard) and genre (fantasy, cyberpunk, horror, sci-fi)
- REST API with OpenAPI-compatible endpoints
- Web UI included

## Quick Start

### 1. Clone and setup

```bash
git clone https://github.com/YOUR_USERNAME/dnd-generator.git
cd dnd-generator
python -m venv venv

# Windows:
venv\Scripts\activate

# Mac / Linux:
source venv/bin/activate

pip install -r requirements.txt
```

### 2. Add OpenAI API key

Create `.env` file in the project root:

```
OPENAI_API_KEY=sk-your-key-here
```

Get a key at https://platform.openai.com/api-keys

### 3. Run

```bash
python backend/main.py
```

Open http://localhost:8000 in browser for the web UI.

Or use the API directly:

```bash
curl -X POST http://localhost:8000/generate-quest \
  -H "Content-Type: application/json" \
  -d '{"genre": "fantasy", "difficulty": "medium"}'
```

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/generate-quest` | POST | Generate a quest (body: `{genre, difficulty}`) |
| `/api/races` | GET | List all D&D races |
| `/api/classes` | GET | List all D&D classes |
| `/api/monsters` | GET | List all monsters |
| `/api/items` | GET | List all magic items |
| `/docs` | GET | Swagger UI documentation |

## Project Structure

```
dnd-generator/
├── backend/
│   ├── main.py            # FastAPI server
│   └── knowledge_base.py  # D&D data (races, classes, monsters, etc.)
├── frontend/
│   └── index.html         # Web UI
├── requirements.txt
└── .env
```

## Deploy

Push to GitHub and deploy on Render / Railway / Fly.io for free.

Example `render.yaml` for easy deploy will be auto-detected if added.
