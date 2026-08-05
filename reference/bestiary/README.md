# bestiary/ — used creature archive, not a bestiary

**This directory is not a monster catalogue.** The catalogue is
`reference/sourcebooks/malleus-monstrorum-zh.md` — 223 entries, official stat blocks. The
searchable index over all 223 (plus everything here) is `reference/tables/monster-index.md`.
This directory holds only the creatures that have actually been **written up** for table use:
generic, campaign-neutral monsters and Mythos entities — **tiers L2 (creature), L3 (servitor),
and L4 (unique entity)** — with a Reveal, a fair out, and (if it maps to a malleus entry) the
book's raw numbers translated into a full stat card. Produced by the `create-monster` skill
using `templates/monster.md`. One creature per file, `kebab-case.md`.

**Do not pre-populate this directory from the transcript.** Writing a `.md` for all 223 would
duplicate numbers that already live in the transcript — change one there and the copy here goes
stale silently. Add an entry here only when a creature is actually about to be used at a table
(see `update_plan/2026-08-02-monster-templates-traits.md` definition 9 for the three-layer
reasoning: transcript = full catalogue, `monster-index.md` = searchable summary, `bestiary/` =
what's been built).

**L5 (deity) entries do not go here** — a god's page is lore-shaped (origin, waking
conditions, signs, how a cult worships it), not a stat card. Those live in
`reference/mythos/great-old-ones/`, per `core/07-create-monster.md`.

Work from `reference/sourcebooks/malleus-monstrorum-zh.md` (the official creature compendium)
— read the nearest published entry for stat scale and SAN cost. **The published
numbers may be taken directly into an entry** as long as the file names the book and chapter;
the reveal, lore, and behaviour prose is written fresh (`core/00-how-to-run.md` → ground
rules). Its stat tables are clean; check the file's own header for the current list of small
known defects before trusting an edge case.

Keep these **portable** — stats, behaviour, and Sanity cost, but no campaign plot. When a
creature becomes entangled in a specific game, copy it into that campaign's `world/` or
`scenes/` and add the plot-specific secrets there.

Header tags, per `templates/monster.md`: `type` (`independent-race` / `servitor-race` /
`unique-entity` — add a `(beast)`/`(undead)` modifier where it fits), `tier` (L2/L3/L4, see
`reference/rules/monster-scale.md`), `threat` (trivial / moderate / deadly / mythic — the ±
inside the tier), `sanity` (the X/Y to see it). Any numeric trait on the entry comes from
`reference/tables/monster-traits.md` and must stay at or under the tier's load ceiling.

Two more header fields feed `reference/tables/monster-index.md` and are **mandatory** — a blank
one fails `python scripts/build-reference-index.py --check`, same as a missing citation block:

- **`Serves`** — the deity/faction this creature answers to (e.g. `Cthulhu`), or exactly
  `Independent — serves no god`. Answers "what's this boss's elite guard?"
- **`Index summary`** — one clause, ≤40 characters, English, what a Keeper needs to pick between
  similar-tier creatures. **This is not the Reveal.** The Reveal is read aloud at the table; the
  index summary is scanned (by a Keeper or a model) to choose between candidates before a Reveal
  is ever written. The two serve different moments and must not be merged into one field.
