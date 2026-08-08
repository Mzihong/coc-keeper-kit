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
> **Don't hand it straight to players.** A player-facing version is a separate, opt-in artifact
> (furniture layer + `python scripts/render-map.py <path>.json --player`) — see
> `core/09-description.md` → Output for the cost-disclosure step that must happen before
> generating it.

```json
{"title": "<scene label>", "rooms": [{"id": "…", "name": "…", "x": 0, "y": 0, "w": 3, "h": 3,
  "doors": [{"edge": "bottom", "pos": 0.5}],
  "furniture": [{"s": "rect", "x": 0.3, "y": 0.3, "w": 1.5, "h": 0.4, "label": "…"}]}]}
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
