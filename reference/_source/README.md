# `_source/` — 第三方原件与从中抽出的素材

**这个目录不是归档区,是料场。** 归档区是 `decks/` 与 `sourcebooks/`,进那两个目录的文件
按 `core/14-archive-reference.md` 走完整流程(命名、头部块、`## 引用出处`、接线、重跑索引)。
放在这里的东西还没走那套流程,可能永远也不会走——它们是**给计划当料的原始素材**。

## 入库边界(2026-08-04 改)

原先整个目录 gitignore,「永不入库」。**现在改成:原件不入库,从原件抽出的文本与图入库。**

| | 入库? | 是什么 |
|---|---|---|
| `.pdf` / `.docx` 原件 | ❌ 本地 | 体量大、是别人的成品文件本身;由根 `.gitignore` 的 `*.pdf` `*.docx` 两条挡住 |
| 转出的 `.md` 文本 | ✅ 入库 | 计划真正读的那一份 |
| 抽出的图 | ✅ 入库 | 同上,P5 的渲染要素逐张对着它们定 |

**改这条的理由是可复现,不是版权松动。** 计划(P5、P10)明写「渲染要素照 `interior-1/2/4`
的体例」「§一 提炼自 9 段区导言」——料不在库里,fresh clone 出来这些计划就无法复核,
只能相信当初那个会话的记忆。规则书与 malleus 转录稿早就是入库的,同一个道理。

## ⚠️ 入库 ≠ 可以转录它的文字

**`core/00-how-to-run.md` → ground rules 的三分法一个字没动。** 尤其第 ②
类(虚构散文)在本目录里占多数:

- **`arkham-zh.md` 是 Chaosium 商业设定书的中译,归 ② 虚构散文** —— kit 写东西时
  **只取手法,永不取文字**,更不许进 `campaigns/`。P10 的产出是
  `reference/craft/town-anatomy-zh.md`(kit 自己的话),不是把这份文本搬过去。
- 地图同理:P5 拿它们定**记法**(正投影、粗实心黑墙、房间名写在房间里),
  不是拿来复制内容。

这个目录**变成了「拿得到」,没变成「可以抄」。** 那是两条正交的线——前者管
clone 下来有没有,后者管 kit 的产出里能出现什么。`reference/README.md` → 原创 vs 第三方
是后者的权威表述。

## 现存内容

| 文件 | 出自 | 用途 |
|---|---|---|
| `arkham-zh.md`(6723 行 / 14 万字符 / 0 图) | `阿卡姆.docx` 转换 | P10 城镇解剖提炼稿的源材料 |
| `arkham-maps/`(20 张,8.2 MB) | **同一份** `阿卡姆.docx` 抽出 | P5 低成本地图的渲染参照 |
| `阿卡姆.docx`(12 MB,本地) | Keeper 提供 | 上面两项的共同原件;归档时算**一个**出处 |
| `克苏鲁时空穿梭6.pdf`(3.9 MB / 52 页,本地) | Keeper 提供 | 已提炼成 `reference/rules/eras/` 六个年代包(P11) |

两份原件保留原中文名:它们不入库,ASCII 文件名那条硬约定管的是仓库里的文件。

### `arkham-maps/` 命名对照

Keeper 当初按内容起的中文名已按硬约定改为 ASCII。**P5 计划里按编号引用的那几张就是下表**:

| 现名 | 原名 | 图种 |
|---|---|---|
| `city-neighborhoods-and-trolley-1928.jpeg` | `Akam_ca_1928_neibourhood_trolley` | 城市图 |
| `district-campus-east/-west.jpeg` | `Campus_校园东/西` | 城市图 |
| `district-downtown.jpeg` | `Downtown_中心区` | 城市图 |
| `district-east-town.png` | `East_Town_东区` | 城市图 |
| `district-french-hill-south.jpeg` | `French_Hill_法兰西山区南` | 城市图 |
| `district-merchant-east.png` / `-west.jpeg` | `Merchant_District_商业区东/西` | 城市图 |
| `district-northside.jpeg` | `Northside_北区` | 城市图 |
| `district-rivertown.jpeg` | `River_town_河区` | 城市图 |
| `district-uptown.jpeg` | `uptown_富人区` | 城市图 |
| `region-lovecraft-country.jpeg` | `lovecraft_country_洛夫克拉夫特乡村地区` | 城市图(区域尺度) |
| `region-outskirts.jpeg` | `郊区地图` | 城市图(区域尺度) |
| `interior-1/2/3/4.jpeg` | `室内1/2/3/4`(**4 = 密大图书馆**) | 室内平面图 |
| `exterior-1/2.jpeg` | `室外1/2` | 站点/庄园图 |
| `site-crowninshield-manor.jpeg` | `克罗因谢尔德老庄园` | 站点/庄园图 |

三种图种的渲染差异见 `update_plan/2026-08-02-low-cost-maps.md` 的勘察表。

## 索引脚本怎么看这个目录

`scripts/build-reference-index.py` 的 `ARCHIVE_DIRS` / `ORIGINAL_DIRS` **都不含
`_source/`**,所以这里的文件不需要各自的 `## 引用出处` 块,也不会因为没人引用而被判孤儿。
出处集中记在本文件下方一节。要把某份料**正式收录**(让 spec 直接依赖、进反向索引),
那是另一件事:走 `core/14-archive-reference.md`,搬进 `sourcebooks/` 或 `decks/`。

## 引用出处

| 字段 | 值 |
|---|---|
| 作品 | 《阿卡姆》/ *Arkham*(城市设定书);《克苏鲁时空穿梭》/ *Cthulhu Through the Ages*(设定合集) |
| 版权方 | Chaosium Inc. |
| 版本 | 《克苏鲁的呼唤》第七版(CoC 7e) |
| 本文来源 | Keeper 提供的中译电子件。*Arkham*:**未署译者名,译本出处不详**;*Cthulhu Through the Ages*:七宫涟个人汉化第 6 版 |
| 收录范围 | *Arkham*:全文转换稿(docx → md,0 图)+ 从同一 docx 抽出的 20 张地图。*Cthulhu Through the Ages*:仅本地 PDF,不入库 |
| 收录用途 | P10(`craft/town-anatomy-zh.md` 的源材料)、P5(地图记法参照)。**均为「读它、写自己的」,不作转录来源** |
| 已知问题 | docx → md 转换稿丢失全部图片(图另行抽出);段落编号与原书页码不对应,不要按它引页 |

本 kit 不主张对上述作品的任何权利,与 Chaosium Inc. 无隶属关系。收录件在此是为了让
**已持有正版的 KP** 备课更快,非商业、不用于传播。版权方可提 issue,任何文件即刻撤下。
