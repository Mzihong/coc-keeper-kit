# Update Plan — bundle 退役:kit 只面向能读文件的 agent

> 日期:2026-08-04
> 状态:**已完成(014ffe6)** —— 唯一的执行级选择已按倾向定为 **A 删干净**
> 来源:Keeper 2026-08-04 会话——「去掉 bundle 吧,一律用 agent,限制多,用途少」
> 触发:P12(速查表自足化)在估"三份补齐后 bundle 会涨 10–17%"时,Keeper 直接否掉了
> 这笔账该不该算
> 前置:无

## 目标

**删掉 `dist/bundle.md` 这条分发链路,连同它在整个仓库里派生出的那套约定。**

kit 从此只有一种用法:**agent 直接读仓库文件**(Claude Code / codex / gemini CLI)。
不再维护"给没有仓库的 ChatGPT/Gemini Keeper 上传一份单文件副本"这条路。

## 为什么

Keeper 的判断是「限制多,用途少」。拆开看,这两句各自都能验证:

### 限制多——bundle 是一条横穿全仓库的约束

它不是一个脚本,是一条**贯穿式约定**。现在仓库里因为它而存在的东西:

| 位置 | 因 bundle 而存在的东西 |
|---|---|
| `scripts/build-bundle.sh` | 整个脚本(含一份**手写白名单**,新建目录必须记得来这里加一行) |
| `WORKLOG.md` 硬约定 2 | 「什么进 bundle 只有一条线——kit 自己写的进,第三方转录的不进」 |
| `WORKLOG.md` 硬约定 7 | 「归档件不进 bundle」的推论:**任何 spec 引用归档件都必须写成可选**(`if present locally`),不得当前置依赖 |
| `reference/README.md` § 什么进 bundle | 通则本体,9 处提及 |
| `reference/decks/README.md`、`sourcebooks/README.md`、`craft/README.md` | 各自复述"本目录不进 bundle"及其推论 |
| `scripts/build-reference-index.py:72` | `ORIGINAL_IN_BUNDLE` 字典 + 三处 `in_bundle` 字段写入 |
| 七份 `index.json` | 每份都带 `in_bundle` 字段 |
| `core/00-how-to-run.md:120,170` · `core/14-archive-reference.md:42,43,101` | 布局说明与归档流程里的 bundle 分支 |
| `AGENTS.md:35–37` · `README.md:26,75,96,100,104` | 面向用户的上传说明 |

**代价最重的是硬约定 7。** 它逼着每一条引用第三方资料的 spec 都写成"如果本地有的话",
因为 bundle 链路的 KP 拿不到那些文件。**没有 bundle,这条约束整条消失**——spec 可以
直接说"去读 `reference/decks/phobias-and-manias-zh.md`",因为读得到就是读得到。

`craft/README.md` 那条「不许指向 `update_plan/`」的术语自足约定,理由也是 bundle
(计划文档不进 bundle)。退役后该条要**换理由保留**,不是删掉——指向计划文档仍然是
坏引用,只不过原因从"拿不到"变成"计划会归档、链接会烂"。

### 用途少——它服务的那个场景已经不成立

bundle 的设定用户是「**没有仓库**的 ChatGPT/Gemini Keeper」。而 kit 现在的三份适配器
(`CLAUDE.md`/`GEMINI.md`/`AGENTS.md`)服务的都是**能读文件的 agent**;2026-08-04 那次
codex 测试暴露的问题(模型一题没问就开建)也是文件加载路径的问题,不是上传路径的问题。

**一条没人走的路,却在给每一次改动上税。**

## 一个额外的好处:版权面收窄

现在的分发逻辑是"kit 自己写的进 bundle,第三方转录的不进"——**bundle 本身就是唯一的
对外分发物**。删掉它之后,kit 不再产出任何"可以整份递给别人"的文件,仓库回到纯粹的
本地工作台。

这和 P12 拍板 ① 的方向一致:规则条文可以直接引用,前提是 kit「面向持有正版的 KP、
不盈利、**不用于传播**」。**删掉 bundle = 把"不用于传播"从一句声明变成一个事实。**

## 已定(执行时选 A)

**`index.json` 里的 `in_bundle` 字段留不留?**

| 选项 | 做法 | 取舍 |
|---|---|---|
| **A 删干净** | 去掉 `ORIGINAL_IN_BUNDLE` 与三处 `in_bundle` 写入,七份 index.json 重生成 | 最彻底。代价:index.json 的 diff 会很大(七份全动) |
| **B 改名保留** | `in_bundle` → `kind` 已有的原创/第三方之分已经覆盖了同一信息 | 其实 A 就够——`kind: kit-original-content` vs `third-party-source-material` 本来就是那条线,`in_bundle` 是它的冗余投影 |

**选 A,已执行。** 理由写在上面 B 里:那个字段是冗余的,`kind` 已经承载了同样的区分。
七份 `index.json` 已重生成,`--check` 报 no problems。

## 方案

分发链路整条删,**目录分类保留**。

```
删
  scripts/build-bundle.sh
  dist/                      ← 已 gitignore,直接删本地目录
  ORIGINAL_IN_BUNDLE + in_bundle 字段(scripts/build-reference-index.py)
  硬约定 2(什么进 bundle)
  硬约定 7(归档件不进 bundle 的推论)——连同它派生的 "if present locally" 写法

留(理由要换)
  reference/ 的原创 vs 第三方之分   ← 理由从"分发"换成"版权 + 牌桌"
  craft/README.md 的术语自足约定    ← 理由从"计划文档不进 bundle"换成"计划会归档,链接会烂"
```

## 阶段 1 — 删链路

- [x] 删 `scripts/build-bundle.sh`
- [x] 删本地 `dist/`;`.gitignore` 里的 `/dist/` 一行也删(没有产物了)
- [x] `scripts/build-reference-index.py`:去掉 `ORIGINAL_IN_BUNDLE`(第 72 行)与
      三处 `in_bundle` 写入(502 / 530 / 575 行)
- [x] 重跑 `python scripts/build-reference-index.py` → 七份 index.json 重生成,
      **必须报 no problems**

## 阶段 2 — 拆约定

**这一阶段是本计划的实质,阶段 1 只是删文件。**

- [x] `WORKLOG.md` 硬约定 2:整条删除;硬约定 7:整条删除
- [x] `reference/README.md`:删掉 `## 什么进 dist/bundle.md` 整节(9 处提及);
      **原创 vs 第三方的区分要在同一处换理由重写**,别连着一起删
- [x] `reference/decks/README.md:63`、`reference/sourcebooks/README.md`、
      `reference/craft/README.md:37` 三处复述同步
- [x] `reference/craft/diagram-conventions-zh.md:85` —— 那句话是 P5 阶段 0 用来解释
      "为什么本文件要存在"的,理由里含 bundle。**改理由,别改结论**
- [x] `core/00-how-to-run.md:120,170`(布局图与那句"stated once with its reasoning")
- [x] `core/14-archive-reference.md:42,43,101`:归档流程里的 bundle 分支删掉
- [x] **全仓 grep `if present locally` / `本地若有` / `optional` 的归档件引用**——
      硬约定 7 没了之后这些限定语可以拿掉,spec 可以直接依赖归档件。
      **这是本计划真正的收益,别漏做**
- [x] `AGENTS.md:35–37`、`CLAUDE.md`、`GEMINI.md` 三份适配器同步(完结清单第 4 项)
- [x] `README.md:26,75,96,100,104`:快速开始一节里的"生成并上传 bundle"整段删掉,
      换成"用能读文件的 agent 打开这个仓库"

## 阶段 3 — 收尾

- [x] `CHANGELOG.md`:写面向 Keeper 的变化——「不再需要跑构建脚本上传;
      kit 现在只支持能直接读仓库的 agent」
- [x] `WORKLOG.md` 结构速览里的 `dist/` 一行删掉
- [x] 走 `update_plan/README.md` 完结清单七项

## 风险与边界

1. **这是一条单向门。** 删掉 bundle 后,一个只能上传单文件的 Keeper 就用不了 kit 了。
   Keeper 已经明确这不是目标用户(「一律用 agent」)。**要恢复的话 `git revert` 即可**
   ——脚本本身很短,真正难恢复的是阶段 2 拆掉的那些约定文字。
2. **别顺手删掉原创 vs 第三方的分类。** 那条线有**两个**理由,bundle 只是其中之一:
   另一个是版权与牌桌(搬来的 NPC 是别人都知道底牌的人)。删 bundle 只废掉分发那个理由。
3. **和 P12 的关系:无硬依赖,但别同批 commit。** 两边都要动 `reference/README.md`、
   `core/00`、三份适配器。同批改会把「规则条文可转录」和「不再分发」两件事的理由搅在
   一起,以后 `git log` 读不出来哪句是为哪件事改的。
4. **`.claude/skills-eval-workspace/benchmark.json` 里也提到 bundle**——那是评测工作区,
   不是 kit 本体,**本计划不动它**;若评测用例依赖 bundle 存在,另开一条。
   执行时核实:该目录**确实在版本控制里**(`.claude/` 跟踪 17 个文件,其中 2 个属于
   `skills-eval-workspace/`),但它唯一那处 `bundle` 只是评测报告正文里的一句
   "the bundled PDFs",不是对构建链路的依赖。照计划未动,也不需要另开计划。

## 执行记录(2026-08-04)

三个阶段全部执行,清单逐条勾完。除计划已写明的之外,落地时另做了六处判断:

1. **硬约定重新编号。** 删掉旧 2 与旧 7 之后,原 3–6 顺次上移成 2–5。仓库里有三处按
   号引用「硬约定 6」(`WORKLOG.md` 的 P10 条目、P12 计划的拍板 ①、`update_plan/README.md`
   的建议执行顺序第 8 条),已同步改成 5 并在 P12 那处标了旧编号,**否则 P12 执行时会
   照号去改错一条**。
2. **`_source/` 成了「可选引用」的唯一剩余理由。** 硬约定 7 死掉之后,全仓只有一类文件
   真的可能不存在:`reference/_source/`(整目录 gitignore)。`core/14` 第 5 步与
   `reference/README.md` 都改成「直接引用,`_source/` 除外」,而不是把可选写法整条删光
   ——删光的话以后有人给 `_source/` 写引用就没有约束可依。
3. **回收的限定语共 10 处**(行号为改后):`core/02:7`、`core/06:13,71`、`core/07:41`、
   `core/13:15,23`、`reference/mythos/README.md:23`、`reference/bestiary/README.md:23`、
   `reference/rules/magic.md:4`、`reference/rules/monster-scale.md:4`、
   `reference/rules/character-creation.md:276`。后四处不是 spec 而是提炼稿头部的
   「local only」自述,grep `if present locally` 查不到——**按语义查而不是按短语查**。
4. **`core/02` 那处会被 P12 再动一次。** P12 阶段 1.2 要 `git rm --cached`
   `keeper-rulebook-7e-zh.md`,那之后规则书**又变成本地若有**。P12 计划的引用表已经写着
   「删掉整段」,所以不冲突;但**P12 执行时别把本计划刚拿掉的限定语原样加回去**——
   正确写法是那一段整体降级,不是恢复 hedge。
5. **README 的三节快速开始并成一节。** 原来按 Claude Code / Gemini CLI / ChatGPT 分三节,
   删掉第三节后前两节内容几乎相同,合成一节「用能读文件的 agent 打开这个文件夹」,
   并把 codex 的工作目录陷阱写进去(那正是 95dfdf2 那次 intake 事故的可疑根因之一)。
6. **CHANGELOG 当天条目里有两条已被本计划推翻**(「bundle 收录 bestiary/mythos」与
   「改完不必重建 bundle」),已就地重写成三条准确的。同一天的条目会合并,留着两条
   自相矛盾的记录比改掉更糟。
