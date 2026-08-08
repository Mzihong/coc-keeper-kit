#!/usr/bin/env python3
"""Render a CoC Keeper Kit map DSL (JSON) into an SVG floor plan.

Usage:  python scripts/render-map.py <path/to/map.json>

Writes the .svg file alongside the .json (same basename). Deterministic — same input always
produces the same output byte-for-byte; there is no randomness and no hand-drawn jitter (see
`update_plan/2026-08-02-low-cost-maps.md` — that C/D-tier look was evaluated and rejected).

One DSL file = one floor / one image. A multi-storey building is multiple DSL files
("manor-1f.json", "manor-2f.json", ...) rendered separately and stacked in the location's
Markdown, not one file with nested floors — see `reference/craft/town-anatomy-zh.md`-adjacent
plan note "每层一张图纵向堆叠,不做楼层叠加".

DSL shape (all coordinates in grid units, not pixels — `unit` controls the pixel scale):

    {
      "title": "<shown above the map>",
      "unit": 40,                              // optional, px per grid unit, default 40
      "rooms": [
        {"id": "hall", "name": "门厅", "x": 0, "y": 0, "w": 4, "h": 3,
         "doors":   [{"edge": "bottom", "pos": 0.5, "width": 0.6}],
         "windows": [{"edge": "top", "pos": 0.3}]},
        {"id": "tower", "name": "塔楼", "shape": "circle", "cx": 6, "cy": 1.5, "r": 1}
      ],
      "stairs":   [{"x": 4.2, "y": 0.5, "w": 1, "h": 2, "direction": "up", "label": "通往二楼"}],
      "callouts": [{"x": 1, "y": 0.2, "text": "上锁的门 ?", "secret": true}],
      "legend":   ["门厅 = 唯一对外出入口"]
    }

Two rooms that share a wall must give that wall's edge the *exact same span* (same two
endpoints) in both rooms' x/y/w/h — the renderer dedupes and thins a wall by matching
endpoints exactly, not by proximity. A partial overlap still renders (as two exterior
segments, a visible seam) rather than erroring — this is a prototype-tier renderer, not a
CAD tool.

`doors`/`windows` are addressed by `edge` ("top"/"right"/"bottom"/"left") + `pos` (0–1 fraction
along that edge, measured from the edge's canonical start — top/bottom run left→right,
left/right run top→bottom) rather than absolute coordinates, because a model computing
absolute door coordinates reliably gets them wrong; edge+fraction never drifts off the wall.

`secret: true` on a room/callout/door is schema-forward for the `--player` filter that stage 2
(the furniture layer) adds — this renderer always renders everything, it never filters. Stage 1
output is Keeper-facing only (see the plan's functest-one/two split).

stdlib only, no dependencies.
"""
import json
import sys
import pathlib

DEFAULT_UNIT = 40
PAD = 40
WALL_OUTER = 6
WALL_INNER = 3
ROOM_FILL = "#ffffff"
PAGE_BG = "#f2f2f0"
INK = "#1a1a1a"

EDGE_ENDPOINTS = {
    # (dx1, dy1, dx2, dy2) as fractions of (w, h) from the room's (x, y) corner —
    # canonical direction fixed here so pos=0..1 means the same physical point regardless of
    # which room's door/window list references the shared edge.
    "top": (0, 0, 1, 0),
    "bottom": (0, 1, 1, 1),
    "left": (0, 0, 0, 1),
    "right": (1, 0, 1, 1),
}


def edge_segment(room, edge):
    x, y, w, h = room["x"], room["y"], room["w"], room["h"]
    dx1, dy1, dx2, dy2 = EDGE_ENDPOINTS[edge]
    return (round(x + dx1 * w, 4), round(y + dy1 * h, 4)), (round(x + dx2 * w, 4), round(y + dy2 * h, 4))


def seg_key(p1, p2):
    return frozenset((p1, p2))


def lerp(p1, p2, t):
    return (p1[0] + (p2[0] - p1[0]) * t, p1[1] + (p2[1] - p1[1]) * t)


def collect_wall_segments(rooms):
    """Every rectangular room's 4 edges, deduped by exact endpoint match. Returns
    {seg_key: {"p1", "p2", "count", "doors": [...], "windows": [...]}}."""
    walls = {}
    for room in rooms:
        if room.get("shape") == "circle":
            continue
        for edge in ("top", "right", "bottom", "left"):
            p1, p2 = edge_segment(room, edge)
            key = seg_key(p1, p2)
            entry = walls.setdefault(key, {"p1": p1, "p2": p2, "count": 0, "doors": [], "windows": []})
            entry["count"] += 1
            for d in room.get("doors", []):
                if d["edge"] == edge:
                    entry["doors"].append(d)
            for w in room.get("windows", []):
                if w["edge"] == edge:
                    entry["windows"].append(w)
    return walls


def wall_sub_segments(p1, p2, doors):
    """Split a wall segment into the pieces that remain solid once each door's gap is cut
    out, plus the list of door gaps (as (gap_start_point, gap_end_point)) for drawing wedges."""
    cuts = []
    for d in doors:
        width = d.get("width", 0.6)
        span = max(abs(p2[0] - p1[0]), abs(p2[1] - p1[1])) or 1
        half = min(width / span, 0.49) / 2
        pos = min(max(d["pos"], half), 1 - half)
        cuts.append((pos - half, pos + half))
    cuts.sort()
    pieces, gaps, cursor = [], [], 0.0
    for start, end in cuts:
        if start > cursor:
            pieces.append((cursor, start))
        gaps.append((start, end))
        cursor = max(cursor, end)
    if cursor < 1.0:
        pieces.append((cursor, 1.0))
    return pieces, gaps


def svg_line(p1, p2, width, dash=None, cls=""):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return (f'<line x1="{p1[0]:.2f}" y1="{p1[1]:.2f}" x2="{p2[0]:.2f}" y2="{p2[1]:.2f}" '
            f'stroke="{INK}" stroke-width="{width}" stroke-linecap="square"{d} class="{cls}"/>')


def render_walls(walls, to_px):
    out = []
    for entry in walls.values():
        p1, p2, count = entry["p1"], entry["p2"], entry["count"]
        width = WALL_INNER if count >= 2 else WALL_OUTER
        pieces, gaps = wall_sub_segments(p1, p2, entry["doors"])
        for a, b in pieces:
            out.append(svg_line(to_px(lerp(p1, p2, a)), to_px(lerp(p1, p2, b)), width))
        for a, b in gaps:
            ga, gb = lerp(p1, p2, a), lerp(p1, p2, b)
            gax, gay = to_px(ga)
            gbx, gby = to_px(gb)
            # Apex sits perpendicular to the gap, offset by half the gap's own length — a
            # fixed 45° wedge (∧) regardless of gap size, not an arc.
            mx, my = (gax + gbx) / 2, (gay + gby) / 2
            dx, dy = gbx - gax, gby - gay
            length = (dx ** 2 + dy ** 2) ** 0.5 or 1
            ox, oy = -dy / length, dx / length
            apex = (mx + ox * length / 2, my + oy * length / 2)
            out.append(f'<polyline points="{gax:.2f},{gay:.2f} {apex[0]:.2f},{apex[1]:.2f} '
                       f'{gbx:.2f},{gby:.2f}" fill="none" stroke="{INK}" stroke-width="2"/>')
        for win in entry["windows"]:
            wp = lerp(p1, p2, win["pos"])
            wx, wy = to_px(wp)
            dx, dy = p2[0] - p1[0], p2[1] - p1[1]
            length = (dx ** 2 + dy ** 2) ** 0.5 or 1
            ox, oy = -dy / length, dx / length
            span = 10
            out.append(svg_line((wx - dx / length * span, wy - dy / length * span),
                                 (wx + dx / length * span, wy + dy / length * span),
                                 3, dash="4,3"))
    return out


def render_rooms(rooms, to_px, unit):
    out = []
    for room in rooms:
        if room.get("shape") == "circle":
            cx, cy = to_px((room["cx"], room["cy"]))
            r = room["r"] * unit
            out.append(f'<circle cx="{cx:.2f}" cy="{cy:.2f}" r="{r:.2f}" '
                        f'fill="{ROOM_FILL}" stroke="{INK}" stroke-width="{WALL_OUTER}"/>')
            out.append(f'<text x="{cx:.2f}" y="{cy:.2f}" text-anchor="middle" '
                        f'dominant-baseline="middle" font-size="14">{room["name"]}</text>')
            continue
        x, y = to_px((room["x"], room["y"]))
        w, h = room["w"] * unit, room["h"] * unit
        out.append(f'<rect x="{x:.2f}" y="{y:.2f}" width="{w:.2f}" height="{h:.2f}" fill="{ROOM_FILL}"/>')
        out.append(f'<text x="{x + w / 2:.2f}" y="{y + h / 2:.2f}" text-anchor="middle" '
                    f'dominant-baseline="middle" font-size="14">{room["name"]}</text>')
    return out


def render_stairs(stairs, to_px, unit):
    out = []
    for s in stairs:
        x, y = to_px((s["x"], s["y"]))
        w, h = s["w"] * unit, s["h"] * unit
        out.append(f'<rect x="{x:.2f}" y="{y:.2f}" width="{w:.2f}" height="{h:.2f}" '
                    f'fill="none" stroke="{INK}" stroke-width="2"/>')
        step = max(h, w) / 6
        for i in range(1, 6):
            if h >= w:
                yy = y + step * i
                out.append(svg_line((x, yy), (x + w, yy), 1))
            else:
                xx = x + step * i
                out.append(svg_line((xx, y), (xx, y + h), 1))
        arrow = "↑" if s.get("direction") == "up" else "↓"
        label = s.get("label", "")
        out.append(f'<text x="{x + w / 2:.2f}" y="{y + h + 14:.2f}" text-anchor="middle" '
                    f'font-size="13">{arrow} {label}</text>')
    return out


def render_callouts(callouts, to_px):
    out = []
    for c in callouts:
        ax, ay = to_px((c["x"], c["y"]))
        tx, ty = ax + 24, ay - 20
        out.append(svg_line((ax, ay), (tx, ty), 1))
        style = ' font-style="italic"' if c.get("secret") else ""
        out.append(f'<text x="{tx + 4:.2f}" y="{ty:.2f}" font-size="12"{style}>{c["text"]}</text>')
    return out


def render_legend(legend, width, height):
    if not legend:
        return []
    out = [f'<text x="{PAD}" y="{height - 8}" font-size="11" fill="#444">'
           f'{" · ".join(legend)}</text>']
    return out


def render(dsl):
    unit = dsl.get("unit", DEFAULT_UNIT)
    rooms = dsl.get("rooms", [])
    stairs = dsl.get("stairs", [])
    callouts = dsl.get("callouts", [])
    legend = dsl.get("legend", [])

    max_x = max([r["x"] + r["w"] for r in rooms if r.get("shape") != "circle"] +
                [r["cx"] + r["r"] for r in rooms if r.get("shape") == "circle"] +
                [s["x"] + s["w"] for s in stairs] + [c["x"] + 1 for c in callouts] + [1])
    max_y = max([r["y"] + r["h"] for r in rooms if r.get("shape") != "circle"] +
                [r["cy"] + r["r"] for r in rooms if r.get("shape") == "circle"] +
                [s["y"] + s["h"] for s in stairs] + [c["y"] + 1 for c in callouts] + [1])

    title_h = 28 if dsl.get("title") else 0
    legend_h = 20 if legend else 0
    width = max_x * unit + PAD * 2
    height = max_y * unit + PAD * 2 + title_h + legend_h

    def to_px(p):
        return (p[0] * unit + PAD, p[1] * unit + PAD + title_h)

    walls = collect_wall_segments(rooms)

    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width:.0f}" height="{height:.0f}" '
             f'viewBox="0 0 {width:.0f} {height:.0f}" font-family="sans-serif">',
             f'<rect x="0" y="0" width="{width:.0f}" height="{height:.0f}" fill="{PAGE_BG}"/>']
    if dsl.get("title"):
        parts.append(f'<text x="{PAD}" y="24" font-size="16" font-weight="bold">{dsl["title"]}</text>')
    parts += render_rooms(rooms, to_px, unit)
    parts += render_walls(walls, to_px)
    parts += render_stairs(stairs, to_px, unit)
    parts += render_callouts(callouts, to_px)
    parts += render_legend(legend, width, height)
    parts.append("</svg>")
    return "\n".join(parts)


def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <path/to/map.json>", file=sys.stderr)
        sys.exit(1)
    src = pathlib.Path(sys.argv[1])
    dsl = json.loads(src.read_text(encoding="utf-8"))
    svg = render(dsl)
    out = src.with_suffix(".svg")
    out.write_text(svg, encoding="utf-8")
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()
