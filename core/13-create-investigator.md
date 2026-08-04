# 13 — Create Investigator

Build a player investigator — usually a **pregen** for a one-shot or a new player, sometimes an
**elite NPC** (a named cultist, a rival investigator) reusing the same mechanical skeleton.
The JSON record is the source of truth; the Markdown card is a rendered view for the table.

## First

- **Read `reference/rules/character-creation.md`** before rolling anything.
- Read the campaign `CLAUDE.md` for era, tone, and premise — every surviving backstory hook
  must tie into it; a hook that connects to nothing in the campaign is decoration, not prep.
- Use `templates/investigator.schema.json` (data) and `templates/investigator.md` (view).
  `templates/investigator.example.json` is a complete, arithmetically-audited record — copy
  its shape rather than guessing which fields a full card needs.
- **`reference/decks/busybodies-zh.md`, if present, is 47 worked examples of a finished 1920s
  card** — occupation, stat spread, the six or seven skills worth listing, and every 7e
  backstory prompt filled at usable length. Read the nearest occupation before rolling; it
  settles "how much is enough" faster than the schema does. Its own guidance for pressing a
  card into service as a **replacement PC** — hand the player 100 extra points on
  free-choice skills, let them rewrite the backstory — is a sound emergency pregen recipe.
  Optional: the deck is a local file.
  Its numbers are transcription, not gospel — SIZ and MOV are known to be off on some cards.
  Recompute every derived stat yourself; never copy a card's arithmetic forward.
- Two more local-only decks feed specific fields: `reference/decks/phobias-and-manias-zh.md`
  for the backstory `phobias` / `manias` entries (32 written-out conditions rather than a bare
  name), and `reference/decks/weapons-and-artifacts-zh.md` for anything in the gear list.

## Build in this order

The order matters: age moves characteristics, characteristics set the point budgets, and the
budgets decide what the backstory can plausibly claim. Working out of order means redoing it.

1. **Concept.** One line: who they are, what they want out of this case.
2. **Occupation.** Pick or invent one. It supplies exactly three things — the skill-point
   formula, the Credit Rating band, and the occupation skill list (including its free-choice
   slots). Record all three in `occupation_detail`; an invented occupation needs the Keeper's
   sign-off before points are spent.
3. **Age.** Choose it, then pay for it: physical deduction, APP penalty, EDU improvement
   checks, Move penalty. Do this **before** computing skill points — most formulas pay out of
   EDU, and the improvement checks change EDU. Record what was applied in `age_modifiers`.
4. **Characteristics and derived stats.** Roll or assign, then derive HP, major wound, MP,
   SAN (start and max), Move, Build, Damage Bonus, Dodge. Recompute — don't eyeball.
5. **Skill points.** Occupation points onto occupation-list skills only (Credit Rating first,
   up to at least the band's lower bound), then INT × 2 personal-interest points anywhere.
   Name every umbrella specialisation. Keep the ledger in `skill_points` and make it balance.
6. **Wealth.** Credit Rating → lifestyle, cash, assets, casual spending, in the campaign's
   declared currency and era scale.
7. **Backstory.** Fill every 7e prompt (description, ideology, significant people, locations,
   possessions, traits, scars, phobias/manias), then keep only what this campaign can pull on
   — cut the rest rather than pad the file. Mark the one or two entries the investigator
   genuinely *is* in `backstory_keys`; those are what Sanity rewards and punishes.
8. **Hooks and kit.** Turn the surviving backstory and the occupation's contacts into `hooks`
   that each name something real: an NPC, a faction, a location, or the central mystery. Add
   only the weapons and gear the scenario can actually use.

## Storage

- **Source of truth:** `campaigns/<slug>/investigators/<name>.json`, validated against
  `templates/investigator.schema.json`.
- **Rendered view:** `campaigns/<slug>/investigators/<name>.md` — generate it with
  `scripts/render-investigator.py`, or write it directly from the JSON. The two must never
  disagree; regenerate the `.md` whenever the `.json` changes.
- An optional `campaigns/<slug>/investigators/roster.csv` can index name/occupation/status for
  a quick glance at the table; it is always derived, never the source of truth.

## Pregens vs. elite NPCs

Elite cultists or other mechanically-full villains (`core/06-create-npc.md` NPCs who need
complete stats) may use this schema instead of a lighter NPC stat block — set
`"type": "elite-npc"` in the JSON.

**The rendered card is always KP-facing, for both types.** This tool builds player sheets for
the Keeper to hand-review, not something that goes to a player unedited — players build their
own characters, and the Keeper enters the agreed sheet as JSON. Nothing is held back by
`type`: `scripts/render-investigator.py` renders every populated section (spells, notes,
the skill-point ledger, `mythos_encounters`, all of it) the same way for a pregen and an
elite NPC — there is no separate "player view" to strip spoilers from. If a campaign wants
a pre-built card actually handed to a player, that's decided once at intake
(`core/01-intake.md`), not solved by the renderer guessing the audience.

## Self-validation

`scripts/render-investigator.py` checks the record on every run and reports to stderr —
default is **warn but still render**; `--strict` turns any violation into a hard failure:

- **Arithmetic (unconditional):** derived-stat formulas, the skill-point ledger balancing,
  each skill's `value = base + occupation + interest + growth`, Credit Rating sitting in the
  occupation's band.
- **Thresholds (configurable):** the creation-time skill cap and characteristic ranges, read
  from `campaigns/<slug>/investigators/validation.json` if present (intake writes this file
  with the campaign's declared numbers; falls back to `reference/rules/character-creation.md`
  defaults otherwise — see the script's `DEFAULT_VALIDATION`).

This doesn't replace `core/11-review.md` — it catches the mechanical typos a reviewer would
otherwise have to recompute by hand; continuity, three-clue coverage, and spoiler hygiene are
still a human read.

## Output

- Write prose fields in the campaign's declared **output language**. Stat notation (`STR 60`,
  skill percentages) stays English per `core/02-rules-reference.md`.

## Quality bar

- The JSON validates against `templates/investigator.schema.json`.
- Every derived stat traces back correctly to the **post-age** characteristics
  (`reference/rules/character-creation.md`) — recompute, don't eyeball.
- The point ledger balances: occupation points spent = the formula's total, interest points
  spent = INT × 2, and each skill's `value` = base + occupation + interest + growth.
- Occupation points touched only occupation-list skills; free-choice slots are named;
  every umbrella skill carries a specialisation.
- Credit Rating sits inside the occupation's band, or the deviation is deliberate and noted.
- Every surviving backstory hook ties into something the campaign can actually use, and at
  least one entry is marked key.
- The `.md` view and the `.json` source agree; no stat appears in one but not the other.
