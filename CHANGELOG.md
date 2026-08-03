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

## 2026-08-03 (c5dbaf1, 待提交)

对应计划:[P4 antagonist-budget](update_plan/Archived/2026-08-02-antagonist-budget.md)、
[P6 investigator-cards](update_plan/Archived/2026-08-02-investigator-cards.md)——两者内容
均已在 2026-08-02 落盘完成,本轮只是收尾归档,无新增用户可见能力。

### 修复问题

- P4/P6 的计划文件头、`update_plan/README.md` 状态表在内容早已提交完成后仍停留在
  "等提交"/"进行中"措辞,现已回填 commit hash 并归档进 `update_plan/Archived/`。
- `CHANGELOG.md` 2026-08-02 条目头部的 commit 列表此前只列了 4 个(含一个"待提交"
  占位),现已核实补全为当天实际的全部 16 个 commit。

---

## 2026-08-02 (713cd1c, 9c011f3, a7cb4f6, 97c87d8, 39d1625, 0769902, 610dd3b, 9c47d98, 7e42d2a, ef4936a, e34d3db, 0c736ee, 66d32d2, d91f487, e0d026b, aceddf9)

对应计划:[P2 multi-arc-and-branching](update_plan/Archived/2026-08-02-multi-arc-and-branching.md)、
[P3 conventions-gaps](update_plan/Archived/2026-08-02-conventions-gaps.md) 第 1/2/5/6/7 项
(第 5 项玩家卡后续拆出为 [P6 investigator-cards](update_plan/2026-08-02-investigator-cards.md))、
[P6 investigator-cards](update_plan/2026-08-02-investigator-cards.md) 第二轮、
[P4 antagonist-budget](update_plan/Archived/2026-08-02-antagonist-budget.md)(人类侧,已完成并归档)、
[P1 cult-doc-integration](update_plan/Archived/2026-08-02-cult-doc-integration.md)(全部四章 + 阶段 2 + NPC 互动史附加项,阶段 0-2 已归档;阶段 3 收尾拆出为 [cult-doc-wrapup](update_plan/2026-08-02-cult-doc-wrapup.md))

### 修复问题

- 维护规则要求填 changelog,但仓库里没有 `CHANGELOG.md`,现已补上。
- 已归档的 P2 计划文件头与状态表不一致,现已同步为"已完成(e0d026b)"。
- Maintenance 规则此前只写在 `CLAUDE.md`,现三份适配器已同步一致。
- 投资者建卡顺序颠倒(先算技能点再定年龄,年龄会改 EDU),现改为先定年龄再算点数。
- 投资者卡渲染会丢失技能专精(两条 `Science` 渲成一样),现合成显示为 `Science (Engineering)`。
- `build-reference-index.py` 不递归扫描,`mythos/` 子目录下的文件此前完全漏检,现已改为递归扫描。

### 更新内容

- 新增 `update_plan/README.md` 的完结清单(状态同步、changelog、产物重建等七组收尾检查项)。
- 新增同一 campaign 内的多章(arc)编号与索引惯例。
- canon-log 新增 Interlude(幕间)条目,记录章节间的时间跳跃与世界变化。
- 新增平行世界分支 campaign 惯例(`Lineage` 字段 + 父线只读继承)。
- 新增章节结清后归档 event-clock 的惯例。
- 新增剧本结束时的 SAN 回复与成长判定惯例。
- 新增 `create-investigator` 技能:JSON 唯一真源 + 渲染投资者卡面。
- 新增追逐、人物创建、理智三份速查表。
- `design-scenario` 新增在既有 campaign 开新章的路径。
- 人数缩放惯例并入 `design-scenario` 与 `review-material` 的审查项。
- 投资者卡 schema 按真实车卡表重建,补齐年龄补正、点数账本、装备、背景等字段(旧记录仍合法)。
- `character-creation.md` 补齐年龄补正、Build/伤害加值、技能基础值等建卡数据,可用来审核他人交的卡。
- `create-investigator` 建卡顺序改为八步,并加上点数账本必须平的验收口径。
- 新增 `investigator.example.json` 一张字段填满、算术已核对的样卡。
- kit 转载规则改为分层:生成内容不含原文,官方资料可收录但须标注 `## 引用出处`、只取结构不取文字。
- 补上一个 bundle 缺件:洛夫克拉夫特笔法笔记此前从未进 `dist/bundle.md`,现已收进 bundle。
- 新增 `reference/craft/`(手法提炼稿),与 `reference/rules/`(数值速查)分工。
- 反向索引扩到全部七个目录,新增 orphan(无人引用)检查。
- `reference/decks/`(卡组)与 `reference/sourcebooks/`(整书)分类归位,本轮收录 7 份官方资料。
- 官方法术、怪物、规则原文本地可查(卡组/书本身不进 `dist/bundle.md`,所有引用按可选处理)。
- 新增归档第三方资料的技能 `archive-reference`,七步走完分类、命名、引用、接线、重建索引。
- 新增反向索引 `reference/index.json`(按 `## 引用出处` 解析出处、全仓库扫描引用行号)。
- P7 魔法速查阻塞解除(转换稿已归档为 `grand-grimoire-zh.md`)。
- 新增 `WORKLOG.md`,给接手会话的协作者用的结构与约定速览。
- 新增 `reference/decks/` 与首份收录件 `busybodies-zh.md`(官方好事者卡组,47 张 NPC 卡)。
- `character-creation.md` 各小节补上数据来源指路(标明取自哪个源文件/章节)。
- 新增收尾维护会话技能 `close-session`,收尾时强制 grep 核对日志里的数量词/路径。
- 新增人类反派强度预算:普通人类照官方 NPC 卡校准,首领按法术资历或装备总价加增量。
- 新增邪教设计方法论 `craft/cult-design-zh.md`,配四张骰表与 `templates/cult.md` 模板。
- 教团文档第一/二章落盘:新增克苏鲁本体 lore、历史条目表与五个具体教团全档。
- 教团文档第四章落盘(P1 四章全部完成):新增邪教徒原型速查、8 个怪物、造物与配套法术。
- intake 新增"The threat"与反派强化两问,答案写入 campaign `Threat` 字段供后续 spec 读取。
- NPC 档案新增互动史记录节(当前态度 + 逐场一行事实),`update-canon` 收尾清单纳入必需项。

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
