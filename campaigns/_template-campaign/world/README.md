# world/

Places, regions, factions, and timeline for this campaign. Built with the `build-world`
skill from `templates/location.md`. One place/faction per file, `kebab-case.md`.

**`event-clock.md` lives here too** — the campaign's doom track and trigger table, built with
`build-event-clock` from `templates/event-clock.md`. It's one of the four files every
generator reads by default (`campaigns/README.md`), so the live path never moves: when an arc
closes, its settled clock is archived to `archive/event-clock-<arc-slug>.md` and a fresh one
is built at `event-clock.md` for the next arc's threat.

A place may carry a **map** — a `<name>.json` map DSL beside its `<name>.md`, rendered to
`<name>.svg` by `python scripts/render-map.py`. Most locations don't need one; see the
optional Map section in `templates/location.md`.

Campaign-specific canon lives here (with its secrets). Generic, reusable settings belong in
the root `reference/`.

## When to open which file

**Only `event-clock.md` is read by default every session** (`core/00-how-to-run.md` → "What
to read by default each session"). Everything else below is read **on demand** — open a row
when a scene actually needs it, not preemptively. Keep this table current as `world/` grows;
it's the thing that makes "on demand" actually work instead of collapsing back into "read the
whole folder."

| File | What it holds | Open it when… |
|---|---|---|
| `<name>.md` | <place / faction / region — one line> | <the trigger — e.g. "the party heads toward X", "a scene needs this faction's structure"> |

*Add a row per file as `build-world` creates it. A file with no row is a file nobody knows
when to open — that's the failure mode this table exists to prevent.*
