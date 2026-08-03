# update_plan/Archived/ — 归档计划索引

已完成(或已完成大部分、剩余部分拆成新计划)的 `update_plan/` 计划文件存档目录。

**分工:** `../README.md` 的状态索引表只对归档条目留一行指针(名称 + 链接 + 极简状态),
不重复这里的范围描述——归档计划数量会一直增长,把全部细节留在主索引里会让每次读
`update_plan/README.md` 的 token 成本跟着涨。本文件才是归档计划的详细记录。

## 已归档

| # | 计划 | 范围 | 归档时状态 |
|---|---|---|---|
| P1 | [cult-doc-integration](2026-08-02-cult-doc-integration.md) | 克苏鲁教团 docx 四章提炼进 kit(历史/教团/设计方法论/邪教徒与怪物)+ 敌对势力 intake 问题(`The threat`)+ NPC 互动史附加项 | 阶段 0/1/2 与附加项全部完成;阶段 3(收尾:索引登记、review-material 审计、提交)拆分为独立计划 [`2026-08-02-cult-doc-wrapup.md`](../2026-08-02-cult-doc-wrapup.md) |
| P2 | [multi-arc-and-branching](2026-08-02-multi-arc-and-branching.md) | 多章 campaign(续作/时间跳跃)与平行世界分支的结构惯例——按 canon 是否分叉划界:不分叉留同文件夹补"arc"惯例,分叉新开兄弟 campaign 声明血缘 | 已完成(e0d026b) |
| P3 | [conventions-gaps](2026-08-02-conventions-gaps.md) | 对 core/ 全部 13 份 spec 的出版惯例评估,一次性列出七项缺口。结算 SAN 奖励、成长阶段、追逐规则速查、人数缩放侧栏四项本计划内落盘;魔法速查、低成本地图、玩家卡生成三项体量与阻塞点不同,拆出为 P7/P5/P6 独立跟踪 | 已完成(e0d026b) |
| P4 | [antagonist-budget](2026-08-02-antagonist-budget.md) | 反派强度预算(仅人类侧):普通人类模板取材 `busybodies-zh.md`,法术型首领增量取材 `grand-grimoire-zh.md` 资历法术表 / 非法术型走装备总价,属性技能走标准创建规则 + 标准池公式,技能选择由背景定、数值上限由致命性倒推。落盘于 `character-creation.md` §11,`core/02/06/07/11` 接线。怪物侧种类阶梯(待讨论 7)转交 P9,不卡本计划完结 | 已完成(610dd3b,intake 接线随 66d32d2) |
| P6 | [investigator-cards](2026-08-02-investigator-cards.md) | 玩家卡(投资者):JSON 唯一真源(`campaigns/<slug>/investigators/<name>.json`)+ 渲染 md 卡面 + `create-investigator` 技能。schema 按真实车卡表(`COC apolo.xlsx`)重建,新增 `investigator.example.json` 完整核算样卡。收尾判断:精英邪教徒满卡化按需生成、不预造;`roster.csv` 花名册暂不做——唯一在跑战役目前零份投资者档案,没有对象可索引 | 已完成(97c87d8) |

## 读法

- 每份归档文件头部的 `> 状态:` 是权威记录;本表只是索引,和文件本身对不上时以文件为准。
- 归档记录**不删减、不改写内容**——它们是"当初为什么这么定"的设计备忘。拆出的后续
  计划(如 P1 → wrapup)只承接未完成的执行清单,不重复背景说明,需要背景时回读这里。
- 新增归档时:移文件进本目录、在上表加一行、归档文件头状态改成
  `已完成(<commit>)` 或"已完成大部分,剩余拆出为 <新计划>",`../README.md`
  对应行改成指针形式(见该文件"完结清单"第 7 项)。
