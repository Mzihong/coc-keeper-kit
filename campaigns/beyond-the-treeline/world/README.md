# world/

Places, regions, factions, and timeline for this campaign. Built with the `build-world`
skill from `templates/location.md`. One place/faction per file, `kebab-case.md`.

**`event-clock.md` lives here too** — the campaign's doom track and trigger table, built with
`build-event-clock` from `templates/event-clock.md`. It's one of the three files every
generator reads (`campaigns/README.md`), so the live path never moves: when an arc closes, its
settled clock is archived to `archive/event-clock-<arc-slug>.md` and a fresh one is built at
`event-clock.md` for the next arc's threat.

A place may carry a **map** — a `<name>.json` map DSL beside its `<name>.md`, rendered to
`<name>.svg` by `python scripts/render-map.py`. Most locations don't need one; see the
optional Map section in `templates/location.md`.

Campaign-specific canon lives here (with its secrets). Generic, reusable settings belong in
the root `reference/`.
