# npcs/

The people the investigators meet in this campaign. Built with the `create-npc` skill
(`core/06-create-npc.md`), two tiers:

- **Stub (default)** — a row in `roster.md` (`templates/npc-roster.md`): name, role, want,
  secret, one line of voice. No file. Most named NPCs stay here.
- **Card** — a full file, one NPC per file, `kebab-case.md`, from `templates/npc.md`. Only
  built once an NPC meets an upgrade criterion (`core/06` → Two tiers: a check will target
  them, they fight or get chased, real dialogue, or the Keeper/players fixed on them). Keep
  each card's secret in its `> **KEEPER ONLY**` block.

**After each session, every NPC the party actually dealt with gets updated** — a card
overwrites its current attitude and appends one line to the `> **KEEPER ONLY — Interaction
history**` log (facts and relationship changes only; the narration already lives in
`canon-log.md`, cross-link the session number instead of repeating it); a stub overwrites its
roster row's **Status** column instead — it has no file to log into. This is a required step
of `core/12-canon-update.md`, not an optional one — it's what keeps "does this NPC trust
them?" answerable without rereading the whole campaign.
