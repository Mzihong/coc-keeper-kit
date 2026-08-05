# 7e Magic — cheat-sheet

> Casting mechanics, tome conventions, and spell-design cost scaling — not a spell list.
> Distilled from two archived sources: the tome/study rules
> in `reference/sourcebooks/keeper-rulebook-7e-zh.md` (the 7e core rulebook — last word on any
> number here), and the spell cost/casting-time patterns sampled across
> `reference/sourcebooks/grand-grimoire-zh.md` (550+ spells, official supplement). This sheet
> keeps the mechanics and number ranges, never the source text.

## Casting a spell

- **Cost is written `X 点魔法值；Y 点理智值`** (MP, then SAN), with **POW** added as a third
  cost only when the spell demands a permanent sacrifice. `可变`(variable) means the caster
  chooses how much MP/POW to invest — more investment buys a bigger or more likely effect.
- **Casting time sets initiative.** 即时 (instant) resolves at the caster's DEX**+50** this
  round (like a readied gun). **1 轮** resolves at the caster's own DEX this round; **N 轮**
  resolves at DEX on the caster's Nth round from now. Ritual spells instead run
  minutes/hours/days, and the caster is exposed and interruptible for the whole span.
- **Resisted effects use an opposed POW roll** — POW vs. the target's POW, or (for wards,
  barriers, and thresholds) POW vs. **5× the MP invested** — never a skill check. Cthulhu
  Mythos/Occult only gate *learning* or *diagnosing* a spell, never casting it.
- **SAN loss on a cast is a flat number**, not the X/Y success/failure notation used for
  witnessing something (`reference/rules/sanity.md`) — it's paid whether or not the spell
  succeeds. Casters at SAN 0 are conventionally written as ignoring it.

## Cost tiers (calibration ladder, sampled across the grand-grimoire)

Pick the tier matching the effect's reach when inventing a spell or a caster's known list,
then round to a number that feels earned — don't default to the cheapest end. Four tiers,
**小术/中术/大术/仪式级**, so any future spell-strength tooling (indexing, tagging) has one
shared vocabulary instead of a second incompatible ladder:

| Tier | MP | SAN | POW | Casting time | Example |
|---|---|---|---|---|---|
| 小术 (minor) | 1–6 | 0–1D4 | — | rounds–minutes | detect, ward an object, small curse |
| 中术 (moderate) | 变 or 5–15 | 1D4–1D8 | — | 即时–1 轮 | direct harm, mind-affecting, most Bind/Summon (creature) |
| 大术 (major) | 10–25 | 1D6–2D10 | 5–15 (often permanent) | hours–1 天 | shapechange, life-extension, a curse that sticks |
| 仪式级 (ritual-tier) | 20–100+ | 1D10–3D6 | 15–350 | hours–days, always ritual | Call/Summon (Great Old One) |

## Spell design — the cost-conversion convention

- **Power and cost move together.** Doubling an effect (damage, duration, range) should
  roughly double its MP/SAN — a cheap-and-strong spell breaks the action economy.
- **Permanent effects cost permanent POW, not MP.** MP recovers overnight; a bound servitor
  or a curse that never lifts shouldn't be payable in something the caster gets back by
  sleeping.
- **God-taught spells break the curve on purpose** — lower MP for the same effect, but
  usually a steeper SAN cost, a POW sacrifice, or a string attached (the deity remembers).
  That difference is what makes a Nyarlathotep-taught spell feel unlike one reverse-engineered
  from a stolen page.
- **Investigators get the weak end of every curve.** A PC-only discount on a spell's cost
  quietly turns them into a superhero — an NPC casting the same effect should pay the same.
- **Flavour is free.** The description (sound, smell, visual) can be reskinned at no
  mechanical cost; only the cost and effect are the levers that matter for balance.
- **A counter-spell must cost at least one tier less than the spell it counters.** This is a
  hard design law, not a guideline: a ward or banishing that costs as much (or more) than the
  attack it stops is a fair-out in name only — see `core/07-create-monster.md`'s "the fair
  out" and `core/08-create-puzzle.md`. A 大术-tier curse needs a 中术-or-cheaper counter
  somewhere in the world, discoverable through play.

## Tomes / grimoires

Every tome carries five fixed values, decided once when the tome is written and never
changed by who reads it: **SAN loss** (a flat die roll, not X/Y), **CMI** (Cthulhu Mythos
Initial — the % gained on skimming), **CMF** (Cthulhu Mythos Full — the % gained on full
study), **MR** (Mythos Rating — see below), and **study time** in weeks.

- **泛读 (skim) first, always.** Cover, script, and a read of the language tell the reader
  whether they can read it at all. A **reading check** (the relevant Language skill, or the
  reader's Occult/CM if no check is called for) may be required — difficulty scales with the
  tome's condition: **Regular** for a clean modern print, **Hard** for a handwritten or old
  copy, **Extreme** for a decayed original with mixed marginalia. Failure costs nothing (no
  SAN, no Mythos) — just a wasted attempt. Success grants **CMI immediately**, the flat SAN
  roll (believers only — a declared non-believer's *max* SAN drops but current SAN doesn't),
  a sense of what spells the tome holds, and how long full study will take.
- **精读 (full study) is the real gate** — commonly weeks for a minor text, months to over a
  year for a dense one; a *Necronomicon*-class tome runs 30–70 weeks. No reading check (it
  was already resolved at the skim). On completion, roll the SAN loss again, then compare the
  reader's current Cthulhu Mythos skill to the tome's **MR**: below MR → the reader gains the
  full **CMF**; at or above MR → only **CMI** again (diminishing returns once the reader has
  outgrown the tome). Re-studying the same tome is allowed — each subsequent pass **doubles
  the previous study time** but pays the same SAN/CM rules, so a tome keeps paying out (worse
  and worse per hour) until the reader's CM skill clears its MR.
- **A translated/abridged copy** of the same work typically has a **lower MR, faster study
  time, and a smaller CMI/CMF** than the original manuscript, and usually teaches fewer of the
  spells — the trade-off that makes collecting multiple editions of one tome worthwhile.
- Only **one tome can be under active study at a time** per reader.

| Weight | Study time | SAN loss | CMI / CMF | MR |
|---|---|---|---|---|
| Minor / cult pamphlet | 1–14 weeks | 1D3–1D6 | +1/+2 – +4/+9 | 9–18 |
| Standard grimoire | 6–36 weeks | 1D6–2D6 | +2/+4 – +4/+8 | 18–36 |
| Major tome (*Necronomicon*-class) | 32–68 weeks | 2D8–2D10 | +4/+8 – +5/+12 | 36–51 |

## Spell entry format & categories (for `reference/mythos/spells/`)

Each entry: **消耗**(cost) → **施法用时**(casting time) → **效果**(effect) → optional
**深层魔法**(a stronger variant for SAN-0 casters and Mythos entities) → **别名**(aliases —
useful so players can't pattern-match a spell by name alone). Tag loosely with the
sourcebook's own categories, more than one where it fits: 驱逐和控制、召唤怪物和神祇、战斗、
交流、幻梦境、附魔、环境、续命、民俗魔法、加害魔法(战斗外)、支配他人、制造怪物、其他、保护、
时间相关、变形、旅行和交通。

## Quality bar

- Cost (MP/SAN, +POW if the effect is permanent) matches the tier table for what the spell
  actually does — no MP-only immortality, no discount spells for PCs.
- Casting time is stated in 即时/N 轮/duration notation, never "takes a while".
- A tome states all five values together — SAN loss, CMI, CMF, MR, study time — not just a
  single "Mythos gain" number.
- A resisted effect names exactly what it's opposed against (POW vs. POW, or vs. 5× MP).
- Any spell written as "the fair out" for another spell costs at least one tier less than
  the spell it counters.
