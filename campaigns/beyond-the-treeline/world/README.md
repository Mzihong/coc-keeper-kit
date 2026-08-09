# world/

Places, regions, factions, and timeline for this campaign. Built with the `build-world`
skill from `templates/location.md`. One place/faction per file, `kebab-case.md`.

**`event-clock.md` lives here too** — the campaign's doom track and trigger table, built with
`build-event-clock` from `templates/event-clock.md`. It's one of the four files every
generator reads by default (`campaigns/README.md`), so the live path never moves: when an arc
closes, its settled clock is archived to `archive/event-clock-<arc-slug>.md` and a fresh one
is built at `event-clock.md` for the next arc's threat. **Not yet built for this campaign** —
`core/05-event-clock.md` hasn't run yet; the two open questions it needs to resolve (what the
migrating thing is, whether the relay station is still transmitting) are flagged
`> **KEEPER ONLY**` in `timeline.md` and `CLAUDE.md`.

A place may carry a **map** — a `<name>.json` map DSL beside its `<name>.md`, rendered to
`<name>.svg` by `python scripts/render-map.py`. Most locations don't need one; see the
optional Map section in `templates/location.md`.

Campaign-specific canon lives here (with its secrets). Generic, reusable settings belong in
the root `reference/`.

## When to open which file

**Only `event-clock.md` is read by default every session** (`core/00-how-to-run.md` → "What
to read by default each session"). Everything else below is read **on demand**.

| File | What it holds | Open it when… |
|---|---|---|
| `event-clock.md` | Doom track, trigger table — **not yet built** | Every session, once `core/05-event-clock.md` has run |
| `velga.md` | 韦尔加谷 — the home base: 谷心/坡上/林缘三片布局、五位 notable NPC 所在 | A scene is set in the village, or the party interacts with a roster stub keyed to a house here (图沃/卡蕤/恩珊/佐仑/维珂) |
| `velga-region.md` | Geography, travel times between all four places, 沃辛/科瓦两家的排班世仇, 骨铁贸易的三方分账张力, treeline rule (public story + KEEPER ONLY real reason) | A scene involves travel between locations, or either faction tension (排班表 / 贡额分账) becomes live |
| `stone-watch.md` | 石哨 — the relay-station tower, its two floors, the "must be two people" mechanism, 桑塔/沃尔克两位瞭望员 | The on-duty pair (the investigators, by default) are at or heading to the tower |
| `stone-watch-1f.json` / `.svg`, `stone-watch-2f.json` / `.svg` | Keeper-facing floor plans for the tower's two levels | Running a scene inside the tower and room layout/sightlines matter |
| `the-barrens.md` | 不生原 — the ruin field past the tower: 断阵/卧城/新垒/径痕四个区,结构性危险清单 | The party pushes past Stone Watch toward the ruins |
| `inherited-holding.md` | 守井宅 — the inherited property, its full-moon condition and consequences ladder, the ledger's two mismatched clues | The inheritance hook is engaged, or a full-moon deadline is approaching |
| `timeline.md` | Watch-Year public chronicle + the KEEPER ONLY hidden timeline (the Collapse, the blank 800 years, Kaivren's team) | A historical or chronology question comes up that the standing canon doesn't already answer |
