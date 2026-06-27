RACES = {
    "human": {
        "traits": ["Versatile", "Ambitious"],
        "description": "Adaptable and diverse, humans are the most common race in the realms.",
        "bonuses": {"any": 1},
    },
    "elf": {
        "traits": ["Keen Senses", "Fey Ancestry", "Trance", "Darkvision 60ft"],
        "description": "Graceful and long-lived, elves are attuned to the magic of the world.",
        "bonuses": {"dex": 2},
        "subraces": ["High Elf", "Wood Elf", "Dark Elf (Drow)"],
    },
    "dwarf": {
        "traits": ["Dwarven Resilience", "Darkvision 60ft", "Stonecunning"],
        "description": "Stout and hardy, dwarves are master craftspeople and warriors.",
        "bonuses": {"con": 2},
        "subraces": ["Hill Dwarf", "Mountain Dwarf"],
    },
    "halfling": {
        "traits": ["Lucky", "Brave", "Halfling Nimbleness"],
        "description": "Small but brave, halflings are known for their luck and cheerfulness.",
        "bonuses": {"dex": 2},
    },
    "dragonborn": {
        "traits": ["Draconic Ancestry", "Breath Weapon", "Damage Resistance"],
        "description": "Proud and powerful, dragonborn are descended from dragons.",
        "bonuses": {"str": 2, "cha": 1},
    },
    "gnome": {
        "traits": ["Gnome Cunning", "Darkvision 60ft"],
        "description": "Inventive and curious, gnomes are natural tinkerers and illusionists.",
        "bonuses": {"int": 2},
        "subraces": ["Forest Gnome", "Rock Gnome"],
    },
    "half-elf": {
        "traits": ["Fey Ancestry", "Skill Versatility"],
        "description": "Bridging two worlds, half-elves are charismatic and adaptable.",
        "bonuses": {"cha": 2, "any": 2},
    },
    "half-orc": {
        "traits": ["Relentless Endurance", "Savage Attacks", "Darkvision 60ft"],
        "description": "Strong and intimidating, half-orcs combine human ambition with orcish ferocity.",
        "bonuses": {"str": 2, "con": 1},
    },
    "tiefling": {
        "traits": ["Hellish Resistance", "Infernal Legacy", "Darkvision 60ft"],
        "description": "Descended from fiends, tieflings possess innate magical abilities.",
        "bonuses": {"cha": 2, "int": 1},
    },
}

CLASSES = {
    "barbarian": {
        "hit_die": 12,
        "primary_ability": "Strength",
        "saving_throws": ["Strength", "Constitution"],
        "description": "A fierce warrior driven by rage.",
    },
    "bard": {
        "hit_die": 8,
        "primary_ability": "Charisma",
        "saving_throws": ["Dexterity", "Charisma"],
        "description": "A performer whose magic weaves through music and words.",
    },
    "cleric": {
        "hit_die": 8,
        "primary_ability": "Wisdom",
        "saving_throws": ["Wisdom", "Charisma"],
        "description": "A divine champion wielding holy magic.",
    },
    "druid": {
        "hit_die": 8,
        "primary_ability": "Wisdom",
        "saving_throws": ["Intelligence", "Wisdom"],
        "description": "A guardian of nature who commands beasts and elements.",
    },
    "fighter": {
        "hit_die": 10,
        "primary_ability": "Strength or Dexterity",
        "saving_throws": ["Strength", "Constitution"],
        "description": "A master of martial combat and tactics.",
    },
    "monk": {
        "hit_die": 8,
        "primary_ability": "Dexterity & Wisdom",
        "saving_throws": ["Strength", "Dexterity"],
        "description": "A martial artist harnessing inner ki energy.",
    },
    "paladin": {
        "hit_die": 10,
        "primary_ability": "Strength & Charisma",
        "saving_throws": ["Wisdom", "Charisma"],
        "description": "A holy knight sworn to a sacred oath.",
    },
    "ranger": {
        "hit_die": 10,
        "primary_ability": "Dexterity & Wisdom",
        "saving_throws": ["Strength", "Dexterity"],
        "description": "A wilderness warrior skilled with bow and blade.",
    },
    "rogue": {
        "hit_die": 8,
        "primary_ability": "Dexterity",
        "saving_throws": ["Dexterity", "Intelligence"],
        "description": "A cunning infiltrator and master of stealth.",
    },
    "sorcerer": {
        "hit_die": 6,
        "primary_ability": "Charisma",
        "saving_throws": ["Constitution", "Charisma"],
        "description": "A spellcaster with innate magical power.",
    },
    "warlock": {
        "hit_die": 8,
        "primary_ability": "Charisma",
        "saving_throws": ["Wisdom", "Charisma"],
        "description": "A magic-user bound to a powerful patron.",
    },
    "wizard": {
        "hit_die": 6,
        "primary_ability": "Intelligence",
        "saving_throws": ["Intelligence", "Wisdom"],
        "description": "A scholar of arcane magic and spellcraft.",
    },
}

MONSTERS = {
    "goblin": {
        "cr": "1/4",
        "hp": 7,
        "armor_class": 15,
        "description": "Small, cowardly humanoid with sharp teeth.",
        "traits": ["Nimble Escape"],
    },
    "orc": {
        "cr": "1/2",
        "hp": 15,
        "armor_class": 13,
        "description": "Brutal, muscular humanoid with a hunger for battle.",
        "traits": ["Aggressive"],
    },
    "skeleton": {
        "cr": "1/4",
        "hp": 13,
        "armor_class": 13,
        "description": "Animated bones of the dead, mindlessly serving its master.",
        "traits": ["Undead Fortitude"],
    },
    "zombie": {
        "cr": "1/4",
        "hp": 22,
        "armor_class": 8,
        "description": "Shambling corpse driven by dark necromancy.",
        "traits": ["Undead Fortitude"],
    },
    "giant spider": {
        "cr": "1",
        "hp": 26,
        "armor_class": 14,
        "description": "Massive arachnid that hunts in darkness.",
        "traits": ["Web", "Poison"],
    },
    "wolf": {
        "cr": "1/4",
        "hp": 11,
        "armor_class": 13,
        "description": "Pack hunter with sharp instincts.",
        "traits": ["Pack Tactics"],
    },
    "bandit": {
        "cr": "1/8",
        "hp": 11,
        "armor_class": 12,
        "description": "Humanoid outlaw who preys on travelers.",
        "traits": [],
    },
    "shadow": {
        "cr": "1/2",
        "hp": 16,
        "armor_class": 12,
        "description": "Incorporeal undead born from darkness.",
        "traits": ["Strength Drain", "Amorphous"],
    },
    "mimic": {
        "cr": "2",
        "hp": 58,
        "armor_class": 12,
        "description": "Shape-shifting monster that disguises as objects.",
        "traits": ["Adhesive", "Shapechanger"],
    },
    "displacer beast": {
        "cr": "3",
        "hp": 85,
        "armor_class": 13,
        "description": "Large magical panther-like creature with two tentacles.",
        "traits": ["Displacement"],
    },
    "young dragon": {
        "cr": "3-5",
        "hp": 100,
        "armor_class": 17,
        "description": "A young chromatic or metallic dragon.",
        "traits": ["Breath Weapon", "Damage Resistance"],
    },
    "mind flayer": {
        "cr": "7",
        "hp": 71,
        "armor_class": 15,
        "description": "Psionic humanoid from the Far Realm that feeds on brains.",
        "traits": ["Mind Blast", "Extract Brain"],
    },
    "beholder": {
        "cr": "13",
        "hp": 180,
        "armor_class": 18,
        "description": "Floating aberration with eyestalks that shoot magic rays.",
        "traits": ["Antimagic Cone", "Eye Rays"],
    },
    "lich": {
        "cr": "21",
        "hp": 135,
        "armor_class": 17,
        "description": "Undead archmage who achieved immortality through necromancy.",
        "traits": ["Legendary Resistance", "Phylactery"],
    },
    "kobold": {
        "cr": "1/8",
        "hp": 5,
        "armor_class": 12,
        "description": "Small, cowardly draconic humanoid. Traps are their specialty.",
        "traits": ["Pack Tactics", "Sunlight Sensitivity"],
    },
    "harpy": {
        "cr": "1",
        "hp": 38,
        "armor_class": 11,
        "description": "Vicious half-bird, half-humanoid with a hypnotic song.",
        "traits": ["Luring Song"],
    },
    "treant": {
        "cr": "9",
        "hp": 138,
        "armor_class": 16,
        "description": "Animate tree guardian of ancient forests.",
        "traits": ["Animate Trees", "Siege Monster"],
    },
    "gelatinous cube": {
        "cr": "2",
        "hp": 84,
        "armor_class": 6,
        "description": "Transparent cube of ooze that engulfs everything in its path.",
        "traits": ["Transparent", "Engulf"],
    },
}

MAGIC_ITEMS = {
    "potion_of_healing": {
        "rarity": "Common",
        "description": "Restores 2d4+2 hit points.",
    },
    "bag_of_holding": {
        "rarity": "Uncommon",
        "description": "Magical bag with an extradimensional space. Holds up to 500 lbs.",
    },
    "cloak_of_elvenkind": {
        "rarity": "Uncommon",
        "description": "Grants advantage on Stealth checks.",
    },
    "boots_of_speed": {
        "rarity": "Rare",
        "description": "Allows the wearer to dash as a bonus action.",
    },
    "flame_tongue": {
        "rarity": "Rare",
        "description": "A sword wreathed in fire, dealing extra 2d6 fire damage.",
    },
    "wand_of_magic_missiles": {
        "rarity": "Uncommon",
        "description": "Cast Magic Missile without using spell slots. 7 charges.",
    },
    "ring_of_protection": {
        "rarity": "Rare",
        "description": "+1 to AC and saving throws.",
    },
    "amulet_of_health": {
        "rarity": "Rare",
        "description": "Sets your Constitution score to 19.",
    },
    "vorpal_sword": {
        "rarity": "Legendary",
        "description": "On a critical hit, severs the target's head.",
    },
    "deck_of_many_things": {
        "rarity": "Legendary",
        "description": "A deck of cards that can grant great power or doom.",
    },
}

SPELLS = {
    "magic_missile": {
        "level": 1,
        "school": "Evocation",
        "description": "Three glowing darts that always hit, dealing 1d4+1 force each.",
    },
    "fireball": {
        "level": 3,
        "school": "Evocation",
        "description": "A 20ft radius sphere of flame, 8d6 fire damage.",
    },
    "cure_wounds": {
        "level": 1,
        "school": "Evocation",
        "description": "Heals a creature for 1d8 + spellcasting modifier.",
    },
    "shield": {
        "level": 1,
        "school": "Abjuration",
        "description": "Reaction: +5 AC until your next turn.",
    },
    "invisibility": {
        "level": 2,
        "school": "Illusion",
        "description": "Touch a creature to become invisible for 1 hour.",
    },
    "counterspell": {
        "level": 3,
        "school": "Abjuration",
        "description": "Reaction to negate another creature's spell.",
    },
    "revivify": {
        "level": 3,
        "school": "Necromancy",
        "description": "Restores a creature that died within the last minute to life.",
    },
    "misty_step": {
        "level": 2,
        "school": "Conjuration",
        "description": "Bonus action teleport up to 30ft.",
    },
}

LOCATIONS = {
    "dungeon": "Dark, winding underground complex filled with traps and monsters.",
    "castle": "Fortified stronghold of a lord or king, with thick walls and towers.",
    "forest": "Dense woodland, home to fey creatures, hidden groves, and ancient ruins.",
    "swamp": "Murky wetlands, plagued by undead, hags, and poisonous creatures.",
    "mountain_pass": "Treacherous high-altitude trail through rocky peaks.",
    "cavern": "Massive underground cave system with glowing crystals and deep lakes.",
    "tavern": "Warm, noisy inn where adventurers gather for quests and rumors.",
    "library": "Ancient repository of forbidden knowledge and magical tomes.",
    "temple": "Sacred place dedicated to a deity, often guarded by divine magic.",
    "desert": "Vast, scorching wasteland hiding buried ruins and nomadic tribes.",
    "underdark": "Vast network of underground caverns lit by bioluminescent fungi.",
    "coastal_cliffs": "Wind-swept cliffs overlooking a raging sea, home to seabirds and pirates.",
    "enchanted_grove": "Magical forest clearing where fey creatures dance under moonlight.",
    "necropolis": "City of the dead, crawling with undead and dark necromancers.",
    "floating_island": "Landmass suspended in the sky by ancient magic.",
}

QUESTS = [
    "Retrieve a stolen artifact from a goblin-infested ruin.",
    "Slay a monster terrorizing a remote village.",
    "Escort a merchant caravan through dangerous wilderness.",
    "Rescue a captured noble from a bandit stronghold.",
    "Investigate strange disappearances in a haunted forest.",
    "Destroy a cursed object hidden in a forgotten temple.",
    "Protect a sacred ritual from cultist interference.",
    "Discover the source of a magical plague.",
    "Broker peace between warring factions.",
    "Explore a newly discovered dungeon beneath an old castle.",
    "Recover a lost spellbook from a wizard's tomb.",
    "Defend a settlement from an incoming horde.",
    "Sabotage an enemy war camp before the assault begins.",
    "Seek an audience with a reclusive dragon to gain its favor.",
    "Steal a treasure from a heavily guarded vault.",
    "Break a curse afflicting a local lord.",
    "Find a rare herb to cure a dying monarch.",
    "Disrupt a slaving operation in a port city.",
    "Navigate a magical labyrinth to reach the prize at its center.",
    "Confront a doppelganger who has replaced a town leader.",
]

NPC_ROLES = [
    "Village Elder — wise but cautious leader of a small community.",
    "Mysterious Stranger — appears with cryptic warnings and hidden motives.",
    "Corrupt Guard — takes bribes and turns a blind eye for coin.",
    "Mad Prophet — rambles about impending doom, but knows fragments of truth.",
    "Reluctant Hero — former adventurer who swore off violence.",
    "Greedy Merchant — willing to sell anyone out for profit.",
    "Forgotten Prince — rightful heir in hiding, seeking allies.",
    "Shadowy Informant — has eyes everywhere, for a price.",
    "Drunken Bard — knows all the songs, rumors, and secrets of the realm.",
    "Cult Leader — charismatic speaker preaching dark prophecies.",
    "Exiled Mage — powerful wizard banished for forbidden research.",
    "Ghost of a Betrayed Ally — bound to the mortal plane seeking justice.",
]

PLOT_TWISTS = [
    "The quest giver is actually the villain manipulating the party.",
    "The artifact they seek was destroyed long ago; what they find is a fake.",
    "The monster terrorizing the village is a guardian protecting a greater threat.",
    "The kidnapped noble willingly disappeared to escape a greater danger.",
    "Two factions are both right — and both wrong. The party must choose.",
    "The curse was cast by the victim themselves in a moment of despair.",
    "The enemy leader is a mind-controlled former hero.",
    "The treasure is sentient and corrupts whoever holds it.",
    "The patron paying for the quest plans to betray the party upon completion.",
    "The entire quest is a test orchestrated by a mysterious order.",
    "The real monster is the town's beloved leader transformed by dark magic.",
    "The party is being haunted by someone they wronged in a past life.",
    "The quest repeats in a time loop until the party uncovers the truth.",
    "The allies were secretly working for the enemy all along.",
    "The ancient ruins are a prison, and the party is about to free a god-eater.",
]

MORAL_DILEMMAS = [
    "Save the captured villagers or stop the villain from escaping with a deadly weapon.",
    "Destroy the cursed artifact (and the town it protects) or leave it intact (and let the corruption spread).",
    "Side with the lawful but oppressive guard or the chaotic but violent rebels.",
    "Kill the possessed child or risk the entire city being consumed by the demon within.",
    "Tell the grieving widow the truth about her husband's betrayal or let her remember him as a hero.",
    "Let the traitor go in exchange for critical information or execute them for their crimes.",
    "Save one of two loved ones — the other will die for certain.",
    "Accept help from a known villain to defeat a greater evil, knowing they will betray you later.",
    "Destroy the lich's phylactery and doom the innocent souls powering it, or leave it and let the lich rise again.",
    "Reveal the corruption in the church and shatter the faith of thousands, or stay silent and protect their belief.",
]

FACTIONS = [
    "Emerald Circle — druids who protect ancient forests from civilization's expansion.",
    "Iron Dominion — expansionist empire that believes order must be enforced through strength.",
    "Crimson Cartel — crime syndicate controlling underground trade in poisons, relics, and slaves.",
    "Order of the Silver Flame — paladins and clerics hunting undead, fiends, and heretics.",
    "The Veiled Hand — secret society of manipulators pulling strings across kingdoms.",
    "Freefolk Alliance — scattered tribes united against imperial conquest.",
    "Arcane Academy — wizards who hoard magical knowledge and regulate spellcasting.",
    "Cult of the Devourer — doomsday cult worshiping a primordial entity of destruction.",
    "Merchant Guild of Highport — trade consortium that values profit above all laws.",
    "The Pale Host — undead legion serving a deathless queen from beyond the grave.",
    "Dwarven Forge Clans — isolationist craftspeople who control the best weapon-smithing.",
    "Gnomish Tinker Collective — inventors selling magical gadgets to the highest bidder.",
]

EVENTS = [
    "A meteor crashes nearby, bringing strange crystals that warp reality.",
    "The full moon turns red, and the dead rise from their graves across the land.",
    "A plague of magical sleep spreads through the city — victims never wake.",
    "The rivers run dry, revealing ancient rune-carved passages beneath the riverbed.",
    "A wizard's tower materializes in the town square, filled with clones of the missing archmage.",
    "The king announces a tournament — the prize is a wish granted by the royal dragon.",
    "An eclipse heralds the opening of rifts to other planes. Monsters pour through.",
    "A magical storm floods the valley with impossible colors, and those touched gain strange powers.",
    "A dragon's roar echoes from the mountain — it has not been heard in a thousand years.",
    "The gods go silent. No cleric receives divine magic. Panic spreads.",
]
