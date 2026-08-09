# module/

Compiled, readable module text — one file per **closed** arc, built from `templates/module.md`
via `core/16-compile-module.md`. Empty until an arc has actually been played; this is a
keepsake and rereadable record, not something to generate ahead of a session (that's
`sessions/`).

```
00-campaign-primer.md    ← shared across every arc: worldview, translation glossary,
                             cast index, map index
<arc>-<slug>.md          ← one file per arc; split into -part2.md, -part3.md, … past ~1200 lines
appendix-handouts.md     ← every handout in the compiled arc(s), numbered H1/H2/…
```

Entirely Keeper-facing — nothing here is safe to hand a player as-is. Facts live in the source
files (`world/`, `npcs/`, `scenes/`, the scenario file); a module text is a derived, one-way
compile. Fix a fact at its source and recompile, never here.

**Current status (2026-08-08):** only `00-campaign-primer.md` exists. It is campaign-level and
arc-independent, so it doesn't wait on play the way `<arc>-<slug>.md` does — but this campaign
hasn't run a session yet, so there is no arc file here at all. `core/16-compile-module.md`'s
hard rule still applies to the arc file: compile after the arc is played, never before.
