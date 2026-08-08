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
