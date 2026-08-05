# Monster Scale — cheat-sheet

> The strength ladder for non-human threats, and the numeric baseline each rung sits at.
> Distilled by sampling `reference/sourcebooks/malleus-monstrorum-zh.md`
> — **all 223 stat blocks** in it (129 dice-notation species entries +
> 94 fixed-value deity/unique entries; the count is stated in that file's own header), matched
> to the book's own classification label and bucketed per tier. Coverage of the sampled fields:
> HP 87%, Sanity loss 92%, attack skill 88%, armour ~68% of the entries that state one.
> This sheet keeps the mechanics and number ranges, never the source text.
> **Human antagonists don't use this ladder** — `reference/rules/character-creation.md` §11.

## The five-tier ladder

Five rungs, ordered by what a Keeper can throw at a table and how badly it goes:

| Tier | Malleus category | What it looks like at the table |
|---|---|---|
| **L1 — human** | *(not covered here)* | A cult leader, a hired gun, an obsessed academic. `character-creation.md` §11. |
| **L2 — creature** | 独立种族 (independent race) / 传说生物 (fabulous creature) | The baseline monster: dangerous on its own, doesn't answer to anything. Most "one scary thing in the basement" encounters live here. |
| **L3 — servitor** | 仆从种族 (servitor race) | A god's guard dog, kidnapper, or messenger. Similar raw power to L2 — the difference is *purpose*, not necessarily strength — so **L2 and L3 overlap heavily**; a tough independent race can out-threat a weak servitor. |
| **L4 — unique** | 唯一存在 (unique entity) | A named individual, not a species — a particularly powerful cult idol, a rogue member of a race, a rising demigod. Clear step up from L2/L3. |
| **L5 — deity** | 旧神 / 旧日支配者 / 梦境诸神 / 外神 / 化身 (all five deity classes, one tier) | Cthulhu-scale. Encountering it directly is rarely a fair fight — see `core/07-create-monster.md`'s "the fair out". |

**Overlap rule:** adjacent tiers may overlap (a mythic-threat L2 can rival a trivial-threat L3
or L4) — **non-adjacent tiers may never overlap** (an L2 creature, however built up, does not
reach L4 unique-entity numbers). This is what makes the ladder a ladder and not a suggestion.

## Threat bands within a tier

The existing four-band `threat` field (trivial / moderate / deadly / mythic) still applies —
it's the **± inside a tier**, not a replacement for it. Within each tier below, `trivial` sits
at the low end of the range and `mythic` at the high end; `moderate` and `deadly` split the
middle. A tier's `trivial` can land inside the tier below it's `mythic` — that's the overlap
rule above, working as intended.

**At L2 and L3, check the source's 上级/下级 label first** — see the sub-tier section below.
It picks the half of the band range for you, and it's more reliable than eyeballing.

## Baseline ranges per tier

Ranges below come from the sampled distribution's rough quartiles, then rounded to numbers a
Keeper would actually write down. **Sanity loss** is X/Y notation (success/failure); the
X-side (success) is usually 0–1 at L2/L3 and climbs at L4/L5 — even *surviving* the sight of
something that size costs a little. **HP** for Mythos entities is usually stated directly
rather than derived from CON+SIZ (many have no CON, or an N/A SIZ) — treat the HP figure as
canon for the tier, not something to recompute.

### L2 — creature (独立种族 / 传说生物)

| Threat | Sanity loss (typical) | HP | Armour | Attack skill |
|---|---|---|---|---|
| trivial | 0/1D3 – 0/1D4 | 8–15 | 0–3, often none | 25–40% |
| moderate | 0/1D6 | 15–20 | 2–5 | 40–55% |
| deadly | 0/1D6 – 0/1D8 | 20–30 | 4–10 | 50–70% |
| mythic | 1D3/1D20 – 1D6/2D20 | 30–60 (rare outliers past 300 — a handful of huge, ancient members of a race) | 8–30, or a named immunity clause | 65–90% |

### L3 — servitor (仆从种族)

| Threat | Sanity loss (typical) | HP | Armour | Attack skill |
|---|---|---|---|---|
| trivial | 0/1 – 0/1D2 | 8–12 | 0–2, often none | 15–30% |
| moderate | 0/1D4 – 0/1D6 | 12–16 | 2–4 | 30–45% |
| deadly | 0/1D6 – 1/1D6 | 16–25 | 3–7 | 45–65% |
| mythic | 1D3/1D20 – 1D6/1D20 | 25–60 | 5–10, or an immunity clause | 60–100% |

### 上级 / 下级 — the book's own free calibration (L2 and L3 only)

**Read this before picking a threat band at L2 or L3.** Malleus labels most species entries
**上级** (greater) or **下级** (lesser), and that label separates them harder than the threat
band does. Sampling the two groups apart:

| Sub-tier | n | HP (median) | Attack skill (median) | Sanity loss (typical) |
|---|---|---|---|---|
| 下级独立种族 — lesser independent | 43 | **14** | **35%** | 0/1D3 – 0/1D8 (0/1D6 is by far the most common) |
| 上级独立种族 — greater independent | 10 | **36** | **80%** | 1D3/1D20 – 1D6/1D20 |
| 下级仆从种族 — lesser servitor | 56 | **14** | **35%** | 0/1D2 – 0/1D6 |
| 上级仆从种族 — greater servitor | 15 | **27** | **75%** | 1/1D8 – 1D6/1D20 |

**How to use it:** if the entry you're calibrating against is labelled **下级**, take the
`trivial`/`moderate` rows of its tier below; if **上级**, take `deadly`/`mythic`. The greater
group runs **2–2.6× the lesser group's HP and roughly double its attack skill** — a wider gap
than the whole four-band spread within a pooled tier, which is why the pooled ranges below read
broad in the middle. When the book gives you the label, it beats your judgement; use it.

**Not split by sub-tier:** armour (too few entries state a value to split the sample honestly)
and L4/L5 (no 上级/下级 labels there). Those stay pooled below.

### L4 — unique (唯一存在)

Thin sample in the source (8 named individuals) — treat these as a shape to calibrate against,
not a tight statistical range.

| Threat | Sanity loss (typical) | HP | Armour | Attack skill |
|---|---|---|---|---|
| trivial | 0/1D4 – 1/1D8 | 13–25 | usually a narrative immunity, not a point value | 20–40% |
| moderate | 1/1D8 – 0/1D10 | 25–45 | same | 35–55% |
| deadly | 1/1D10 – 1D6/1D20 | 45–61 | 6+ or immunity | 55–80% |
| mythic | 1D10/1D100 | 55–65+ | immunity to most conventional weapons | 75–100% |

### L5 — deity (神格, all five deity classes)

| Threat | Sanity loss (typical) | HP | Armour | Attack skill |
|---|---|---|---|---|
| trivial | 0/1 – 0/1D3 | 15–35 | 0–5, or a narrative immunity | 40–60% |
| moderate | 1/1D10 – 1D4/1D10 | 35–60 | 5–10 | 55–75% |
| deadly | 1D3/1D20 – 1D8/1D20 | 60–110 | 8–20, or "only magic/enchanted weapons harm it" | 70–90% |
| mythic | 1D10/1D100 – 1D20/1D100 | 100–420+ | usually a full immunity clause, not a point value | 85–100% |

## Attacks per round

Most entries carry **1–3 distinct attack forms** (a grab, a bite, a special effect) regardless
of tier — tier changes how dangerous each one is, not how many there are. A single form used
repeatedly (e.g. one crushing attack at a flat skill %) is normal at L2/L3; L4/L5 entries are
more likely to have 2–3 forms with distinct effects (physical + a mind/POW-draining option).

## Armour convention

Roughly **28% of sampled entries carry no armour at all** — raw HP and a high attack skill do
the work instead. Where armour is stated, it's overwhelmingly either (a) a flat point value
(sampled median 8, most entries 2–10, deity-tier outliers up to 50) subtracted from damage like
a human's armour, or (b) a **narrative immunity clause** ("only fire and enchanted weapons
harm it", "impaling weapons do minimum damage") rather than a number. Prefer (b) for anything
L4 or above — a point value implies conventional weapons can grind it down, which undercuts
"the fair out" being something other than a bigger gun.

## Trait load budget (feeds `reference/tables/monster-traits.md`)

Each tier has a rough ceiling on how many numeric traits (from the traits table) a single
entry should carry before it stops reading as "this tier, pumped up" and starts reading as
"the wrong tier with a costume on":

| Tier | Load ceiling | Why |
|---|---|---|
| L2 creature | 2 traits | Base monsters stay simple — texture comes from the attack/reveal, not a trait stack. |
| L3 servitor | 2 traits | Same budget as L2 (the tiers overlap; the budget should too). |
| L4 unique | 3 traits | A named individual earns one extra trait over its base race/tier — that's *why* it's unique. |
| L5 deity | 4 traits | Gods can stack the most, but even here more than 4 usually means the entry needs a rewrite, not another trait. |

A trait's load cost is defined per-trait in `monster-traits.md`; **sum the loads, don't just
count traits** — a cheap trait and an expensive one both count as "1 trait" for flavour
purposes but not for budget purposes.

## `core/07`'s strength formula, in full

`core/07-create-monster.md` used to leave this as a placeholder. The full answer:

**Monster strength = tier baseline (this sheet) + trait load (`monster-traits.md`), capped by
the tier's load ceiling above.** Pick the tier, pick the threat band inside it, read the
baseline ranges, then layer on traits until the entry feels right — never past the ceiling.
