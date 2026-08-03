# Update Plan — 玩家卡(投资者)生成

> 日期:2026-08-02(收尾归档于 2026-08-03)
> 状态:**已完成** —— 基线 e0d026b;第二轮「照真实车卡表重建 schema」已交付
> (97c87d8);2026-08-03 收尾:跨 P1 项确认为"schema 就绪、按需生成"无需本计划再动作,
> `roster.csv` 判断为"暂不做"(理由见文末)
> 来源:从 `Archived/2026-08-02-conventions-gaps.md` §5 拆出独立跟踪(2026-08-02)
> 关联:`2026-08-02-cult-doc-integration.md` 第四章(精英邪教徒复用同一 schema)

## 存储格式选型(已定案,记录理由)

**JSON,一人一档。**

- SQL/SQLite 是二进制或需运行时:git diff 不可读、Gemini/ChatGPT 网页难直读,
  违背"三模型共用一份源"的架构,**不采用**
- CSV 表达不了嵌套(技能表、武器表、backstory 多条目),只适合花名册索引
- JSON git 友好、三模型可直读可校验、可派生
- 结构:`campaigns/<slug>/investigators/<name>.json`(唯一真源)+
  由它渲染的 `<name>.md` 人类可读卡(桌面用);`roster.csv` 花名册索引可选

## 已交付基线(e0d026b)

- [x] `reference/rules/character-creation.md` — 车卡速查:特征骰法、
      职业技能点(EDU×4 等)、兴趣点、信用评级区间、背景栏目——机制引用,不转录原文
- [x] `templates/investigator.schema.json` + `templates/investigator.md` —
      JSON schema 与 markdown 卡模板
- [x] `core/13-create-investigator.md` — 新 spec:pregen 流程(概念→职业→数值→
      背景钩子,钩子必须挂进 campaign 前提)、JSON 为真源、md 为视图
- [x] `.claude/skills/create-investigator/` — 薄包装;根三适配器技能表已同步登记
- [x] `scripts/render-investigator.py` — JSON→md 渲染(仅用 stdlib json/pathlib)
- [x] `core/00-how-to-run.md` — 管线与 Layout 登记 `investigators/`
- [x] `core/11-review.md` — 清单加:投资者 JSON 过 schema 校验、数值自洽

## 第二轮:照真实车卡表重建 schema(2026-08-02)

来源:Keeper 提供的 `COC apolo.xlsx`(丛雨 CY23Final 通用车卡,11 个 sheet)。
**只提炼机制,不转录原文**——职业介绍、技能解释、恐惧/躁狂 d100 表都留在规则书里,
本 kit 只记公式、区间和字段形状。

- [x] `templates/investigator.schema.json` **重建**:原来只有 8 属性 + 派生 + 技能名/值,
      对不上一张真卡。现按整张卡建模,新增 `player`/`age`/`sex`/`residence`/`birthplace`/
      `era_year`、`occupation_detail`(公式/信用区间/本职技能表/推荐关系人)、
      `age_modifiers`(年龄补正实际扣了什么)、`skill_points`(点数账本)、
      技能条目的 `base`/`occupation_points`/`interest_points`/`growth_points`/
      `specialization`/`occupation_skill`、`credit_rating` 的生活水平/现金/资产/消费水平、
      武器全字段、`gear`/`experience_packages`/`mythos_encounters`/`backstory_keys`/
      `status`/`party`/`growth_log`。**全部为可选字段**,旧记录仍合法、渲染器不炸
- [x] `reference/rules/character-creation.md` **重写**:补上原来缺的
      年龄补正表(七档)、Build/DB 表、MOV 判定、重伤值、技能基础值表、
      本职技能三要素(公式家族/信用区间/技能表含自由槽)、信用评级→生活水平/现金/资产表
      (1920s 美元,附跨时代缩放说明)、伞技能与专精写法、艺术/科学/语言外溢可选规则、
      技能上限可选规则、经历包(付 SAN 换机制优势+强制背景条目)、背景「关键」标记、
      **点数账本必须平**的验收口径
- [x] `core/13-create-investigator.md`:建卡顺序从 4 步改 8 步——**年龄排在算点数之前**
      (教育进步检定会改 EDU,而多数公式吃 EDU),并补 wealth / backstory_keys / 装备两步
- [x] `templates/investigator.example.json` **新增**:一张完整的、算术已核过的样卡
      (工程师,EDU×4=312 点、INT×2=160 点,两边都花光对得上)。
      **这条同时满足下面「schema 未被真实档案压过」那一项**
- [x] `scripts/render-investigator.py`:修 `specialization` 被丢掉的缺陷——
      两条 `Science` 渲成一模一样、卡面不可用。属于 P8 之外的独立缺陷
      (与 P8 待讨论的「卡面受众」无关,两种受众都要这行),改完已实跑验证
- [x] `reference/rules/character-creation.md` 补**来源指路**:每个小节加一行「来源」,
      标明数据是从 `COC apolo.xlsx` 哪个 sheet 提炼的——不摘原文,只给定位信息,
      跟"不转录原文"规则完全兼容(风险不变,来源可查)。
      其中技能基础值表的"规则书第四章:技能"是源材料自带的引用,直接沿用;
      其余小节没有源材料自带的章节号,老实标了「章节号未核实」,没有编号瞎猜

## 待办

- [x] **跨 P1:** 教团计划第四章的邪教徒精英用同 schema 存档(NPC 用满卡时)——
      **2026-08-03 确认无需本计划再动作。** P1 第四章已落盘(commit 0c736ee),执行时明确判断
      "精英邪教徒满卡化本轮没做——真正需要一张具名精英卡时按需生成,不是提前批量
      造卡占地方"(见 `WORKLOG.md` 第七轮)。schema 早已就绪,满卡生成走
      `core/13-create-investigator.md` 的常规流程,不是 P6 要交付的独立产物,
      故此项无剩余工作,直接勾掉。
- [x] ~~**未验证:** `scripts/render-investigator.py` 从未真跑过~~ ——
      **2026-08-02 已实跑**(本机有 Python 3.14.5,原写的"本机无解释器"已过时)。
      五个 fixture 全跑通,脚本不崩、占位符设计有效;但暴露出字段覆盖缺口,
      拆出 **P8**(`2026-08-02-investigator-render-gaps.md`)。本条到此为止
- [x] ~~**未验证:** schema 未被任何真实投资者档案压过~~ ——
      **2026-08-02 已压过**:`templates/investigator.example.json` 是第一张完整实例,
      且写了一次性核算脚本逐条验过派生值、点数账本、每技能
      `value = base+职业+兴趣+成长`、信用评级落在区间内。
      压出来的结论:必填字段没有过严(只要 5 个,精英 NPC 薄记录仍合法),
      但**原 schema 覆盖面严重不足**——已由上面「第二轮」重建解决

## 可选(已判断:暂不做)

- [x] ~~`roster.csv` 花名册索引~~ —— **判断为暂不做**(2026-08-03)。
      理由:核对唯一在跑的战役 `campaigns/beidaihe-winter/` 目前**没有
      `investigators/` 目录、零份投资者档案**,花名册索引此刻没有对象可索引,
      造一份空表除了占地方没有任何用处。这不是永久否决——`roster.csv` 的字段
      形状(name/occupation/player/status)已经在「存储格式选型」一节记下,
      等某个战役真的有多名投资者需要快速点名时,照那行字段直接开一份 CSV
      即可,不需要重新设计,不必现在预先造好。

## 后续:来源指路精确到规则书章节(不阻塞任何人)

`reference/rules/character-creation.md` 现在的「来源」只到 `COC apolo.xlsx` 的 sheet 级别
(2026-08-02 补的引用,见上面第二轮的最后一条)。这够用,但不是终点——大部分小节标了
「章节号未核实」。

**2026-08-02 更新:这件事现在好做多了。** 规则书全文已归档为
`reference/sourcebooks/keeper-rulebook-7e-zh.md`(28443 行中译转录),不必再从 PDF 里翻——
可以直接搜。两点注意:该译本页码是**英文原书页码**,标章节时用章节名而非页码;
且原译者自述部分章节未系统校对,发现与提炼稿冲突时不要盲从转录稿。

- [ ] 通读 `reference/sourcebooks/keeper-rulebook-7e-zh.md` 的人物创建相关章节,把
      `character-creation.md` 里标"章节号未核实"的引用替换成实际章节号/附录号
      (**只填章节定位,不摘原文**——不改变现在"只提炼公式"的方针,只是把引用精度
      从「xlsx sheet」提到「规则书章节」)
      - 篇幅大(章节数多),建议开新窗口单独处理,不要顺手做
      - 若通读中发现现有提炼(公式、区间、字段形状)跟规则书原文有出入,
        以规则书为准修正,并在这条完成时记一笔改了哪里
