# Update Plan — 魔法速查(magic.md)

> 日期:2026-08-02
> 状态:阻塞(等 Keeper 交付魔法书转换稿——repo 内仅有原始 PDF)
> 来源:从 `Archived/2026-08-02-conventions-gaps.md` §3 拆出独立跟踪(2026-08-02)
> 关联:`2026-08-02-cult-doc-integration.md` 第四章(造物含法术/仪式时以本计划为前置)

## 问题

kit 现在能造 NPC、怪物、剧本,唯独**写不了法术、仪式、魔法书**——没有任何数值标尺。
`core/07-create-monster.md` 里 spellcaster 的法术、`reference/mythos/` 里 tome 的
研读时间与 SAN 损失,目前全靠模型现编。

## 红线(同 og_Norval 的处理口径)

`reference/rules/COC Magic.pdf` 是官方魔法全书,**受版权保护**。
**只提炼机制惯例与数值区间,不复制条目原文**——产出是速查表,不是法术合集的转录。

## 阻塞点

Keeper 将 PDF 自行转换为 Word 后交给模型处理(同教团 docx 的阶段 0 方法:切块通读)。
在拿到转换稿之前本计划无法推进——2026-08-02 检查时 `reference/rules/` 下
只有原始 `COC Magic.pdf`,未见转换稿。

## 改动清单

- [ ] 等 Keeper 提供转换后的文档,切块处理(同教团 docx 的阶段 0 方法)
- [ ] 产出 `reference/rules/magic.md` 速查:施法通则(MP/SAN/POW 消耗、
      施法时间、对抗)、tome 数值惯例(研读时间、SAN 损失、Mythos 增益区间)、
      法术设计的成本换算惯例
- [ ] `core/02-rules-reference.md` — cheat-sheets 清单登记 magic.md,
      "Read this before" 加:写任何法术/仪式/魔法书前
- [ ] `core/07-create-monster.md` 与 `reference/mythos/README.md` —
      spellcaster/tome 数值指向 magic.md
- [ ] 新术语进 `reference/glossary-zh.md`
- [ ] 重跑 `scripts/build-bundle.sh`(动了 `core/` 与 `reference/`)

## 下游

完成后解锁 **P1 第四章**(教团造物落盘)的前置依赖 2。
第四章另一个前置是 P4 反派强度预算——两者都完成才能动第四章。
