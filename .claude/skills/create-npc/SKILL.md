---
name: create-npc
description: Create a Call of Cthulhu 7th Edition NPC — a human (or human-like) character the investigators meet, with a full 7e stat block, personality, a hidden secret, a roleplaying voice, and the clues they can give. Use whenever the user wants a person, character, contact, witness, or human villain ("make the town doctor", "I need a cult leader", "a shopkeeper who knows something") — ally, obstacle, red herring, or victim. For non-human creatures and Mythos entities use create-monster instead. Writes into the campaign's npcs/ folder.
version: "1.0.0"
---

# Create NPC

Make a person the Keeper can *play*, not just a stat line — a face, a want, a secret, and a
tell — mechanically correct for 7e.

## First
- **Load `coc-rules-reference`** before writing the stat block (characteristics, HP, Build,
  Damage Bonus, Dodge, skill values must be 7e-correct).
- Read the campaign `CLAUDE.md` for era/tone; match name, dress, speech, and job to the era.
- Use `templates/npc.md`.

## Ask (or infer sensibly)
- Their **role in play** (ally / obstacle / witness / victim / red herring / villain / source).
- Rough **competence** — bystander, professional, or dangerous — which sets stat scale.
- Whether they may **fight or resist** (full stats) or are a pure social NPC (light stats).

## Build the person
- **One-line concept** first, then a spoken **description** the players actually hear (face,
  voice, a physical tell).
- **Want / fear / mannerism** — the three levers that let a Keeper improvise them live.
- **A secret** in a `> **KEEPER ONLY**` block: what they hide, what makes them talk or flip,
  how they react under pressure.
- **Clues they can give** — and the pressure/approach that unlocks each (ties into fair play:
  never make one NPC the *only* source of a key clue).

## Stat guidance (7e)
- Average human characteristic ≈ 50; scale to concept (a dockworker's STR high, a scholar's
  EDU high). Derive **HP = (CON+SIZ)/10**, **Build/Damage Bonus** from STR+SIZ, **Dodge = ½ DEX**.
- List **only skills likely to matter** at 7e values (e.g. Persuade 60, Spot Hidden 45,
  Fighting (Brawl) 45, Firearms (Handgun) 35). Non-combatants: note it and skip the weapons.
- Villains/cultists: consider Cthulhu Mythos %, spells (cross-link `reference/mythos/`), and
  the SAN implications of what they've done.

## Output
- Save to `campaigns/<slug>/npcs/<name>.md`, `kebab-case.md`, one NPC per file.
- Cross-link the scenes they appear in and any faction they belong to.

## Quality bar
- Playable from the file in ten seconds: concept, voice, want, secret, one clue.
- Stat block is internally consistent and era-appropriate.
- Secret and clues sit in keeper-only blocks; nothing here would spoil the mystery if glanced at.
