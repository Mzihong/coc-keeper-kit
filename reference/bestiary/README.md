# bestiary/ — reusable creatures

Generic, campaign-neutral monsters and Mythos entities — **tiers L2 (creature), L3 (servitor),
and L4 (unique entity)**. Produced by the `create-monster` skill using `templates/monster.md`.
One creature per file, `kebab-case.md`.

**L5 (deity) entries do not go here** — a god's page is lore-shaped (origin, waking
conditions, signs, how a cult worships it), not a stat card. Those live in
`reference/mythos/great-old-ones/`, per `core/07-create-monster.md`.

Work from `reference/sourcebooks/malleus-monstrorum-zh.md` (the official creature compendium,
local only) — read the nearest published entry for stat scale and SAN cost. **The published
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
