# 14 — Archive Reference Material

Take a piece of **third-party material the Keeper hands you** — an official deck, a book, a
transcription — and file it under `reference/` so it is findable, cited, and wired into the
specs that can use it. Doing this by hand always misses a step; follow the checklist.

This spec is about **filing other people's material**. Material the kit writes itself
(cheat-sheets, bestiary entries, roll tables) does not come through here.

## First

- Read the ground rule this implements: `core/00-how-to-run.md` → **Citing official material**.
  Two hard requirements — a `## 引用出处` block on every file, and generators take
  **structure and scale, never text**.
- Read the target directory's README: `reference/decks/README.md` or
  `reference/sourcebooks/README.md`.

## Ask (or infer sensibly)

- **What is it** — which published product, which edition, which language.
- **Where did it come from** — official PDF, a fan translation, a community transcription.
  Ask the Keeper if it isn't in the file. **Never invent a translator or a publisher.**
- **What it is for** — which spec would read it, and to do what. Material nothing will ever
  read does not get archived; say so rather than filing it.

## The checklist

Work in order. Steps 5–7 are the ones people skip, and they are what make the archive usable
rather than a dumping ground.

### 1. Classify

| It is… | Goes to |
|---|---|
| an official card deck — discrete, ready-to-use entries | `reference/decks/` |
| a whole book — read a chapter at a time | `reference/sourcebooks/` |
| a third-party git repo | `reference/external/` as a submodule |
| **the kit's own writing** distilled from any of the above | `reference/rules/`, `bestiary/`, `mythos/`, `tables/` — **not here** |

If it fits none of these, propose a new sibling directory and give it a README stating its
role, its citation rule, and whether it enters `dist/bundle.md`. Don't quietly widen the
meaning of an existing directory.

### 2. Name and normalise

- Filename **English `kebab-case.md`, ASCII only**, even though the content is Chinese
  (`core/00-how-to-run.md` → Conventions). Suffix `-zh` for a Chinese text.
  Prefer the published English title: `malleus-monstrorum-zh.md`, not `怪物之锤.md`.
- Normalise line endings to **LF**.
- Strip conversion artifacts that are not part of the work — PDF-tool banners, page-furniture
  garbage. **Note what you stripped** in the citation block's 收录范围 row. Never silently
  edit the work's actual content.
- If the source PDF is kept, give it the **same basename** next to the transcription
  (`*.pdf` is gitignored, so it stays local).

### 3. Head it

Open the file with a block that tells the next reader what they're holding:

```markdown
# <标题> — <类型>(中译收录)

> **这是第三方官方资料的收录件,不是本 kit 生成的内容。** 出处见文末「引用出处」。
> <一到三行:里面有什么,多少条>
>
> **本 kit 怎么用它**(详见 `reference/<dir>/README.md`):
> - `core/NN-xxx.md` —— <拿它来做什么>
>
> **<警示:已知的转录问题、页码口径、不要照抄的部分>**

---

## 原文转录
```

The warning line is not decoration. Transcriptions are wrong in specific ways — garbled stat
lines, page numbers that point at a different edition, uncorrected chapters. A reader who
doesn't know that will copy a bad number into a stat block.

### 4. Cite it

End the file with a `## 引用出处` section — the exact table in `reference/decks/README.md`:
作品 / 版权方 / 版本 / 本文来源 / 收录范围 / 收录用途, plus a 已知问题 row where one applies,
plus the no-rights-claimed sentence.

**Unknown is a valid value; a guess is not.** If the translator isn't named, write
「未署译者名,译本出处不详」. The point of the citation is that it can be checked.

`scripts/build-reference-index.py` parses this table — it is the single source of truth for
the file's provenance. Get the row labels exactly right or the index will read as empty.

### 5. Wire it in

An archived file nothing points at is invisible; the index reports it as **orphaned** and that
is a failure, not a warning. For each spec that can use it, add a pointer saying *what to take
from it*, not just that it exists.

Every pointer must be phrased as **optional**: archives are local files, absent from
`dist/bundle.md`. A Keeper working from the bundle has to be able to follow the spec without
them. "If present locally" is the standard hedge.

### 6. Rebuild the index

```bash
python scripts/build-reference-index.py
```

Writes `reference/<dir>/index.json` per archive directory and the cross-directory chain in
`reference/index.json`. It fails loudly on a missing citation block, a missing row, or an
orphan. **Fix what it reports; never hand-edit the JSON.**

### 7. Close it out

- Update the target directory's README table (the human-readable view of the same facts).
- Append to root `CHANGELOG.md` — what the Keeper can now do that they couldn't.
- Re-run `scripts/build-bundle.sh` (any `reference/` change requires it) and commit
  `dist/bundle.md` with the source files.
- Check `update_plan/` for anything this material unblocks, and update that plan's 状态.
  Material often arrives precisely because something was waiting on it.

## Output

Report to the Keeper: where it landed and why that directory, what the citation says
(especially anything that came back **不详**), which specs now point at it, and what the index
run said.

## Quality bar

- Filed in the right directory, ASCII `kebab-case.md`, LF endings.
- Header block states what it is, what reads it, and its known defects.
- `## 引用出处` complete, with unknowns marked as unknown rather than guessed.
- At least one spec points at it, phrased as optional.
- `python scripts/build-reference-index.py` reports **no problems**.
- `dist/bundle.md` rebuilt; `CHANGELOG.md` appended; any unblocked `update_plan/` entry updated.
