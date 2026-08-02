# Update Plan — 出版模组惯例缺口补齐

> 日期:2026-08-02
> 状态:待执行
> 来源:对 core/ 全部 13 份 spec 的惯例评估(对照 7e 官方模组与 Keeper 手册惯例)
> 关联:`2026-08-02-cult-doc-integration.md`(第 3 项是其第四章落盘的前置)

## 1+2. 结算奖励:SAN 回复 + 成长阶段(小改,先做)

7e 惯例:剧本结束按成就发放理智回复(如"阻止仪式 +1D6 SAN"),并进行技能
成长检定(development phase)。现 `04` 的 endings 无奖励,`12` 无成长阶段。

**流程设计(结算问卷,放在 `12-canon-update.md`):**
结算时不让 Keeper 自己算,走"**建议 → 询问 → 调整**":

1. canon-update 收尾时增加一步:根据本剧本/本章达成的结局(读 endings 定义
   与 canon-log),**先给出建议数值**——每项成就对应的 SAN 回复、哪些技能
   可做成长检定
2. 明确询问 Keeper:接受 / 调整哪一项(奖励从不静默写入 canon)
3. 确认后把奖励写进 canon-log 的 session 条目(新增 `Rewards` 字段)

**改动清单:**
- [x] `reference/rules/sanity.md` — 补一节"剧本结算 SAN 奖励惯例"数值参考
      (小胜/大胜/击败实体的典型区间),供建议值有据可依
- [x] `core/04-design-scenario.md` — endings 每个分支附建议 SAN 奖励;
      `templates/scenario.md` 同步加字段
- [x] `core/12-canon-update.md` — 增加"结算"步骤:成长检定提醒 + 奖励
      建议→询问→写入流程;canon-log 模板 session 条目加 `Rewards` 行
- [x] `core/11-review.md` — 清单加一条:剧本级材料的 endings 带奖励建议

## 3. 魔法速查与 tome/spell 数值惯例(教团计划第四章的前置)

`reference/rules/COC Magic.pdf` 是官方魔法全书(受版权保护)。Keeper 将自行
转换为 Word 后交给模型处理。红线同 og_Norval:**只提炼机制惯例与数值区间,
不复制条目原文**——产出是速查表,不是法术合集的转录。

- [ ] 等 Keeper 提供转换后的文档,切块处理(同教团 docx 的阶段 0 方法)
- [ ] 产出 `reference/rules/magic.md` 速查:施法通则(MP/SAN/POW 消耗、
      施法时间、对抗)、tome 数值惯例(研读时间、SAN 损失、Mythos 增益区间)、
      法术设计的成本换算惯例
- [ ] `core/02-rules-reference.md` — cheat-sheets 清单登记 magic.md,
      "Read this before" 加:写任何法术/仪式/魔法书前
- [ ] `core/07-create-monster.md` 与 `reference/mythos/README.md` —
      spellcaster/tome 数值指向 magic.md
- [ ] **顺序依赖:** 教团计划第四章造物若含法术/仪式,先完成本项再落盘

## 4. 低成本地图方案

约束:纯 token 生成位图/精细 SVG 成本高且不可维护。方案取"**数据与渲染
分离**"——模型只产出几行结构化数据,渲染交给确定性工具,token 成本 ≈ 写
一张小表:

| 图类型 | 方法 | 成本 |
|---|---|---|
| 场景网/区域关系/势力图 | **mermaid**(GitHub 与 Artifact 原生渲染,repo 内直接可见) | 几行文本 |
| 建筑平面图 | 小 DSL(JSON:房间名+矩形坐标+门窗)+ `scripts/render-map.py` 确定性渲染 SVG | 模型只写坐标 JSON |
| 手绘感调查地图 | 不生成,产出"给 Keeper 的手绘要点清单"(哪些地标、比例、标注) | 几行文本 |

- [ ] 原型验证:挑 beidaihe-winter 一个场景,试做 mermaid 关系图 +
      DSL→SVG 平面图各一张,确认效果/成本后再定稿惯例
- [ ] `scripts/render-map.py` — DSL→SVG 渲染器(无外部依赖,stdlib 即可)
- [ ] `templates/location.md` / `scene.md` — 增加可选 "Map" 一节
      (mermaid 块或 DSL JSON 块)
- [ ] `core/03-build-world.md` / `core/09-description.md` — 各加一行:
      何时附图、用哪种
- [ ] 无文件系统的环境(ChatGPT 网页)降级:只出 mermaid 与文字键位图

## 5. 玩家卡(投资者)生成:模板 + skill + 结构化存储

教团文档第四章含部分可用原型,车卡能力同时服务 pregens 与邪教徒精英。

**存储格式选型(建议,可推翻):JSON,一人一档。**
- SQL/SQLite 是二进制或需运行时:git diff 不可读、Gemini/ChatGPT 网页
  难直读,违背"三模型共用一份源"的架构,**不建议**
- CSV 表达不了嵌套(技能表、武器表、backstory 多条目),只适合花名册索引
- JSON(即你说的 NoSQL 格式)git 友好、三模型可直读可校验、可派生
- 结构:`campaigns/<slug>/investigators/<name>.json`(唯一真源)+
  由它渲染的 `<name>.md` 人类可读卡(桌面用);`roster.csv` 花名册索引可选

- [x] `reference/rules/character-creation.md` — 车卡速查:特征骰法、
      职业技能点(EDU×4 等)、兴趣点、信用评级区间、背景栏目——机制引用,
      不转录原文
- [x] `templates/investigator.schema.json` + `templates/investigator.md` —
      JSON schema 与 markdown 卡模板
- [x] `core/13-create-investigator.md` — 新 spec:pregen 流程(概念→职业→
      数值→背景钩子,钩子必须挂进 campaign 前提)、JSON 为真源、md 为视图
- [x] `.claude/skills/create-investigator/` — 薄包装;根三适配器的 skill
      表同步登记(CLAUDE/GEMINI/AGENTS 一起改,不算行为指令,只是路由表)
- [x] `scripts/render-investigator.py` — JSON→md 渲染(无法在本环境跑
      python 验证——无解释器可用——已仔细复核代码,仅用 stdlib json/pathlib)
- [x] `core/00-how-to-run.md` — 管线与 Layout 登记 `investigators/`
- [x] `core/11-review.md` — 清单加:投资者 JSON 过 schema 校验、数值自洽
- [ ] 与教团计划交叉:第四章邪教徒精英可用同 schema 存档(NPC 用满卡时)
      —— 留给 P1 第四章执行时使用,此处 schema 已就绪

## 6. 追逐规则速查 ✅

- [x] `reference/rules/chases.md` — 从 7e 规则提炼:速度对比、行动点、
      障碍与冒险移动、载具、脱离条件——机制引用,不转录
- [x] `core/02-rules-reference.md` — 登记;`core/04` 场景设计提及追逐时指向

## 7. 人数缩放侧栏 ✅

- [x] `core/04-design-scenario.md` — Principles 加一条:产出剧本时附
      "Scaling" 侧栏——低于/高于基准人数(campaign CLAUDE.md 的 party size)
      时,对手数量、线索冗余、SAN 总压力如何增减
- [x] `templates/scenario.md` — 加 Scaling 侧栏字段;`11` 清单同步

## 执行顺序建议

1. **第 1+2+7 项**先做(纯 spec 小改,半小时级)
2. **第 3 项**等 Keeper 交付转换后的魔法书文档;完成后解锁教团计划第四章
3. **第 4 项**做原型验证后定稿
4. **第 5 项**独立成块,随时可做(教团第四章之前做完更好,精英邪教徒可复用)
5. **第 6 项**随时,与 3 可同批
6. 收尾统一:重跑 `scripts/build-bundle.sh`、填 changelog / README
