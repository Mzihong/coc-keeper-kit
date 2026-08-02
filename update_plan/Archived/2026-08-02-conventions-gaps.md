# Update Plan — 出版模组惯例缺口补齐

> 日期:2026-08-02
> 状态:**已完成(e0d026b)** — 第 3/4/5 项的剩余工作拆成独立计划(P5/P6/P7),归档于 2026-08-02
> 来源:对 core/ 全部 13 份 spec 的惯例评估(对照 7e 官方模组与 Keeper 手册惯例)

## 这份计划做了什么

一次性评估出七项出版模组惯例缺口。**四项(1+2、6、7)在 e0d026b 落盘完结**;
**三项(3 魔法速查、4 低成本地图、5 玩家卡)体量与阻塞点各不相同,已拆成独立计划继续跟踪**
——本文件不再是活动计划,只作为"当初为什么这么定"的设计记录保留。

| # | 缺口 | 去向 |
|---|---|---|
| 1+2 | 结算 SAN 奖励 + 成长阶段 | ✅ 本计划完结(e0d026b) |
| 3 | 魔法速查 magic.md | → **P7** [magic-quickref](../2026-08-02-magic-quickref.md) |
| 4 | 低成本地图方案 | → **P5** [low-cost-maps](../2026-08-02-low-cost-maps.md) |
| 5 | 玩家卡(投资者)生成 | → **P6** [investigator-cards](../2026-08-02-investigator-cards.md) |
| 6 | 追逐规则速查 | ✅ 本计划完结(e0d026b) |
| 7 | 人数缩放侧栏 | ✅ 本计划完结(e0d026b) |

拆分理由:3 阻塞在 Keeper 交付魔法书转换稿、4 阻塞在 Keeper 定视觉风格、
5 的 kit 侧已全部就绪只剩跨 P1 复用与未验证项——三者的等待对象互不相同,
挂在同一份计划里会让状态栏永远写不清"到底在等什么"。

---

## 1+2. 结算奖励:SAN 回复 + 成长阶段 ✅

7e 惯例:剧本结束按成就发放理智回复(如"阻止仪式 +1D6 SAN"),并进行技能
成长检定(development phase)。原 `04` 的 endings 无奖励,`12` 无成长阶段。

**流程设计(结算问卷,放在 `12-canon-update.md`):**
结算时不让 Keeper 自己算,走"**建议 → 询问 → 调整**":

1. canon-update 收尾时增加一步:根据本剧本/本章达成的结局(读 endings 定义
   与 canon-log),**先给出建议数值**——每项成就对应的 SAN 回复、哪些技能
   可做成长检定
2. 明确询问 Keeper:接受 / 调整哪一项(奖励从不静默写入 canon)
3. 确认后把奖励写进 canon-log 的 session 条目(新增 `Rewards` 字段)

- [x] `reference/rules/sanity.md` — 补一节"剧本结算 SAN 奖励惯例"数值参考
      (小胜/大胜/击败实体的典型区间),供建议值有据可依
- [x] `core/04-design-scenario.md` — endings 每个分支附建议 SAN 奖励;
      `templates/scenario.md` 同步加字段
- [x] `core/12-canon-update.md` — 增加"结算"步骤:成长检定提醒 + 奖励
      建议→询问→写入流程;canon-log 模板 session 条目加 `Rewards` 行
- [x] `core/11-review.md` — 清单加一条:剧本级材料的 endings 带奖励建议

## 3. 魔法速查与 tome/spell 数值惯例 → 拆出为 P7

版权红线(只提炼机制惯例与数值区间,不复制条目原文)、执行清单、
阻塞点(等 Keeper 交付转换稿)全部移入 [P7 magic-quickref](../2026-08-02-magic-quickref.md)。
它是 P1 第四章的前置。

## 4. 低成本地图方案 → 拆出为 P5

"数据与渲染分离"的三档方案(mermaid / DSL+`render-map.py` / 手绘要点清单)、
待 Keeper 拍板的视觉风格与 DSL 范围,全部移入
[P5 low-cost-maps](../2026-08-02-low-cost-maps.md)。

拆分时顺带更正了一处记录错误:原状态表写"4 原型已做",但 repo 内无任何原型产物
(无 `scripts/render-map.py`,campaigns 下无示例图)——P5 按"原型未落盘"记录。

## 5. 玩家卡(投资者)生成 → 拆出为 P6

kit 侧七个条目已在 e0d026b 全部交付(schema 为唯一真源、`core/13` 新 spec、
`create-investigator` 技能、`render-investigator.py` 渲染器)。
存储格式选型理由(为什么 JSON 而不是 SQLite/CSV)、交付清单与剩余的
跨 P1 复用、两项未验证项,移入
[P6 investigator-cards](../2026-08-02-investigator-cards.md)。

## 6. 追逐规则速查 ✅

- [x] `reference/rules/chases.md` — 从 7e 规则提炼:速度对比、行动点、
      障碍与冒险移动、载具、脱离条件——机制引用,不转录
- [x] `core/02-rules-reference.md` — 登记;`core/04` 场景设计提及追逐时指向

## 7. 人数缩放侧栏 ✅

- [x] `core/04-design-scenario.md` — Principles 加一条:产出剧本时附
      "Scaling" 侧栏——低于/高于基准人数(campaign CLAUDE.md 的 party size)
      时,对手数量、线索冗余、SAN 总压力如何增减
- [x] `templates/scenario.md` — 加 Scaling 侧栏字段;`11` 清单同步

> 注:P4 反派强度预算讨论的是**强度**(技能点预算带),§7 调的是**数量**,
> 两者的关系见 `../2026-08-02-antagonist-budget.md` 待讨论 4。
