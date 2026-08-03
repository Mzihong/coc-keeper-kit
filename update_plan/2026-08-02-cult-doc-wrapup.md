# Update Plan — 克苏鲁教团文档整合:阶段 3 收尾

> 日期:2026-08-02
> 拆自:`Archived/2026-08-02-cult-doc-integration.md`(原 P1)。该计划阶段 0/1/2 与附加项
> 已全部落盘并归档;本文件只接手阶段 3(收尾)未完成的部分,内容不重复搬运——需要背景
> (来源文档、四章清单、各阶段落盘细节)时回读归档文件。
> 状态:待执行

## 背景

原计划的四章内容提炼、敌对势力 intake 问题(阶段 2)、NPC 互动史附加项均已完成并落盘,
细节见归档文件。只剩阶段 3 的收尾动作没做——登记索引、审计、提交,这些是任何计划完结
都要走的标准流程。拆成独立文件是为了让归档文件保持"已完成"的干净状态,不必在一份已经
归档的设计记录里继续挂着未勾选的待办。

## 阶段 3 — 收尾

- [ ] 更新 `reference/README.md`:登记 `craft/cult-design-zh.md`、`mythos/cults/` 条目、
      `tables/cult-goals.md`、`tables/cult-leader-positions.md`、
      `tables/cult-power-sources.md`、d20 外貌/气质表、`tables/cultist-archetypes.md`
- [ ] 更新 `reference/tables/README.md`:新表按既有分组(seed / prep & play)归位
- [ ] 登记 `templates/cult.md`
- [ ] 重跑 `scripts/build-bundle.sh` 更新 `dist/bundle.md`
- [ ] 用 `review-material` 对新增材料做一次审计(数值、剧透卫生、术语一致性)
- [ ] 按仓库维护规则填 changelog / 更新 README
- [ ] 提交:阶段 1 每章一个 commit,阶段 2 单独一个 commit

完成后按 `update_plan/README.md` 的完结清单收尾,并把本文件移入 `Archived/`
(归档索引记一行指向本文件,归档文件头状态改 `已完成(<commit>)`)。
