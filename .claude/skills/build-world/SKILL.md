---
name: build-world
description: Build or expand the SETTING of a Call of Cthulhu game — a region, town, locale, faction or cult organisation, or historical timeline — with mood, history, factions in tension, and the hidden wrongness beneath. Use whenever the user wants to create, flesh out, or expand a place, world, town, village, area, faction, or backdrop for a campaign ("build the fishing village", "flesh out the cult", "give me the region and its history"). For the read-aloud prose of a single location use scene-description; for the whole mystery's plot use design-scenario. Writes into the campaign's world/ folder.
version: "1.0.0"
---

# Build World

Create places that feel lived-in and quietly wrong — the substrate a mystery grows in. Aim
for **usable texture**, not an encyclopedia: enough for the Keeper to improvise confidently.

## First, orient
- Read the campaign's `CLAUDE.md` for **era, tone, and content lines** — match them.
- Decide the scope requested: **region**, **town/locale**, **faction/organisation**, or **timeline**.
- Use `templates/location.md` for a place; for a region or faction, adapt its headings.

## Principles
- **Ordinary first, then the crack.** Establish a believable, mundane place; hide exactly one
  or two *wrong* things beneath it. Horror lands hardest against normal.
- **Everything wants something.** Give each faction/notable a goal and a fear; let goals
  conflict so players can play them against each other.
- **Seed hooks, not plot.** Leave loose threads (a rumour, an absence, a debt) the Keeper can
  pull into any scenario — don't hard-wire the ending here.
- **Sense of place.** One signature sound, smell, and sight per location; period-true detail
  (transport, tech, money, news) for the campaign's era.
- **Layered secrets.** Surface (what anyone sees) → local knowledge (a check or a chat) →
  Keeper truth (the Mythos underneath). Mark the deepest layer `> **KEEPER ONLY**`.

## Produce
For a **town/locale**: identity & mood; a handful of keyed areas each with an interactive
detail; 3–5 notable NPCs (name + one-line hook — hand to `create-npc` for full stats); local
rumours (mark which are true); the buried wrongness; open hooks.

For a **region**: geography & mood; the settlements and how they relate; powers/factions and
their tensions; a short timeline of what led here; the Mythos undercurrent.

For a **faction**: goal, structure, membership, iconography, methods, and the ordinary face
vs the true agenda.

For a **timeline**: dated beats (public record vs the hidden truth) leading to the present.

## Output
- Save to `campaigns/<slug>/world/<name>.md`. One place/faction per file; `kebab-case.md`.
- Cross-link related places, factions, and NPCs with relative links.
- End with **3–5 open hooks** a scenario could grab.

## Quality bar
- A Keeper could run a scene here from the file alone, and improvise beyond it.
- At least one honest **red herring** and one **true** lead among the rumours.
- Nothing contradicts the campaign's era/tone; secrets are quarantined in keeper blocks.
