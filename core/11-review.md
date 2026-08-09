# 11 — Review

Run this on generated material **before it reaches the table**. It is a verification pass,
not a rewrite: read what exists, check it against the list, report what fails, then fix what
the Keeper asks you to fix.

This spec exists because the quality bars in the other specs are written for the model that
*generates*. This one is written for a model that *audits* — including auditing another
model's output. Assume the material is wrong until each line checks out.

## How to run it

1. Ask what to review, or infer it (a scenario, a session, the whole campaign folder).
2. Read the campaign `CLAUDE.md`, `canon-log.md`, and `world/event-clock.md` for the
   standards this material must meet.
3. Walk the checklist below. For each item: **pass**, **fail**, or **n/a**.
4. Report failures **most-severe first**, each with the file, the specific problem, and a
   concrete fix. Don't report passes individually — one line confirming the rest passed.
5. Fix only what the Keeper approves. A review that silently rewrites is not a review.

## The checklist

### Blocking — the session breaks without these

- [ ] **Three clues per must-know fact — three checks, not a count.** Don't trust the clue
      map's own claim; trace each of the following (`core/04-design-scenario.md` step 5 is
      the generation-side spec these mirror):
      1. **Forward trace (ghost clues).** Walk from the investigators' starting point through
         the scene web. Does the scene holding each clue actually have an inbound edge? A
         clue sitting in an unreachable scene doesn't count as a source.
      2. **Tonight-discovery test (independence).** If the threat learned tonight it's been
         made, how many of the three could it destroy or silence by morning? Two or more
         killable means they aren't independent, whatever the clue map claims.
      3. **Shelf life (decay).** Are all three clues perishable on the same clock? If none is
         marked permanent and the event clock has advanced past them, the "guarantee" may
         already be gone — check `world/event-clock.md`'s current stage, not the scenario
         file's static claim.
- [ ] **No single-roll gates.** No failed check anywhere can end the investigation. Trace each
      required clue back: if the only route is one roll, it fails.
- [ ] **Every lock has ≥2 keys.** Puzzles, locked doors, and uncooperative NPCs all have an
      alternate route plus a mercy path.
- [ ] **Every monster has a fair out**, and it is discoverable in play — not only in the
      Keeper's notes.
- [ ] **At least one non-combat resolution** to the central threat exists.
- [ ] **No unwinnable state.** Is there any sequence of reasonable player choices that leaves
      the scenario with no path forward? Name it if so.
- [ ] **A reference to an ungenerated NPC or handout is two different findings — tell them
      apart before reporting either.** The demand-driven default (`core/00-how-to-run.md` →
      "preview, then confirm, then expand"; `core/06-create-npc.md` → Two tiers) means most
      named NPCs are *supposed* to not have a card yet, so "the file doesn't exist" alone is
      not a finding:
      1. **Stub, registered — pass.** The name appears as a row in `npcs/roster.md`. Not yet
         generated is the intended state; don't flag it.
      2. **Broken link — fail.** The name appears in a scene, clue map, or scenario file but
         is **absent from `npcs/roster.md` entirely** — no stub, no card. That's not "not yet
         generated," that's a dangling reference nothing will resolve at the table.
      Same logic for handouts: a handout named in the clue matrix but absent from
      `handouts/` — **pass** if it's honestly not built yet and nothing downstream assumed it
      existed; **fail** only if something (a scene's "if the players…" branch, a puzzle) reads
      as though the handout is already in hand.
- [ ] **`campaigns/<slug>/module/` files: trace it both ways** — mirrors
      `core/16-compile-module.md` step 3. **n/a** if nothing under `module/` is in scope.
      1. **Forward (catches invented facts).** Spot-check a sample of claims (a timeline beat,
         an NPC's stated want, a clue's location) against `world/`, `npcs/`, `scenes/`, or the
         scenario file it was compiled from. A fact that exists only in the module text is a
         fail regardless of how plausible it reads — compiling never invents.
      2. **Backward (catches withdrawn facts).** Forward tracing cannot see the failure that
         actually happens most: the module says something the sources **used to** say and have
         since changed. Walk the module's open questions, glossary rows, and location
         descriptions back against the current `CLAUDE.md` and `world/` — anything the sources
         no longer support is a fail even though it traced fine when it was written.
         **Open questions are the worst offender: an answered one looks exactly like a live
         one.** Nothing in its formatting expired. A recompile does not fix this by itself —
         a section can be regenerated and still carry the old question forward.
- [ ] **Three-clue coverage audits the clue *matrix*, not the file count.** All three clues for
      a must-know fact must be **registered** in the scenario's clue map — but an individual
      clue is allowed to route through an NPC who's still a stub, or a scene that's still
      gist-only (`core/09-description.md` → Output). Don't fail a clue for pointing at
      ungenerated prose; fail it only if it's missing from the matrix altogether or the check
      above already flagged its source as a broken link.

### Continuity

- [ ] Nothing contradicts `canon-log.md` — dead NPCs stay dead, revealed facts stay revealed.
- [ ] Nothing contradicts `world/event-clock.md`'s current stage or fired triggers.
- [ ] **The campaign's own files agree with each other.** The two checks above read
      `CLAUDE.md` and `canon-log.md` as the *standard* the material is measured against; this
      one puts them **on the table as material too**. Take each fact the campaign states more
      than once — what an object actually is, which questions are still open, what a place is
      called, when something happened — and compare `CLAUDE.md` against `world/`, `overview.md`,
      `canon-log.md`, and `module/`. **A disagreement is a fail, and the report says which side
      is newer with the evidence for it (git history, dated markers, the Auto-filled table's
      rulings) — but the report does not pick a winner.** The Keeper rules; a review that
      resolves conflicts on its own is how the divergence got there.
      Two cautions, both from real misfires:
      - **A precedence rule doesn't make this check unnecessary.** "`CLAUDE.md` always wins"
        decides *how a conflict is settled once raised*; it does not mean the conflict may go
        unmentioned, and the Keeper may rule that the authoritative file is the wrong one.
      - **Confirm both sources are counting the same thing before calling it a contradiction.**
        Two lists of different lengths conflict only if they index the same set — a
        proper-noun lock and a demand-driven NPC roster are meant to differ.
- [ ] Names, dates, and place-names match their earlier spellings exactly.
- [ ] Cross-links resolve — every relative link points at a file that exists.
- [ ] **Rolled content traces back to `campaigns/<slug>/rolls.log`.** If the material rolled
      anything (a seed table, an NPC quirk, a complication), the campaign has a `rolls.log`
      and its entries match what the material claims was rolled — a fail here usually means a
      result was reported from memory instead of `python scripts/roll.py`.

### Craft

- [ ] Every NPC has a **want**, a **secret**, and a **prepared lie**.
- [ ] Every scene is keyed by purpose (clue / choice / shock / breather).
- [ ] **Every must-reach scene has ≥3 inbound edges** on the scene web (mirrors
      `core/04-design-scenario.md` step 5 and `reference/craft/diagram-conventions-zh.md` §三
      — a scene the players *must* hit with fewer than 3 clues pointing to it is a stall point).
      Trace it from the investigators' starting point; don't trust the diagram's own claim.
- [ ] Scenes **other than** the must-reach ones form a web too — most of them reachable in
      more than one order, not a single required sequence (`core/04` step 6).
- [ ] Boxed text: 3–6 sentences, ≥2 senses, one wrong detail, ends on a hook.
- [ ] SAN hits are spaced, not stacked; the biggest lands at the reveal.
- [ ] Scenario-level material: each ending carries a suggested SAN reward (or explicitly none
      for muddled/grim), and a Scaling sidebar exists if the table's size differs from baseline.
- [ ] **Puzzles: the 3-rung hint ladder (nudge / lead / gift) is written out**, not merely
      implied — `core/08-create-puzzle.md`.
- [ ] **Event clock: every trigger has both a fires-branch and a fails/half-succeeds branch**,
      and at least two doom stages are marked reversible — `core/05-event-clock.md`'s quality
      bar. A trigger with one outcome is a railroad tie.

### Mechanics

- [ ] Stat blocks internally consistent: HP = (CON+SIZ)/10, Dodge = ½ DEX, Build and Damage
      Bonus derived from STR+SIZ. **Recompute them; don't eyeball.**
- [ ] **Human antagonists: skill height is lethality-derived, not background-derived.**
      Background picks *which* skills a villain has; it never justifies *how high* one goes.
      If a skill value would land a single successful roll as an unrecoverable outcome on an
      investigator, that's the ceiling regardless of the character's backstory
      (`reference/rules/character-creation.md` §11). Cross-check against the campaign
      `CLAUDE.md`'s declared **lethality** field.
- [ ] Difficulties (Regular/Hard/Extreme) are set deliberately and only where failure is
      interesting.
- [ ] Sanity costs are proportionate to the horror, not to the gore.
- [ ] **Content matches the campaign's declared Era.** Technology, equipment, and common
      knowledge in stat blocks and prose don't leak in from the wrong period (a 1920s default
      showing up in a `dark-ages` scene, cars where the era's Technology & common knowledge
      section says there are none) — see `reference/rules/eras/README.md`. If the Era resolves
      to path B, confirm `campaigns/<slug>/rules-era.md` exists, follows the five-section
      convention, and is marked derived/not book-backed — and that the material actually
      layers it rather than defaulting to the nearest indexed era or to 1920s.
- [ ] Any `investigators/*.json` validates against `templates/investigator.schema.json`; its
      derived stats are internally consistent and its `.md` view agrees with the JSON.
- [ ] **Non-human monsters: every numeric trait has a discoverable counter-play.** For each
      trait listed under "Special abilities (traits)", confirm the entry (or a linked file)
      states how a player could find or use that trait's 破解口 — a counter-play that exists
      only in `reference/tables/monster-traits.md` and never reaches the table doesn't count.
      N traits demand N *findable* answers; one missing is a broken fair-out, not a nitpick.
- [ ] **Non-human monsters: trait load is at or under the tier ceiling.** Sum the loads on
      "Trait load total" against `reference/rules/monster-scale.md`'s ceiling for that tier
      (L2/L3 = 2, L4 = 3, L5 = 4). Over budget means the entry reads as the wrong tier wearing
      a costume, not a legitimately scarier version of its actual tier.

### Safety & spoilers

- [ ] Declared **lines** appear nowhere. Declared **veils** are off-screen.
- [ ] Heavy material is flagged for the Keeper, not silently included.
- [ ] Every player-facing file (`handouts/`, boxed text) is spoiler-clean — read it as a
      player would and confirm it gives away nothing.
- [ ] Keeper-only content is inside `> **KEEPER ONLY**` blocks, never in player files.

### Language

- [ ] Everything is in the campaign's declared **output language** — no drifted-back-to-English
      paragraphs.
- [ ] 简体中文 material uses `reference/glossary-zh.md` terms consistently; no 繁体 characters;
      no two translations of the same game term.
- [ ] **Proper nouns follow the setting, not the output language.** A 简体中文 campaign set
      abroad (the default is American — `core/01-intake.md`) transliterates people, places,
      and institutions per `reference/glossary-zh.md` → 外文专名的译写: one spelling per name
      campaign-wide, original in parentheses on first appearance, Japanese names in 汉字
      rather than re-transliterated through English.
- [ ] Filenames are English `kebab-case.md`.
- [ ] Any cipher or wordplay actually works in the script it's written in.

## Report format

```
BLOCKING
1. campaigns/dagon-bay/the-red-tide.md — "the ledger" is the only route to Fact 2.
   Fix: add a second source (the harbourmaster's slip) and a third (the dredging photos).

CRAFT
2. npcs/mary-tang.md — has a secret but no prepared lie; the Keeper will have to invent
   her answer mid-scene. Fix: add what she says when asked directly about the boat.

Everything else on the checklist passes.
```

## Quality bar

- Every blocking item was actually traced, not assumed. Say how you verified the three-clue
  count and the stat arithmetic.
- Findings are specific enough to act on without re-reading the whole file.
- Nothing was rewritten without approval.
- If the material passes, say so plainly rather than inventing findings.
