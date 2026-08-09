# WORKLOG — 给接手会话的上手速览

**这份文件的用途:让新对话不必重新摸一遍项目结构。** 开工前读这一份,而不是把
`core/`、`reference/`、`update_plan/` 挨个翻一遍。

和另外两份的分工:

| 文件 | 写给谁 | 内容 |
|---|---|---|
| `CHANGELOG.md` | **Keeper(用户)** | 每次改动后"你现在能做什么" |
| `WORKLOG.md`(本文件) | **接手的模型/协作者** | 结构在哪、约定是什么、**哪里有坑** |
| `update_plan/README.md` | 两者 | 计划级状态索引与完结清单 |

> **本文件手工维护,而且刻意保持短——硬上限 ~180 行。** 它是**活知识**的清单,不是历史档案。
>
> **组织轴:按「接手的人会踩什么坑」分节,不按「我们做过什么」分节。** 没有人带着
> 「P9 做了什么」这个问题来,他们带着「什么会咬我」来。
>
> **三条剪枝规则(第 2、3 条 2026-08-08 补立):**
> 1. **`会话记录` 只留未提交的工作。** 改动一旦 commit,那条就删——`git log`/`git show` 才是
>    权威历史。收尾流程见 `core/15-close-session.md`("Prune before you add")。
> 2. **已归档计划的执行史不留在这里。** P1–P18 怎么做的、当时怎么权衡的,权威在
>    `update_plan/Archived/<计划文件>` 与 `git log`。本文件只留**还在生效的结论**。
> 3. **不要照着上一条的样子写,照着本节的规则写。** 这是 2026-08-08 诊断 `CHANGELOG.md`
>    体例膨胀时找到的病因,本文件得的是同一种病:每个会话在末尾追加自己的执行叙述,从不删,
>    于是涨到 502 行,然后没人读。同日剪回约 180 行。

---

## 一句话

CoC 7e 守秘人备课工作台。**所有指令都在 `core/`**,根目录三个 `*.md` 只是路由适配器。
`core/00-how-to-run.md` 是唯一入口——不确定任何事时读它,它压过一切。

## 结构速览

```
core/00 … 16        指令本体。00=入口/管线/路由/铁律/布局,02=规则查询(写数前必读)
                    01 intake · 03 world · 04 scenario · 05 clock · 06 npc · 07 monster
                    08 puzzle · 09 description · 10 handout · 11 review · 12 canon
                    13 investigator · 14 archive-reference · 15 close-session
                    16 compile-module(一幕演完后编成可读模组)
CLAUDE/GEMINI/AGENTS.md   三份薄适配器。改行为改 core,不改这三份;但三份必须彼此一致
.claude/skills/<name>/    Claude Code 技能壳,只有一句"读 core/NN"
templates/          每种产物的空壳。investigator 是 JSON schema + md 卡面双件
reference/          跨战役共享
  ├ rules/          kit 自己写的 7e 速查:**数字**(含 eras/ 六个年代包)
  ├ craft/          kit 自己写的手法提炼稿:**写法**
  ├ bestiary/ mythos/ tables/   原创可复用素材
  ├ decks/          官方卡组转录(第三方、带引用出处)
  ├ sourcebooks/    官方书籍全文转录(同上,体量更大)
      ↑ 上面五个是 kit 原创,下面两个是第三方转录——通则见 reference/README.md
  ├ index.json      七个目录的反向索引 + 校验(脚本生成,各目录另有一份)
  ├ _source/        第三方料场(不是归档区,详见下)
  ├ og_Norval/      洛夫克拉夫特全集 82 篇 → 提炼稿 craft/lovecraft-zh.md
  └ glossary-zh.md  中文术语锁,写中文必查(脊梁文件,故意留在根目录)
campaigns/          一战役一目录,_template-campaign/ 是模板
update_plan/        改动计划 + 完结清单;README.md 是状态索引,Archived/ 是已完结的
scripts/            render-investigator.py · build-reference-index.py · roll.py · render-map.py
```

**没有构建产物,也没有构建步骤。** kit 由能读文件的 agent 就地读取(Claude Code / codex /
gemini CLI),`dist/bundle.md` 单文件链路已于 2026-08-04 退役(P13)。

## 硬约定(踩了就是 bug)

1. **改行为改 `core/`,不改根适配器**;但 `CLAUDE.md`/`GEMINI.md`/`AGENTS.md` 三份必须一致,
   只存在于一份里的指令本身就是 bug。
2. **每次改动在 `CHANGELOG.md` 追加**;同一天合并进同一条,不新开。**每条 ≤2 行**
   (2026-08-08 补的硬上限,见该文件顶部)。
3. **文件名一律英文 ASCII `kebab-case.md`**,哪怕内容是中文。
4. **输出语言按战役声明**,kit 脚手架和文件名保持英文;写中文查 `reference/glossary-zh.md`。
5. **转载三分法**——边界是**规则条文 vs 虚构散文**,不是"数值 vs 描述性文字":
   - **① 规则条文**(数值、机制、条文本身的措辞)→ **可转录**,文件末尾必须有 `## 引用出处`。
   - **② 虚构散文**(小说、战役文本、`craft/` 源材料、`_source/` 里的设定书)→ **只取手法,
     永不取文字**。
   - **③ 具名角色 + 绑定商业产品** → **不收录**。
   - **这条线管的是「能不能搬进 `campaigns/`」,不是「能不能读」**——归档件就在仓库里,spec
     可以直接读、直接依赖。进 `campaigns/` 的一律自己写,理由是**牌桌**(搬来的 NPC 是别人
     都知道底牌的人),不是版权。唯一真正拿不到的是 `.pdf`/`.docx` **原件**。
   - 规则本体在 `core/00-how-to-run.md` → ground rules。

## 反直觉的约定(想当然会写错)

- **`reference/rules/` 全目录是「中文正文 + 英文术语括注」。** 2026-08-06(P12 阶段 2)定的,
  **推翻了此前"英文正文 + 中文术语括注"的旧惯例**,`eras/` 六个年代包同批改成中文。看到旧
  提交里的英文正文,别以为那是现行体例。
- **`reference/bestiary/` 不是怪物目录。** 目录是 `sourcebooks/malleus-monstrorum-zh.md`
  (223 条 / 10159 行),检索层是 `tables/monster-index.md`(274 行,每条带行号锚点)。
  bestiary/ 只放**已经写过揭示文与公平出路**的 17 条 + 无处安放的原创生物。
  **`ls reference/bestiary/` 当可用怪物清单是已观测到的真实翻车**(2026-08-08),
  已在 `core/00` 路由表与 `reference/README.md` 两处写死指路。
- **神格级(L5)条目住在 `reference/mythos/great-old-ones/`,不在 `bestiary/`。** 现有 6 份。
- **`reference/_source/` 是料场,不是归档区。** 没走 `core/14`、没有各自的 `## 引用出处`、
  不进反向索引(`build-reference-index.py` 的 `ARCHIVE_DIRS`/`ORIGINAL_DIRS` 都不含它)。
  入库边界:**原件(`.pdf`/`.docx`)不入库,转出的 `.md` 与抽出的图入库**——理由是 fresh
  clone 出来的 kit 不能是残的。**拿得到 ≠ 可以抄**,里面多数是三分法第 ② 类。
- **`keeper-rulebook-7e-zh.md` 已退出查询链路,但仍在版本库里。** 查规则去 `reference/rules/*`
  速查表;规则书只用来对账(P12 阶段 1)。

## 会连锁爆炸的地方(动之前先 grep)

- **`reference/rules/character-creation.md` 的小节编号。** `core/` 五处 +
  `_template-campaign/CLAUDE.md` + `tables/cultist-archetypes.md` + `tables/weapons-index.md`
  + `rules/monster-scale.md` 都硬编码引用着 **§11 = 人类反派基线**。
  **改小节顺序前先 `grep -r 'character-creation\.md.*§'`。** 2026-08-06 新增"其它建卡方法"时
  就是靠追加成 §12 绕开的,没敢插中间。
- **`build-reference-index.py` 的 `mi_match_bestiary()` 有匹配盲区。** 算法要求英文标题里有
  ≥2 个 4 字母以上单词才判定匹配转录稿原行,`Byakhee`/`Deep One` 这类短标题因此覆盖不到自己
  的转录稿行,会在 `monster-index.md` 里产生**重复行**。现有绕法是把标题改成书本原名全式
  (`Byakhee, the Star-Steeds`),**没有改共享算法本身**——以后遇到短名字可复用这一手,也可以
  放宽阈值,但那要对全部 223 条重跑回归。

## 还没还的债(接手可以直接捡)

| # | 债 | 在哪 |
|---|---|---|
| 1 | 三处指着**已摘除的 `external/` 子模块**(目录条目 + `og_Norval/` 那句"same rule as external" + 原创/第三方对照表)。`.gitmodules` 不存在 | `reference/README.md` |
| 2 | 种子表写成 `npc-quirks`,P14 阶段 2 已改名 **`complications`**,父目录 README 没跟着改 | `reference/README.md:31-32` |
| 3 | `--check` **不是只校验**:注释写 `validate only`,但 `main()` 无条件先跑 `build()`,而 `build()` 总是写盘;`--check` 只改退出码 | `scripts/build-reference-index.py:7, 655-657` |
| 4 | P7 计划第 5 行行数写 13731,实际 5365;`sourcebooks/index.json` 行数字段同样没清 | `update_plan/Archived/` |
| 5 | `grand-grimoire-zh.md` / `keeper-rulebook-7e-zh.md` 两份头部的"转录质量"警示未复核(malleus 那份已随换稿重写) | `reference/sourcebooks/` |
| 6 | **`core/03` 允许地点文件越权收紧 intake。** 实例:`beyond-the-treeline` 的 `stone-watch.md` 把 intake 写明的 `<party-agnostic>` 硬化成"调查员就是当值的那一对"。`core/11` 现在查不出这类越权 | `core/03` / `core/11` |
| 7 | **codex 到底读没读 `core/01-intake.md`** 从未确认。若它压根没打开 `core/` 任何文件,那是另一种病(codex 只加载 cwd 及祖先的 `AGENTS.md`),`95dfdf2` 的硬门禁治不了 | — |

**1、2 同属完结清单第 8 项(反向扫描)本该抓到的类型。**

## 活着的计划(状态权威在 `update_plan/README.md`,这里只记阻塞点)

- **P5(低成本地图)** —— 只剩一项:功能一/二的**实际 token 差没有回填**那个 3–5× 的估算。
  要真实生成一次互动场景图才测得出,不阻塞任何别的事。
- **P18(编译模组)** —— 阶段 1–3 已落地提交,计划仍在
  [`update_plan/2026-08-08-compile-module.md`](update_plan/2026-08-08-compile-module.md)。
  **阶段 4 条件执行、阶段 5 阻塞,都等 `beyond-the-treeline` 真的跑出第一幕。**

**其余 P1–P17 全部完成并归档。** 怎么做的、当时怎么权衡的,看 `update_plan/Archived/<对应文件>`
与 `git log`——**不要在本文件里找**(剪枝规则 2)。

## 两条治过的病,值得记住

- **intake 硬门禁:问完就停,Keeper 回复前不建任何文件(`95dfdf2`)。** 起因是 Keeper 用 codex
  测「创建新团」,模型一题没问就开建。**根因不在路由,在 `core/01-intake.md` 的写法**:全文只有
  一句要求提问,却有四处把零提问描述成合格结果。
  **可复用的教训:一条规则如果只写一次,而反例在同一份文件里写了四次,那条规则不存在。**
- **`CHANGELOG.md` 与本文件的体例膨胀(2026-08-08)。** 规则一直在顶部,没人改过;drift 的机制
  是**每个会话照着文件里前一条的样子写,而不是照着顶部的规则写**,自我强化。
  **药是可量化的硬约束**(changelog「每条 ≤2 行」、本文件「~180 行」)+ 显式写明「不要照上一条写」。

---

## 会话记录

本节只留**未提交**的工作(剪枝规则 1)。

### 2026-08-08 · changelog 体例回归(未提交)

`CHANGELOG.md` 的 08-05/08-06/08-07/08-08 四条压回一条一句的写法(414 → 133 行,条目数
86 → 90:压的是篇幅不是内容);合并重复的 `### 更新内容` 小节、补齐条目间缺的 `---` 与四条
标题漏掉的 commit(`e40071a` `c80530f` / `22aaf78` `2075e88` `e46bfd8`),并补记了 **P18
`compile-module` 这条此前完全没进 changelog 的用户可见变化**。三处各加了「**每条 ≤2 行**」
的硬约束并写明「不要照上一条写」:`CHANGELOG.md` 顶部、`update_plan/README.md` 第 2 节、
`core/15-close-session.md` 的 Quality bar。历史条目里的数字按**当时状态**保留,没有改写成
今天的值——changelog 是历史,不是现状快照。

### 2026-08-08 · 怪物索引路由修复 + 本文件瘦身(未提交)

- **`core/00-how-to-run.md` 路由表**:原「a non-human threat, creature, Mythos entity」一行
  拆成 **造(`core/07`)** 与 **挑(`monster-index.md`)** 两行。缺的一直是后者——一个只是在
  挑怪、没有在造怪的会话不会加载 `core/07`,也就看不到索引层存在。
- **`reference/README.md`** 的 `bestiary/` 条目改写成「**not the monster catalogue**」,写明
  正确入口与这是**已观测到的**失败模式(本会话自己踩的:`ls reference/bestiary/` 后误报
  "kit 里没有飞天水螅条目",而它就在 `malleus-monstrorum-zh.md:1536`,索引里有)。
- **本文件从 502 行剪到当前长度**,补立剪枝规则 2、3 与 ~180 行硬上限,并把「当前状态」那
  350 行按计划编号排的执行史,换成按读者用途分的四节(反直觉的约定 / 会连锁爆炸的地方 /
  还没还的债 / 活着的计划)。

### 2026-08-08 · `beyond-the-treeline` 战役重构(未提交,**不进 CHANGELOG**——战役内容不是 kit 改动)

`campaigns/beyond-the-treeline/CLAUDE.md` **整份重写**。守秘人推翻了 intake 的多项自动填充:
崩溃定在**公元 1999**(战役当下 ≈ 3200)、教会改成**真实基督教退化版**(推翻旧版"不许填入
真实世界宗教内容")、幕后具名存在定为**飞天水螅**(推翻旧版"无具名旧日支配者")、代价机制
定为**意志 POW 永久流失**、**石哨删除并入守井宅**作为法阵锚点、**调查员改成镇上人**。

**`world/` 六份文件尚未跟上,与新 `CLAUDE.md` 冲突**;待改清单在新 `CLAUDE.md` 的
「Rewrite queue」一节,`module/00-campaign-primer.md` 同样过期。顺带发现的 `core/03` 越权
缺陷已记进上面「还没还的债」第 6 条。
