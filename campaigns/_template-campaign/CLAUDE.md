# CLAUDE.md — <Campaign Name>

> Every generator reads this file to match your game's voice.
>
> **Fill in what you know. Leave anything else as `<auto>`** — `core/01-intake.md` will roll
> or infer it, then show you what it chose so you can accept or reroll. The one exception is
> **content lines and veils**, which are never auto-filled.
>
> Read alongside `canon-log.md` (what has actually happened) and `world/event-clock.md`
> (where the threat currently stands).

## Lineage
> **Optional — delete this section for a standalone campaign (the default).** Only fill it in
> if this campaign is a parallel-world/branching offshoot of another campaign in `campaigns/`.
> See `campaigns/README.md` → "Multi-arc & branching campaigns".

- **Forked from:** <parent-slug> @ session <n> / <in-fiction date>
- Canon before the fork is read-only inherited from the parent's `canon-log.md`; this
  campaign's own `canon-log.md` never writes back to the parent.

## Premise (one paragraph)
<What this campaign is about — the situation, the dread, the promise to the players.>

## Setting
- **Era:** <fixed slug, matched against `reference/rules/eras/README.md`'s index —
  `1920s` (baseline, the default) or one of `cthulhu-invictus` / `dark-ages` /
  `mystic-iceland` / `gaslight` / `icarus` / `end-times`, or a Keeper-approved path-B slug
  (see that file's three-path table). `core/02-rules-reference.md` reads this field
  literally, so keep it to the slug — put "1890s London, fog-choked and gaslit" in the
  Premise/Tone prose below instead, not here.>
- **Region / base of operations:** <city, town, ship, expedition>
- **Timeframe:** <a season, a year, an open-ended chronicle>

## Output language
- **Generated content:** 简体中文
- Everything the table sees — prose, NPC names, boxed text, handouts — is written in this
  language. Kit scaffolding, filenames, and stat-block notation (`STR 60`, `1D6/2D10`) stay
  English.
- When this is 简体中文, every game term follows `reference/glossary-zh.md`. Do not improvise
  translations; do not mix 繁体.
- *Change this line to whatever your table speaks.*

## Tone & style
- **Mood:** <slow dread / pulp action / folk horror / cosmic bleakness / noir investigation>
- **Horror dial:** <creeping and psychological ↔ visceral and violent>
- **Lethality:** <deadly and unforgiving / standard 7e / heroic>
- **Combat frequency:** <rare and lethal / occasional / pulp-frequent>
- **Register for boxed text:** <sparse and cold / lush and gothic>

## Shape
- **Length:** <one-shot (3–4h) / short arc (3–5 sessions) / open-ended chronicle>
- **Party size:** <n>

## The threat
- **Category:** <cult/organisation / lone sorcerer or family / independent monster /
  the place itself / natural or cosmic phenomenon — no human antagonist>
- **Human antagonist strength:** <combat-emphasised / background-first (default) — see
  `reference/rules/character-creation.md` §11. Delete this line if category has no human
  antagonist.>
- <If category is a cult/organisation: name + one-line identity + link to its full
  `world/<name>.md` (built via `core/03-build-world.md`'s cult sub-path, structure mirrors
  `templates/cult.md`). Otherwise: one line naming the antagonist/monster/phenomenon and a
  link to where it's built out.>
- `core/04-design-scenario.md` reads this before constructing the Keeper's truth — it does
  not re-ask this question.

## Content lines & veils (session-zero safety)
> **Never auto-filled.** If undeclared, generators write `<not declared — confirm at session
> zero>` here and generate conservatively.

- **Lines (never appears):** <…>
- **Veils (happens off-screen / faded):** <…>
- Generators must honour these and flag, not silently include, heavy material.

## The investigators
- <name — occupation — one hook tying them to the premise>
- <name — occupation — hook>

*If unknown, write `<party-agnostic>` and the world will be built to accept any group.*

## Investigator cards
- **Pre-built pregens:** <not needed yet / name who needs one — built via
  `core/13-create-investigator.md`>
- **Creation-time validation:** <default (see `investigators/validation.json`) / overridden,
  see that file>
- Config lives in `investigators/validation.json`, read by `scripts/render-investigator.py`;
  edit it directly to change the thresholds later.

## Canon so far (truth — keeper only)
> **KEEPER ONLY**
> - **The real situation:** <the Mythos truth beneath the campaign>
> - **The rolled angle:** <which `mythos-angles.md` result this came from, if any>
> - **The clock:** see `world/event-clock.md` — current stage lives there, not here
> - **Key secrets established:** <structural facts only; session-by-session detail lives in
>   `canon-log.md`>

## House rules
- <any table rulings that differ from 7e default — Luck recovery, pushing, sanity house rules>

## Sources & inspiration
- See `references.md` for books, modules, films, and real history this draws on.

---

## Auto-filled at intake
> Recorded so you always know which decisions were yours and which were the kit's.

| Field | Value | Why |
|---|---|---|
| <field> | <value> `[auto]` | <rolled hooks.md 14 / inferred from era> |
