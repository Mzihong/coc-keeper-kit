# Update Plan — 按需生成:预览—确认—展开 + NPC 两级制 + 降低每场上下文成本

> 日期:2026-08-08
> 状态:进行中(内容全部落地,阶段 1–5 与阶段 6 前三项已完成;等提交后回填 commit 并走完结
> 清单第 1/7 项与归档)
> 来源:Keeper 2026-08-08 会话——「intake 后和 KP 确认世界观(这里会消耗一大部分 token)
> 先不推进创建 npc 和场景,因为那会大量消耗 token,以订阅制为主的用户来说负担太大,
> 角色和场景应该和 KP 商量着一步一步落实」
> 前置:无。**P18(编译模组)的阶段 2 依赖本计划阶段 2 的 roster 状态列**

## 目标

**把 kit 的默认从「一次铺完」改成「一次铺一件,KP 点单」**,并把每场必付的上下文成本
压到一个固定的小包里。

不以「输出写短一点」为目标——那治不了本。真正的开销是**两笔**:

1. **一次性的生成开销**:跑一次 scenario 就级联出五张完整人物卡 + 十段朗读散文。
2. **每场重复的读取开销**:每次备课把 `world/` 整个灌进上下文。生成付一次,读取付 N 次。

## 诊断:级联是写在规格里的,不是模型话多

### ① 管线表把「建完」写成了默认

[`core/00-how-to-run.md:37`](../core/00-how-to-run.md) —— *"Steps 1–4 happen once per
campaign."* 第 4 步是 **Cast**,产物是 `npcs/`、`reference/bestiary/`、`investigators/`
([`core/00:31`](../core/00-how-to-run.md))。照字面读,一个战役在见到第一个玩家之前就该
把全部 NPC 造完。

### ② `core/04` 第 7 步是级联的扳机

[`core/04-design-scenario.md:78`](../core/04-design-scenario.md) —— *"**Cast & threats.**
Name the NPCs and creatures (hand to `core/06` / `core/07`)"*。设计一场模组必然点到
5–8 个人名,这一句把每一个都交给 `core/06` 出完整 7e 卡。**没有任何一句说"哪些现在要、
哪些先欠着"。**

`beyond-the-treeline` 现在停在「五个名字有了、钩子有了、一张卡都没做」
([`overview.md:36`](../campaigns/beyond-the-treeline/overview.md)),那是 Keeper 手动踩的
刹车,不是 kit 让它停的。

### ③ 散文是单位 token 最贵、桌前最容易被改掉的东西

[`core/09-description.md:48`](../core/09-description.md) 的 Mode A 默认落盘到 `scenes/`
([`core/09:100`](../core/09-description.md))。Mode B(临场动作描写)本来就是对话里返回、
不写文件——**同一份规格里两种模式对"要不要落盘"的判断不一致**,而更贵的那一半选了落盘。

### ④ 每场重复付的读取成本没有任何人管

`campaigns/beyond-the-treeline/world/` 现在 6 份 md 合计 **1000+ 行**
(`velga.md` 288 / `stone-watch.md` 201 / `velga-region.md` 194 / `the-barrens.md` 187 /
`inherited-holding.md` 141 / `timeline.md` 137)。
[`campaigns/README.md:20`](../campaigns/README.md)「The three files every generator reads」
只圈了 `CLAUDE.md` / `canon-log.md` / `world/event-clock.md` 三份,**没有任何一句说
`world/` 的其余部分该按需打开**。`world/README.md` 现在写的是"这个目录是什么",
不是"什么时候需要读哪一份"。

跑二十场就把这 1000 行付二十遍。**这笔比生成 NPC 贵,而且完全看不见。**

## 拍板结果(2026-08-08 会话)

- ① **不加预算档位字段**(省/标准/全量三档)。每个 spec 为三档分支写规则,维护成本高、
  收益低。只要一条默认「按需」+ 一个显式逃生阀(KP 说"全量展开"就照旧铺完)。
- ② **不给 stub 单独模板文件。** stub 的全部价值在于它是一张表里的一行;给它
  `templates/npc-stub.md` 等于鼓励开文件,把省下来的又花回去。
- ③ **排序原则写进 kit:先写会被翻的,后写会被念的。** 数值与线索矩阵永远落盘
  (桌前要查、临场编不出来);朗读散文默认不落盘(临场可即兴、预生成八成用不上)。

## 阶段 1 — 「预览—确认—展开」升成全 kit 铁律

**这是全计划里最省钱的一条**,而且零结构改动。真正省下来的不是"写短了",是
**不写 KP 根本没打算要的那三份**。

- [x] `core/00-how-to-run.md` → ground rules 增一条(与 "Fair play" 同级),措辞要点:
      任何生成型 spec(`core/03`–`core/10`、`core/13`)开跑前,先产出一份 **≤15 行的清单
      预览**——打算写哪几个文件、每份放什么、大致篇幅;**KP 确认或删减后才展开**。
      KP 明说"全量展开 / 你决定"时跳过预览。
- [x] `CLAUDE.md` / `GEMINI.md` / `AGENTS.md` **三份同步**(硬约定 1)。
- [x] `core/01-intake.md` 现有的"先问后写、写之前停"**不动、不削弱**——它比通则更严
      (连 agent harness 让它自动跑完都不认)。只在 `core/00` 新条目里注明 intake 是它的
      加强特例,避免下一个接手的人以为通则放宽了 intake。
- [x] 逐 spec 在开头 `## First` 一节加一句指向新铁律(`core/03`/`04`/`06`/`07`/`08`/
      `09`/`10`/`13` 共 8 处)。

**已知局限,不设兜底:** 预览是过程不是产物,事后无法用 `core/11` 审。这条和 P14 的
"模型可能绕过 `roll.py`"不同——掷骰能靠 `rolls.log` 落盘查,预览查不了。接受它。

## 阶段 2 — NPC 两级制:stub 与成卡

- [x] `core/06-create-npc.md` 新增一节 **Two tiers**:
      - **stub(默认)** —— 名字 / 身份与所在 / 想要什么 / 藏着什么 / 一句口吻。四五行,
        **不开文件**,写进 `npcs/roster.md` 的一行。
      - **成卡** —— 现有的完整 7e 输出,独立文件,照 `templates/npc.md`。
- [x] 写死**升级判据**(满足任一条才升级,否则留 stub):
      1. 下一场确定会被技能检定针对(说服/心理学/侦查……有明确对象);
      2. 会进入战斗或追逐(需要 HP/DB/闪避/武器);
      3. 会有超过一个来回的实质对话(需要秘密、谎言、给什么线索);
      4. KP 点名,或玩家已经自己盯上了他。
- [x] 新建 `templates/npc-roster.md`(**表本身有模板,stub 没有**——见拍板 ②):
      列为 `名字 | 身份/所在 | 想要什么 | 藏着什么 | 状态 | 文件`。
      **状态取值用英文以便 grep:`stub` / `card` / `on-table` / `off-stage`。**
- [x] `campaigns/_template-campaign/npcs/roster.md` 预置空表(与 `rolls.log` 不同——
      空表**有**信息:它的表头就是惯例本身,而空 `rolls.log` 没有任何信息)。
- [x] `core/04-design-scenario.md:78` 第 7 步改写:名字先落 roster 为 stub;
      **只把符合升级判据的交给 `core/06`/`core/07`**。
- [x] `core/00-how-to-run.md:31` 管线表第 4 步产物加 `npcs/roster.md`,并注明默认是 stub。
- [x] **必须一并改 `core/12-canon-update.md`**:现在
      [`npcs/README.md`](../campaigns/_template-campaign/npcs/README.md) 要求每场给**每个
      交手过的 NPC 文件**追一行 interaction history,而 stub **没有文件**。
      改成:成卡追进自己文件;stub 追进 roster 行(或因为上桌了直接升级成卡)。
      **这条不改,canon 更新会去写不存在的文件——是本阶段最容易漏的一处。**
- [x] `campaigns/_template-campaign/npcs/README.md` 同步两级制与 roster。
- [x] `campaigns/beyond-the-treeline/`:把 [`velga.md`](../campaigns/beyond-the-treeline/world/velga.md)
      名录里已有的五人(图沃/卡蕤/维珂/佐仑/恩珊)与三位不在场者(塔恩/梧岑/凯佛伦)
      收进 roster,状态全填 `stub`。**这一步是纯搬运,不生成新内容。**

## 阶段 3 — 场景与散文默认不落盘

- [x] `core/09-description.md` Mode A 的 Output(第 100 行一节)改:**默认在对话里返回**;
      KP 说"留着"才写进 `scenes/`。与 Mode B 的现有做法对齐,消掉同一规格内的不一致。
- [x] `templates/scene.md` 的 `## Read-aloud (boxed text)` 允许留 `<pending>` 占位,
      并说明要点版(有什么 / 能问出什么 / 出口在哪)才是场景文件的必需部分。
- [x] `core/04` 第 6 步建 scene web 时注明:节点默认只出要点版。
- [x] 把拍板 ③ 那句排序原则(**先写会被翻的,后写会被念的**)写进 `core/00` ground rules,
      它同时管 NPC、场景、讲义三处,不只是散文。

## 阶段 4 — 压每场重复付的读取成本

- [x] `campaigns/README.md:20`「The three files every generator reads」→ **四份**,
      加 `npcs/roster.md`。目标是这四份加起来 **≤400 行**。
- [x] `core/00` 新增一小节「每场默认读什么」:默认只读这四份(canon-log 读尾部),
      `world/` 的其余文件**按需打开**。
- [x] `campaigns/_template-campaign/world/README.md` 从"这个目录是什么"改成**路由表**:
      一行一文件 + **什么时候才需要打开它**("队伍进不生原时读 `the-barrens.md`")。
- [x] `campaigns/beyond-the-treeline/world/README.md` 照新格式重写(6 份 + 2 张 svg)。
- [x] `core/05-event-clock.md`:clock 默认**只建到第 3 刻**,后续刻度随打随补。
      理由——clock 是唯一"一份产出两用"的东西(它同时是 P18 模组文本的「时间线」与
      「近期事件」),但把六刻全建完属于预支未发生的分支。

## 阶段 5 — 审查适配(不做这条,省下的钱会换成更贵的问题)

- [x] `core/11-review.md` → `### Blocking` 增一条,**区分两种"不存在"**:
      - 线索/场景指向 roster 里**存在**的 stub → **pass**(尚未生成,正常);
      - 指向 roster 里**没有**的名字 → **fail**(断链)。
- [x] 同一逻辑覆盖讲义与场景:`handouts/` 里没有的讲义,若已在 scenario 的线索矩阵登记
      则 pass,未登记则 fail。
- [x] 三线索规则的审查口径写清:**三条线索必须都已登记在矩阵里**,但其中未展开的那几条
      不算失败——审的是矩阵完整性,不是文件数。

## 阶段 6 — 收尾

- [x] `CHANGELOG.md` 记一条(面向 Keeper:"现在生成前会先给你一份清单""NPC 默认只出
      名录行")
- [x] 根 `README.md` 快速开始与流程图(级联改按需,属于入口说明变化)
- [x] `WORKLOG.md`(改了硬约定)
- [~] `update_plan/README.md` 完结清单八项——内容项(2–6、8)已走完,第 1/7 项(commit 回填、
      归档)依赖提交,提交需 Keeper 明确要求,留待下一步

## 风险与边界

1. **预览无法事后审计**(阶段 1 已注明)。这是本计划最大的执行风险,且没有兜底。
2. **stub 太薄会让临场跑不动。** 判据:stub 能不能撑一场即兴对话。若实测常撑不住,
   把 stub 从 5 行加到 8 行(补"他会怎么撒谎""他先说哪句"),**而不是回退两级制**。
3. **roster 会变长。** 长团 30+ 人。约定:退场/已死的行移到表末 `off-stage` 小节
   **不删**(canon 不能丢),活跃部分保持在 400 行预算内。
4. **和 `core/12` 的冲突是硬冲突**(阶段 2 已列),不是可选项。
5. **和 P18 的接口:** roster 的**状态列**是 P18 gap report 的输入。本计划阶段 2 落地
   之前,P18 的 gap report 只能人工列。
6. **别同批提交:** 本计划与 P18 都动 `core/00` 的管线表与三适配器。

## 明确不做

- 预算档位字段(拍板 ①)
- `templates/npc-stub.md`(拍板 ②)
- 任何形式的 token 计量/预算脚本——kit 读不到会话的用量,写出来只能是估算,估算会被当
  成真数用
