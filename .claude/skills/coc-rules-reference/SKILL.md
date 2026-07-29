---
name: coc-rules-reference
description: Look up Call of Cthulhu 7th Edition (CoC 7e) rules so any generated numbers are correct — difficulty bands (Regular/Hard/Extreme), skill checks, Sanity loss (X/Y), combat, HP, Build and Damage Bonus, Dodge, and base skill values. Load this FIRST, before writing any stat block or setting a check or Sanity cost, whenever a task touches CoC mechanics, dice, percentages, or "how does this rule work" — even if the user never names a rule. This is a lookup/reference skill only; to actually generate an NPC, monster, or scene use those skills instead.
version: "1.0.0"
---

# CoC 7e Rules Reference

Keep generated content mechanically correct for **Call of Cthulhu 7th Edition**. This skill
points to the cheat-sheets in `reference/rules/`; read the relevant one before you commit
numbers. It references mechanics — it does not reproduce the rulebook.

## Load this before you
- Write any NPC or monster **stat block** → confirm characteristics, HP, Build, Damage Bonus.
- Set a **skill check difficulty** → pick Regular / Hard / Extreme deliberately.
- Assign a **Sanity cost** → keep it proportionate to the horror.

## Cheat-sheets (source of truth)
- `reference/rules/skill-checks.md` — d100 under target; Regular/Hard/Extreme; fumbles;
  bonus/penalty dice; pushing; Luck; opposed rolls; base skill values.
- `reference/rules/sanity.md` — SAN = POW; X/Y loss notation; typical loss table; bout of
  madness; temporary vs indefinite insanity; recovery.
- `reference/rules/combat.md` — DEX order; dodge vs fight back; Build & Damage Bonus table;
  HP = (CON+SIZ)/10; major wounds; manoeuvres.

## Fast facts (verify against the sheets)
- **Check:** roll 1d100 ≤ value. **Hard** = ½ value, **Extreme** = ⅕ value, **Critical** = 01.
- **Characteristics** run ~15–90 (3d6×5, or (2d6+6)×5 for SIZ/INT/EDU). Average human ≈ 50.
- **HP** = (CON + SIZ) ÷ 10. **MP** = POW ÷ 5. **SAN** starts = POW; max = 99 − Cthulhu Mythos.
- **Dodge** base = ½ DEX. **Move** ≈ 8 for a typical adult (adjust for STR/DEX vs SIZ, age).
- **Damage Bonus / Build** come from STR + SIZ — see the combat sheet's table, don't guess.
- **Sanity loss** is written X/Y (success/failure). Minor Mythos sights ~0/1D6; gods ~1D10/1D100.

## Quality bar for anything with stats
- Numbers are internally consistent: HP, Build, Damage Bonus, Dodge all derive correctly.
- Difficulty is set **before** the roll and only when failure is interesting.
- Never gate the sole path forward behind one roll (hand off to `design-scenario`'s
  three-clue rule).
- When unsure of an exact value, state the assumption in a keeper note rather than inventing
  a rule.
