# CLAUDE.md — 树线之外（Beyond the Treeline）

> Every generator reads this file to match your game's voice.
>
> Read alongside `canon-log.md`（实际发生过什么）与 `world/event-clock.md`（威胁当前走到哪一
> 步）。本文件里 `[auto]` 标记的项在文末「Auto-filled at intake」表里逐条列了理由。

## Premise (one paragraph)

韦尔加谷是山坳里的一座村子，四面被长林围死。林子往外走会死人，所以没人往外走——除了石哨
上的两个人。四百一十二年来，石哨上永远有两个人轮班，日夜不空；这是继承来的差事，谷里没人
记得是谁下的令，也没人问过为什么要「看」。翻过山脊、走出长林，是不生原：一片什么都不长的
地方，地上立着灰砂石砌出来的、太平整太笔直的东西，里面剜得出骨铁，墙上刻满没人认得的先民
纹。一位调查员刚刚继承了一处自己从不知道存在的房产——它在树线之外，而且附带条件。与此同
时，石哨上看见的东西变了。不是从山里出来的，是从**更远的地方搬过来的**：某样东西原来待的
地方，已经待不下去了。

## Setting

- **Era:** `dark-ages`
- **Region / base of operations:** 韦尔加谷（山坳村落，围以长林）；作业前哨为山脊上的**石哨**，
  谷外为**不生原**遗迹带
- **Timeframe:** 第四百一十二个守望年起，开放长团，无预设终点

## Output language

- **Generated content:** 简体中文
- Everything the table sees — prose, NPC names, boxed text, handouts — is written in this
  language. Kit scaffolding, filenames, and stat-block notation (`STR 60`, `1D6/2D10`) stay
  English.
- 每个游戏术语follow `reference/glossary-zh.md`。不自创译名，不混繁体。
- 专名走自造音译（韦尔加、长林、不生原、石哨），不使用真实历史欧洲人名地名；新造专名进了
  战役就锁死，按 glossary「加词的规矩」记进 `canon-log.md`。

## Tone & style

- **Mood:** 民俗恐怖（底色：宇宙荒凉）`[auto]`
- **Horror dial:** 潜行渐进、心理向 `[auto]`
- **Lethality:** 标准 7e
- **Combat frequency:** 罕见、非致命倾向 —— 战斗很少发生；发生时它的目的是制造代价与恐惧，
  不是清点尸体。压力来自理智、结构性危险（塌方、封闭空间、找不到回程）与不可逆的选择。
- **Register for boxed text:** 冷峻简白 `[auto]`
- **双层地点描述（表 / 里）—— 本战役硬规约，所有生成器必须遵守。** 任何与遗迹沾边的地点、
  物件、声音，都产出两段：
  - **里层（`> **KEEPER ONLY**`）**：它实际上是什么。用现代词写清楚——中继站、配电间、承重
    柱、光纤井、伺服电机。守秘人靠这一层做裁定：结构会不会塌、门为什么打不开、那个还在响
    的东西靠什么供能、水从哪来。
  - **表层（读给玩家）**：一个黑暗时代的调查员**能**看到什么。她的词汇里没有「混凝土」
    「金属合金」「电」这些概念，只有类比和触感。**表层里不许出现里层的任何一个词。**
  - 谜面不在"这是什么"，而在"她拿什么去理解它"。表层写对了，玩家会先于角色认出那是什么——
    那一拍就是这个战役的核心快感。

  **转译规约（种子表，`core/03-build-world.md` 跑起来后移进 `world/` 并扩写）：**

  | 里层（真实） | 表层（谷里的说法） |
  |---|---|
  | 混凝土 | **灰砂石** —— 一种没人会造、也没人见过谁造的石头；太平整，边太直 |
  | 钢筋 / 钢梁 | **骨铁** —— 硬度远超剑，锻不动、凿不断，只能从灰砂石里剜出来 |
  | 玻璃 | **凝水** —— 冻住的水，不化，割手 |
  | 显示器 / 屏幕 | **死镜** —— 照不出人的镜子 |
  | 电缆 / 线束 | **石中筋** —— 灰砂石断口里露出的、裹着软皮的细骨铁 |
  | 塑料 | **不腐皮** —— 埋多久都不烂，烧起来发臭 |
  | 印刷文字 / 标识牌 | **先民纹** —— 被当成符咒或装饰；谷里没人知道那是字 |
  | 指示灯 / 应急灯 | **不灭的火** —— 不烫，不用油，风吹不动 |
  | 机器运转声 / 蜂鸣 | **山在念** —— 一种低而稳的声音；谷里认为是山自己在说话 |
  | 楼梯间 / 走廊 | **直洞** —— 太直、太规整，不像人挖的 |

## Shape

- **Length:** 开放长团（open-ended chronicle）
- **Party size:** 2

## The threat

- **Category:** 独立存在 —— **迁徙而来的东西**，无人类反派 `[auto]`
- 它在这里，不是因为被召唤、被崇拜或被唤醒，而是因为**它原来待的地方待不下去了**。它对韦尔加
  谷没有意图；谷地只是它路线上的一处地形。没有邪教，没有具名旧日支配者——因此不读
  `reference/mythos/great-old-ones/`，本战役也不跑 `cult-goals`。
- 具体形态与它逃离的**那个东西**，由 `core/05-event-clock.md` 与 `core/07-create-monster.md`
  落定；那是本战役最大的问号，intake 阶段刻意不封死。
- `core/04-design-scenario.md` reads this before constructing the Keeper's truth — it does
  not re-ask this question.

## Content lines & veils (session-zero safety)

> **由守秘人明确声明，非自动填充。**

- **Lines (never appears):** **残虐儿童** —— 对儿童施加虐待或折磨的内容，任何形式、任何层级；
  不上屏，也不放在幕后暗示。
  - *守秘人给出的读法：* 儿童**可以**处于危险中、可以死、可以是悲剧的一部分。线卡在「虐待 /
    折磨的描写」上，不是卡在「儿童出现」上。
- **Veils (happens off-screen / faded):** 其余重口内容不设硬限，但**只为黑暗绝望的调性服务，
  且点到为止**——性暴力、细节化自伤、对动物的折磨、极端肢体损毁一律幕后处理或一笔带过，
  不做细节铺陈。剂量原则：一场里最多一处，够冷就收。
- Generators must honour these and flag, not silently include, heavy material.

## The investigators

- `<party-agnostic>` —— 世界建成能接纳任意队伍。
- 唯一约束：每位调查员都要跟**「进遗迹」这件事**挂得上钩（守望轮值、剜骨铁的匠人、认先民纹的
  学者、带路的猎人、收遗迹赃物的商人、被派去查那处房产的教士……任选）。
- **石哨的班是两人一组** —— 队伍规模 2 与掷出的地点天然咬合；默认这两位就是当值的那一对。

## Investigator cards

- **Pre-built pregens:** 暂不需要 —— 守秘人要先定世界观与背景，再决定是否预生成。
- **Creation-time validation:** default（见 `investigators/validation.json`）
- Config lives in `investigators/validation.json`, read by `scripts/render-investigator.py`;
  edit it directly to change the thresholds later.

## Canon so far (truth — keeper only)

> **KEEPER ONLY**
>
> - **The real situation:** 石哨的里层是**旧世界的一座监测中继站**——它既在测什么，也在把测到
>   的东西往外传。两人一组、日夜不空的排班是它原本的**人事编制**，不是民俗；这条编制活了下
>   来，仪式活了下来，理由死了。四百一十二年前有人把这个班**重新捡了起来**，那批人知道自己
>   在守什么；之后的人不知道。现在，被守的那样东西终于沿着它的路线到了。
> - **两个未决的问号（留给 `core/05` 与 `core/04`，intake 不封死）：** ① 它逃离的那个东西是
>   什么；② 中继站**还在往外传吗**，传给谁。
> - **时间结构（决定一切常识判断）：** 崩溃距今约**一千两百年**；韦尔加谷现行的守望制度只有
>   **四百一十二年**，中间约八百年是完全的空白。谷里不知道有这段空白——他们从「第一个守望年」
>   纪年，那之前在他们的历法里根本不存在。**后果：谷里对旧世界没有任何分层概念。**
>   一千两百年前的遗物和四百年前的遗物在他们眼里同龄、同类、同一批「先民」造的。这条会反复
>   咬人，调查员会把两个年代的东西当成一个年代的——那不是玩家的失误，是这个世界的认知缺陷。
> - **The rolled angle:** `mythos-angles.md` 掷 **18** ——「迁徙：某个来自别处的东西之所以在
>   这里，是因为它原来的地方待不下去了」。配套：`hooks.md` **5**（继承一处不知道存在的房产，
>   附带条件）、`locations.md` **15**（勘测站/灯塔/中继站，两人一组轮班驻守）、
>   `complications.md` **11**（在一个不该被认出来的地方被认了出来，留作伏笔）。原始输出见
>   `rolls.log`。
> - **The clock:** see `world/event-clock.md` —— 尚未建立（`core/05-event-clock.md` 还没跑）。
> - **Key secrets established:** 仅上述结构性事实；逐场细节写进 `canon-log.md`。

## House rules

- 无 —— 完全照 7e 默认跑。
- 年代差集按 `dark-ages` 包叠加（路径 A，书本背书）：本国知识 / 外邦知识 / 宗教 / 格斗〔盾〕 /
  射击（弓·弩·投石索）、「剑见箭」护甲与盾牌、地位取代信用评级、人生节点表、宗族与世仇。
  这些**不是**桌规，是年代包本身；见 `reference/rules/eras/dark-ages.md`。

## Sources & inspiration

- See `references.md` for books, modules, films, and real history this draws on.

---

## Auto-filled at intake

> Recorded so you always know which decisions were yours and which were the kit's.

| Field | Value | Why |
|---|---|---|
| Slug | `beyond-the-treeline` `[auto]` | 从前提推出：树线是村子的实际边界，遗迹全在它之外 |
| Premise | 见上 `[auto]` | hooks **5** + locations **15** + mythos-angles **18** 三条合成，没有一条被丢掉 |
| Region / base | 韦尔加谷 · 石哨 · 不生原 `[auto]` | locations 掷 **15**「勘测站、灯塔或中继站，两人一组轮班驻守」→ 石哨；村与原为承载它所需的地形 |
| Timeframe | 第 412 个守望年，开放 `[auto]` | 由下一行的时间结构推出 |
| 崩溃距今 | ~1200 年；守望制度 412 年 `[auto]` | 你给的是「一千年以上 或 auto 一个有说服力的」。选这个双层数字的理由：一份**不断代**跑了 1200 年的排班表不可信，但一份断了 800 年后被**重新捡起**的排班表既可信又更狠——它顺带解释了谷里为什么对旧世界毫无分层概念 |
| Mood | 民俗恐怖（底色宇宙荒凉）`[auto]` | 与世隔绝的村落 + 世代相传的守望职责 + 不可越过的树线 = 民俗恐怖的标准骨架；掷出的角度「迁徙、无意图」提供宇宙荒凉的底色 |
| Horror dial | 潜行渐进、心理向 `[auto]` | 与「战斗罕见、非致命」和「残虐儿童为红线」一致；恐怖来自**认知**（那不是石头）而不是血肉 |
| Register | 冷峻简白 `[auto]` | 表层描述必须用一个没有「混凝土」这个词的视角来写；华丽哥特腔会让「未曾见过的沙石」这类句子失去分量 |
| Threat category | 独立存在（迁徙而来），无人类反派 `[auto]` | mythos-angles 掷 **18**，反推得到；掷出的是「某个东西」，不是组织也不是术士，因此不是邪教 |
| Human antagonist strength | 整行删除 `[auto]` | 模板说明：类别无人类反派时删除该行 |
| 转译词表 | 10 条 `[auto]` | 从你给的两条种子（水泥→未曾见过的沙石、钢筋→远超剑硬度的铁）按同一逻辑扩写 |
| 专名命名 | 韦尔加 / 长林 / 不生原 / 石哨 / 守望年 `[auto]` | 你说「人名随意，合理即可」；取自造音译 + 谷里视角的功能性命名 |
