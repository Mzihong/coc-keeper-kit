# WORKLOG — 给接手会话的上手速览

**这份文件的用途:让新对话不必重新摸一遍项目结构。** 开工前读这一份,而不是把
`core/`、`reference/`、`update_plan/` 挨个翻一遍。

和另外两份的分工:

| 文件 | 写给谁 | 内容 |
|---|---|---|
| `CHANGELOG.md` | **Keeper(用户)** | 每次改动后"你现在能做什么" |
| `WORKLOG.md`(本文件) | **接手的模型/协作者** | 结构在哪、约定是什么、现在卡在哪、上次做了什么 |
| `update_plan/README.md` | 两者 | 计划级状态索引与完结清单 |

> 本文件**手工维护**。改了结构、约定或计划状态就顺手更新这里;它过期比不存在更糟。

---

## 一句话

CoC 7e 守秘人备课工作台。**所有指令都在 `core/`**,根目录三个 `*.md` 只是路由适配器。
`core/00-how-to-run.md` 是唯一入口——不确定任何事时读它,它压过一切。

## 结构速览

```
core/00 … 14        指令本体。00=入口/管线/路由/铁律/布局,02=规则查询(写数前必读)
                    01 intake · 03 world · 04 scenario · 05 clock · 06 npc · 07 monster
                    08 puzzle · 09 description · 10 handout · 11 review · 12 canon
                    13 investigator · 14 archive-reference(归档第三方资料)
CLAUDE/GEMINI/AGENTS.md   三份薄适配器。改行为改 core,不改这三份;但三份必须彼此一致
.claude/skills/<name>/    Claude Code 技能壳,只有一句"读 core/NN"
templates/          每种产物的空壳。investigator 是 JSON schema + md 卡面双件
reference/          跨战役共享
  ├ rules/          kit 自己写的 7e 速查:**数字**(原创、进 bundle)
  ├ craft/          kit 自己写的手法提炼稿:**写法**(原创、进 bundle)
  ├ bestiary/ mythos/ tables/   原创可复用素材
  ├ decks/          官方卡组转录(第三方、带引用出处、不进 bundle)
  ├ sourcebooks/    官方书籍全文转录(同上,体量更大)
  ├ index.json      六个目录的反向索引 + 校验(脚本生成,各目录另有一份)
  ├ og_Norval/      洛夫克拉夫特全集 82 篇 → 提炼稿 craft/lovecraft-zh.md
  └ glossary-zh.md  中文术语锁,写中文必查(脊梁文件,故意留在根目录)
campaigns/          一战役一目录,_template-campaign/ 是模板
update_plan/        P1–P9 改动计划 + 完结清单;README.md 是状态索引
scripts/            build-bundle.sh · render-investigator.py · build-reference-index.py
dist/bundle.md      构建产物:整个 kit 拼成一份,给没有仓库的 ChatGPT/Gemini
```

## 硬约定(踩了就是 bug)

1. **改行为改 `core/`,不改根适配器**;但 `CLAUDE.md`/`GEMINI.md`/`AGENTS.md` 三份必须一致,
   只存在于一份里的指令本身就是 bug。
2. **动过 `core/`/`templates/`/`reference/` 必须重跑 `bash scripts/build-bundle.sh`**,
   `dist/bundle.md` 和源文件同一个 commit。不重建,ChatGPT 用户就永远用着旧规则。
3. **每次改动在 `CHANGELOG.md` 追加**;同一天合并进同一条,不新开。
4. **文件名一律英文 ASCII `kebab-case.md`**,哪怕内容是中文。
5. **输出语言按战役声明**,kit 脚手架和文件名保持英文;写中文查 `reference/glossary-zh.md`。
6. **转载规则(2026-08-02 改)**:kit *生成*的内容不含任何受版权原文;官方资料**可以收录**
   进 `reference/decks/`、`sourcebooks/`,但文件末尾必须有 `## 引用出处` 表,且生成器
   **只取结构和数值刻度,不取文字**。规则本体在 `core/00-how-to-run.md` → ground rules。
7. **归档件不进 bundle**,所以任何 spec 引用它们都要写成可选("if present locally")。

## 当前状态(2026-08-02)

计划 P1–P9 的权威状态在 `update_plan/README.md` 的状态索引表,**不要在这里读状态**,
只记两条容易漏的:

- **P7 魔法速查阻塞已解除** —— 它等的转换稿就是现在的
  `reference/sourcebooks/grand-grimoire-zh.md`,可以开工了。
- **P9 怪物模板的"来源红线"部分有答案** —— 转载规则已改,且
  `reference/sourcebooks/malleus-monstrorum-zh.md` 已可读;剩下要 Keeper 定的是范围。

`update_plan/README.md` 末尾还有一张**按可动性排序的表**(哪个计划现在能动、卡在等谁),
接手时先看那张。

---

## 会话记录

### 2026-08-02 — reference/ 归档体系

**做了什么**

1. **改了 kit 的转载规则。** 原规则一刀切"不复制任何受版权文本",把官方卡组这类有用的
   取材源挡在门外。新规则见上面硬约定第 6 条。同步改了 `core/00`、`CLAUDE.md`、
   `CONTRIBUTING.md`、`README.md` 免责声明——原本这几处都写着与新事实不符的话。
2. **`reference/` 根目录 7 份散落的 md 全部归位**,分成两类:

   | 目录 | 收了什么 |
   |---|---|
   | `decks/` | 好事者、恐惧症、惨事、武器与造物 4 份官方卡组 |
   | `sourcebooks/` | 7e 规则书、魔法大典、怪物之锤 3 份整书转录(共约 5.4 万行) |

   每份都改成英文 `kebab-case.md`、LF、加头部导读(含已知转录缺陷警示)、加 `## 引用出处`。
   两份 PDF 也从 `rules/` 挪到 `sourcebooks/` 与转录稿同名并列。
3. **反向索引** `scripts/build-reference-index.py` → `reference/index.json` 及各目录
   `index.json`。出处从各文件的 `## 引用出处` 表**解析**而来(引用块是唯一真源),
   引用关系靠全仓库扫描,精确到行号。脚本同时是校验器:缺引用块、缺行、或归档件没人引用
   都会报错。**改归档件后重跑它。**
4. **归档流程规范化** `core/14-archive-reference.md` + 技能 `archive-reference`,
   七步清单(分类→命名→头部→引用→接线→重建索引→收尾),已在三份适配器路由表登记。
5. **接线**:7 份资料接进 `core/02/04/06/07/13`、`reference/rules|tables|bestiary|mythos`。
   顺带解除 P7 阻塞、更新 P6/P9 的相关条目。

**为什么这么分**

`decks/` 与 `sourcebooks/` 分开,是因为用法不同:卡组是现成条目、随取随用;书是深查、
为一个数字翻一章。合成一个目录会让"我该读哪份"变模糊。
`rules/` 保持只放 kit 原创速查——它进 bundle,而转录件不进。

**留下的判断**

- **`glossary-zh.md` 故意留在 `reference/` 根目录**,不归任何子目录。它有 26 处引用、
  21 个文件,其中三处是硬依赖(`build-bundle.sh` 白名单、两个战役的 `CLAUDE.md`、
  `benchmark.json`);更重要的是它的角色是**脊梁文件**,和 `README.md` 同级,不是某个
  分类下的一份资料。为它单开只装一个文件的目录,只有改名成本没有分类收益。
  这条判断记在 `reference/index.json` 的 `kit_original_loose_files` 里。
- `og_Norval/`(82 篇洛氏原作)也是第三方资料,但它是公共领域且已自成目录,这轮没并进
  归档体系,只在 `reference/index.json` 的 `third_party_elsewhere` 里登记了位置。
  以后若要统一到一个 `source/` 伞下,那是一次独立的大改名。
- 仓库是公开的,收录 7 份官方资料原文是 Keeper 明确拍板的决定。标注出处解决了署名与
  可追溯,但不等于取得授权;`README.md` 免责段已加"版权方可开 issue 要求下架"。

**同日第二轮:新增 `reference/craft/`**

`lovecraft-craft-notes-zh.md` → `craft/lovecraft-zh.md`。理由不是"根目录要干净",而是
**P1 已经排好了它的同类**:`update_plan/2026-08-02-cult-doc-integration.md` 第三章 A 项
要产出邪教设计手法稿,计划里写明"定位对标 lovecraft 笔记"。不建目录,它就会再落到根下。
该计划的落点已同步改成 `craft/cult-design-zh.md`。

`craft/` 与 `rules/` 的分工:**rules 管数字,craft 管写法**。两边都是 kit 原创、都进 bundle,
但一个错了数值不对,另一个错了文字平庸。

顺手修了一个既有 bug:`core/09-description.md` 把这份笔记当硬依赖("Both draw on…"),
但它**从来不在 `dist/bundle.md` 里**——用 bundle 的 Keeper 被指去读一份拿不到的文件。
已把 `reference/craft/*.md` 加进 bundle 白名单。

索引脚本同时扩到六个目录(原本只索引 decks/sourcebooks),kit 原创目录不校验引用出处、
只做 orphan 检查;`bestiary/`、`mythos/` 是内容库,没人引用属正常,不计为错误
(`ORPHAN_IS_ERROR`)。
