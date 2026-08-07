#!/usr/bin/env python3
"""Render a CoC Keeper Kit investigator JSON record into its Markdown card.

Usage:  python scripts/render-investigator.py [--strict] campaigns/<slug>/investigators/<name>.json

Writes the .md file alongside the .json (same basename). Deterministic — never invents
values; a missing *required-shape* field renders as the template's own "<...>" placeholder
so gaps stay visible instead of silently disappearing. Optional sections (spells, gear,
party, ...) are omitted entirely when the JSON has nothing to say — that keeps a plain
pregen card short instead of padding it with empty headers.

The card is always KP-facing (core/13-create-investigator.md) — every field renders
regardless of `type`; nothing is held back for "elite-npc" vs "pregen".

Self-validation runs on every render and reports to stderr:
- hard arithmetic (derived-stat formulas, the skill-point ledger, per-skill totals) — these
  are never configurable, they're just 7e maths.
- threshold checks (creation-time skill cap, characteristic ranges) — configurable per
  campaign via campaigns/<slug>/investigators/validation.json (falls back to the defaults
  below, which mirror reference/rules/character-creation.md, if that file is absent).

By default, violations are warned but the card still renders. `--strict` turns any hard
*error* into a hard failure (nothing is written) — warnings never abort the render, even
under `--strict`, because several of them (e.g. the characteristic-range check) are
threshold checks with known legitimate exceptions (point-buy, an aged/scaled NPC) rather
than unconditional 7e maths.

stdlib only, no dependencies.
"""
import json
import re
import sys
import pathlib

PLACEHOLDER = "<...>"

BACKSTORY_FIELDS = [
    ("Description", "description"),
    ("Ideology/beliefs", "ideology_beliefs"),
    ("Significant people", "significant_people"),
    ("Meaningful locations", "meaningful_locations"),
    ("Treasured possessions", "treasured_possessions"),
    ("Traits", "traits"),
    ("Injuries/scars", "injuries_scars"),
    ("Phobias/manias", "phobias_manias"),
]

CHARACTERISTICS = ["STR", "CON", "SIZ", "DEX", "APP", "INT", "POW", "EDU"]

# Keep in sync with campaigns/_template-campaign/investigators/validation.json — that's the
# file a fresh campaign's validation.json gets copied from at intake (core/01 question 14).
DEFAULT_VALIDATION = {
    "skill_cap": 90,
    "characteristic_ranges": {
        "STR": [15, 90], "CON": [15, 90], "DEX": [15, 90],
        "APP": [15, 90], "POW": [15, 90], "Luck": [15, 90],
        "SIZ": [40, 90], "INT": [40, 90], "EDU": [40, 99],
    },
}

# (min STR+SIZ, max STR+SIZ, Build, DamageBonus labels) — reference/rules/character-creation.md §3
BUILD_BANDS = [
    (2, 64, -2, ["-2", "−2"]),
    (65, 84, -1, ["-1", "−1"]),
    (85, 124, 0, ["none", "0"]),
    (125, 164, 1, ["+1D4"]),
    (165, 204, 2, ["+1D6"]),
    (205, 284, 3, ["+2D6"]),
    (285, 364, 4, ["+3D6"]),
    (365, 444, 5, ["+4D6"]),
]


def skill_label(skill):
    """Umbrella skills (Science, Art/Craft, Fighting, ...) are meaningless without their
    specialisation — two "Science" entries on one card are indistinguishable otherwise."""
    name = skill.get("name", "?")
    spec = skill.get("specialization")
    return f"{name} ({spec})" if spec else name


def fmt_skills(skills):
    if not skills:
        return PLACEHOLDER
    return ", ".join(f"{skill_label(s)} {s.get('value', '?')}%" for s in skills)


def fmt_weapons(weapons):
    if not weapons:
        return f"- {PLACEHOLDER} *(omit if unarmed/non-combatant)*"
    return "\n".join(
        f"- {w.get('name', '?')}, {w.get('skill_pct', '?')}%, {w.get('damage', '?')}"
        for w in weapons
    )


def fmt_gear(gear):
    lines = []
    for g in gear:
        if isinstance(g, str):
            lines.append(f"- {g}")
        else:
            name = g.get("name", "?")
            notes = g.get("notes")
            lines.append(f"- {name}" + (f" — {notes}" if notes else ""))
    return "\n".join(lines)


def fmt_spells(spells):
    lines = []
    for s in spells:
        if isinstance(s, str):
            lines.append(f"- {s}")
        else:
            bits = [s.get("name", "?")]
            if s.get("cost"):
                bits.append(f"({s['cost']})")
            line = "- " + " ".join(bits)
            if s.get("effect"):
                line += f" — {s['effect']}"
            lines.append(line)
    return "\n".join(lines)


def fmt_experience_packages(packages):
    lines = []
    for p in packages:
        bits = [p.get("name", "?")]
        if p.get("san_cost"):
            bits.append(f"(SAN {p['san_cost']})")
        line = "- " + " ".join(bits)
        extra = []
        if p.get("grants"):
            extra.append(f"grants: {p['grants']}")
        if p.get("requires"):
            extra.append(f"requires: {p['requires']}")
        if extra:
            line += " — " + "; ".join(extra)
        lines.append(line)
    return "\n".join(lines)


def fmt_mythos_encounters(encounters):
    lines = []
    for e in encounters:
        bits = [e.get("entity", "?")]
        if e.get("result"):
            bits.append(f"— {e['result']}")
        line = "- " + " ".join(bits)
        if e.get("notes"):
            line += f" ({e['notes']})"
        lines.append(line)
    return "\n".join(lines)


def fmt_growth_log(entries):
    lines = []
    for g in entries:
        session = g.get("session")
        prefix = f"[{session}] " if session else ""
        lines.append(f"- {prefix}{g.get('change', '?')}")
    return "\n".join(lines)


def fmt_party(party):
    lines = []
    for p in party:
        bits = [p.get("name", "?")]
        if p.get("player"):
            bits.append(f"(player: {p['player']})")
        line = "- " + " ".join(bits)
        if p.get("relationship"):
            line += f" — {p['relationship']}"
        lines.append(line)
    return "\n".join(lines)


def fmt_occupation_skills(items):
    return ", ".join(items) if items else PLACEHOLDER


def render(inv):
    c = inv.get("characteristics", {})
    d = inv.get("derived", {})
    cr = inv.get("credit_rating") or {}
    od = inv.get("occupation_detail") or {}
    am = inv.get("age_modifiers") or {}
    sp = inv.get("skill_points") or {}
    bs = inv.get("backstory", {})
    status = inv.get("status") or {}
    hooks = inv.get("hooks") or [PLACEHOLDER]
    links = inv.get("links") or [PLACEHOLDER]

    lines = [
        f"# {inv.get('name', PLACEHOLDER)}",
        "",
        f"*{inv.get('concept', PLACEHOLDER)}*",
        "",
        f"- **Occupation:** {inv.get('occupation', PLACEHOLDER)} · "
        f"**Era/locale:** {inv.get('era_locale', PLACEHOLDER)}",
        f"- **Type:** {inv.get('type', 'pregen')}",
        "",
        "## Characteristics",
        "| " + " | ".join(CHARACTERISTICS) + " |",
        "|" + "|".join(["-----"] * len(CHARACTERISTICS)) + "|",
        "| " + " | ".join(str(c.get(k, "00")) for k in CHARACTERISTICS) + " |",
        "",
        f"- **HP** {d.get('HP', 0)} · **MP** {d.get('MP', 0)} · **SAN** {d.get('SAN', 0)} · "
        f"**Luck** {d.get('Luck', 0)} · **Move** {d.get('Move', 0)} · "
        f"**Build** {d.get('Build', 0)} · **Damage Bonus** {d.get('DamageBonus', 0)} · "
        f"**Dodge** {d.get('Dodge', 0)}",
        f"- **Cthulhu Mythos:** {inv.get('cthulhu_mythos', 0)}% · "
        f"**SAN max:** {d.get('SAN_max', PLACEHOLDER)}",
    ]
    if d.get("Armor"):
        lines.append(f"- **Armor:** {d['Armor']}")

    lines += ["", "## Credit Rating"]
    lines.append(
        f"- **Value:** {cr.get('value', PLACEHOLDER)} ({cr.get('band', PLACEHOLDER)}) · "
        f"**Lifestyle:** {cr.get('lifestyle', PLACEHOLDER)}"
    )
    lines.append(
        f"- **Cash:** {cr.get('cash', PLACEHOLDER)} · **Assets:** {cr.get('assets', PLACEHOLDER)} · "
        f"**Spending level:** {cr.get('spending_level', PLACEHOLDER)} "
        f"({cr.get('currency', PLACEHOLDER)})"
    )
    if cr.get("asset_notes"):
        lines.append(f"- **Assets are:** {cr['asset_notes']}")

    if od:
        lines += ["", "## Occupation detail"]
        lines.append(f"- **Skill points formula:** {od.get('skill_points_formula', PLACEHOLDER)}")
        lines.append(f"- **Credit Rating band:** {od.get('credit_rating_band', PLACEHOLDER)}")
        lines.append(f"- **Occupation skills:** {fmt_occupation_skills(od.get('occupation_skills'))}")
        if od.get("contacts"):
            lines.append(f"- **Contacts:** {od['contacts']}")

    if am or sp:
        lines += ["", "## Creation ledger (KP audit)"]
        if am:
            lines.append(
                f"- **Age band:** {am.get('band', PLACEHOLDER)} · "
                f"**Physical deduction:** {am.get('physical_deduction', 0)}"
                + (f" ({am['deduction_split']})" if am.get("deduction_split") else "")
            )
            lines.append(
                f"- **APP penalty:** {am.get('app_penalty', 0)} · "
                f"**EDU penalty:** {am.get('edu_penalty', 0)} · "
                f"**EDU checks:** {am.get('edu_improvement_checks', 0)} "
                f"(gained {am.get('edu_gained', 0)}) · "
                f"**Move penalty:** {am.get('move_penalty', 0)}"
                + (f" · **Luck rolls:** {am['luck_rolls']}" if am.get("luck_rolls") else "")
            )
        if sp:
            lines.append(
                f"- **Occupation points:** {sp.get('occupation_spent', PLACEHOLDER)} / "
                f"{sp.get('occupation_total', PLACEHOLDER)} · "
                f"**Interest points:** {sp.get('interest_spent', PLACEHOLDER)} / "
                f"{sp.get('interest_total', PLACEHOLDER)}"
                + (f" · **Cap:** {sp['cap']}" if sp.get("cap") else "")
            )

    lines += ["", "## Skills", fmt_skills(inv.get("skills")), "", "## Weapons", fmt_weapons(inv.get("weapons"))]

    gear = inv.get("gear")
    if gear:
        lines += ["", "## Gear", fmt_gear(gear)]

    spells = inv.get("spells")
    if spells:
        lines += ["", "## Spells", fmt_spells(spells)]

    if status:
        lines += ["", "## Status"]
        lines.append(
            f"- **Physical:** {status.get('physical', PLACEHOLDER)} · "
            f"**Mental:** {status.get('mental', PLACEHOLDER)}"
        )
        if status.get("phobias"):
            lines.append(f"- **Phobias:** {', '.join(status['phobias'])}")
        if status.get("manias"):
            lines.append(f"- **Manias:** {', '.join(status['manias'])}")

    lines += ["", "## Backstory"]
    for label, key in BACKSTORY_FIELDS:
        lines.append(f"- **{label}:** {bs.get(key, PLACEHOLDER)}")
    if inv.get("backstory_keys"):
        lines.append(f"- **Key entries:** {', '.join(inv['backstory_keys'])}")

    packages = inv.get("experience_packages")
    if packages:
        lines += ["", "## Experience packages", fmt_experience_packages(packages)]

    encounters = inv.get("mythos_encounters")
    if encounters:
        lines += ["", "## Mythos encounters", fmt_mythos_encounters(encounters)]

    growth = inv.get("growth_log")
    if growth:
        lines += ["", "## Growth log", fmt_growth_log(growth)]

    party = inv.get("party")
    if party:
        lines += ["", "## Party", fmt_party(party)]

    lines += ["", "## Hooks tying them to this campaign"]
    lines += [f"- {h}" for h in hooks]

    if inv.get("notes"):
        lines += ["", "## Notes", inv["notes"]]

    lines += ["", "## Links"]
    lines += [f"- {l}" for l in links]
    lines.append("")
    return "\n".join(lines)


def _band(build_total):
    for lo, hi, build, db_labels in BUILD_BANDS:
        if lo <= build_total <= hi:
            return build, db_labels
    if build_total > BUILD_BANDS[-1][1]:
        # Above 444, every further 80 points adds +1D6/+1 Build — not asserted here,
        # just skip the check rather than guess a label.
        return None, None
    return None, None


def _parse_band(band_str):
    if not band_str:
        return None, None
    nums = re.findall(r"\d+", band_str)
    if len(nums) < 2:
        return None, None
    return int(nums[0]), int(nums[1])


def _parse_trailing_int(text):
    if not text:
        return None
    nums = re.findall(r"\d+", text)
    return int(nums[-1]) if nums else None


def validate(inv, cfg):
    """Returns (errors, warnings) — both are lists of human-readable strings.
    errors = hard arithmetic (unconditional, 7e maths). warnings = threshold-type,
    configurable per campaign."""
    errors = []
    warnings = []

    c = inv.get("characteristics", {})
    d = inv.get("derived", {})

    con, siz, pow_, dex, str_ = c.get("CON"), c.get("SIZ"), c.get("POW"), c.get("DEX"), c.get("STR")

    if con is not None and siz is not None and "HP" in d:
        expected = (con + siz) // 10
        if d["HP"] != expected:
            errors.append(f"HP {d['HP']} != (CON+SIZ)/10 = {expected}")

    if pow_ is not None and "MP" in d:
        expected = pow_ // 5
        if d["MP"] != expected:
            errors.append(f"MP {d['MP']} != POW/5 = {expected}")

    if pow_ is not None and "SAN" in d:
        if d["SAN"] != pow_:
            errors.append(f"SAN (start) {d['SAN']} != POW {pow_}")

    mythos = inv.get("cthulhu_mythos", 0) or 0
    if "SAN_max" in d:
        expected = 99 - mythos
        if d["SAN_max"] != expected:
            errors.append(f"SAN_max {d['SAN_max']} != 99 - Cthulhu Mythos = {expected}")

    if dex is not None and "Dodge" in d:
        floor_dodge = dex // 2
        if d["Dodge"] < floor_dodge:
            errors.append(f"Dodge {d['Dodge']} is below DEX/2 = {floor_dodge}")

    if str_ is not None and siz is not None and ("Build" in d or "DamageBonus" in d):
        build, db_labels = _band(str_ + siz)
        if build is not None:
            if "Build" in d and d["Build"] != build:
                errors.append(f"Build {d['Build']} != expected {build} for STR+SIZ={str_ + siz}")
            if "DamageBonus" in d and d["DamageBonus"] not in db_labels:
                errors.append(
                    f"DamageBonus {d['DamageBonus']!r} != expected {db_labels[0]!r} "
                    f"for STR+SIZ={str_ + siz}"
                )

    sp = inv.get("skill_points")
    if sp:
        ot, os_ = sp.get("occupation_total"), sp.get("occupation_spent")
        if ot is not None and os_ is not None and ot != os_:
            errors.append(f"skill_points: occupation spent {os_} != total {ot}")
        it, is_ = sp.get("interest_total"), sp.get("interest_spent")
        if it is not None and is_ is not None and it != is_:
            errors.append(f"skill_points: interest spent {is_} != total {it}")

    for s in inv.get("skills", []):
        value = s.get("value")
        if value is None:
            continue
        base = s.get("base", 0) or 0
        occ = s.get("occupation_points", 0) or 0
        interest = s.get("interest_points", 0) or 0
        growth = s.get("growth_points", 0) or 0
        expected = base + occ + interest + growth
        if value != expected:
            errors.append(
                f"skill {skill_label(s)}: value {value} != base+occupation+interest+growth = {expected}"
            )

    cr = inv.get("credit_rating")
    od = inv.get("occupation_detail")
    if cr and cr.get("value") is not None and od and od.get("credit_rating_band"):
        lo, hi = _parse_band(od["credit_rating_band"])
        if lo is not None and not (lo <= cr["value"] <= hi):
            warnings.append(
                f"Credit Rating {cr['value']} sits outside occupation band "
                f"{od['credit_rating_band']} (fine if deliberate — see core/13 quality bar)"
            )

    # ---- threshold checks (configurable) ----
    cap = cfg.get("skill_cap", DEFAULT_VALIDATION["skill_cap"])
    declared_cap = _parse_trailing_int(sp.get("cap")) if sp else None
    effective_cap = declared_cap if declared_cap is not None else cap
    for s in inv.get("skills", []):
        # Own Language just mirrors EDU (character-creation.md §5's "special" row) — it isn't
        # bought against the cap, so a high-EDU investigator legitimately exceeds it here.
        if s.get("name") == "Own Language":
            continue
        base = s.get("base", 0) or 0
        occ = s.get("occupation_points", 0) or 0
        interest = s.get("interest_points", 0) or 0
        creation_value = base + occ + interest
        if creation_value > effective_cap:
            warnings.append(
                f"skill {skill_label(s)}: creation-time value {creation_value}% "
                f"exceeds cap {effective_cap}%"
            )

    ranges = cfg.get("characteristic_ranges", DEFAULT_VALIDATION["characteristic_ranges"])
    for field, bounds in ranges.items():
        lo, hi = bounds[0], bounds[1]
        value = d.get("Luck") if field == "Luck" else c.get(field)
        if value is not None and not (lo <= value <= hi):
            warnings.append(
                f"{field} {value} is outside the expected roll range {lo}-{hi} "
                f"(fine if point-buy or an aged/scaled NPC)"
            )

    return errors, warnings


def load_validation_config(src):
    cfg_path = src.parent / "validation.json"
    if not cfg_path.exists():
        return DEFAULT_VALIDATION
    try:
        return json.loads(cfg_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        print(f"Warning: {cfg_path} is not valid JSON ({e}); using built-in defaults", file=sys.stderr)
        return DEFAULT_VALIDATION


def main():
    strict = "--strict" in sys.argv[1:]
    args = [a for a in sys.argv[1:] if a != "--strict"]
    if len(args) != 1:
        print(f"Usage: {sys.argv[0]} [--strict] <path/to/investigator.json>", file=sys.stderr)
        sys.exit(1)

    src = pathlib.Path(args[0])
    inv = json.loads(src.read_text(encoding="utf-8"))
    cfg = load_validation_config(src)
    errors, warnings = validate(inv, cfg)

    for w in warnings:
        print(f"Warning: {w}", file=sys.stderr)
    for e in errors:
        print(f"Error: {e}", file=sys.stderr)

    if errors and strict:
        print("Aborting render (--strict, errors above).", file=sys.stderr)
        sys.exit(1)

    out = src.with_suffix(".md")
    out.write_text(render(inv), encoding="utf-8")
    tail = f" ({len(errors)} error(s), {len(warnings)} warning(s))" if errors or warnings else ""
    print(f"Wrote {out}{tail}")


if __name__ == "__main__":
    main()
