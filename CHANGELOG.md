# Changelog

本 kit 的改动记录。**每完成一个 `update_plan/` 计划(或任何改变 kit 行为的改动)必须在
此追加一条**,见 `update_plan/README.md` 的「完结清单」。

格式:按日期倒序,**同一天的所有改动合并成同一条**,标题为
`## YYYY-MM-DD (<commit>, <commit>, ...)`。正文只有两个小节(没有的省略):

- `### 修复问题` —— **一个问题一句话**,说清原来错在哪、现在怎样。
- `### 更新内容` —— **一项更新一句话**,说清 Keeper 现在能做什么/必须怎么做。

只写**面向使用者**的变化——"改了哪个 spec 的哪句话"不用写。当天已有条目时,把新改动
补进那条的对应小节并在标题追加 commit,**不要为同一天新开一条**。

---

## 2026-08-02 (713cd1c, e0d026b, aceddf9)

对应计划:[P2 multi-arc-and-branching](update_plan/Archived/2026-08-02-multi-arc-and-branching.md)、
[P3 conventions-gaps](update_plan/Archived/2026-08-02-conventions-gaps.md) 第 1/2/5/6/7 项
(第 5 项玩家卡后续拆出为 [P6 investigator-cards](update_plan/2026-08-02-investigator-cards.md))、
[P6 investigator-cards](update_plan/2026-08-02-investigator-cards.md) 第二轮

### 修复问题

- 维护规则一直要求"填 changelog",但仓库里根本没有 `CHANGELOG.md`,现已补上本文件。
- 已归档的 P2 计划文件头仍写着"状态:待执行",与状态表里的"已完成(e0d026b)"矛盾,现已同步。
- Maintenance 规则此前只存在于 `CLAUDE.md`,`GEMINI.md` 与 `AGENTS.md` 里缺失(只存在于一个适配器的指令本身就是 bug),现三份适配器一致。
- **投资者卡的建卡顺序原本是错的**:先算技能点再定年龄。年龄的教育进步检定会改 EDU,而多数职业公式吃 EDU——照原顺序建出来的卡点数必然对不上。现在年龄排在算点数之前。
- 投资者卡渲染时会丢掉技能专精,同一张卡上两条 `Science` 渲成一模一样,读卡的人分不出哪条是工程学、哪条是物理。现已合成显示为 `Science (Engineering)`。

### 更新内容

- `update_plan/README.md` 增加**完结清单(Definition of Done)**:状态两处同步、changelog、产物重建、三适配器一致性、术语、计划间关系、提交与归档共七组。
- 新增**同一 campaign 内的多章(arc)惯例**:剧本骨架编号 `01-<slug>.md`、`02-...`,`overview.md` 增加 Arcs 索引,`sessions/` 全局连续编号不按章清零。
- 新增 **canon-log 的 Interlude(幕间)条目**:时间跳跃时记录流逝时长、幕后世界变化、人物状态清扫与带进下一章的后果。
- 新增**平行世界分支 campaign**:兄弟文件夹加 campaign `CLAUDE.md` 的可选 `Lineage` 字段(`Forked from: <parent-slug> @ session <n>`),分叉点前的父线 canon 只读继承、永不写回,共享实体 copy-on-write。
- 新增 **event-clock 归档惯例**:一章威胁结清后归档到 `world/archive/event-clock-<arc>.md` 并重建 `world/event-clock.md`,live clock 路径不变、现有 spec 引用零改动。
- 新增**结算奖励与成长阶段**:剧本结束时的 SAN 回复与成长判定写进 spec,`templates/scenario.md` 增加对应小节。
- 新增**投资者(玩家卡)生成**:`create-investigator` 技能加 `core/13-create-investigator.md`,以 `templates/investigator.schema.json` 为唯一真相源,`scripts/render-investigator.py` 渲染成 `templates/investigator.md` 卡面。
- 新增**追逐速查** `reference/rules/chases.md`,以及**人物创建与理智速查** `reference/rules/character-creation.md`、`reference/rules/sanity.md`。
- `core/04-design-scenario.md` 增加"在既有 campaign 开新章"路径:读全部前章 canon 与归档钟,不重建世界。
- `core/00-how-to-run.md` 的 Layout 图补上 `world/archive/` 与编号骨架。
- 人数缩放惯例并入 `core/04-design-scenario.md` 与 `core/11-review.md` 的审查项。
- **投资者卡现在照一张真实车卡建模,不再只是个属性块**:`templates/investigator.schema.json` 重建,补上年龄补正、点数账本、技能的基础值/职业点/兴趣点/专精、信用评级对应的生活水平与现金资产、装备、经历包、神话遭遇、背景「关键」标记、伙伴与成长记录。旧记录仍然合法——新字段全部可选。
- **建卡知识大幅补齐** `reference/rules/character-creation.md`:年龄七档补正表、Build/伤害加值表、MOV 判定、重伤值、技能基础值表、职业的三要素(点数公式家族/信用区间/本职技能表含自由槽)、信用评级→生活水平/现金/资产/消费水平换算表、伞技能专精写法、可选规则(技能上限、艺术/科学/语言外溢、经历包)。**用它可以逐条审一张别人交上来的卡**。
- `core/13-create-investigator.md` 的建卡顺序改为八步,并加上**点数账本必须平**的验收口径:职业点花完 = 公式总额、兴趣点花完 = INT×2、每条技能 `value = 基础值+职业点+兴趣点+成长点`。
- 新增 `templates/investigator.example.json` —— 一张字段填满、算术已逐条核过的样卡。建卡时照它的形状抄,不用猜一张满卡需要哪些字段。
- `reference/rules/character-creation.md` 每个小节加**来源指路**:标明数据是从 `COC apolo.xlsx` 哪个 sheet 提炼的,不摘原文、只给定位信息——技能基础值表的"规则书第四章:技能"是源材料自带的引用,其余小节如实标注"章节号未核实"而非编号瞎猜。`reference/README.md` 记录了这条惯例本身,供以后其他速查文件照做。

---

## 2026-08-01 (d213f2e, bd7cd5a, 55d1e8e, 93f8258)

### 修复问题

- 端到端彩排暴露的四处 spec 缺陷已修复。

### 更新内容

- **所有指令收进 `core/`**,`CLAUDE.md` / `GEMINI.md` / `AGENTS.md` 降级为三份薄适配器,Claude、Gemini、ChatGPT 共用同一份来源——**改 kit 行为改 `core/`,不改根适配器**。
- `.claude/skills/` 下的技能全部改为指向 `core/` 对应 spec 的薄包装。
- `scene-description` 技能更名为 `description`。
- 新增 `dist/bundle.md`(由 `scripts/build-bundle.sh` 生成),供 ChatGPT 单文件上传。
- `reference/` 扩充:中文术语表 `glossary-zh.md`、洛氏写作笔记、怪物与神话资料。

---

## 2026-07-29 (339a89b, 4558135)

### 更新内容

- CoC 7 版 Keeper 准备工作台首次发布:intake → 世界 → 事件钟 → 卡司 → 剧本 → 审查 → canon 更新的完整流水线,以及配套技能与模板。
