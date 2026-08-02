# 06 — Create NPC

Make a person the Keeper can *play*, not just a stat line — a face, a want, a secret, and a
tell — mechanically correct for 7e.

## First

- **Read `core/02-rules-reference.md`** before writing the stat block (characteristics, HP,
  Build, Damage Bonus, Dodge, skill values must be 7e-correct).
- Read the campaign `CLAUDE.md` for era/tone/output language; match name, dress, speech, and
  job to the era and the place. Check `canon-log.md` — this person may already exist.
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
- **The lie they tell.** What do they say when asked directly? Every NPC with a secret needs
  a prepared cover story, or the Keeper has to invent one mid-scene.

Roll `reference/tables/npc-quirks.md` for at least the mannerism. A rolled tic beats the
model's default "nervous, wrings hands."

## Stat guidance (7e)

- Average human characteristic ≈ 50; scale to concept (a dockworker's STR high, a scholar's
  EDU high). Derive **HP = (CON+SIZ)/10**, **Build/Damage Bonus** from STR+SIZ,
  **Dodge = ½ DEX**.
- List **only skills likely to matter** at 7e values (e.g. Persuade 60, Spot Hidden 45,
  Fighting (Brawl) 45, Firearms (Handgun) 35). Non-combatants: note it and skip the weapons.
- Villains/cultists: consider Cthulhu Mythos %, spells (cross-link `reference/mythos/`), and
  the SAN implications of what they've done.

## Output

- Save to `campaigns/<slug>/npcs/<name>.md`, `kebab-case.md` in English, one NPC per file.
- Write the content in the campaign's declared **output language**. Stat block notation stays
  English (`STR 60`, `Dodge 35%`); use `reference/glossary-zh.md` for skill names in Chinese.
- Cross-link the scenes they appear in and any faction they belong to.

## Quality bar

- Playable from the file in ten seconds: concept, voice, want, secret, one clue.
- Has a want **and** a secret **and** a prepared lie.
- Stat block is internally consistent and era-appropriate.
- Secret and clues sit in keeper-only blocks; nothing here would spoil the mystery if glanced
  at.
