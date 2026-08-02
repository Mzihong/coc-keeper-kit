# sourcebooks/ — 官方书籍全文收录(第三方资料)

**整本官方书的转录件**,给生成器当数值标尺和原文核查用。和 `decks/` 同属第三方资料,
同一套[引用标注规则](../decks/README.md#引用标注规则强制);区别只是**体量与用法**:
卡组是现成条目、随取随用,书是深查——为一个数字翻一章。

**这里不是 `rules/`。** `rules/` 是本 kit 自己写的 7e 速查表(原创、提炼、可进 bundle);
`sourcebooks/` 是原文转录(第三方、逐字、不进 bundle)。**两者冲突时以本目录为准**,
并且要回头修 `rules/` 里那份速查表。

## 现有条目

| 文件 | 是什么 | 谁在用 |
|---|---|---|
| `keeper-rulebook-7e-zh.md` | 《克苏鲁的呼唤》第七版规则书全文 | `core/02-rules-reference.md`、`reference/rules/*` 的溯源 |
| `grand-grimoire-zh.md` | 《克苏鲁神话魔法大典》,550+ 法术 | `core/07-create-monster.md`、`core/06-create-npc.md`、`reference/mythos/` |
| `malleus-monstrorum-zh.md` | 《怪物之锤》神话生物图鉴 | `core/07-create-monster.md`、`reference/bestiary/` |

同名 `.pdf` 是转录所依据的原始文件,被 `.gitignore` 的 `*.pdf` 规则挡在版本库外,
只在本地留存。**转录稿与 PDF 同名并列**,便于核对哪份 md 出自哪份 PDF。

## 转录稿不是权威

每份都是 PDF 文字提取的产物,**质量参差**:断字、表格错行、目录页码混进正文、
部分章节原译者自述未校对。头部的警示块逐份写明了已知问题。

**取任何数值前先人工判读,不要直接喂给生成器。** 转录稿的用途是让你能*查到*,
不是让你能*照抄*。

## 用法

和 `decks/` 一样:**取结构和数值刻度,不取文字**(`core/00-how-to-run.md` → ground rules)。
提炼出来的速查表写进 `reference/rules/`,并在每节标注 `来源` 指路——指到本目录的哪份书、
哪一章,不摘原文。这条惯例的样板见 `reference/rules/character-creation.md`。

## 不进 bundle

`scripts/build-bundle.sh` 不打包本目录 —— 三份加起来五万余行,且属第三方文本。
用 `dist/bundle.md` 的 Keeper 读不到,所以**任何 spec 都不得把这里当前置依赖**。

## 新增条目

走 `core/14-archive-reference.md`(skill:`archive-reference`)。手工搬文件必漏步骤——
命名、头部导读、`## 引用出处`、重建索引、接线到消费 spec、CHANGELOG,一步不能少。
