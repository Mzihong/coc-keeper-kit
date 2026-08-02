# Update Plan — 投资者卡渲染缺口(待讨论)

> 日期:2026-08-02
> 状态:**待讨论** —— 缺陷 1、2、4 已实测确认,但修法形状取决于待讨论 1,故暂不出执行清单
> (缺陷 3 与受众正交,2026-08-02 已直接修掉)
> 起因:`2026-08-02-investigator-cards.md`(P6)的「未验证」条目——
> `scripts/render-investigator.py` 首次实跑。跑通了,但跑出两个代码复核没看出来的缺口
> 关联:P6(本计划从其未验证项外溢);P1 第四章(11 个邪教徒原型将复用同一渲染路径)

## 环境事实更正

P6 的阻塞理由「本机无 Python 解释器」**已过时**。本机现有 `python 3.14.5`
(`C:\Users\User\.local\bin\python.exe`),脚本可直接运行。

## 实跑记录(2026-08-02)

三个自造 fixture,未写入仓库:

| 用例 | 结果 |
|---|---|
| 字段填满(pregen) | 渲染正常,表格/技能行/武器表/backstory 八栏全对 |
| 仅 schema 必填项 | 缺失字段落成 `<...>` 占位,未静默吞掉 |
| 中文姓名/职业 | UTF-8 读写正常,无乱码 |
| 不带参数 | usage 打到 stderr,exit 1,符合设计 |
| `type: elite-npc` + 法术 | **见下列缺陷 1、2** |

结论:脚本本身能跑、不崩、占位符设计有效。缺口在**字段覆盖**,不在实现质量。

## 缺陷 1 — 三个 schema 字段被渲染器整个丢弃

`spells`、`cthulhu_mythos`、`notes` 在 `templates/investigator.schema.json` 有定义
(72、73、92 行),但 `scripts/render-investigator.py` 的 `render()` 没有任何对应段落,
`templates/investigator.md` 也没有对应栏位。**是模板与渲染器一起缺,不是单边遗漏。**

实测:一个 `spells` 三条、`cthulhu_mythos: 45`、`notes` 一条的邪教首领,
渲出的卡上这三项**一个字都没有**。

严重度不在 pregen(调查员罕有法术),在 **elite-npc**:
- 教团计划第四章的精英邪教徒正是靠 `"type": "elite-npc"` 复用本 schema
- 一个施法者反派的守秘人卡上没有法术栏,等于卡面不可用于跑团
- 这直接违反 kit **自己写的质量线**——`core/13-create-investigator.md:55`:
  「`.md` 视图与 `.json` 源一致;不得有任何数据只出现在一方」

## 缺陷 2 — `elite-npc` 仍然渲染 Hooks 段

`core/13-create-investigator.md:41` 明写:elite-npc「skip the player-facing
backstory-hooks section」。渲染器第 83–84 行**无条件**输出 Hooks 段,不看 `type`。

实测确认:`type: elite-npc` 的 fixture 照样渲出「## Hooks tying them to this campaign」。

即 spec 说跳过、脚本不跳过。两条缺陷合起来指向同一个根因:
**渲染器不区分卡面受众。**

## 缺陷 3(已修,2026-08-02)— `specialization` 被丢弃

P6 第二轮把 schema 照真实车卡表重建后,技能条目多了 `specialization` 字段。
渲染器不认,伞技能全渲成光秃秃的家族名:同一张卡上出现两条
`Science 51%, Science 30%`,读卡的人无法知道哪条是工程学、哪条是物理。

**已直接修掉**,不进本计划的待讨论:这条与「卡面受众」正交
(玩家卡和守秘人卡都必须显示专精),修法只有一种,且改完当场跑通验证。
`render-investigator.py` 新增 `skill_label()`,`name` + `specialization` 合成显示。

## 缺陷 4 — 重建后的 schema 有一大批字段仍未渲染

P6 第二轮新增的字段里,除 `specialization` 外**全部**没有卡面出口:

| 字段 | 卡面价值 |
|---|---|
| `occupation_detail`(公式/信用区间/本职技能表/关系人) | 审卡要用;关系人是现成钩子源 |
| `age_modifiers` | 审卡要用(能否从骰值重算出最终属性) |
| `skill_points` 点数账本 | 审卡要用——**这是新验收口径的核心** |
| `credit_rating` 的生活水平/现金/资产/消费水平 | 桌面直接要查 |
| `gear`、`status`、`party`、`backstory_keys` | 桌面直接要查 |
| `experience_packages`、`mythos_encounters`、`growth_log` | 老练调查员与精英 NPC 要用 |

注意这些**大多不该进玩家卡**(点数账本、年龄补正是审卡视图,不是桌面视图),
所以缺陷 4 其实指向**第三种受众:审卡视图**——待讨论 1 的选项表原本只考虑了
「玩家 / 守秘人」两种。请 Keeper 一并考虑。

## 待讨论 1 — 卡面受众:一套模板还是两套?

pregen 卡是**玩家**拿的,elite-npc 卡是**守秘人**拿的。现在两者走同一个 `render()`,
输出完全相同的段落集合。缺陷 2 是这个设计的直接后果,缺陷 1 的修法也取决于它。

| 选项 | 优点 | 缺点 |
|---|---|---|
| A. 按 `type` 分支,一个脚本两套段落集 | 改动最小;真源仍是一份 schema;受众差异集中在一处可读 | `render()` 出现条件分支,模板文件与实际输出不再一一对应 |
| B. 拆两个模板文件(`investigator.md` / `elite-npc.md`),脚本按 type 选 | 模板即所见;守秘人段落(法术、notes、弱点)可自由扩张不污染玩家卡 | 两份模板要同步维护;`templates/` 文件数增加 |
| C. 不分受众,全渲染,靠 Keeper 自己删 | 零改动 | 违反 `core/13:41` 现有 spec;玩家卡可能带守秘人信息,是剧透风险 |

倾向 **A**(受众差异现在只有两三段,不值得拆文件),但若第四章的精英邪教徒后续还要加
「弱点/战斗战术/被识破后的反应」等纯守秘人栏,B 会更快变成正确答案——**请 Keeper 定**。

## 待讨论 2 — `notes` 该不该上卡面?

`notes` 是自由文本,schema 未限定用途。实际写进去的多半是守秘人备忘
(测试 fixture 里我写的是「他在第三场就已经知道调查员的名字」这类)。

- 若卡面**不渲染** `notes`:它就只是 JSON 里的注释,人看 JSON 才看得到
- 若**渲染**:必须只在守秘人视图渲(依赖待讨论 1 的结论)

顺带一问:kit 需不需要一个明确的「守秘人专用字段」约定(如统一前缀
`keeper_*`),而不是靠字段名个案判断?这会影响 schema 是否要改。

## 待讨论 3 — 渲染器要不要做 schema 校验?

现在 `render()` 全用 `.get()` 兜底,结构错的 JSON 会**安静渲出一张残卡**,
不报错。`core/11-review.md` 把 schema 校验放在人工审计清单里,所以这不算 bug,
但值得定个口径:

- 脚本只管渲染,校验归审计(现状)——好处是 stdlib only 的约束不破
- 脚本兼做校验——`jsonschema` 不在 stdlib,要么引依赖(破坏「仅 stdlib」的设计),
  要么手写必填字段检查(几十行,能覆盖 `required` 但覆盖不了类型/范围)

倾向维持现状 + 在脚本 docstring 里写明「不校验,校验见 `core/11`」,
但若第四章要批量生成 11 个原型,一个 `--check` 开关的价值会变高——**请 Keeper 定**。

## 需要先查清的事(执行前)

- [ ] `core/07-create-monster.md` 与 `core/06-create-npc.md` 的守秘人侧卡面
      有没有既成栏位惯例(法术/弱点怎么摆),避免 elite-npc 卡自成一格
- [ ] `reference/rules/` 是否已有法术表述格式(与 P7 魔法速查重叠,可能要等 P7)
- [ ] `dist/bundle.md` 是否收录了 `templates/investigator.md`——决定改模板后
      是否必须重跑 `scripts/build-bundle.sh`

## 影响与时机

**不阻塞 P6 收尾**:P6 的 pregen 基线不受这两条影响(调查员通常无法术、无 notes)。

**卡着 P1 第四章的卡面可用性**:第四章的精英邪教徒一旦落盘,渲出的卡就是缺法术的。
建议在第四章开工**前**至少定完待讨论 1,和 P4(反派强度预算)、P7(魔法速查)
一并作为第四章的前置。

## 讨论定案后再写执行清单

待讨论 1、2 定了再补 `- [ ]` 执行项。缺陷 1、2 本身无争议,只等修法形状。
