# craft/ — 手法知识提炼稿

**从大部头里提炼出来的「怎么写」,按「哪个 spec 读哪一节」分节。**

和 `rules/` 的分工是本目录存在的理由:`rules/` 管**数字**——难度带、SAN 损失、伤害加值;
`craft/` 管**写法**——怎么揭示一个怪物、一段读稿从哪个感官切入、一个邪教为什么可怕。
两边都是 kit 原创提炼稿,都进 `dist/bundle.md`,但一个错了会让数值不对,另一个错了会让
文字平庸。别把手法写进 `rules/`,也别把公式写进这里。

## 现有条目

| 文件 | 提炼自 | 谁在读 |
|---|---|---|
| `lovecraft-zh.md` | `reference/og_Norval/`(洛夫克拉夫特原著 82 篇通读) | `core/09-description.md`(§一 基调、§二 场景/行动)、`core/07-create-monster.md`(§三 怪物设计) |

机器可读版本是 `index.json`,由 `scripts/build-reference-index.py` 生成。

## 写一份新的

1. **分节按消费方组织,不按源材料的目录组织。** 每一节要能被某个 spec 指名去读
   ——「`core/09` 读 §一和 §二」,而不是「第三章的读书笔记」。spec 里也要写上是哪一节。
2. **只记「他怎么做到的」,不复述「他写了什么」。** 这是技法字典,不是文摘。
   源材料若受版权保护,适用 `core/00-how-to-run.md` 的口径:**取结构和手法,不取文字**;
   指认技法所需的最短范例是上限,不可延伸引用。
3. **每条技法附出处**,便于追溯查证。
4. **篇幅克制。** `lovecraft-zh.md` 90 行覆盖了 82 篇小说。生成时模型要整份读进上下文,
   写成一本书就没人读得起。
5. 收尾:接线进要读它的 spec → 重跑 `scripts/build-reference-index.py`(没人引用会报
   orphaned)→ 重跑 `scripts/build-bundle.sh` → 记 `CHANGELOG.md`。

## 已排期的下一份

`update_plan/2026-08-02-cult-doc-integration.md` 第三章 A 项要产出邪教设计手法稿,
落点 `craft/cult-design-zh.md`,定位对标 `lovecraft-zh.md`。
