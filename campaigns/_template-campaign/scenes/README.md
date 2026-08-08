# scenes/

Locations and set-pieces with read-aloud boxed text. Built with the `description` skill
(Mode A) from `templates/scene.md`. One scene per file, `kebab-case.md`. Read-aloud text sits in a `>`
blockquote; secrets and escalation go in keeper-only blocks below it.

A scene may carry a **floor plan** when connectivity or sightlines matter to play — a
`<name>.json` map DSL beside its `<name>.md`, rendered to `<name>.svg` by
`python scripts/render-map.py`. That SVG is **Keeper-facing and may carry secrets inline;
don't hand it to the players.** The player-facing version is a separate, opt-in artifact
(`--player`) that costs roughly 3–5× the tokens, must be quoted to the Keeper before it's
generated, and lands in `handouts/` rather than here — see `core/09-description.md` → Output.
