# 07 — Create Monster

Stat a threat that is frightening *and* fair — the players can learn what it is and how to
live through it. In CoC the monster is usually an obstacle to survive, not a boss to beat.

## First

- **Picking WHICH creature, not just how strong** (e.g. "the campaign's boss is Hastur — what's
  a fitting elite guard/servitor?") — read `reference/tables/monster-index.md` first. It covers
  all 223 malleus entries plus this kit's own `reference/bestiary/`, each with a `Serves` field
  (who it answers to) and a short index summary, so you don't have to read the full 10k-line
  transcript to find a candidate. It's generated (see `scripts/build-reference-index.py`), and
  it is the **only** channel a Keeper without the repo has into the 223 malleus entries — the
  transcript itself never ships. `reference/bestiary/` does ship, so its creatures can be read
  in full rather than through the index.
- **Read `core/02-rules-reference.md`** — especially `reference/rules/combat.md` (Build,
  Damage Bonus, HP) and `reference/rules/sanity.md` (X/Y loss). Numbers must be 7e-correct.
- **Decide the tier**, then the threat band inside it — read
  `reference/rules/monster-scale.md` before assigning any number. Five tiers, ordered by power:

  | Tier | type value | Malleus category |
  |---|---|---|
  | L1 human | *(not this spec)* | — |
  | L2 creature | `independent-race` (add `beast`/`undead` as a parenthetical modifier if it fits, e.g. `independent-race (undead)`) | 独立种族 / 传说生物 |
  | L3 servitor | `servitor-race` | 仆从种族 |
  | L4 unique | `unique-entity` | 唯一存在 |
  | L5 deity | `great-old-one` | 旧神/旧日支配者/梦境诸神/外神/化身,全部记作这一档 |

  `beast` and `undead` are no longer standalone types — they're descriptive modifiers on
  whichever of L2/L3/L4 the creature actually is (a zombie is `independent-race (undead)`,
  not a fourth category). **Threat** (trivial / moderate / deadly / mythic) is still the field
  that sets fine-grained stat scale and SAN **inside** a tier — `monster-scale.md` has the
  baseline ranges for both axes together. Adjacent tiers may overlap; never skip a tier.
- **Filing by tier:** L5 entries go in `reference/mythos/great-old-ones/`, not
  `reference/bestiary/` — a god's page is lore-shaped (origin, signs, how a cult worships it),
  not a stat card. **L2/L3/L4 all go in `reference/bestiary/`.**
- **Human antagonists don't use this spec.** A cultist, a cult leader, or any other human
  villain is built with `reference/rules/character-creation.md` §11 (baseline + increment),
  not this spec's type/threat scale.
- Use `templates/monster.md`.
- **Source material — read the relevant one before inventing numbers:**
  `reference/sourcebooks/malleus-monstrorum-zh.md` is the official creature
  compendium — read the nearest published entry to calibrate stat scale, armour, and SAN cost
  before inventing your own; its stat tables are clean, but check its own header for the
  current list of known small defects (mixed synonymous terms, a few inconsistent renderings).
  `reference/sourcebooks/grand-grimoire-zh.md` covers spells for anything that casts and is
  still a PDF-extraction transcription with known garbling — judge every number there by eye.
  Published numbers may be taken directly into a `reference/bestiary/` entry with the source
  named; the reveal, lore, and behaviour prose is written fresh (`core/00-how-to-run.md` →
  ground rules).

## Design the horror

- **The reveal first.** Write 2–4 sensory sentences of *wrongness* (motion, sound, smell) —
  the Keeper reads this, THEN calls the Sanity roll. Lead with the image, not the stat line.
- **Sanity cost proportionate** to what it is: minor servitor ~0/1D6, major entity ~1D6/2D10,
  a god ~1D10/1D100. Don't inflate for gore alone.
- **Attacks with texture** — not just damage. A grab that drags, a touch that drains POW, a
  gaze that ages. Give per-round attack count, skill %, damage (with db where physical).
- **Armour / immunities** — many Mythos things shrug off bullets or knives. Say what *does*
  work (fire, cold iron, a ward, a name).
- **The fair out.** Every creature needs a discoverable way to be **fled, warded, tricked,
  burned, or endured**. Combat is the failure branch; give a better one.
- **Weakness = a clue.** The out should be findable through investigation (a tome, a survivor,
  an experiment) — hand that thread to `core/08-create-puzzle.md` / `core/04-design-scenario.md`.

### Lovecraftian design craft

`reference/craft/lovecraft-zh.md` §三 distills how H. P. Lovecraft's own monsters and
entities are built and revealed, from a full read of his original stories. A few techniques
map directly onto the bullets above:

- **Reaction over anatomy.** The strongest reveals never fully describe the creature — they
  describe what witnessing it *does* to a witness (collapse, permanent insomnia, a crew
  driven mad). Write the reveal sentences as effect-on-observer before you write what the
  thing looks like; it's a stronger, more efficient version of "the reveal first" above.
- **Precise numbers, then broken biology.** Establish credibility with a concrete measurement
  (height, limb count, a stat) before the one detail that breaks known anatomy (a joint that
  folds the wrong way, an eye where a joint should be). The concreteness makes the wrongness
  land harder than vagueness would.
- **Society, not specimen.** For threats meant to feel bigger than a single encounter, give
  the creature a culture — taboos, a hierarchy, things it worships or fears. This is a cheap
  way to make a `mythic` or plot-recurring entity feel like an iceberg instead of a boss fight.
- **Refuses to manifest.** For things the party genuinely cannot fight, consider never staging
  a direct encounter — only its environmental effects (cold, silence, an unlocatable sound).
  This *is* a form of "the fair out": if it's never seen, running is the only sane response,
  and that's a legitimate design.
- **Polite and orderly, not just hostile.** For a god-tier or highly intelligent entity,
  bureaucratic courtesy (it explains itself, offers a choice, keeps its word) is more
  unsettling than aggression, and reads as more dangerous — malice would at least be
  understandable.

Use one or two of these per creature, not all of them — the point is a sharper reveal, not a
checklist.

## Stat guidance (7e)

- Give **average characteristics** (note "roll/scale per individual" if many appear).
- Derive **HP = (CON+SIZ)/10**, **Build & Damage Bonus** from STR+SIZ, **Move** to fit the body.
- Big entities have high SIZ → high Build → hard to grapple and heavy Damage Bonus; reflect it.
- Spellcasters: list spells and their MP/SAN costs — read `reference/rules/magic.md` for the
  cost-tier ladder before assigning numbers; cross-link `reference/mythos/`.

## Output

- **Reusable, campaign-neutral** → `reference/bestiary/<name>.md` (no plot). Write these in
  **English** — they are shared across campaigns with different output languages.
- **Plot-bound** (its origin *is* the mystery) → `campaigns/<slug>/world/` or `scenes/`, in
  that campaign's output language, with secrets in a `> **KEEPER ONLY**` block.
- One creature per file, `kebab-case.md`.

## Quality bar

- Stats internally consistent; SAN cost proportionate; attacks and armour concrete.
- There is at least one **non-combat way to survive** the encounter, and it's discoverable.
- Keeper-only lore is quarantined; the reveal text is ready to read aloud.
