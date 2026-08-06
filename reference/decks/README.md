# decks/ — 官方卡组收录(第三方资料)

这里放**官方出版的卡组/资料的转录件**,给生成器当取材源和数值标尺用。

和 `reference/` 其他目录不同,**这里的内容不是本 kit 写的,也不算 kit 的 canon**。
`bestiary/`、`mythos/`、`tables/` 是原创可复用素材;`decks/` 是别人的东西,我们只是引用。

整本书的转录件不放这儿,放 [`../sourcebooks/`](../sourcebooks/README.md) —— 同一套规则,
体量和用法不同:卡组是现成条目、随取随用,书是深查。

## 现有条目

| 文件 | 卡组 | 内容 | 谁在用 |
|---|---|---|---|
| `busybodies-zh.md` | 好事者 *Busybodies* | 47 张 1920 年代 NPC 卡,含属性、技能、武器、完整背景字段和**一个秘密** | `core/06-create-npc.md`、`core/13-create-investigator.md`、`reference/tables/npc-quirks.md` |
| `phobias-and-manias-zh.md` | 恐惧症 *Phobias* | 47 张疯狂结果卡:即时症状 9、总结症状 6、恐惧症 16、躁狂症 16 | `core/02-rules-reference.md`、`core/13-create-investigator.md` |
| `miseries-zh.md` | 惨事 *Miseries* | 现成的「当场出事」事件卡,含空白卡 | `core/04-design-scenario.md`、`reference/tables/complications.md` |
| `weapons-and-artifacts-zh.md` | 武器与造物 *Weapons & Artifacts* | 武器/造物速查:技能、成功率、伤害、射程、故障值、年代 | `core/06-create-npc.md`、`core/13-create-investigator.md`、`core/10-create-handout.md` |

这张表是人读的;机器读的版本是 `index.json`,由 `scripts/build-reference-index.py` 生成。

## 引用标注规则(强制)

收录任何官方资料进本仓库,文件**末尾必须有一节 `## 引用出处`**,以表格给出:

| 字段 | 说明 |
|---|---|
| 作品 | 中英文全名 |
| 版权方 | 出版方(如 Chaosium Inc.) |
| 版本 | 规则版本 / 年代设定 |
| 本文来源 | 从哪来的——PDF 转录、译本、社群整理;译者不详就写「不详」,**不要编** |
| 收录范围 | 全文转录 / 节选 / 摘要改写 |
| 收录用途 | 哪个 spec 会读它、读来干什么 |

外加一句不主张权利、与版权方无隶属关系的声明。**没有这一节的收录件不许进仓库。**

来源写不清楚的,宁可不收:标注的意义是可追溯,不是免责咒语。

## 反向索引

`index.json` 是本目录的机器可读索引,由 `scripts/build-reference-index.py` 从各文件的
`## 引用出处` 表 + 全仓库反查生成,**不要手改**。它回答两个方向的问题:

- **正向**:这个目录里有什么、每份的出处与已知问题(`entries[].provenance` / `known_issues`)。
- **反向**:某份资料**被谁引用**(`entries[].referenced_by`,精确到文件与行号)——
  删档或换版本前先看这里,知道会打断哪些 spec。

跨目录的完整索引链在 `reference/index.json`。

## 生成器怎么用

**规则内容可以照取,人物必须自己写。** 卡组的价值在于:一个「古董商」该有多少 EDU、一个
「狂热者」的恐吓开在几点、一条「秘密」写多长才可用——这些**数值与条文本身**都能直接
取用,在 kit 自己的 `reference/` 文件里引用或转录也可以(边界是**规则条文 vs 虚构
散文**,不是"数值 vs 描述性文字"——见 `core/00-how-to-run.md` → ground rules),
标明出处就行。

**但人名、背景故事、具体秘密不能搬进 `campaigns/`。** 这条不是版权顾虑,是**牌桌顾虑**:
搬来的 NPC 是每个用同一套卡组的 KP 都已经知道底牌的人,而"生成一个只属于这一桌的人"
正是这个 kit 存在的理由。

- `core/06-create-npc.md` —— 建 NPC 前查一遍同职业的卡,校准数值刻度与技能选取。
- `core/13-create-investigator.md` —— 预生成卡 / 替补调查员的现成骨架。

本目录是第三方资料(通则见 [`../README.md`](../README.md) → 原创 vs 第三方),但**就在仓库里**
——spec 可以直接读、直接依赖。那条线管的是**能不能搬进 `campaigns/`**,不是能不能读。
