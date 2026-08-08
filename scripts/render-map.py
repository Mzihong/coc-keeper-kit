#!/usr/bin/env python3
"""Render a CoC Keeper Kit map DSL (JSON) into an SVG floor plan or site diagram.

Usage:  python scripts/render-map.py <path/to/map.json> [--player]

Writes the .svg file alongside the .json (same basename); `--player` writes
`<basename>-player.svg` instead, so the Keeper file and the handout file coexist. Deterministic
— same input always produces the same output byte-for-byte; there is no randomness and no
hand-drawn jitter (see `update_plan/2026-08-02-low-cost-maps.md` — that C/D-tier look was
evaluated and rejected).

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
         "windows": [{"edge": "top", "pos": 0.3}],
         "furniture": [{"s": "rect", "x": 1, "y": 0.5, "w": 2, "h": 0.4, "label": "书架"},
                       {"s": "circle", "x": 3, "y": 2, "r": 0.6, "label": "阅览桌"}]},
        {"id": "tower", "name": "塔楼", "shape": "circle", "cx": 6, "cy": 1.5, "r": 1}
      ],
      "stairs":   [{"x": 4.2, "y": 0.5, "w": 1, "h": 2, "direction": "up", "label": "通往二楼"}],
      "callouts": [{"x": 1, "y": 0.2, "text": "上锁的门 ?", "secret": true}],   // ① + side note
      "features": [{"s": "rect", "x": 8, "y": 1, "w": 3, "h": 2, "label": "果园"}],
      "paths":    [{"pts": [[0, 3], [2, 4], [5, 4]], "label": "小路,步行 5 分钟", "style": "dashed"}],
      "compass":  true,
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

## Furniture (B-tier, per room — the interactive/player-facing layer)

`furniture` lives on a room and is a list of `{"s": "rect"|"circle", ...size fields, "label"}`.
**No icon library** — a shape plus a label is the whole vocabulary (`interior-4`, the packed
Miskatonic library sample, has high furniture density but not one icon: shelves are thin
rectangles, tables are circles, everything else rides on the label text). Coordinates are in
grid units **relative to the room's own (x, y) origin** — `{"x": 1, "y": 0.5}` in a room at
`{"x": 5, "y": 2}` sits at world position `(6, 2.5)` — not the whole map's absolute coordinates,
because a model placing furniture only ever needs to think about one room at a time.

The renderer rejects (non-zero exit, no SVG written) any furniture item that falls outside its
room's own `w`/`h`, or that overlaps another furniture item in the same room — silently
rendering a sofa through a wall or on top of a desk is worse than refusing to draw it.

## Callouts: a numbered circle on the map, the note itself beside it

A `callout` is `{x, y, text, secret}` — an anchor point plus a sentence about what sits there.
It renders as **two separate things**: a small numbered circle (white fill, black rim, no leader
line) at the anchor, and a matching numbered entry in a fixed-width **note column down the right
side of the canvas**. The prose never touches the map surface.

This is the book's city/region-plate device (`district-*`, where dozens of sites can't fit their
own names) pulled down to room and site scale, and it applies **only to `callouts`**: room names
still sit inside their room, furniture and feature labels still sit on their shape — those are
short words. The one departure from the source plates is that the notes live inside the SVG
rather than in surrounding body text, because a `--player` render is a handout: the table has the
picture and nothing else.

The renderer cannot measure text (no font metrics, and reading system fonts would destroy
determinism), so `wrap_text()` estimates width from a frozen per-character table — CJK and other
fullwidth codepoints count 1.0 em, everything else 0.55 em — and breaks greedily, backing up to
the last space when it would otherwise split an ASCII word. It is an approximation that errs
toward extra whitespace; the goal is "not clipped, reads fine", not typesetting. The canvas is
`map width + note column`, and its height is `max(map, note column)` — a floor with more note
than picture makes the page taller, and nothing ever falls outside the `viewBox`.

Numbering is **declaration order in the DSL**, not sorted by position, so editing the JSON has a
predictable effect on which note is which number. **Restraint rule (not enforced by the
script):** one floor should carry **at most 8 callouts**. Past that you are pasting the location
text into the picture — split the diagram or send the detail back to the prose.

Placing an anchor is still the author's job: the disc is opaque, so an `(x, y)` on top of a room
name or a stair label punches a hole in it. Keep anchors off the room's centre line (that's where
the name sits) and a disc's width apart from each other; the check is cheap to eyeball once the
SVG exists.

## Site diagrams (B-tier reused at map scale — manor grounds, a farmstead, a churchyard)

An outdoor site is not a new diagram type: it is a floor plan with an **empty `rooms` array**
and only the graphic-primitive layer. `features` is the top-level (map-scale, absolute-coordinate)
counterpart of room `furniture` — same two shapes, same "shape + label, no icons" rule — for
things like a labelled forest block, an orchard, a free-standing outbuilding, or a folly.
`paths` draws a lane/stream/treeline as a polyline (`style: "solid"|"dashed"`); `compass: true`
draws a small fixed north arrow in the corner (the same fixture used on the book's city/region
plates). **Restraint rule (not enforced by the script):** a site diagram should read as 5–9
elements total — the farmstead sample in the source material gets by on four (a rise, a dashed
boundary, a ruined farmhouse, a well). More than that, split into two diagrams or fall back to
prose; what a shape can't say (how far, what's visible from where) belongs in the scene text,
not the picture.

## `--player`: the spoiler-safe render

`secret: true` on a room, a door, a furniture item, or a callout marks something the Keeper's
version can show but the table's version must not. **The KP file (no flag) always renders
everything, secrets included** (italicised for callouts) — it never filters, so it stays the
single working copy. Passing `--player` produces the second, filtered file:

- **Secret door** → the gap disappears; that stretch of wall renders solid, same as if no door
  were declared there. The door's existence, not just its lock state, is hidden.
- **Secret room / feature** → its `name`/`label` is replaced by `player_name`/`player_label` if
  given (a cover story — "储藏室" over "祭坛室"), otherwise left blank; the shape itself still
  renders; the room is not "not there" in an already-toured building.
- **Secret furniture item** → replaced by its `player_label` if given, otherwise omitted
  entirely — the default for something the table has no business perceiving at all (a hidden
  safe), while a `player_label` covers the "visible but its true nature is secret" case (a
  painting hiding a safe).
- **Secret callout** → dropped entirely from both the circle layer and the note column, rather
  than the KP file's italicised-but-visible treatment. Because the dropped ones leave holes in
  the numbering, **the player render renumbers its callouts consecutively** — a gap (①③④) would
  itself announce "there is a note here you aren't being shown". The two files therefore disagree
  about which number is which note, so the **KP note column carries a grey `(PL n)` cross-
  reference** on every non-secret callout: the Keeper's copy is its own translation table and can
  answer "look at ③" at the table without opening the handout.

A single DSL file renders both versions; never hand-author two files for the same room — they
would drift.

`stairs`, `windows`, and `legend` have no `secret` handling — none of the three can carry
KP-only information by construction.

stdlib only, no dependencies.
"""
import argparse
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
FURNITURE_INK = "#3a3a3a"
NOTE_MUTED = "#8a8a85"
NOTE_RULE = "#c9c9c4"
EPS = 1e-6

CALLOUT_R = 11          # px radius of the numbered circle sitting on the anchor
NOTE_COL = 260          # px text width of the note column down the right side
NOTE_FONT = 12
NOTE_LINE_H = 17        # px baseline-to-baseline inside one wrapped note
NOTE_GAP = 8            # px between two notes
LEGEND_FONT = 11
LEGEND_LINE_H = 15

# Frozen character-width table for `wrap_text`. Reading real font metrics would make the
# renderer non-deterministic (the hard constraint of the whole map plan), so width is estimated
# from the codepoint alone: anything in these ranges counts as one em, everything else as
# EM_NARROW. Deliberately generous — over-estimating costs whitespace, under-estimating costs a
# clipped line.
EM_WIDE = 1.0
EM_NARROW = 0.55
WIDE_RANGES = (
    (0x1100, 0x115F),   # Hangul Jamo
    (0x2013, 0x2014),   # en/em dash — set full-width in CJK text
    (0x2026, 0x2026),   # horizontal ellipsis, likewise
    (0x2460, 0x24FF),   # enclosed alphanumerics — the ① note markers themselves
    (0x2E80, 0xA4CF),   # CJK radicals through Yi: kana, CJK punctuation, CJK Unified
    (0xAC00, 0xD7A3),   # Hangul syllables
    (0xF900, 0xFAFF),   # CJK compatibility ideographs
    (0xFE30, 0xFE4F),   # CJK compatibility forms
    (0xFF00, 0xFF60),   # fullwidth forms
    (0xFFE0, 0xFFE6),   # fullwidth signs
)

def char_em(ch):
    o = ord(ch)
    for lo, hi in WIDE_RANGES:
        if lo <= o <= hi:
            return EM_WIDE
    return EM_NARROW


def text_px(s, font_size):
    """Estimated rendered width of `s`. See WIDE_RANGES — an approximation, on purpose."""
    return sum(char_em(c) for c in s) * font_size


def _is_word_char(ch):
    return ch.isascii() and (ch.isalnum() or ch in "-'")


def wrap_text(s, budget, font_size, first_budget=None):
    """Greedy, deterministic line breaking to a pixel budget, using the frozen width table.

    CJK breaks at any character (correct for Chinese); a run of ASCII word characters backs up
    to the last space on the line rather than splitting mid-word. `first_budget` narrows the
    first line only — the note column uses it to leave room for the `①` and `(PL n)` prefixes.
    A space that lands on a break is swallowed, so no line carries edge whitespace. Returns at
    least one (possibly empty) line."""
    lines, cur, cur_w = [], "", 0.0
    limit = budget if first_budget is None else first_budget
    for ch in s:
        if ch == "\n":
            lines.append(cur.rstrip())
            cur, cur_w, limit = "", 0.0, budget
            continue
        if ch == " " and not cur:
            continue
        w = char_em(ch) * font_size
        if cur and cur_w + w > limit:
            cut = cur.rfind(" ") if _is_word_char(ch) and _is_word_char(cur[-1]) else -1
            if cut > 0:
                lines.append(cur[:cut])
                cur = cur[cut + 1:]
            else:
                lines.append(cur.rstrip())
                cur = ""
            cur_w = text_px(cur, font_size)
            limit = budget
            if ch == " " and not cur:
                continue
        cur += ch
        cur_w += w
    if cur.rstrip():
        lines.append(cur.rstrip())
    return lines or [""]


def circled(n):
    """① … ⑳ for 1–20, plain (21) past that — the note column's number glyph."""
    return chr(0x2460 + n - 1) if 1 <= n <= 20 else f"({n})"


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


def visible_doors(room, player):
    doors = room.get("doors", [])
    if not player:
        return doors
    return [d for d in doors if not d.get("secret")]


def collect_wall_segments(rooms, player):
    """Every rectangular room's 4 edges, deduped by exact endpoint match. Returns
    {seg_key: {"p1", "p2", "count", "doors": [...], "windows": [...]}}. In player mode,
    secret doors are excluded from a wall's door list so that stretch renders solid."""
    walls = {}
    for room in rooms:
        if room.get("shape") == "circle":
            continue
        doors = visible_doors(room, player)
        for edge in ("top", "right", "bottom", "left"):
            p1, p2 = edge_segment(room, edge)
            key = seg_key(p1, p2)
            entry = walls.setdefault(key, {"p1": p1, "p2": p2, "count": 0, "doors": [], "windows": []})
            entry["count"] += 1
            for d in doors:
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


def room_display_name(room, player):
    if player and room.get("secret"):
        return room.get("player_name", "")
    return room.get("name", "")


def render_rooms(rooms, to_px, unit, player):
    out = []
    for room in rooms:
        name = room_display_name(room, player)
        if room.get("shape") == "circle":
            cx, cy = to_px((room["cx"], room["cy"]))
            r = room["r"] * unit
            out.append(f'<circle cx="{cx:.2f}" cy="{cy:.2f}" r="{r:.2f}" '
                        f'fill="{ROOM_FILL}" stroke="{INK}" stroke-width="{WALL_OUTER}"/>')
            if name:
                out.append(f'<text x="{cx:.2f}" y="{cy:.2f}" text-anchor="middle" '
                            f'dominant-baseline="middle" font-size="14">{name}</text>')
            continue
        x, y = to_px((room["x"], room["y"]))
        w, h = room["w"] * unit, room["h"] * unit
        out.append(f'<rect x="{x:.2f}" y="{y:.2f}" width="{w:.2f}" height="{h:.2f}" fill="{ROOM_FILL}"/>')
        if name:
            out.append(f'<text x="{x + w / 2:.2f}" y="{y + h / 2:.2f}" text-anchor="middle" '
                        f'dominant-baseline="middle" font-size="14">{name}</text>')
    return out


def furniture_bbox(item):
    if item["s"] == "rect":
        return item["x"], item["y"], item["x"] + item["w"], item["y"] + item["h"]
    if item["s"] == "circle":
        return item["x"] - item["r"], item["y"] - item["r"], item["x"] + item["r"], item["y"] + item["r"]
    raise ValueError(f"unknown shape {item['s']!r} (expected 'rect' or 'circle')")


def boxes_overlap(a, b):
    ax0, ay0, ax1, ay1 = a
    bx0, by0, bx1, by1 = b
    return ax0 < bx1 - EPS and bx0 < ax1 - EPS and ay0 < by1 - EPS and by0 < ay1 - EPS


def validate_furniture(rooms):
    """Non-zero-exit, don't-draw validation: furniture must stay inside its room, and must not
    overlap another piece of furniture in the same room. Silent mis-placement is worse than a
    refusal to render (see the docstring's Furniture section)."""
    for room in rooms:
        items = room.get("furniture", [])
        if not items:
            continue
        room_id = room.get("id", "?")
        if room.get("shape") == "circle":
            room_w = room_h = 2 * room["r"]
        else:
            room_w, room_h = room["w"], room["h"]
        boxes = []
        for item in items:
            label = item.get("label", item["s"])
            bx0, by0, bx1, by1 = furniture_bbox(item)
            if bx0 < -EPS or by0 < -EPS or bx1 > room_w + EPS or by1 > room_h + EPS:
                raise ValueError(
                    f"room '{room_id}': furniture '{label}' ({bx0:.2f},{by0:.2f})–({bx1:.2f},{by1:.2f}) "
                    f"falls outside the room's own {room_w:g}x{room_h:g} bounds")
            boxes.append((label, (bx0, by0, bx1, by1)))
        for i in range(len(boxes)):
            for j in range(i + 1, len(boxes)):
                if boxes_overlap(boxes[i][1], boxes[j][1]):
                    raise ValueError(
                        f"room '{room_id}': furniture '{boxes[i][0]}' overlaps '{boxes[j][0]}'")


def render_shape_layer(items, origin, to_px, unit, player, missing_id):
    """Shared renderer for room `furniture` (origin = room's x,y) and top-level `features`
    (origin = (0, 0)) — same two primitives, same secret/player_label handling."""
    out = []
    ox, oy = origin
    for item in items:
        if player and item.get("secret") and "player_label" not in item:
            continue
        if player and item.get("secret"):
            label = item["player_label"]
        else:
            label = item.get("label", "")
        if item["s"] == "rect":
            px, py = to_px((ox + item["x"], oy + item["y"]))
            w, h = item["w"] * unit, item["h"] * unit
            out.append(f'<rect x="{px:.2f}" y="{py:.2f}" width="{w:.2f}" height="{h:.2f}" '
                        f'fill="none" stroke="{FURNITURE_INK}" stroke-width="1.5"/>')
            if label:
                out.append(f'<text x="{px + w / 2:.2f}" y="{py + h / 2:.2f}" text-anchor="middle" '
                            f'dominant-baseline="middle" font-size="10">{label}</text>')
        elif item["s"] == "circle":
            cx, cy = to_px((ox + item["x"], oy + item["y"]))
            r = item["r"] * unit
            out.append(f'<circle cx="{cx:.2f}" cy="{cy:.2f}" r="{r:.2f}" '
                        f'fill="none" stroke="{FURNITURE_INK}" stroke-width="1.5"/>')
            if label:
                out.append(f'<text x="{cx:.2f}" y="{cy + r + 12:.2f}" text-anchor="middle" '
                            f'font-size="10">{label}</text>')
        else:
            raise ValueError(f"{missing_id}: unknown shape {item['s']!r} (expected 'rect' or 'circle')")
    return out


def render_furniture(rooms, to_px, unit, player):
    out = []
    for room in rooms:
        if room.get("shape") == "circle" or not room.get("furniture"):
            continue
        out += render_shape_layer(room["furniture"], (room["x"], room["y"]), to_px, unit, player,
                                   f"room '{room.get('id', '?')}'")
    return out


def render_features(features, to_px, unit, player):
    return render_shape_layer(features, (0, 0), to_px, unit, player, "features")


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


def number_callouts(callouts, player):
    """Assign each callout the number it wears in this render, in DSL declaration order.

    Returns `(n, pl, callout)` triples for the callouts this version shows. On the KP render
    `n` is the declaration index and `pl` is the number the same callout will carry in the
    player render (`None` for secret ones, which the player file drops). On the player render
    the secrets are gone and `n` is the resequenced, gap-free number — a hole in the numbering
    would advertise the note it hides."""
    out, pl = [], 0
    for i, c in enumerate(callouts, start=1):
        secret = bool(c.get("secret"))
        if not secret:
            pl += 1
        if player:
            if not secret:
                out.append((pl, None, c))
        else:
            out.append((i, None if secret else pl, c))
    return out


def render_callout_circles(numbered, to_px):
    """The on-map half: a numbered disc at the anchor, no leader line (the book's plates have
    none — the circle already sits on the thing it annotates). Drawn after the walls so the
    white fill punches through anything underneath."""
    out = []
    for n, _pl, c in numbered:
        cx, cy = to_px((c["x"], c["y"]))
        out.append(f'<circle cx="{cx:.2f}" cy="{cy:.2f}" r="{CALLOUT_R}" fill="{ROOM_FILL}" '
                    f'stroke="{INK}" stroke-width="1.5"/>')
        out.append(f'<text x="{cx:.2f}" y="{cy:.2f}" text-anchor="middle" '
                    f'dominant-baseline="middle" font-size="12" font-weight="bold">{n}</text>')
    return out


def layout_notes(numbered):
    """Wrap every visible callout to the note column's fixed width. One function does the
    wrapping for both the height calculation and the drawing, so the canvas can never be sized
    for a different number of lines than get drawn. Returns (blocks, total_px_height)."""
    blocks = []
    for n, pl, c in numbered:
        num = circled(n)
        num_w = text_px(num + " ", NOTE_FONT)
        marker = f"(PL {circled(pl)})" if pl is not None else ""
        marker_w = text_px(marker + " ", NOTE_FONT) if marker else 0.0
        lines = wrap_text(c["text"], NOTE_COL - num_w, NOTE_FONT,
                          first_budget=NOTE_COL - num_w - marker_w)
        blocks.append({"num": num, "num_w": num_w, "marker": marker, "marker_w": marker_w,
                       "lines": lines, "secret": bool(c.get("secret"))})
    height = sum(len(b["lines"]) * NOTE_LINE_H + NOTE_GAP for b in blocks)
    return blocks, height


def render_notes(blocks, x0, y0):
    """The beside-the-map half: `① (PL ②) 注释…`, hanging-indented under the number, wrapped.
    Secret notes stay italic here, the same treatment stage 1 gave them on the map surface."""
    out = []
    y = y0
    for b in blocks:
        style = ' font-style="italic"' if b["secret"] else ""
        first = y + NOTE_LINE_H - 4
        out.append(f'<text x="{x0:.2f}" y="{first:.2f}" font-size="{NOTE_FONT}" '
                    f'font-weight="bold">{b["num"]}</text>')
        if b["marker"]:
            out.append(f'<text x="{x0 + b["num_w"]:.2f}" y="{first:.2f}" font-size="{NOTE_FONT}" '
                        f'fill="{NOTE_MUTED}">{b["marker"]}</text>')
        for i, line in enumerate(b["lines"]):
            lx = x0 + b["num_w"] + (b["marker_w"] if i == 0 else 0.0)
            out.append(f'<text x="{lx:.2f}" y="{first + i * NOTE_LINE_H:.2f}" '
                        f'font-size="{NOTE_FONT}"{style}>{line}</text>')
        y += len(b["lines"]) * NOTE_LINE_H + NOTE_GAP
    return out


def render_paths(paths, to_px):
    out = []
    for p in paths:
        pts = [to_px(tuple(pt)) for pt in p["pts"]]
        points_str = " ".join(f"{x:.2f},{y:.2f}" for x, y in pts)
        dash = ' stroke-dasharray="6,4"' if p.get("style") == "dashed" else ""
        out.append(f'<polyline points="{points_str}" fill="none" stroke="{INK}" stroke-width="2"{dash}/>')
        if p.get("label"):
            mx, my = pts[len(pts) // 2]
            out.append(f'<text x="{mx:.2f}" y="{my - 6:.2f}" font-size="11">{p["label"]}</text>')
    return out


def render_compass(map_w):
    """Fixed north arrow, top-right corner *of the map area* (not of the whole canvas — the note
    column is page furniture, the compass belongs to the picture), drawn in pixel space: it
    doesn't participate in the grid-unit coordinate system since it isn't part of the place."""
    cx, cy = map_w - PAD - 6, PAD + 26
    return [
        f'<line x1="{cx:.2f}" y1="{cy + 12:.2f}" x2="{cx:.2f}" y2="{cy - 10:.2f}" '
        f'stroke="{INK}" stroke-width="1.5"/>',
        f'<polyline points="{cx - 5:.2f},{cy - 3:.2f} {cx:.2f},{cy - 12:.2f} {cx + 5:.2f},{cy - 3:.2f}" '
        f'fill="none" stroke="{INK}" stroke-width="1.5"/>',
        f'<text x="{cx:.2f}" y="{cy - 16:.2f}" text-anchor="middle" font-size="11">N</text>',
    ]


def render_legend(lines, top):
    """Footer strip under everything else. Wrapped by the caller with the same `wrap_text()` the
    note column uses — a single unwrapped `<text>` used to run off the right edge here too."""
    return [f'<text x="{PAD}" y="{top + 12 + i * LEGEND_LINE_H:.2f}" font-size="{LEGEND_FONT}" '
            f'fill="#444">{line}</text>' for i, line in enumerate(lines)]


def render(dsl, player=False):
    unit = dsl.get("unit", DEFAULT_UNIT)
    rooms = dsl.get("rooms", [])
    stairs = dsl.get("stairs", [])
    callouts = dsl.get("callouts", [])
    features = dsl.get("features", [])
    paths = dsl.get("paths", [])
    legend = dsl.get("legend", [])

    validate_furniture(rooms)
    numbered = number_callouts(callouts, player)

    # A callout occupies exactly its circle — the old `c["x"] + 1` reserved a grid unit of fake
    # room for text that is no longer drawn on the map at all.
    callout_pad = CALLOUT_R / unit
    path_pts = [pt for p in paths for pt in p["pts"]]
    max_x = max([r["x"] + r["w"] for r in rooms if r.get("shape") != "circle"] +
                [r["cx"] + r["r"] for r in rooms if r.get("shape") == "circle"] +
                [s["x"] + s["w"] for s in stairs] +
                [c["x"] + callout_pad for _n, _pl, c in numbered] +
                [f["x"] + f.get("w", f.get("r", 0)) for f in features] +
                [pt[0] for pt in path_pts] + [1])
    max_y = max([r["y"] + r["h"] for r in rooms if r.get("shape") != "circle"] +
                [r["cy"] + r["r"] for r in rooms if r.get("shape") == "circle"] +
                [s["y"] + s["h"] for s in stairs] +
                [c["y"] + callout_pad for _n, _pl, c in numbered] +
                [f["y"] + f.get("h", f.get("r", 0)) for f in features] +
                [pt[1] for pt in path_pts] + [1])

    title_h = 28 if dsl.get("title") else 0
    map_w = max_x * unit + PAD * 2
    map_h = max_y * unit + PAD * 2 + title_h

    # Canvas = map + note column side by side; its height is whichever of the two is taller, so
    # a floor with more note than picture grows the page instead of clipping the notes.
    note_blocks, notes_h = layout_notes(numbered)
    notes_top = PAD + title_h
    width = map_w + NOTE_COL + PAD if note_blocks else map_w
    body_h = max(map_h, notes_top + notes_h + PAD) if note_blocks else map_h
    legend_lines = wrap_text(" · ".join(legend), width - PAD * 2, LEGEND_FONT) if legend else []
    legend_h = len(legend_lines) * LEGEND_LINE_H + 8 if legend_lines else 0
    height = body_h + legend_h

    def to_px(p):
        return (p[0] * unit + PAD, p[1] * unit + PAD + title_h)

    walls = collect_wall_segments(rooms, player)

    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width:.0f}" height="{height:.0f}" '
             f'viewBox="0 0 {width:.0f} {height:.0f}" font-family="sans-serif">',
             f'<rect x="0" y="0" width="{width:.0f}" height="{height:.0f}" fill="{PAGE_BG}"/>']
    if dsl.get("title"):
        parts.append(f'<text x="{PAD}" y="24" font-size="16" font-weight="bold">{dsl["title"]}</text>')
    parts += render_rooms(rooms, to_px, unit, player)
    parts += render_walls(walls, to_px)
    parts += render_furniture(rooms, to_px, unit, player)
    parts += render_features(features, to_px, unit, player)
    parts += render_paths(paths, to_px)
    parts += render_stairs(stairs, to_px, unit)
    parts += render_callout_circles(numbered, to_px)
    if dsl.get("compass"):
        parts += render_compass(map_w)
    if note_blocks:
        rule_x = map_w - PAD / 2
        parts.append(f'<line x1="{rule_x:.2f}" y1="{notes_top:.2f}" x2="{rule_x:.2f}" '
                     f'y2="{body_h - PAD:.2f}" stroke="{NOTE_RULE}" stroke-width="1"/>')
        parts += render_notes(note_blocks, map_w, notes_top)
    parts += render_legend(legend_lines, body_h)
    parts.append("</svg>")
    return "\n".join(parts)


def main():
    # Windows consoles default to a non-UTF-8 codepage; error messages here can carry Chinese
    # room/furniture labels, so reconfigure before anything prints (same fix as roll.py).
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")

    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("path", type=pathlib.Path, help="path to the map DSL .json file")
    parser.add_argument("--player", action="store_true",
                         help="render the spoiler-filtered, table-safe version")
    args = parser.parse_args()

    dsl = json.loads(args.path.read_text(encoding="utf-8"))
    try:
        svg = render(dsl, player=args.player)
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        sys.exit(1)

    out = args.path.with_name(args.path.stem + "-player.svg") if args.player else args.path.with_suffix(".svg")
    out.write_text(svg, encoding="utf-8")
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()
