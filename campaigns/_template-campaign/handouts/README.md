# handouts/

Player-facing props — letters, clippings, journal pages, telegrams, reports. Built with the
`create-handout` skill from `templates/handout.md`. One prop per file, `kebab-case.md`.

**These files are player-safe by rule:** no answers or keeper interpretation inside the prop
text. Anything printable goes between the `---` dividers.

A **player-facing scene map** is filed here too: the `--player` render from
`scripts/render-map.py` (`<name>-player.svg`) plus a short `<name>.md` wrapper saying what it
is and how the players get it. The SVG is the printable part, so it sits beside the wrapper
rather than between the dividers — but it goes through the same spoiler check as every other
handout. See `core/09-description.md` → Output.
