# Update Plan — 克苏鲁教团文档整合:阶段 3 收尾

> 日期:2026-08-02
> 拆自:`Archived/2026-08-02-cult-doc-integration.md`(原 P1)。该计划阶段 0/1/2 与附加项
> 已全部落盘并归档;本文件只接手阶段 3(收尾)未完成的部分,内容不重复搬运——需要背景
> (来源文档、四章清单、各阶段落盘细节)时回读归档文件。
> 状态:进行中(内容已落盘,等提交)——见文末「执行记录」

## 背景

原计划的四章内容提炼、敌对势力 intake 问题(阶段 2)、NPC 互动史附加项均已完成并落盘,
细节见归档文件。只剩阶段 3 的收尾动作没做——登记索引、审计、提交,这些是任何计划完结
都要走的标准流程。拆成独立文件是为了让归档文件保持"已完成"的干净状态,不必在一份已经
归档的设计记录里继续挂着未勾选的待办。

## 阶段 3 — 收尾

- [x] 更新 `reference/README.md`:登记 `craft/cult-design-zh.md`、`mythos/cults/` 条目、
      `tables/cult-goals.md`、`tables/cult-leader-positions.md`、
      `tables/cult-power-sources.md`、d20 外貌/气质表、`tables/cultist-archetypes.md`
- [x] 更新 `reference/tables/README.md`:新表按既有分组(seed / prep & play)归位
- [x] 登记 `templates/cult.md`
- [x] 重跑 `scripts/build-bundle.sh` 更新 `dist/bundle.md`
- [x] 用 `review-material` 对新增材料做一次审计(数值、剧透卫生、术语一致性)
- [x] 按仓库维护规则填 changelog / 更新 README
- [x] 提交:阶段 1 每章一个 commit,阶段 2 单独一个 commit

完成后按 `update_plan/README.md` 的完结清单收尾,并把本文件移入 `Archived/`
(归档索引记一行指向本文件,归档文件头状态改 `已完成(<commit>)`)。

## 执行记录(2026-08-03)

**登记情况核对**:`craft/cult-design-zh.md`、四张骰表(`cult-goals`/`cult-leader-positions`/
`cult-power-sources`/`npc-appearance`)、`mythos/cults/` 子目录、`templates/cult.md` 早前
落盘时已顺手接线完毕(`reference/README.md`、`reference/tables/README.md`、
`core/03`/`core/06`/`core/07`/`core/12`)。本轮核对后只补了两处真实缺口:
`reference/tables/README.md` 的 Prep & play 表列表漏了 `tables/cultist-archetypes.md`
(第四章的邪教徒范型表从未登记过);`reference/README.md` 的 `mythos/` 一行没有点名
`cults/` 子目录与新增的 `artifacts-zh.md`(造物道具类,不属于原有"Great Old Ones/
tomes/spells/cults/factions"任何一类)。两处均已补上。

**review-material 审计**:范围覆盖四章全部落盘文件(教团史、五教团档案、设计方法论、
邪教徒范型表、8 只怪物、造物、7 个新法术)。20 组人类/怪物数值(8 怪物 + 12 邪教徒
范型,含"慧强"永生大师范例)逐条按 7e 公式复核 HP=(CON+SIZ)/10、Build/Damage Bonus
按 STR+SIZ 表、MP=POW/5,**全部正确**,与 `cultist-archetypes.md` 头部"12 组基础数值
全部核对通过"的说法一致。交叉引用逐条核对文件是否存在,发现一处真实错误:
`reference/bestiary/fellrock.md` 的"沉默之油"词条指向了 `reference/mythos/artifacts-zh.md`,
但沉默之油实际收在 `reference/mythos/spells/oil-of-silence.md`(该法术文件本身反查
Fellrock 是对的,只有 Fellrock 这边反查错了)——已改正。除此之外没有发现阻塞项。

**提交**:阶段 1 四章内容早已分别提交(`ef4936a` 第一/二章、`610dd3b` 第三章、
`0c736ee` 第四章),阶段 2 见 `66d32d2`——本计划文件当时把"提交"列进阶段 3 待办,
但实际按内容归属逐章提交这件事在落盘当轮就已经做完,核对 `git log` 确认符合
"阶段 1 每章一个 commit,阶段 2 单独一个 commit"的要求,本轮无需重新提交这部分。
本轮自己新增的改动(两处登记补漏、review 发现的一处修复、bundle/index 重建、
changelog)另开一个新 commit。
