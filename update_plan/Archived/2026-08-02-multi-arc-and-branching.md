# Update Plan — 多剧本 Campaign 结构(续章与平行世界)

> 日期:2026-08-02
> 状态:待执行
> 与 `2026-08-02-cult-doc-integration.md` 互相独立,可任意插序执行。

## 问题

现有结构的隐含假设:**一个 campaign 文件夹 = 一条时间线 = 一本 append-only canon-log
= 一个在跑的 event-clock**。两类需求会打破它:

- **A. 同线续作/时间跳跃**("1 年后" 开新剧本)——时间线没断,但缺"章"这一层。
- **B. 平行世界/强关联分支**——canon 分叉,单本 append-only log 无法承载两条
  互相矛盾的世界线。

## 划界原则

**看 canon 是否分叉。** 不分叉 → 留在同一文件夹,补"arc(章)"惯例;
分叉 → 新开兄弟 campaign 文件夹,声明血缘(Lineage)。

## 方案 A — 同一 campaign 内的多章(arc)

- 剧本骨架编号:`01-<scenario-slug>.md`、`02-...`;`overview.md` 增加 Arcs 索引
- `sessions/` 全局连续编号,**不按章清零**(canon-log 按 session 号引用)
- canon-log 新增 **Interlude(幕间)条目**:时间跳跃时追加一条——流逝时长、
  幕后世界变化、人物状态清扫(老去/死亡/迁移)、带进下一章的后果。
  格式同 session 条目,标 `Interlude`,append-only 规则不变
- event-clock:一章威胁结清后归档到 `world/archive/event-clock-<arc>.md`,
  为新威胁重建 `world/event-clock.md` —— live clock 路径永远不变,spec 引用零改动
- `world/` 是可变现状,直接向前编辑;历史由 canon-log 负责

## 方案 B — 平行世界/分支 campaign

- 新开兄弟文件夹 `campaigns/<slug>-<branch>/`,**本身是完全合法的 campaign**
  (五件套齐全),所有生成器零改动照常工作
- campaign `CLAUDE.md` 增加可选 **Lineage** 字段:
  `Forked from: <parent-slug> @ session <n> / <剧内日期>`
  - 分叉点之前的父线 canon **只读继承**:生成时读父线 canon-log 至第 n 条
  - **永不写回父线**;分歧只记在本分支
- 共享实体 **copy-on-write**:内容一致时相对链接指向父线文件;分支改动某实体时
  才拷贝进分支,文件头注明 `> Diverged from <父路径> @ <分歧点>`
- 跨世界联动(A 世界行动影响 B 世界)不加新机制:写成各自 event-clock 的
  trigger,条件引用对方 campaign 的 canon-log

## 改动清单(全在 core/ + 模板,不碰根适配器)

- [x] `campaigns/README.md` — 新增 "Multi-arc & branching campaigns" 章节,
      写清上面两套惯例与划界原则
- [x] `campaigns/_template-campaign/CLAUDE.md` — 可选 `Lineage` 字段
      (默认 standalone)
- [x] `campaigns/_template-campaign/canon-log.md` — 增加 Interlude 条目示例
- [x] `core/12-canon-update.md` — 幕间条目类型 + 章节收尾清单
      (归档 event-clock、人物状态清扫、更新 CLAUDE.md 结构性 canon 块)
- [x] `core/04-design-scenario.md` — "在既有 campaign 开新章"路径:
      读全部前章 canon 与归档钟,骨架编号,不重建世界
- [x] `core/05-event-clock.md` — 钟的归档惯例(结清 → `world/archive/`,重建 live)
- [x] `core/00-how-to-run.md` — Layout 图补 `world/archive/` 与编号骨架一行
- [x] 重跑 `scripts/build-bundle.sh` 更新 `dist/bundle.md`
- [x] 按维护规则填 changelog / 更新 README(无 CHANGELOG.md;本次改动不涉及
      根 README 面向用户的入口,`overview.md`/`canon-log.md` 模板已同步 Arcs
      索引,视为满足维护规则)
