# Location — <name>

*<one-line identity — what this place is and its mood>*

- **Region / campaign:** <link>
- **Era feel:** <match the campaign>
- **Tone:** <cosy / decaying / hostile / uncanny>

## At a glance (say this out loud)
> <3–5 sensory sentences establishing the place.>

## Layout / areas
- **<Area 1>** — <what's here, who's here, one interactive detail>
- **<Area 2>** — <…>
- **<Area 3>** — <…>

## People
- <NPC link> — <why they're here>

## Map *(optional)*
> Only for a place worth drawing (a multi-room interior, a site with real layout) — most
> locations don't need one. Render with `python scripts/render-map.py <path>.json`; DSL shape
> and conventions in that script's docstring, wall/door/window elements per
> `reference/craft/diagram-conventions-zh.md`. One DSL file = one floor; a multi-storey
> building gets one block per floor, stacked in reading order.
>
> **A `callout` renders as a numbered circle on the map plus its note in a column beside the
> map** — the prose never sits on the picture. Keep it to **≤ 8 callouts per floor**; past that
> you are pasting the location text into the diagram, so split it or send the detail back to the
> sections above. Keep an anchor off the room's centre (the room name is there) — the circle is
> opaque.
>
> **An outdoor site** (manor grounds, a farmstead, a churchyard) uses the same renderer with an
> empty `rooms` array — leave out `"rooms"` entirely and use `features` (labelled shapes at
> map scale, not nested in a room), `paths` (a lane/stream as a polyline), and `compass: true`
> instead. Keep it to **5–9 elements**; more than that, split into two diagrams or fall back to
> prose — see the script's docstring for the full site-diagram section.

```json
{"title": "<floor label>", "rooms": [{"id": "…", "name": "…", "x": 0, "y": 0, "w": 3, "h": 3,
  "doors": [{"edge": "bottom", "pos": 0.5}]}]}
```

## Rumours & hooks
- <what locals say; which is true, which is a red herring>

## Clues present
- <clue → where it points> (keep to the three-clue rule across the scenario)

## Hazards / secrets
> **KEEPER ONLY** — <traps, hidden areas, the thing beneath, escalation triggers>

## Links
<relative links to scenes, NPCs, handouts>
