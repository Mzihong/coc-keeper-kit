# 03 — Build World

Create places that feel lived-in and quietly wrong — the substrate a mystery grows in. Aim
for **usable texture**, not an encyclopedia: enough for the Keeper to improvise confidently.

## First, orient

- Read the campaign's `CLAUDE.md` for **era, tone, output language, and content lines** —
  match them. Read `canon-log.md` if the campaign has been played.
- If the campaign already declares a **Threat** (category + name), building that faction
  means building *that one* — don't roll or invent a competing threat instead.
- Decide the scope requested: **region**, **town/locale**, **faction/organisation**, or
  **timeline**.
- Use `templates/location.md` for a place; for a region or faction, adapt its headings.
- If this is the campaign's first world-building pass, run
  `python scripts/roll.py locations mythos-angles --campaign <slug>` before writing. Take
  what you roll.

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
detail; 3–5 notable NPCs (name + one-line hook — hand to `core/06-create-npc.md` for full
stats); local rumours (mark which are true); the buried wrongness; open hooks.

For a **region**: geography & mood; the settlements and how they relate; powers/factions and
their tensions; a short timeline of what led here; the Mythos undercurrent.

For a **faction**: goal, structure, membership, iconography, methods, and the ordinary face
vs the true agenda.

**Cult sub-path.** When the faction is a cult, don't just point at the craft note — walk its
build order. Read `reference/craft/cult-design-zh.md` §一–§三 first (why a cult works as a
villain, what makes a *Cthulhu* cult specific, then the ordered build: concept → leader →
goal → structure → membership → induction → funding → Mythos-exposure tiers → weaknesses →
enemies → relationship diagram). Run
`python scripts/roll.py cult-goals cult-leader-positions --campaign <slug>` (want × means, and
the leader's social front) rather than inventing either. Use `templates/cult.md`, which
mirrors this same faction structure with the cult
build order folded in. `reference/mythos/cults/` also has five fully-worked cult dossiers
(same shape as this template) — reskin one directly (era/place/name) rather than building
from zero when one fits the campaign's needs.

For a **timeline**: dated beats (public record vs the hidden truth) leading to the present. If
the throughline is Cthulhu-cult history, `reference/mythos/cthulhu-cult-history-zh.md` has
27 reusable historical beats (plus an "immortal masters" throughline spanning three of them) —
pull dated entries from there rather than inventing a history from nothing, and reframe/relocate
freely to fit the campaign's era and place.

## Output

- Save to `campaigns/<slug>/world/<name>.md`. One place/faction per file; `kebab-case.md`
  in English, even when the content is Chinese.
- Write the content in the campaign's declared **output language**. Place, street, and
  institution names follow the *setting* — a 简体中文 campaign defaults to an American one
  (`core/01-intake.md`), so write its towns and roads per `reference/glossary-zh.md` →
  外文专名的译写, not as if the map were Chinese.
- Cross-link related places, factions, and NPCs with relative links.
- **Add a mermaid diagram when the structure is the point** — a faction with more than a
  handful of moving parts, or a region whose settlements need travel times. Follow
  `reference/craft/diagram-conventions-zh.md`: §一 (general rules — every edge carries a
  label naming what actually connects the two), §二 (faction diagrams), §四 (region
  diagrams). Skip the diagram for 2–3 nodes; a sentence is faster.
- End with **3–5 open hooks** a scenario could grab.

## Quality bar

- A Keeper could run a scene here from the file alone, and improvise beyond it.
- At least one honest **red herring** and one **true** lead among the rumours.
- Nothing contradicts the campaign's era/tone/canon; secrets are quarantined in keeper blocks.
- The rolled seeds are visible in the result — not the first place the model would have
  thought of unprompted.
