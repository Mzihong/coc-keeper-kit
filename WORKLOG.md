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
                    check-campaign-consistency.py(战役一致性机械检查,--check 有问题退 1、
                    SKIPPED 退 2;SKIPPED 不等于通过)
```

**没有构建产物,也没有构建步骤。** kit 由能读文件的 agent 就地读取(Claude Code / codex /
gemini CLI),`dist/bundle.md` 单文件链路已于 2026-08-04 退役(P13)。

## 硬约定(踩了就是 bug)

1. **改行为改 `core/`,不改根适配器**;但 `CLAUDE.md`/`GEMINI.md`/`AGENTS.md` 三份必须一致,
   只存在于一份里的指令本身就是 bug。
2. **每次改动在 `CHANGELOG.md` 追加**;同一天合并进同一条,不新开。**每条 ≤2 行**
   (2026-08-08 补的硬上限,见该文件顶部)。
3. **发现两份已有文件对同一事实说法不同 → 报给守秘人,不自己解决。** 说清哪边更新、依据是
   什么(git 记录 / 文件内日期 / Auto-filled 的裁决记录)。**优先级规则不是静默套用的许可**
   ——战役 `CLAUDE.md` 赢是给守秘人裁决用的判据,而守秘人完全可能裁定权威那一边才是错的
   (2026-08-09 就发生过,方向还相反的两次)。判之前先确认两边在数同一样东西。
4. **改动 ≥3 份战役文件、或动了任何已声明的规约设定 → 收尾必须跑
   `python scripts/check-campaign-consistency.py --campaign <slug>` + `core/11-review.md`,
   并把结论写进当天 changelog 或会话日志。** 手写待办清单不算替代——它只覆盖想得到的项。
5. **文件名一律英文 ASCII `kebab-case.md`**,哪怕内容是中文。
6. **输出语言按战役声明**,kit 脚手架和文件名保持英文;写中文查 `reference/glossary-zh.md`。
7. **转载三分法**——边界是**规则条文 vs 虚构散文**,不是"数值 vs 描述性文字":
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
| 1 | 三处指着**已摘除的 `external/` 子模块**(`og_Norval/` 那句 "same rule as `external/` below" + `external/` 条目本身 + 原创/第三方对照表)。`.gitmodules` 与 `reference/external/` 都不存在 | `reference/README.md:70, 73-79, 87` |
| 2 | 仍把 `npc-quirks` 列为第四张**种子表**。实际种子表是 **`complications`**(`core/01-intake.md:139`);`npc-quirks.md` **没被改名**——只是移出种子表集,仍由 `core/06-create-npc.md:73` 掷。`tables/README.md` 已修,父目录没跟着改 | `reference/README.md:37-38` |
| 3 | `--check` **不是只校验**:注释写 `validate only`,但 `main()` 无条件先跑 `build()`,而 `build()` 总是写盘;`--check` 只改退出码 | `scripts/build-reference-index.py:7, 655-657` |
| 4 | `grand-grimoire-zh.md` 是**唯一还在查询链路上**的转录稿,头部却**没有转录质量声明**(malleus 有,见其第 14 行)。`keeper-rulebook-7e-zh.md` 头部那句"部分章节尚未系统校对"从未复核,但它已退出查询链路(见上一节),优先级低 | `reference/sourcebooks/` |
| 5 | **`core/03` 允许地点文件越权收紧 intake,而 `core/11` 查不出这类越权。** 原始实例 `stone-watch.md` 已随 `b511607` 删除、守秘人已在 `campaigns/beyond-the-treeline/CLAUDE.md:199` 手工推翻——**但两份 spec 至今没有护栏,下一个战役会再犯** | `core/03` / `core/11` |
| 6 | **codex 到底读没读 `core/01-intake.md`** 从未确认。若它压根没打开 `core/` 任何文件,那是另一种病(codex 只加载 cwd 及祖先的 `AGENTS.md`),`95dfdf2` 的硬门禁治不了 | — |

**1、2 同属完结清单第 8 项(反向扫描)本该抓到的类型。**

> **本表逐条 grep 核验于 2026-08-09**(上次核验:写下它的 `b511607`)。核验删掉一条已还清的债,
> 重写了三条(前提失效 / 行号漂了 / 引的例证文件已被删)——**行号是本表最先烂掉的部分**,
> 捡之前自己再复核一遍。
> 复核义务写在 `core/15-close-session.md` 的 "Re-verify the debt table"。

## 活着的计划(状态权威在 `update_plan/README.md`,这里只记阻塞点)

- **P5(低成本地图)** —— 只剩一项:功能一/二的**实际 token 差没有回填**那个 3–5× 的估算。
  要真实生成一次互动场景图才测得出,不阻塞任何别的事。
- **P18(编译模组)** —— 阶段 1–3 已提交(`e46bfd8`),计划在
  [`update_plan/2026-08-08-compile-module.md`](update_plan/2026-08-08-compile-module.md)。
  **阶段 4 已解除阻塞、是当前唯一可动的一条**;阶段 5(样张)仍等第一幕跑过。
  动手前先读该计划阶段 4 的「实测回填」——**实测推翻了它原定的做法**:第一份真实编译产物
  (`beyond-the-treeline/module/00-campaign-primer.md`)24 小时内漂移两次,主要那次是
  **「重编译了但某一节把旧内容带了过来」,时间戳全绿,mtime/哈希抓不到**。由此暴露一处
  spec 缺口:**`core/16` 步骤 3 与 `core/11` 的镜像审查只防「新造事实」,不防「已被撤回的
  事实」**,而「留白问号」那一节的过期是隐形的——答案是单向的,一个已被答掉的问号读起来和
  一个仍然敞着的问号一模一样。

**其余 P1–P17 全部完成并归档。** 怎么做的、当时怎么权衡的,看 `update_plan/Archived/<对应文件>`
与 `git log`——**不要在本文件里找**(剪枝规则 2)。

## 三条治过的病,值得记住

- **intake 硬门禁:问完就停,Keeper 回复前不建任何文件(`95dfdf2`)。** 起因是 Keeper 用 codex
  测「创建新团」,模型一题没问就开建。**根因不在路由,在 `core/01-intake.md` 的写法**:全文只有
  一句要求提问,却有四处把零提问描述成合格结果。
  **可复用的教训:一条规则如果只写一次,而反例在同一份文件里写了四次,那条规则不存在。**
- **`CHANGELOG.md` 与本文件的体例膨胀(2026-08-08)。** 规则一直在顶部,没人改过;drift 的机制
  是**每个会话照着文件里前一条的样子写,而不是照着顶部的规则写**,自我强化。
  **药是可量化的硬约束**(changelog「每条 ≤2 行」、本文件「~180 行」)+ 显式写明「不要照上一条写」。
- **没有人负责回头查的东西一定会烂(2026-08-09,两个会话同一天独立撞上)。** 债表烂了四个提交
  没人发现——`core/15` 步骤 2 的 fact-check 只覆盖**本次会话写下的**内容;同日战役全面冲突,
  因为完结清单第 8 项「反向扫描」本该抓到它,而 `core/15` 列举 ad-hoc 适用哪几项时**漏了第 8
  项**(P15 后加的,这份枚举从没跟上)。**两层教训:① 加规则时把所有指向它的清单一并改;
  ② 只靠"记得做"的义务等于不存在——要么留下能被事后核的产物,要么写成脚本。** 手写待办清单
  两次都不管用:它只覆盖想得到的项。

---

## 会话记录

本节只留**未提交**的工作(剪枝规则 1)。

*(空 —— 2026-08-09 的两轮工作已随 `deb48b9` / `8ea31e0` / `ea1865a` 提交;结论进了上面的
「三条治过的病」与硬约定 3、4,执行叙述在 `git log` 与 `update_plan/2026-08-09-conflict-reporting.md`。)*
