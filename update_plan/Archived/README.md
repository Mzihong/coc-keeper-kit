# update_plan/Archived/ — 归档计划索引

已完成(或已完成大部分、剩余部分拆成新计划)的 `update_plan/` 计划文件存档目录。

**分工:** `../README.md` 的状态索引表只对归档条目留一行指针(名称 + 链接 + 极简状态),
不重复这里的范围描述——归档计划数量会一直增长,把全部细节留在主索引里会让每次读
`update_plan/README.md` 的 token 成本跟着涨。本文件才是归档计划的详细记录。

## 已归档

| # | 计划 | 范围 | 归档时状态 |
|---|---|---|---|
| P1 | [cult-doc-integration](2026-08-02-cult-doc-integration.md) 阶段 0-2 + [cult-doc-wrapup](2026-08-02-cult-doc-wrapup.md) 阶段 3 | 克苏鲁教团 docx 四章提炼进 kit(历史/教团/设计方法论/邪教徒与怪物)+ 敌对势力 intake 问题(`The threat`)+ NPC 互动史附加项 + 阶段 3 收尾(README 索引登记、review-material 审计、发现并修正一处怪物条目交叉引用错误) | 全部完成(阶段 0-2 见各章落盘 commit;阶段 3:58da4fa) |
| P2 | [multi-arc-and-branching](2026-08-02-multi-arc-and-branching.md) | 多章 campaign(续作/时间跳跃)与平行世界分支的结构惯例——按 canon 是否分叉划界:不分叉留同文件夹补"arc"惯例,分叉新开兄弟 campaign 声明血缘 | 已完成(e0d026b) |
| P3 | [conventions-gaps](2026-08-02-conventions-gaps.md) | 对 core/ 全部 13 份 spec 的出版惯例评估,一次性列出七项缺口。结算 SAN 奖励、成长阶段、追逐规则速查、人数缩放侧栏四项本计划内落盘;魔法速查、低成本地图、玩家卡生成三项体量与阻塞点不同,拆出为 P7/P5/P6 独立跟踪 | 已完成(e0d026b) |
| P4 | [antagonist-budget](2026-08-02-antagonist-budget.md) | 反派强度预算(仅人类侧):普通人类模板取材 `busybodies-zh.md`,法术型首领增量取材 `grand-grimoire-zh.md` 资历法术表 / 非法术型走装备总价,属性技能走标准创建规则 + 标准池公式,技能选择由背景定、数值上限由致命性倒推。落盘于 `character-creation.md` §11,`core/02/06/07/11` 接线。怪物侧种类阶梯(待讨论 7)转交 P9,不卡本计划完结 | 已完成(610dd3b,intake 接线随 66d32d2) |
| P6 | [investigator-cards](2026-08-02-investigator-cards.md) | 玩家卡(投资者):JSON 唯一真源(`campaigns/<slug>/investigators/<name>.json`)+ 渲染 md 卡面 + `create-investigator` 技能。schema 按真实车卡表(`COC apolo.xlsx`)重建,新增 `investigator.example.json` 完整核算样卡。收尾判断:精英邪教徒满卡化按需生成、不预造;`roster.csv` 花名册暂不做——唯一在跑战役目前零份投资者档案,没有对象可索引 | 已完成(97c87d8) |
| P7 | [magic-quickref](2026-08-02-magic-quickref.md) | 魔法速查 `reference/rules/magic.md`:施法通则(消耗记法、施法用时、POW 对抗)、按 `grand-grimoire-zh.md` 抽样得出的四档消耗区间(小术/中术/大术/仪式级)、法术设计成本换算惯例(含"反制法术代价须低至少一档"设计铁律)、魔法书研读机制(据 `keeper-rulebook-7e-zh.md` 的 CMI/CMF/MR + 泛读/精读两阶段,比原计划设想的"现编"更准确)。`core/02`/`core/07`/`reference/mythos/README.md` 已接线 | 已完成(84dba55)——`dist/bundle.md`/`index.json` 因与并行 P8 会话共享工作区暂未提交,见 `WORKLOG.md` 2026-08-03 第二轮 |
| P8 | [investigator-render-gaps](2026-08-02-investigator-render-gaps.md) | 投资者卡渲染缺口:`spells`/`cthulhu_mythos`/`notes`/P6 重建后新增字段(`occupation_detail`/`age_modifiers`/`skill_points`/`credit_rating` 细目/`gear`/`status`/`party`/`experience_packages`/`mythos_encounters`/`growth_log`)全部补全渲染出口,渲染永远面向 KP(不再按 `type` 分受众);渲染器加两层自校验——硬性算术(派生值公式、点数账本、每技能加总)无条件跑,阈值型(技能上限、特征区间)读 `campaigns/<slug>/investigators/validation.json`,默认警告照渲、`--strict` 拒渲。`core/13`/`character-creation.md` §9/`core/01`(新增问题 14)已接线 | 已完成(d9e1fef) |
| P9 | [monster-templates-traits](2026-08-02-monster-templates-traits.md) | 怪物侧强度标尺,三阶段。**阶段 A**(标尺与词条):`reference/rules/monster-scale.md` 五级阶梯(human/creature/servitor/unique/deity)+ 上级/下级子档区间、`reference/tables/monster-traits.md` 18 条数值词条(强制带破解口)、`core/07` 的 type/threat 重排。**阶段 B**(索引层):扩 `scripts/build-reference-index.py` 新增 `parse_malleus_entries()`/`build_monster_index()`,生成 `reference/tables/monster-index.md`(223 条转录稿全覆盖 + 人写 `monster-index-data.json` 的 `Serves`/摘要 + 现有 bestiary 条目覆盖,进 bundle),现有 9 只 bestiary 条目按新标尺回改。**阶段 C**(神格铺设):5 个新神格页(`dagon-and-hydra`/`hastur`/`nyarlathotep`/`shub-niggurath`/`yog-sothoth`,均含「眷族与仆从」反链)+ 7 个新眷族/化身 bestiary 条目(Deep One、Byakhee、Spawn of Hastur、Hunting Horrors、Black Pharaoh、Dark Young、Sons of Yog-Sothoth),修正索引脚本一处英文标题匹配盲区。三阶段合计把 kit 从"几乎只有克苏鲁"拓宽到覆盖五位主要外神,"黄衣之王的精英怪是什么"这类查询首次能被 `monster-index.md` 直接答出 | 已完成(阶段 A 819971e,阶段 B 059ba63,阶段 C e125ad1) |

## 读法

- 每份归档文件头部的 `> 状态:` 是权威记录;本表只是索引,和文件本身对不上时以文件为准。
- 归档记录**不删减、不改写内容**——它们是"当初为什么这么定"的设计备忘。拆出的后续
  计划(如 P1 → wrapup)只承接未完成的执行清单,不重复背景说明,需要背景时回读这里。
- 新增归档时:移文件进本目录、在上表加一行、归档文件头状态改成
  `已完成(<commit>)` 或"已完成大部分,剩余拆出为 <新计划>",`../README.md`
  对应行改成指针形式(见该文件"完结清单"第 7 项)。
