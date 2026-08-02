# bestiary/ — reusable creatures

Generic, campaign-neutral monsters and Mythos entities. Produced by the `create-monster`
skill using `templates/monster.md`. One creature per file, `kebab-case.md`.

Calibrate against `reference/sourcebooks/malleus-monstrorum-zh.md` (the official creature
compendium, local only) — read the nearest published entry for stat scale and SAN cost, then
write your own. Structure and scale, never text.

Keep these **portable** — stats, behaviour, and Sanity cost, but no campaign plot. When a
creature becomes entangled in a specific game, copy it into that campaign's `world/` or
`scenes/` and add the plot-specific secrets there.

Suggested tags in each file's header: `threat` (trivial / moderate / deadly / mythic),
`type` (human / beast / undead / mythos-servitor / independent-race / great-old-one),
`sanity` (the X/Y to see it).
