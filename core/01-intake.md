# 01 — Intake: Start a Campaign

Turn a spark of an idea into a filled-in campaign `CLAUDE.md` the rest of the kit can read.

The Keeper should be able to answer **as much or as little as they want**. Ask properly —
detailed questions get a campaign that feels like *theirs* — but never require an answer.
Any question can be answered `auto` and you will decide it well.

## How to run intake

1. Ask the questions below **in one message**, grouped and numbered, with the defaults shown.
2. State clearly, up front:
   > Answer any subset. Reply **`auto`** to any question and I'll choose. Reply
   > **`all auto`** and I'll build the whole thing and show you the result to accept or reroll.
3. For every unanswered question, resolve it with **Auto-fill** (below) — never leave a
   template field blank and never invent a fourteenth question.
4. Write `campaigns/<slug>/CLAUDE.md` from `campaigns/_template-campaign/CLAUDE.md`.
5. Show the Keeper a **summary of every auto-filled choice**, marked `[auto]`, and offer:
   *accept* / *reroll this one* / *reroll all*. Do not proceed to the world until they accept.

## The questions

Ask all of these. They are the ones that actually change downstream output.

**A. The game**
1. **Era & place** — when and where? (e.g. 1920s New England, 1930s Shanghai, present-day
   Hong Kong, 1890s Gaslight London)
2. **Premise** — one line. What's wrong, or what's the promise to the players?
3. **Output language** — what language should the generated material be in?
   *Default: 繁體中文（香港）.* Filenames and kit scaffolding stay English regardless.

**B. The feel**
4. **Mood** — slow dread / folk horror / pulp action / cosmic bleakness / noir investigation.
5. **Horror dial** — creeping and psychological ↔ visceral and violent.
6. **Lethality** — how survivable? (deadly and unforgiving / standard 7e / heroic)
7. **Combat frequency** — rare and lethal / occasional / pulp-frequent.
8. **Register for boxed text** — sparse and cold / lush and gothic.

**C. The table**
9. **Length** — one-shot (3–4h) / short arc (3–5 sessions) / open-ended chronicle.
10. **Party size** — how many investigators?
11. **The investigators** — names, occupations, and one hook each tying them to the premise.
    (If unknown, say so — the world will be built to accept any party.)

**D. Safety — never auto-filled**
12. **Lines** — content that never appears at your table.
13. **Veils** — content that happens off-screen or fades to black.

> **Question 12 and 13 have no default and are never auto-filled.** If the Keeper skips them,
> ask once more, plainly: *"I won't guess at safety content — what's off the table?"* If they
> decline again, write `<not declared — confirm at session zero>` into the campaign file and
> generate conservatively: no on-screen harm to children or animals, no sexual violence, no
> detailed self-harm.

**E. Optional, ask only if they're engaged**
14. **House rules** — anything you run differently from 7e default.
15. **Touchstones** — films, books, or real history this should feel like.

## Auto-fill

When a question is unanswered, resolve it in this order:

1. **Infer from what they did say.** "1930s Shanghai" implies era, currency, transport,
   name conventions, and a plausible mood. Use it. Consistency beats novelty.
2. **Roll the seed tables** in `reference/tables/` — `hooks.md`, `locations.md`,
   `mythos-angles.md`, `complications.md`. Roll; don't pick the first plausible thing you
   think of.
3. **Apply the defaults** for anything the tables don't cover:

| Field | Default |
|---|---|
| Era & place | 1920s, a small coastal town — the genre's home ground |
| Output language | 繁體中文（香港） |
| Mood | slow dread |
| Horror dial | creeping and psychological |
| Lethality | standard 7e |
| Combat frequency | rare and lethal |
| Register | sparse and cold |
| Length | short arc, 3–5 sessions |
| Party size | 4 |
| Investigators | unknown — build the world party-agnostic |

### The anti-generic rule

Left to itself, every model writes the same campaign: Arkham, a cult, a Great Old One
stirring. **You must roll**, and the roll must survive into the output.

- Roll `mythos-angles.md` and take what you get. If the result is not obviously compatible
  with the era and premise, that friction *is* the campaign — make it work.
- Roll `locations.md` for at least one place that isn't the obvious one.
- Roll `hooks.md` for the way the investigators are pulled in.
- Before finishing, check: **would this be different if I'd rolled again?** If the rolled
  results left no fingerprint on the result, you ignored them. Redo it.

## Output

- Write `campaigns/<slug>/CLAUDE.md`, filled completely — no `<placeholder>` text left.
- `<slug>` is English kebab-case, derived from the premise (`dagon-bay`, `the-red-tide`).
- Copy the rest of `campaigns/_template-campaign/` alongside it, including `canon-log.md`.
- Report every auto-filled field, marked `[auto]`, with a one-line reason.

## Quality bar

- The Keeper answered as few as zero questions and still has a complete, specific campaign.
- Every `[auto]` choice is disclosed — the Keeper is never surprised by a decision they
  didn't make.
- Lines and veils are declared, or explicitly marked as undeclared with conservative
  generation in force.
- The rolled seeds are visibly present in the result: name a place, an angle, and a hook
  that came from the tables rather than from habit.
