# 09 — Description

Write the prose a Keeper says aloud — dread built from concrete, ordinary detail with one
thing quietly wrong. Evocative but *tight*: players stop listening after a few sentences.

Two modes share this craft:

- **A. Scene description** — the boxed text for a place: what the investigators see, hear,
  and feel when they arrive somewhere, or the reveal of a horror.
- **B. Investigator action description** — the prose for what *an investigator does*: picking
  the lock, wading into the flooded cellar, reading the ritual aloud. Same senses, same
  restraint, but the camera is on the character's body and choices, not the room.

Both draw on `reference/craft/lovecraft-zh.md` — §一 (tone) applies to either mode, §二
splits into scene-description and investigator-action technique sections specifically for
this file.

## First

- Read the campaign `CLAUDE.md` for **era, tone, register, output language, content lines** —
  period-true detail only.
- Decide which mode is being asked for, and the passage's **purpose**: a clue, a choice, a
  shock, a breather, or (for Mode B) a moment of competence, risk, or discovery. Purpose sets
  length and where the paragraph "points."
- For Mode A, use `templates/scene.md` (full scene) or just draft the boxed text if that's all
  that's asked. Mode B rarely needs its own file — see Output below.

## The shared craft

- **3–6 sentences.** Long enough to immerse, short enough to keep the table's attention.
- **Multi-sensory:** always beyond sight — sound, smell, temperature, the feel of the air,
  the quality of the light. Two or three senses per passage. `reference/craft/lovecraft-zh.md`
  §二's most consistent finding: **smell and sound arrive before sight**, often replacing it
  entirely — lead with what's heard or smelled, let the visual confirmation lag or never come.
- **Concrete over abstract.** "The wallpaper is furred with damp" beats "it feels creepy."
  Precise numbers (a stair count, a measurement) read as more credible than adjectives, and
  make the eventual wrongness land harder — see §二's "精確測量製造真實的巨大感".
  Let players draw the dread; don't tell them they're scared.
- **One wrong detail** for a scene, or **one telling action** for an investigator — a single
  off-key note (a clock stopped at the same time in every room; an animal that won't come
  near) does more than a pile of adjectives. §二 calls this "以缺席/否定定義異樣" — absence
  and refusal read as more unsettling than an added monster.
- **End on a hook, not a full stop** — something that invites action ("the cellar door stands
  open") rather than closing the moment down.
- **Say only what they perceive.** Keep interpretation, mechanics, and secrets *out* of the
  read-aloud text — those go in keeper notes below it.

## Mode A: Scene description

- Everything above, aimed at a place. If it's a full scene, assemble it (see below); if it's
  just the boxed text, draft that alone.
- **For a physical confrontation**, ground the space in its `confrontation-grounds.md` roll
  (`core/04-design-scenario.md` step 6) rather than inventing the room from habit — let the
  terrain and what's usable there pick which senses and which "wrong detail" you write.
- **For a horror reveal**, lead with the **image and motion**, then hand off the Sanity roll
  to the monster's entry (`core/07-create-monster.md`). Describe wrongness through effect
  (what it does to the light, the smell it brings) rather than a full anatomy dump — see
  `reference/craft/lovecraft-zh.md` §三 for how HPL stages a reveal before this handoff.

### Assemble the scene (if full)

Boxed text → what's here (clues, NPCs, features) → "if the players…" branches → the checks
that might come up (set difficulty, never gate the only path) → `> **KEEPER ONLY**` truth and
escalation.

## Mode B: Investigator action description

Use this when the Keeper asks what happens *when an investigator does something* — picks a
lock, reaches into dark water, reads the incantation aloud — rather than what a place looks
like.

- **Describe the act, not just the outcome.** A procedural, almost mechanical detail (counting
  stairs, checking a knot, re-reading a line before speaking it) works as a psychological
  anchor for the character and for the reader — `reference/craft/lovecraft-zh.md` §二's
  "程序化動作作為對抗恐懼的心理防線". If that detail breaks off mid-action, that break *is*
  the tension beat — don't narrate the fear directly, let the interruption carry it.
- **Physical symptom over stated emotion.** A hand that won't stop shaking, a breath held too
  long, hearing your own voice crack before you register you're afraid — show the body, not
  the feeling word. See §二's "生理徵狀外顯心理狀態".
- **Competence is a lens, not armour.** If the investigator has a relevant skill or profession,
  let their expertise shape *how* they describe what they're doing (a doctor's clinical
  vocabulary, a sailor's knot-work) — it makes the eventual failure or wrongness land harder
  by contrast, not softer.
- **Keep it to 2–4 sentences** unless the action is the climax of a scene. This is a beat, not
  a set-piece.
- **Don't resolve the mechanics inside the prose.** Narrate the attempt and its sensory
  texture; the dice/skill roll that determines success sits outside this text, same spoiler
  discipline as Mode A.

## Writing in 简体中文 (both modes)

- Read it aloud in your head. This prose is **spoken**, so favour 口语书面语 that a Keeper can
  say naturally; avoid dense 文言 and long attributive chains that need a second pass to parse.
- Keep sentences short. Chinese tolerates fewer subordinate clauses than English before a
  reader loses the thread out loud.
- Sensory vocabulary carries the weight — 潮、腥、黏、锈、闷、发霉 — not adjective stacking.
- Period register matters: 1920s 上海 and present-day 香港 should not sound alike.
- Follow `reference/glossary-zh.md` for any game term that appears.

## Output

- **Mode A:** save to `campaigns/<slug>/scenes/<name>.md`, `kebab-case.md` in English. Boxed
  text goes in a `>` blockquote so it's obvious what to read aloud. Cross-link NPCs, monsters,
  puzzles, and handouts present.
- **Add a floor-plan map when connectivity or sightlines matter to how the scene plays**
  (which room the sound came from, whether the window is reachable) — use `templates/scene.md`'s
  optional Map section and `python scripts/render-map.py`. Skip it when the boxed text alone
  already tells the Keeper everything they'd need to adjudicate movement.
- **Mode B:** usually returned inline, not saved — it's a live-play beat, not a standing
  artifact. If it belongs to a specific prepared scene (e.g. what happens when they try the
  risky thing), fold it into that scene file's "If the players…" branch instead of creating a
  separate file.

## Quality bar

- Reads aloud smoothly in ~20–30 seconds; no tongue-twisters or stage directions mid-prose.
- At least two senses and one "wrong" detail (Mode A) or one telling physical/procedural beat
  (Mode B); ends on a hook.
- No secrets, mechanics, or player interpretation leaked into the read-aloud text.
