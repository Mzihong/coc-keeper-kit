#!/usr/bin/env python3
"""Render a CoC Keeper Kit investigator JSON record into its Markdown card.

Usage:  python scripts/render-investigator.py campaigns/<slug>/investigators/<name>.json

Writes the .md file alongside the .json (same basename). Deterministic — never invents
values; a missing field renders as the template's own "<...>" placeholder so gaps stay
visible instead of silently disappearing. stdlib only, no dependencies.
"""
import json
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


def render(inv):
    c = inv.get("characteristics", {})
    d = inv.get("derived", {})
    cr = inv.get("credit_rating", {})
    bs = inv.get("backstory", {})
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
        f"- **Credit Rating:** {cr.get('value', PLACEHOLDER)} ({cr.get('band', PLACEHOLDER)})",
        "",
        "## Skills",
        fmt_skills(inv.get("skills")),
        "",
        "## Weapons",
        fmt_weapons(inv.get("weapons")),
        "",
        "## Backstory",
    ]
    for label, key in BACKSTORY_FIELDS:
        lines.append(f"- **{label}:** {bs.get(key, PLACEHOLDER)}")
    lines += ["", "## Hooks tying them to this campaign"]
    lines += [f"- {h}" for h in hooks]
    lines += ["", "## Links"]
    lines += [f"- {l}" for l in links]
    lines.append("")
    return "\n".join(lines)


def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <path/to/investigator.json>", file=sys.stderr)
        sys.exit(1)
    src = pathlib.Path(sys.argv[1])
    inv = json.loads(src.read_text(encoding="utf-8"))
    out = src.with_suffix(".md")
    out.write_text(render(inv), encoding="utf-8")
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()
