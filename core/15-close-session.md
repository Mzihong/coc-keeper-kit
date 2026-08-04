# 15 — Close Out a Working Session

Take a session that changed the kit itself — structure, behaviour, a spec, a convention — and
close it out so the next session (yours or someone else's) can pick it up without re-deriving
what happened. Skipping this is how `WORKLOG.md` goes stale, which is worse than it not
existing at all.

This spec is for **everything that isn't already covered by a more specific closing flow**:

- Finishing a whole `update_plan/PNN-*.md` plan → use `update_plan/README.md`'s **完结清单**
  instead. It has extra steps (status sync in two places, plan-graph unlocking, archiving) this
  spec doesn't repeat.
- Filing third-party material → use `core/14-archive-reference.md` step 7 ("Close it out")
  instead. It's the same idea, scoped to one archived file.
- An ad-hoc session that touched `core/`, `templates/`, `reference/`, `scripts/`, or a
  cross-cutting convention **without** a plan file behind it — that's this spec.

If a session is *both* (e.g. closing a plan that also touched `reference/`), follow the more
specific checklist (`update_plan/README.md` or `core/14`) — it's a superset of this one.

## First

Read `git status` / `git diff` (or recall from the session if nothing's staged yet) before
writing anything down. Build the list of touched files first; a session log written from memory
drifts from what actually changed.

**Prune before you add.** For every existing `会话记录` entry, check whether the files it
describes are now committed (`git status` clean for them). If so, delete that entry —
`git log`/`git show` is the authoritative record once something lands, and `WORKLOG.md` only
needs to carry current state plus whatever is still sitting uncommitted in the working tree.
Keep an entry only while part of what it describes hasn't been committed yet.

## The checklist

### 1. Append a `WORKLOG.md` session entry

Add a dated entry under **会话记录**, following the existing entries' shape (**做了什么** /
**为什么这么分** / **留下的判断**, whichever subsections actually apply — don't force all three
if there's nothing to say). If another entry already exists for today, add a new subsection
under it rather than a second top-level date heading — same rule `CHANGELOG.md` uses.

### 2. Fact-check what you just wrote

**This is the step a plain "update the docs" pass skips, and it's why this spec exists.**
Before treating the WORKLOG/CHANGELOG entry as done, grep the repo for every count,
enumeration, or path you named in it — "six directories," "47 cards," "three sourcebooks" — and
confirm each one against the actual filesystem or a generated artifact (`reference/index.json`,
a script's own output), never against memory or against what an earlier entry said. Numbers
copy forward silently and go stale the moment a directory gets added or removed.

Concrete example this caught: a session added `reference/craft/` as a seventh indexed
directory and wrote up the change correctly in both `WORKLOG.md` and `CHANGELOG.md` — but wrote
"六个目录" (six directories) in both places, plus `reference/README.md` and the script's own
docstring. Nobody re-counted against `python scripts/build-reference-index.py --check`'s actual
output ("indexed ... across 7 directories") until a later session grepped for the literal string
and found it in five places at once.

### 3. Sync affected `README.md`s

If the change added, removed, or renamed a file, directory, or convention that a `README.md`
describes — `reference/README.md`, a subdirectory `README.md`, root `README.md` — update the
description in the same pass. A stale directory listing is the same class of bug as step 2's
stale count; check both together.

### 4. Run the applicable parts of `update_plan/README.md`'s 完结清单

Sections **2 (Changelog)**, **3 (产物重建)**, **4 (三适配器一致性)**, and **5 (术语与语言)**
apply to any structural change regardless of whether a plan file exists. Skip section 1
(状态同步) and section 6 (计划间关系) — those are plan-specific; if this session actually is
closing a plan, go use the full checklist there instead of this one.

In short, for a change touching `core/`, `templates/`, or `reference/`:

- `CHANGELOG.md` gets an entry (merged into today's if one exists).
- `python scripts/build-reference-index.py --check` reports clean if `reference/`'s archive
  directories changed.
- `CLAUDE.md` / `GEMINI.md` / `AGENTS.md` stay consistent if any adapter-visible routing changed
  (new skill, new spec, new top-level convention).
- New rules terminology goes into `reference/glossary-zh.md`.

### 5. Report

Tell the Keeper/collaborator: what changed, what got fact-checked in step 2 (and what it caught,
if anything), what's still open, and whether anything needs sign-off before a commit. Don't
commit unless asked — this spec closes out the working tree, not the git history.

## Quality bar

- `WORKLOG.md` has a dated session entry for this session, appended not overwritten.
- `WORKLOG.md`'s `会话记录` holds no entries for work that's already committed — those are
  pruned, since `git log` already carries them.
- Every count, enumeration, or path written this session has been grep-verified against actual
  repo state or generated output — not asserted from memory or copied from an earlier entry.
- `CHANGELOG.md` has an entry (or an addition to today's).
- Every `README.md` describing the changed structure matches it.
- `python scripts/build-reference-index.py --check` clean if `reference/`'s archives changed.
- The three root adapters still agree with each other and with `core/`.
