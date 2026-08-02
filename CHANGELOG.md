# Changelog

本 kit 的改动记录。**每完成一个 `update_plan/` 计划(或任何改变 kit 行为的改动)必须在
此追加一条**,见 `update_plan/README.md` 的「完结清单」。

格式:按日期倒序,每条 `## YYYY-MM-DD — <标题> (<commit>)`,正文用
`新增 / 变更 / 修复 / 移除` 四类小节(没有的省略)。只写**面向使用者**的变化——
"改了哪个 spec 的哪句话"不用写,"Keeper 现在能做什么/必须怎么做"才写。

---

## 2026-08-02 — 维护流程:完结清单与 changelog (待填 hash)

### 新增
- 本 `CHANGELOG.md`(此前维护规则说"填 changelog",但文件根本不存在)。
- `update_plan/README.md` 增加**完结清单(Definition of Done)**:状态两处同步、
  changelog、产物重建、三适配器一致性、术语、计划间关系、提交与归档七组。

### 修复
- 已归档的 P2 计划文件头仍写着"状态:待执行"——与状态表里的"已完成(e0d026b)"矛盾。
  这正是完结清单第 1 组要防的漏项。

### 变更
- Maintenance 规则从只有 `CLAUDE.md` 有,同步进 `GEMINI.md` 与 `AGENTS.md`
  (按可移植性规则,只存在于一个适配器的指令本身就是 bug)。

---

## 2026-08-02 — 多章 campaign 与平行世界分支 (e0d026b, 归档 aceddf9)

对应计划:[P2 multi-arc-and-branching](update_plan/Archived/2026-08-02-multi-arc-and-branching.md)

### 新增
- **同一 campaign 内的多章(arc)惯例**:剧本骨架编号 `01-<slug>.md`、`02-...`,
  `overview.md` 增加 Arcs 索引;`sessions/` 全局连续编号不按章清零。
- **canon-log 的 Interlude(幕间)条目**:时间跳跃时记录流逝时长、幕后世界变化、
  人物状态清扫与带进下一章的后果。
- **平行世界分支 campaign**:兄弟文件夹 + campaign `CLAUDE.md` 的可选 `Lineage` 字段
  (`Forked from: <parent-slug> @ session <n>`),分叉点前的父线 canon 只读继承、永不写回;
  共享实体 copy-on-write。
- **event-clock 归档惯例**:一章威胁结清后归档到 `world/archive/event-clock-<arc>.md`,
  重建 `world/event-clock.md`;live clock 路径不变,现有 spec 引用零改动。

### 变更
- `core/04-design-scenario.md` 增加"在既有 campaign 开新章"路径:读全部前章 canon 与
  归档钟,不重建世界。
- `core/00-how-to-run.md` 的 Layout 图补 `world/archive/` 与编号骨架。

---

## 2026-08-02 — 出版模组惯例缺口(第一批) (e0d026b)

对应计划:[P3 conventions-gaps](update_plan/2026-08-02-conventions-gaps.md) 第 1/2/5/6/7 项

### 新增
- **结算奖励与成长阶段**:剧本结束时的 SAN 回复与成长判定写进 spec,`templates/scenario.md`
  增加对应小节。
- **投资者(玩家卡)生成**:`create-investigator` 技能 + `core/13-create-investigator.md`,
  以 `templates/investigator.schema.json` 为唯一真相源,`scripts/render-investigator.py`
  渲染成 `templates/investigator.md` 卡面。
- **追逐速查**:`reference/rules/chases.md`。
- **人物创建与理智速查**:`reference/rules/character-creation.md`、`reference/rules/sanity.md`。

### 变更
- 人数缩放惯例并入 `core/04-design-scenario.md` 与 `core/11-review.md` 的审查项。

---

## 2026-08-01 — 重构:kit 围绕 `core/` 组织 (d213f2e, bd7cd5a, 55d1e8e, 93f8258)

### 变更
- **所有指令收进 `core/`**,`CLAUDE.md` / `GEMINI.md` / `AGENTS.md` 降级为三份薄适配器,
  Claude、Gemini、ChatGPT 共用同一份来源。**改 kit 行为改 `core/`,不改根适配器。**
- `.claude/skills/` 下的技能全部改为指向 `core/` 对应 spec 的薄包装。
- `scene-description` 技能更名为 `description`。

### 新增
- `dist/bundle.md`(由 `scripts/build-bundle.sh` 生成),供 ChatGPT 单文件上传。
- `reference/` 扩充:中文术语表 `glossary-zh.md`、洛氏写作笔记、怪物与神话资料。
- 端到端彩排暴露并修复的四处 spec 缺陷。

---

## 2026-07-29 — 初版 (339a89b, 4558135)

CoC 7 版 Keeper 准备工作台首次发布:intake → 世界 → 事件钟 → 卡司 → 剧本 → 审查 →
canon 更新的完整流水线,以及配套技能与模板。
