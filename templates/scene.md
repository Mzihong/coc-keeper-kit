# Scene — <name>

- **Where / when:** <location, time of day, weather>
- **Purpose in the story:** <what this scene is *for* — a clue, a choice, a shock, a breather>
- **Leads in from / out to:** <previous → next scenes>

## Read-aloud (boxed text)
> <The players' first impression — 3–6 sentences. Two or three senses beyond sight (sound,
> smell, temperature, the feel of the air). One concrete, slightly wrong detail. End on
> something that invites action, not a full stop.>

## Map *(optional)*
> Only when the room layout itself matters (connectivity, sightlines, where to hide) — most
> scenes don't need one. Render with `python scripts/render-map.py <path>.json`; DSL shape and
> conventions in that script's docstring and `reference/craft/diagram-conventions-zh.md`.
> This map is **Keeper-facing** — it can carry secrets (a locked door, a hidden room) inline.
> Don't hand it straight to players; a player-safe version needs its own spoiler pass first.

```json
{"title": "<scene label>", "rooms": [{"id": "…", "name": "…", "x": 0, "y": 0, "w": 3, "h": 3,
  "doors": [{"edge": "bottom", "pos": 0.5}]}]}
```

## What's here
- **Clues (see `create-puzzle` for fair-play):**
  - <clue — the skill/action that surfaces it, and where it points>
  - <redundant second route to the key clue>
- **NPCs / creatures:** <links>
- **Features to interact with:** <doors, objects, hazards>

## If the players…
- **…investigate <X>:** <what they find>
- **…do the risky thing:** <consequence>
- **…try to leave / stall:** <what pushes back>

## Checks that may come up
- <Skill> (<Regular/Hard>) — <what success/failure means>. *Don't gate the only path on it.*

> **KEEPER ONLY**
> - **Truth of this place:** <what's really going on>
> - **Escalation:** <what changes if they linger / fail / return>

## Links
<relative links>
