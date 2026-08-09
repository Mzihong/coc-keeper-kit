# 06 — Create NPC

Make a person the Keeper can *play*, not just a stat line — a face, a want, a secret, and a
tell — mechanically correct for 7e.

## First

- **Preview before you expand** — `core/00-how-to-run.md` → ground rules: a ≤15-line list of
  what you're about to write, confirmed by the Keeper, before any file goes to disk. For an
  NPC specifically, the default preview answer is usually **stub** — see Two tiers below.
- **Read `core/02-rules-reference.md`** before writing the stat block (characteristics, HP,
  Build, Damage Bonus, Dodge, skill values must be 7e-correct).
- Read the campaign `CLAUDE.md` for era/tone/output language; match name, dress, speech, and
  job to the era and the place. Check `canon-log.md` — this person may already exist.
- Use `templates/npc.md`.
- **Skim the card closest to this NPC's job in `reference/decks/busybodies-zh.md` before
  writing the stat block.** 47 official 1920s NPC cards — use them to calibrate: what EDU an
  antiquarian actually carries, where a zealot's Intimidate sits, which six or seven skills a
  card bothers to list. The names, backstories, and secrets stay in the deck; only the scale
  comes across. **In a campaign with a different declared Era, that calibration is still
  1920s** — borrow only the scale (how many skills, what value range), never the occupation,
  gear, or skill choices; those follow the era's own delta.

## Two tiers

Most NPCs a scenario names don't need a full card yet — see `core/00-how-to-run.md` →
"write what gets read before what gets narrated". Default to **stub**; upgrade only when a
concrete need shows up.

- **Stub (default).** Name / role & where they're found / what they want / what they're
  hiding / one line of voice. Four or five lines, **no file** — one row in
  `campaigns/<slug>/npcs/roster.md` (`templates/npc-roster.md`). There is no stub template
  file — the row *is* the artifact; a separate template would just invite opening a file for
  something that doesn't need one.
- **Card.** The full output below: independent file, `templates/npc.md`.

**Upgrade a stub to a card when any one of these is true** — otherwise leave it a stub:

1. The next session will definitely put a skill check on them (Persuade, Psychology, Spot
   Hidden… against this specific NPC).
2. They'll fight or be chased (needs HP, Damage Bonus, Dodge, a weapon).
3. They'll carry more than one exchange of real dialogue (needs a secret, a lie, something to
   give up).
4. The Keeper names them specifically, or the players have already latched onto them.

Upgrading is just running the rest of this spec for that one NPC and deleting their roster
row once the file exists (the roster stays the index of who's stub vs. who's carded — a name
shouldn't live in both places).

## Ask (or infer sensibly)

- Their **role in play** (ally / obstacle / witness / victim / red herring / villain / source).
- Rough **competence** — bystander, professional, or dangerous — which sets stat scale.
- Whether they may **fight or resist** (full stats) or are a pure social NPC (light stats).

## Build the person

- **One-line concept** first, then a spoken **description** the players actually hear (face,
  voice, a physical tell).
- **Want / fear / mannerism** — the three levers that let a Keeper improvise them live.
- **A secret** in a `> **KEEPER ONLY**` block: what they hide, what makes them talk or flip,
  how they react under pressure.
- **Clues they can give** — and the pressure/approach that unlocks each (ties into fair play:
  never make one NPC the *only* source of a key clue).
- **The lie they tell.** What do they say when asked directly? Every NPC with a secret needs
  a prepared cover story, or the Keeper has to invent one mid-scene.
- **Interaction history block (cards only):** on a brand-new card, set current attitude to a
  neutral default (e.g. "stranger") and leave the log empty. `core/12-canon-update.md` is what
  appends to it after play — this spec never backfills sessions that haven't happened yet. A
  stub has no file to hold this block; its roster row's **Status** column is the only
  "current attitude" a stub carries, and `core/12` updates that row directly instead.

Run `python scripts/roll.py npc-quirks npc-appearance --campaign <slug>` for at least the
mannerism and the first physical impression. A rolled tic beats the model's default "nervous,
wrings hands," and a rolled appearance beats "middle-aged, tired-looking." For a cult leader
specifically, `python scripts/roll.py cult-leader-positions --campaign <slug>` rolls their
social front and what access it buys — read `reference/rules/character-creation.md` §11 for
how strong to make them.

**Rank-and-file cultists** — `reference/tables/cultist-archetypes.md` has twelve ready-to-use
statted archetypes (academic, blue-collar, criminal, law-enforcement, medical, military,
youth, priest, leader) plus a menu of "Blessing of Cthulhu" powers to sprinkle on one or two
— use one as-is for a faceless NPC, or as the numeric baseline when building a named one.

For the **secret**, the busybodies deck is the length calibration: every one of its 47 cards
carries exactly one, in one or two sentences, and each is a *lever* — a debt, a lie already
told, a dream that keeps recurring — not a plot summary. Match that scale. Anything longer is
backstory, and backstory doesn't survive contact with a table.

> **Take the numbers; invent the person** (`core/00-how-to-run.md` → ground rules). A card's
> stat line and skill spread are calibration you can use directly. Its name, backstory, and
> secret are not — a deck NPC pasted into `campaigns/` is a character every other Keeper
> using that deck already knows the twist to.

## Stat guidance (7e)

- Average human characteristic ≈ 50; scale to concept (a dockworker's STR high, a scholar's
  EDU high). Derive **HP = (CON+SIZ)/10**, **Build/Damage Bonus** from STR+SIZ,
  **Dodge = ½ DEX**.
- List **only skills likely to matter** at 7e values (e.g. Persuade 60, Spot Hidden 45,
  Fighting (Brawl) 45, Firearms (Handgun) 35). Non-combatants: note it and skip the weapons.
- Villains/cultists: consider Cthulhu Mythos %, spells (cross-link `reference/mythos/`), and
  the SAN implications of what they've done. For actual spell numbers, look them up in
  `reference/sourcebooks/grand-grimoire-zh.md`, the official grimoire.
- **A cult leader or other human antagonist meant to be stronger than an ordinary person**
  is not a separate power tier — it's `reference/rules/character-creation.md` §11: the same
  baseline (busybodies deck) plus one increment (spell count for a spellcaster, gear price
  for a non-spellcaster). Skill *choice* comes from backstory; skill *height* is
  lethality-derived — see §11 for the split and `core/11-review.md` for the audit question.
- Arming someone: `reference/decks/weapons-and-artifacts-zh.md` gives skill, base chance,
  damage, range, malfunction, and era availability per weapon — the deck is built to pair with
  the busybodies cards for exactly this.

## Output

- **Stub:** one row appended to `campaigns/<slug>/npcs/roster.md` — no file of its own.
- **Card:** save to `campaigns/<slug>/npcs/<name>.md`, `kebab-case.md` in English, one NPC per
  file.
- Write the content in the campaign's declared **output language**. Stat block notation stays
  English (`STR 60`, `Dodge 35%`); use `reference/glossary-zh.md` for skill names in Chinese.
- **The NPC's name belongs to the setting, not to the output language.** A 简体中文 campaign
  set in 1920s Massachusetts (the default — `core/01-intake.md`) is full of people called
  Kirkland and Whateley; write those names per `reference/glossary-zh.md` →
  外文专名的译写 (音译 + 首次出现括注原文), and keep one spelling per person campaign-wide.
- Cross-link the scenes they appear in and any faction they belong to.

## Quality bar

**Card:**
- Playable from the file in ten seconds: concept, voice, want, secret, one clue.
- Has a want **and** a secret **and** a prepared lie.
- Stat block is internally consistent and era-appropriate.
- Secret and clues sit in keeper-only blocks; nothing here would spoil the mystery if glanced
  at.

**Stub:**
- Playable from the roster row alone for one improvised exchange — a Keeper reading only the
  row can voice this NPC without inventing their want or secret on the spot.
- Doesn't say more than a stub needs to; if it does, it should have been a card.
