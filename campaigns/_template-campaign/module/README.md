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
