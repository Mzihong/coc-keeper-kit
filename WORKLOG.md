# WORKLOG — 给接手会话的上手速览

**这份文件的用途:让新对话不必重新摸一遍项目结构。** 开工前读这一份,而不是把
`core/`、`reference/`、`update_plan/` 挨个翻一遍。

和另外两份的分工:

| 文件 | 写给谁 | 内容 |
|---|---|---|
| `CHANGELOG.md` | **Keeper(用户)** | 每次改动后"你现在能做什么" |
| `WORKLOG.md`(本文件) | **接手的模型/协作者** | 结构在哪、约定是什么、现在卡在哪、上次做了什么 |
| `update_plan/README.md` | 两者 | 计划级状态索引与完结清单 |

> 本文件**手工维护**。改了结构、约定或计划状态就顺手更新这里;它过期比不存在更糟。
>
> **`会话记录`只保留未提交的工作。** 一旦对应改动 commit 落地,那条记录就该删掉——
> `git log`/`git show` 才是权威历史,不用在这里重复背一份。收尾流程见
> `core/15-close-session.md`("Prune before you add")。

---

## 一句话

CoC 7e 守秘人备课工作台。**所有指令都在 `core/`**,根目录三个 `*.md` 只是路由适配器。
`core/00-how-to-run.md` 是唯一入口——不确定任何事时读它,它压过一切。

## 结构速览

```
core/00 … 15        指令本体。00=入口/管线/路由/铁律/布局,02=规则查询(写数前必读)
                    01 intake · 03 world · 04 scenario · 05 clock · 06 npc · 07 monster
                    08 puzzle · 09 description · 10 handout · 11 review · 12 canon
                    13 investigator · 14 archive-reference(归档第三方资料)
                    15 close-session(收尾无计划文件的临时维护会话)
CLAUDE/GEMINI/AGENTS.md   三份薄适配器。改行为改 core,不改这三份;但三份必须彼此一致
.claude/skills/<name>/    Claude Code 技能壳,只有一句"读 core/NN"
templates/          每种产物的空壳。investigator 是 JSON schema + md 卡面双件
reference/          跨战役共享
  ├ rules/          kit 自己写的 7e 速查:**数字**
  ├ craft/          kit 自己写的手法提炼稿:**写法**
  ├ bestiary/ mythos/ tables/   原创可复用素材
  ├ decks/          官方卡组转录(第三方、带引用出处)
  ├ sourcebooks/    官方书籍全文转录(同上,体量更大)
      ↑ 上面五个原创目录进 bundle,下面两个第三方目录不进——通则见 reference/README.md
  ├ index.json      七个目录的反向索引 + 校验(脚本生成,各目录另有一份)
  ├ og_Norval/      洛夫克拉夫特全集 82 篇 → 提炼稿 craft/lovecraft-zh.md
  └ glossary-zh.md  中文术语锁,写中文必查(脊梁文件,故意留在根目录)
campaigns/          一战役一目录,_template-campaign/ 是模板
update_plan/        P1–P9 改动计划 + 完结清单;README.md 是状态索引
scripts/            build-bundle.sh · render-investigator.py · build-reference-index.py
dist/               构建产物,**已 gitignore**。要上传给 ChatGPT/Gemini 时现跑
                    build-bundle.sh 生成 bundle.md,不提交、不需要跟源文件同步
```

## 硬约定(踩了就是 bug)

1. **改行为改 `core/`,不改根适配器**;但 `CLAUDE.md`/`GEMINI.md`/`AGENTS.md` 三份必须一致,
   只存在于一份里的指令本身就是 bug。
2. **`dist/` 不入库,改完源文件不需要重建 bundle。** bundle 是上传前现跑的构建产物,
   不是要跟 `core/` 同步的仓库文件。**什么进 bundle 只有一条线——kit 自己写的进,
   第三方转录的不进**,理由与推论写在 `reference/README.md` → 什么进 bundle,
   别在各目录 README 里重述。
3. **每次改动在 `CHANGELOG.md` 追加**;同一天合并进同一条,不新开。
4. **文件名一律英文 ASCII `kebab-case.md`**,哪怕内容是中文。
5. **输出语言按战役声明**,kit 脚手架和文件名保持英文;写中文查 `reference/glossary-zh.md`。
6. **转载规则(2026-08-02 立,2026-08-03 二次放宽)**:官方资料**可以收录**进
   `reference/decks/`、`sourcebooks/`,文件末尾必须有 `## 引用出处` 表。
   **2026-08-03 改动**:原来那条"只取结构和数值刻度,不取文字"**已作废**——
   kit 自己的 `reference/` 文件**可以引用或转录官方规则内容**(属性行、法术耗费、
   武器伤害),标明是哪本书哪一章即可。过渡期边界(等 P9 定案):**数值随便转,
   描述性文字保持原创**。**进 `campaigns/` 的内容仍然自己写**——这条留下来了,
   但理由从"版权"改成"牌桌"(搬来的 NPC 是别人都知道底牌的人)。
   kit 的定位同时写实为:**面向持有正版的 KP、不盈利、不用于传播**。
   规则本体在 `core/00-how-to-run.md` → ground rules。
   **⚠️ 放宽只覆盖「规则内容」,不覆盖「虚构内容」。** 改完之后仓库里是三分法,别混:
   **① 规则内容**(数值、机制、法术耗费、武器伤害)→ 可转录,标出处;
   **② 虚构散文**(小说、战役文本、`reference/craft/` 的源材料、`external/` 的子模块)
   → 仍然**取手法不取文字**,`craft/README.md` 与 `reference/README.md` 已写明放宽不适用;
   **③ 具名角色 + 绑定商业产品**(如 `cultist-archetypes.md` 里那位"卡尔·斯坦福")
   → 仍不收录。
7. **归档件不进 bundle**(硬约定 2 的推论),所以任何 spec 引用它们都必须写成可选
   ("if present locally"),不得当前置依赖。

## 当前状态(2026-08-04)

计划 P1–P9 的权威状态在 `update_plan/README.md` 的状态索引表,**不要在这里读状态**,
只记几条容易漏的:

- **P1/P2/P3/P4/P6 均已归档**(P1 的阶段 0-2 与阶段 3 收尾两份计划都已进 `Archived/`)。
  2026-08-02 那批 16 个 commit(P1-P4 相关全部内容)与 2026-08-03 的收尾 commit
  均已提交,`git status` 干净。**不存在"待提交"的改动**——下一个会话不用再找
  scratchpad 或未提交的工作区改动。
- **P1 第四章的两个硬前置(P4、P7)现在都已解除,且 P7 本身也已完成**——新增
  `reference/rules/magic.md`,`core/02`/`core/07`/`reference/mythos/README.md` 已接线。
  P1 阶段 0-2 与阶段 3 收尾均已归档,该计划全部完结。
- **`reference/sourcebooks/keeper-rulebook-7e-zh.md`(规则书全文重译,17470 行)已确认
  可读**——P7 落盘时发现它比 grand-grimoire 更权威地给出了魔法书研读机制(CMI/CMF/MR
  三值、泛读/精读两阶段、重复精读耗时翻倍),`magic.md` 的魔法书章节改成从这份规则书
  抽样 20+ 本典籍算出的真实区间,而不是估算。之前"当前状态"没点名这份文件,接手时
  别漏看。
- **P8 投资者卡渲染缺口也已完成**——`scripts/render-investigator.py`/`templates/investigator.md`
  补全全部缺失字段,加了硬性算术+阈值型双层自校验;`core/13`/`character-creation.md`/
  `core/01`(新增问题 14)已接线。**P1–P8 现已全部完成并归档**。
- **P9(怪物强度标尺 + 索引层 + 神格铺设)三阶段已全部完成并归档(2026-08-04)**,
  见 `update_plan/Archived/README.md` 对应条目;计划文件本体在
  `update_plan/Archived/2026-08-02-monster-templates-traits.md`。
  - **阶段 A**(标尺与词条,2026-08-03):`reference/rules/monster-scale.md` + 五级强度阶梯 +
    `reference/tables/monster-traits.md` 的 18 条数值词条,`core/07` 的 X 已回填。
  - **阶段 B**(索引层,2026-08-03):扩了 `scripts/build-reference-index.py`,新增
    `parse_malleus_entries()`(从转录稿抽取全部 223 条的名称/tier/SAN/锚点)+
    `build_monster_index()`(合并 `reference/tables/monster-index-data.json` 里人写的
    223 条 `Serves`/摘要,再被匹配到的 `reference/bestiary/*.md` 条目覆盖),生成
    `reference/tables/monster-index.md`(进 bundle)。校验和缺引用出处同级——
    `Serves`/摘要留空就报错。现有 9 只 bestiary 条目已按新标尺重标,`cthulhu.md`
    补了反向的眷族/仆从小节,`core/07`/`core/04` 已接线检索入口。
  - **阶段 C**(神格铺设,2026-08-04):新增 5 个神格页(`reference/mythos/great-old-ones/`
    下的 `dagon-and-hydra.md`/`hastur.md`/`nyarlathotep.md`/`shub-niggurath.md`/
    `yog-sothoth.md`,体例照 `cthulhu.md`,均含「眷族与仆从」反链)+ 7 个新眷族/化身
    bestiary 条目(`deep-one.md`/`byakhee.md`/`spawn-of-hastur.md`/`hunting-horrors.md`/
    `black-pharaoh.md`/`dark-young.md`/`sons-of-yog-sothoth.md`)。执行时用 5 个并行
    subagent 分神格研究转录稿并起草——落地时发现并修正了 `mi_match_bestiary`
    (`build-reference-index.py`)的一处匹配盲区:算法要求英文标题里有 2 个以上 4 字母+
    单词才判定匹配转录稿原行,`Byakhee`/`Deep One` 这类短标题因此覆盖不到自己的转录稿行,
    曾在 `monster-index.md` 里产生重复行(同一生物一行来自转录稿脚手架、一行来自新写的
    bestiary 条目)。修法是把这两个文件的标题改成书本原名的完整形式(`Byakhee, the
    Star-Steeds` / `Deep One, Gilled Humanoid`)绕开阈值,没有改动共享的匹配算法本身——
    若以后再遇到同类短名字(如未来给"修格斯"单独立档),同一手法可以复用,也可以考虑
    把算法的阈值本身放宽,但那需要针对全部 223 条重新跑一遍回归检查,本轮范围内没做。
- **活动计划现在是三条:P5 + 新立的 P10、P11(2026-08-04)。** P10 = 阿卡姆资料提炼成
  `craft/town-anatomy-zh.md` 城镇解剖手法稿;**P11 = 年代开放**——目标是「KP 报哪个年代
  都能开团」这项能力,不是预挑几个年代建包:`reference/rules/eras/<era>.md` 只写与
  1920s 基准的差集(书里覆盖的全建)、战役声明式加载,**外加书里没覆盖的年代按差集写法
  现场推导的兜底路径**(路径 B,`core/01` 要当场告诉 KP 走的是哪条)。
  两份都**不是**"把资料原样收进来":P10 的源材料是虚构内容,受硬约定 6 的三分法 ②③ 管,
  只能取手法;P11 的源材料是规则内容,可转录标出处。**两个计划的阶段 0 都是"转换+勘察",
  不需要 Keeper 拍板就能动。**
- **P10 阶段 0 已完成(2026-08-04,未提交),复杂度降到三条计划里最低。** docx 已转
  `reference/_source/阿卡姆.md`;勘察结论(章节行号表、地点条目字段体例、门牌编号法则、
  文末 299 条 11 分类的反查名录)写进了计划的「勘察结果」一节。两条对接手会话有用的结论:
  **一是决定不切分**——该文档标题体系规整(`## <编号>` 首位即区号),按行号跳读比切文件
  便宜,`keeper-rulebook-7e-zh.md` 那笔"单文件只能 grep"的教训不适用;
  **二是提炼 §一只需读 9 段区导言,不必碰 300 个地点条目**——条目里具名 NPC 密度高,
  顺着通读必然漏进提炼稿。
- **P10 三个拍板问题同日全部定案,该计划现在零阻塞。** ①**全文不归档**——这条不是取舍,
  是 `core/00` 硬约定已经答了:2026-08-03 的转载放宽**只覆盖规则内容**,已出版的虚构内容
  仍归"取手法永不取文字";`sourcebooks/` 现有三份全是规则内容;
  别拿 `craft/lovecraft-zh.md` 当先例——`og_Norval/` 能全文入库是因为**洛夫克拉夫特是公版**,
  阿卡姆是 Chaosium 商业设定书。②**d20 机构表做**,单独立 `tables/town-institutions.md`。
  ③**文字地图卡 3 张,内容全部原创小镇**(镇级 2 张形状迥异 + 建筑级 1 张)。
  Keeper 对③提了「想规范化但不想定太死」,答法记在计划备忘:**地图卡不是多样性的来源**,
  多样性由掷骰产生,卡只是记法;风险不在"有没有格式"而在"格式里混进了内容"。
- **P10 同日又做了一次整份复评,拍板结论全部维持,执行层改了六处**(逐条见计划文末
  「复评记录」表)。接手时只需记三条改变了动作的:①**地图卡不新建文件**,格式扩进
  `reference/craft/diagram-conventions-zh.md` 当 **§六**——那份文件 §四 第 69 行已经在
  引用一个从未定义过的「文字地图卡」,§六 落地即还清,同时要改 §五 表格那行,
  否则建筑卡与该文件第 10 行的范围声明冲突;②**d20 机构表只收世俗 9 类**,神话典籍 33 +
  恐怖生物 5 那 38 条(12.7%)不是"镇上有什么"而是"藏在镇里的东西",混进同一张表会违反
  `core/03` 的 "Ordinary first, then the crack",这 12.7% 改去当提炼稿 §三 的料;
  ③**阶段 1 前面多了个 1.0 采料步**——9 段区导言其实还没读(阶段 0 明写"未通读全文"),
  且原 §三/§四 是在重复 `core/03` 已有的 Layered secrets 与 3–5 notable NPCs,已换定义。
- **新硬约定(2026-08-04,由上面那处悬空引用倒逼出来):`reference/craft/README.md`
  「写一份新的」第 5 步「术语自足」**——写 `craft/` 下的新文件时,**每个加粗术语落盘前
  确认仓库里有定义**,没有就当场定义或删掉那句,**不许指向 `update_plan/`**(计划文档不进
  bundle)。两类条目都管。**为什么需要它:`build-reference-index.py` 与完结清单查的都是
  文件级引用与孤儿,一个没有路径的裸名词对两者都不可见**,踩了照样报 no problems。
- **P11 阶段 0–2 已完成(2026-08-04,未提交)——年代开放从计划变成了实际能用的六个年代
  包。** 详见「会话记录」最新一条的文件清单;**阶段 3(`core/11` 年代串味审查)还没做**,
  是这条计划唯一剩下的工作,做完才满足归档条件。踩过一次坑值得记一笔:年代文件初稿
  写成了纯中文正文,后来对照 `character-creation.md`/`magic.md` 才发现 kit 的既有惯例
  是**英文正文 + 中文术语括注**,纯中文正文违反"kit 脚手架保持英文"——已重写六份,
  接手后续年代相关改动时留意这条,别重蹈同一个错。
- **`reference/_source/` = 第三方原件与抽出素材的本地存放处,整目录 gitignore,永不入库**
  (2026-08-04 建立)。现有 `阿卡姆.docx`(12 MB)、`阿卡姆.md`(该 docx 的转换稿,
  6723 行 / 14 万字符 / 0 图)、`克苏鲁时空穿梭6.pdf`(3.9 MB)、
  `arkham-maps/`(从**同一份 docx** 抽的 20 张地图,8.2 MB,P5 的视觉参照;
  md 与这些图同源,归档时算一个出处)。`.gitignore` 同时补了
  `*.docx`(此前只挡 `*.pdf`,那份 docx 一度是未跟踪状态,`git add .` 就会永久入库)。
  **要转录归档的走 `core/14-archive-reference.md`,入库的是 `.md` 文本不是原件。**
- **P5 三个待拍板问题已于 2026-08-04 全部定案,不再阻塞**:纯几何线框(不做仿手绘)、
  A 档先落地 / B 家具层可选 / **C 材质阴影与 D 手绘抖动完全否决**、且**拆成两个功能**
  ——功能一给 KP 的场景定位图(A 档,~400 token),功能二给 PL 的可互动场景图
  (A+B,约 3–5×,**必须 KP 主动要且生成前先告知成本**,还要过剧透审查出 player-safe 版)。
  否决理由写在计划的「已定案」一节,以后想重开 C/D 要先推翻那里的理由。
  **同日据阿卡姆地图样本又定了三件事**(样本在 `reference/_source/arkham-maps/`,
  Keeper 已筛到 20 张并按内容重命名):① 书里有**三种图**——城市图(斜视 + 编号圆圈)、
  室内平面图(正投影 + 粗实心黑墙 + **房间名写在房间里**)、站点/庄园图(自由轮廓 + 留白),
  阶段 1 的渲染要素逐条对着 `室内1/2/4` 定,**不是凭空写的**;② **不建图标库**
  ——`室内4`(密大图书馆)家具密度很高但全是几何图元 + 标签文字(书架=细长矩形、
  桌=圆),所以家具 DSL 用 `{s,x,y,w,h,label}` 而不是类型枚举,B 档少掉一半代码;
  ③ **室外站点图复用同一渲染器**(房间数组为空、只有图元层),只新增折线与指北针约 20 行,
  **不另造文字格式**——省的不只是代码,是不用再教模型第三种写法。
  **P5 阶段 0 是还债**:`templates/cult.md:42` 与 `reference/craft/cult-design-zh.md:68`
  两个进 bundle 的文件把 P5 计划文件当 mermaid 规范引用,但那份规范不存在,且
  `update_plan/` 不进 bundle——ChatGPT 链路的 KP 被指去查一份拿不到的空文件。
- **`reference/bestiary/` 现有条目的实测分布(P9 阶段 A 的主要依据,2026-08-03 复查时
  仅有 9 只)**:threat 当时 8/9 都是 `deadly`(`trivial`/`mythic` 从未用过),
  type 六类里 `beast`/`undead`/`great-old-one`/`human` 从未被单独用过。阶段 C 新增
  7 只之后 threat/type 分布已明显更均衡(见新条目自身 header),不必再假设"全是 deadly"。
- **古神级条目住在 `reference/mythos/great-old-ones/`(现有 6 份:`cthulhu.md` +
  阶段 C 新增的 5 份),不在 `bestiary/`。**
- **kit 的神格覆盖面(2026-08-04,阶段 C 完成后)**:除克苏鲁外,达贡与许德拉、哈斯塔、
  奈亚拉托提普、莎布-尼古拉斯、犹格-索托斯五位主要外神现在都有独立的 `great-old-ones/`
  页面与至少一只眷族/化身的完整 bestiary 条目。伊格等仍缺文件——kit 仍以克苏鲁系为主,
  但不再是"只有克苏鲁一个入口"。
- **`bestiary/` 与 `mythos/` 已于 2026-08-04 收进 bundle**(此前不收,是白名单漏项而非
  设计)。走 ChatGPT 链路的 KP 现在拿得到完整 stat block 与神格档案,不再只有
  `monster-index.md` 那一行摘要。仍然拿不到的是 223 条 malleus 转录稿本体——那是
  第三方资料,`monster-index.md` 就是它唯一的对外通道,这一条是设计如此。
- **三份 sourcebook 的手动重译已提交落地**(9c47d98);误建的空文件
  `reference/sourcebooks/新建 Text Document.txt` 已核实不存在(已清理或从未提交)。
  仍未清的账:P7 计划第 5 行的行数(写 13731,现为 5365)、`sourcebooks/index.json`
  的行数字段。malleus 头部的"转录质量"警示已随换稿重写,不再欠账;
  grand-grimoire/keeper-rulebook 两份头部警示仍未复核。

`update_plan/README.md` 末尾还有一张**按可动性排序的表**(哪个计划现在能动、卡在等谁),
接手时先看那张。

---

## 会话记录

### 2026-08-04 — `reference/tables/` 全目录转中文(未提交,无对应计划文件)

守秘人要在场次之间手动往骰表里续条目,中英混排会让新加的行一眼看出不是一批人写的。
**`reference/tables/` 从此是中文目录**,这条约定写进了 `reference/tables/README.md` 头部
和 `reference/README.md` 的 `tables/` 条目(与 `bestiary/` 那条「Written in **English**」
对仗——bestiary 跨语言战役共用,tables 由守秘人手工续写,取向相反)。

改写的七张表 + 一份 README(原先 CJK 占比 0%):`hooks.md`、`locations.md`、
`mythos-angles.md`、`npc-quirks.md`(四张种子表)、`complications.md`、`madness.md`、
`npc-appearance.md`、`README.md`。另外三处是残留英文的收尾:`monster-traits.md` 引言段、
`monster-index.md` 的标题/说明/表头(**这份是生成的,改的是
`scripts/build-reference-index.py` 的 `build_monster_index()` 里的字面量,不是文件本身**)、
以及 `monster-traits.md` 里一个繁体字「額」→「额」。目录里原本就是中文的六份没动
(`cult-goals`、`cult-leader-positions`、`cult-power-sources`、`cultist-archetypes`、
`monster-traits` 表体、`monster-index` 数据行)。

**刻意没改的一处:** `monster-index.md` 的分级标题仍是 `## L2 — creature (独立种族 /
传说生物)`。那四行是照抄 `reference/rules/monster-scale.md` 的分级名,`rules/` 目前整体
是英文;单方面改这边会让两份文件对不上号,要改得连 `monster-scale.md` 一起改。

**没有跨文件引用被打断:** 全仓库对这七张表的引用**全部是路径级**(`core/01`、`core/03`、
`core/06`、`reference/rules/sanity.md`、两份 deck README、战役文件里的「`complications.md`
2 号」这种编号引用),没有任何地方引的是表内英文原文,所以正文改写不牵连别处。`madness.md`
的一级标题从 `# Table — Bout of Madness (real-time)` 改成了 `# madness.md — 疯狂发作
(即时症状)`,与目录内其余文件的 `# 文件名 — 中文小标题` 惯例对齐。

改完跑了 `python scripts/build-reference-index.py`,`reference/index.json` 与
`reference/tables/index.json` 里的 `title`/`context` 字段已随之更新,`--check` 无问题。
`CHANGELOG.md` 补进了 2026-08-04 那条的「更新内容」(这条对 Keeper 有行为影响:现在可以
直接往表里加中文行)。

### 2026-08-04 — P10 整份复评 + 一条防悬空术语的新约定(未提交)

对 P10 做了一次整份复评。**三条拍板结论全部维持**,改的是执行层六处,逐条记在计划文末的
「复评记录」表里。**只有一个文件是 kit 内容改动**(`reference/craft/README.md`),其余全是
计划文档。

**最值得记的一条 —— 发现了一处新造的悬空引用,并补上了防复发约定:**

`reference/craft/diagram-conventions-zh.md:69`(**进 bundle**)写着「出这张图 + **文字地图卡**」,
但「文字地图卡」在仓库里**从未被定义过**——`git log -S"文字地图卡" --all` 为空,全仓库
只有 `update_plan/` 里有这个词。成因:P5 阶段 3(未做)那条 checkbox 的内容,在 P5 阶段 0
插队还债时被提前抄进了 §四。

**为什么既有检查网兜不住(这条最要记住):** 与 P5 阶段 0 还的那笔债是同一类 bug,只是降了
一级——那次是显式路径 `(update_plan/...)`,grep 得到、索引脚本查得出;这次是一个**裸名词**,
`build-reference-index.py` 与完结清单查的都是**文件级**引用与孤儿,**没有路径的术语对两者
都不可见**,当时 `--check` 照样报 no problems。

据此给 `reference/craft/README.md`「写一份新的」加了**第 5 步「术语自足」**(原五步变六步,
惯例规范那条路径三步变四步):**每个加粗术语落盘前确认仓库里有定义,没有就当场定义或删掉
那句,不许写「详见某某」指向 `update_plan/`。两类条目都管。**

改动文件:

- `reference/craft/README.md` — 新增第 5 步「术语自足」+ 头部两类条目说明里三步改四步
  (**本轮唯一的 kit 内容改动**)
- `update_plan/2026-08-04-town-anatomy-from-arkham.md` — 头部加复评标注;产物表地图卡行
  改落点;拍板结果 2 增复评修订 A/B(地图卡落 `diagram-conventions-zh.md` §六、建筑卡与
  §五 冲突);拍板结果 3 增复评修订 C(d20 表剔掉神话典籍 33 + 恐怖生物 5 共 38 条,
  20 行按世俗 261 条的配比分配);阶段 1 新增 §1.0 采料 + 复评修订 D(原 §三/§四 重复
  `core/03`,换定义);阶段 1.2 接线拆成两处;阶段 2 增三条(`tables/README.md` 登记、
  §四 第 69 行还债、§五 同步改);收尾补 `WORKLOG.md`;文末新增「复评记录」;
  **订正备忘里「21 张」→ 20 张**(与本文件第 61–62 行及本 WORKLOG 矛盾,是 33→20 那次
  订正的漏改)
- `update_plan/2026-08-02-low-cost-maps.md`(P5)— 阶段 3 降级路径改指 §六 并记下越界成因;
  **收尾第 1 条「重跑 bundle 且同 commit」划掉**——该硬约定 2026-08-04 已作废,这里是漏改残留
- `update_plan/README.md` — P10 状态行范围与说明、建议执行顺序第 5 条、复杂度表 P10 行、
  依赖图下方软耦合那段

**没记 `CHANGELOG.md`。** 唯一的 kit 改动是给维护者看的写作约定,对 Keeper 而言没有任何
行为变化;CHANGELOG 头部写明「只写**面向使用者**的变化」。同一判断上一条 P10 会话记录也用过。

**一条修正了估算的结论:** d20 机构表比原估贵。"分类学是现成的"只对 20 行中的 8 行成立
(小类各占 1 行),另 12 行要把 163 条「各行各业与专业人员」**重做一次子分类**——那 163 条
本身不是一类东西。P10 整体仍是 ★★,只是工作量从"地图卡新建文件"挪到了这里。

### 2026-08-04 — P10 阶段 0 勘察 + 三个拍板问题全部定案(未提交)

Keeper 把 `reference/_source/阿卡姆.docx` 转成了 `阿卡姆.md`,据此完成 P10 阶段 0
的勘察,并当场把三个待拍板问题全部定掉。**只改计划文档,没动 kit 内容**(故不记
CHANGELOG——对 Keeper 而言没有任何行为变化)。

改动文件:

- `update_plan/2026-08-04-town-anatomy-from-arkham.md` — 状态转「进行中(阶段 0 已完成)」;
  阶段 0 四条全部勾掉;新增「勘察结果」一节(§0 为什么不切分 / §1 章节—行号对照 /
  §2 地点条目字段体例 / §3 门牌编号法则 / §4 反查名录即机构分类学 / §5 表格清单);
  「待 Keeper 拍板」整节换成「拍板结果」;阶段 2 从"可选"转为必做并写死三条反模板化
  挡法;阶段 1 补一条防具名泄漏的读法约束
- `update_plan/README.md` — P10 状态行、依赖图节点、建议执行顺序第 3 条、复杂度表
  (P10 ★★★→★★ 并升到第一)
- `WORKLOG.md` — 本条 + 「当前状态」两处

三条值得记住的勘察结论:

1. **原计划的「按章切分」撤销。** 该约定的真实目的是"能跳读";这份文档标题体系规整
   (4 个 L1;名录条目一律 `## <编号>`,首位数字即区号),按行号跳读已经够用,
   切分只会在 gitignore 目录外多一份副本。
2. **提炼只需读 9 段区导言(约 10 段),不必碰 300 个地点条目。** 条目里具名 NPC 与
   具名机构密度很高,顺着通读必然把名字漏进提炼稿。
3. **文末 6424–6723 行的反查名录(299 条 / 11 个分类)是 d20 机构表的现成骨架**,
   也是一条独立手法(名录之外再挂按用途反查的索引层)。
4. **「归档全文」这个选项其实一开始就不存在**——写计划时以为是 Keeper 的取舍,核过
   `core/00` + `sourcebooks/README.md` 才发现硬约定已经答了。教训:**新立计划里凡是
   写着"要不要收进 `sourcebooks/`"的,先去核三分法,别默认它是可选项。**

核对过的数字:md 6723 行 / 140,640 字符 / 汉字 96,690 / 723 个标题 / 401 行表格 /
0 张图;`arkham-maps/` **20 张**(此前 WORKLOG 记的 33 张有误,已改),8.2 MB,
与 md 同源于那一份 docx。`git status` 确认 `_source/` 两份文件均未跟踪。

### 2026-08-04 — P11 阶段 0–2:年代包全建(未提交)

执行 `update_plan/README.md`「建议执行顺序」里排第一、二的两步:阶段 1(声明 1920s
基准)先做,再做阶段 0(转换勘察)+ 阶段 2(建包接线)。**阶段 3(review 串味审查)
不在本轮范围内,故意留着**。

**阶段 0 — 转换与勘察:**`reference/_source/克苏鲁时空穿梭6.pdf`(52 页,已在
`.gitignore` 内)用 `pdfplumber`(`uv run --with pdfplumber`,repo 本身没装这个包)
逐页转文本落到 scratchpad,按英文分章标题(`Cthulhu Invictus`/`Cthulhu Dark Age`/
`Mystic Iceland`/`Cthulhu Gaslight`/`Dreamlands`/`Cthulhu Icarus`/`Cthulhu End Times`)
定位七个设定的页码边界,只读目录与各章首页,勘察结果写进了计划文件新增的「勘察结果」
一节。**两个反直觉的发现**:「剑见箭 Swords and Arrows」不是独立年代,是给三个古代
设定共用的近战规则附录;「幻梦境 Dreamlands」也不是年代,是任何年代都能进入的平行
位面——两者都没建成年代文件,理由写在 `eras/README.md` 的索引表下面。

**阶段 1 — 声明基准:**`character-creation.md` 头部加了「本文是 1920s 基准」;
`chases.md` 的 Move 速率表(机动车/摩托车两行隐含机械时代假设)加了指向
`eras/README.md` 的提示;`combat.md` 抽查后确认不含武器表(战斗力学本身跨年代通用),
不需要改;`core/02-rules-reference.md` 补了「Default era: 1920s」段。

**阶段 2 — 建包与接线:**新增 `reference/rules/eras/`(README.md 五节差集体例 + 路径
A/B/C 判定表 + 六个年代文件:`cthulhu-invictus.md`/`dark-ages.md`/`mystic-iceland.md`/
`gaslight.md`/`icarus.md`/`end-times.md`,每条改动都标了原书页码出处)。`core/02`
登记了 `eras/README.md`;`core/01-intake.md` 问题 1 扩写成当场三路径判定,并要求
明说走的是哪条;`campaigns/_template-campaign/CLAUDE.md` 的 Era 字段从自由文本改成
固定 slug(对照 `eras/README.md` 索引);`reference/glossary-zh.md` 新增「年代包专属
术语」一节(20+ 词条)。`python scripts/build-reference-index.py --check` 报 no
problems(`reference/rules/index.json` 靠既有的 `list_md_files_recursive` 自动收录了
`eras/*.md`,不用改脚本)。

**踩过的坑:**六份年代文件初稿写成了纯中文正文,提交前对照
`character-creation.md`/`magic.md` 才发现违反 kit 既有惯例(英文正文 + 中文术语括注,
"来源"引用行例外保留中文)——已全部重写,以后再写 `reference/rules/` 下的文件先看一眼
同目录现有文件的语言体例,不要想当然按"这是给中文战役用的"就整篇写中文。

**决定不做的一件事:**没有把整本《克苏鲁时空穿梭6》转录进 `reference/sourcebooks/`——
六份年代文件已经把规则内容(技能/装备/职业/机制)转换完并标了页码,原书又是粉丝汉化
而非官方原文,没有必要另起一份整本转录,理由写在计划文件「收尾」一节。

CHANGELOG.md 已补进当天已有条目;WORKLOG「当前状态」已加一条 P11 进度摘要。commit
后需回填:`update_plan/2026-08-04-era-rule-packs.md` 状态表头、
`update_plan/README.md` 状态索引表的 P11 行。**阶段 3 做完前不满足归档条件**,
提交后这条记录先留着,别删。

### 2026-08-04 — bundle 收编 bestiary/mythos + `dist/` 退出版本控制(未提交)

起点是 Keeper 的一个质疑:「bundle 有必要么?reference 加不进去的话弱化好多」。查下来
前提不成立——`reference/` 本来就是 bundle 的主体(重建前 351,793 字符里占 205k),
真正被排除的是三类,理由各不相同,而**只有一类是没道理的**:

- `og_Norval/` + `sourcebooks/` 合计约 740 万字符 —— 塞不进去,也不该进(第三方)
- `decks/` —— 法律线:bundle 的用途就是上传给第三方,那正是不再分发规则挡的动作
- **`bestiary/` + `mythos/` —— kit 自己写的,却被白名单静默漏掉**,这次收编

**改动三件:**

1. **`build-bundle.sh` 收 `bestiary/` 与整个 `mythos/`**(含 `cults/`、`great-old-ones/`、
   `spells/` 三个子目录)。白名单同时全部改成 `<dir>/*.md` + `<dir>/*/*.md`,免得下次新建
   子目录又被静默漏掉——P9 和本次踩的是同一个坑。bundle 5400 行 / 60 文件 → **8423 行 /
   98 文件**(533,926 字符,+52%)。
2. **`dist/` 进 `.gitignore`,`git rm --cached dist/bundle.md`。** 之前 42 个 commit 里有
   16 个动了 bundle,每次都是 5000 行 diff 噪音。它是纯导出产物(没有任何 `core/` spec 读
   它),上传前现跑即可。由此**硬约定「必须重跑 bundle 且同 commit」整条作废**,已从
   三适配器、`core/14`、`core/15`、`update_plan/README.md` 完结清单、`craft/README.md`
   收尾步骤里删除。
3. **规则统一到一处**:`reference/README.md` 新增「什么进 `dist/bundle.md`」一节——
   一条线(kit 原创的进、第三方转录的不进)+ 理由(再分发,不是体量)+ 唯一要记的推论
   (指向不进 bundle 的目录一律写成可选)+ 正解(提炼层进 bundle、本体留本地)。
   各目录 README、`core/` spec、两个脚本注释里的重复表述**全部删掉改成指向它**,
   `decks/`/`sourcebooks/` 的两节「## 不进 bundle」压成一句话。

**顺带解掉的待拍板项**:P11 的「bundle 取舍待阶段 0 实测行数后定」不存在了——
`rules/eras/` 是原创目录,按通则整个自动进,脚本已经收得到。

`build-reference-index.py` 的 `ORIGINAL_IN_BUNDLE` 里 bestiary/mythos 改 True,
`--check` 报 no problems(66 文件 / 7 目录)。

### 2026-08-04 — 新立 P10 / P11 + P5 定案 + P5 阶段 0 落地(未提交)

**⚠️ 本轮动了 `core/`、`reference/`、`templates/`,bundle 与索引都已重跑**
(`dist/bundle.md` 5400 行 / 60 文件;`build-reference-index.py` 报 no problems)。
`CHANGELOG.md` 已在当天已有的 2026-08-04 条目下追加(更新内容 + 修复问题各一条)。
**commit hash 待提交后回填三处**:`CHANGELOG.md` 该条标题、P5 计划文件头、
`update_plan/README.md` 状态表。

**P5 阶段 0(还债)已完成** —— 新增 `reference/craft/diagram-conventions-zh.md`(87 行,
进 bundle):§一 通用规则 / §二 势力图 / §三 场景网 / §四 区域关系图 / §五 不该画图的情况。
`templates/cult.md` 与 `reference/craft/cult-design-zh.md` 两处指向不存在规范的引用已改;
`core/03`(Output)与 `core/04`(三线索规则 → 场景网,入边 < 3 即卡点)各接一行;
`reference/craft/README.md` 现在写明**本目录有两类条目**——提炼稿(受「取手法不取文字」管)
与惯例规范(kit 自订、无源材料),新写文件前先分清自己在写哪一类。

其余改动:

- 新建 `update_plan/2026-08-04-town-anatomy-from-arkham.md`(P10)、
  `update_plan/2026-08-04-era-rule-packs.md`(P11)
- 改写 `update_plan/2026-08-02-low-cost-maps.md`(P5):三个待拍板问题定案、拆两个功能、
  阶段 0 补 mermaid 还债
- `update_plan/README.md`:状态表 + 依赖图 + 执行顺序 + 复杂度表
- `.gitignore`:补 `*.docx` 与 `/reference/_source/`
- 文件移动(**都在 gitignore 内,git 看不到**):`reference/阿卡姆.docx` 与
  `reference/rules/克苏鲁时空穿梭6.pdf` → `reference/_source/`;新增
  `reference/_source/arkham-maps/`(33 张)

提交后删掉这条记录。

---

以上之外没有其他会话记录——其余改动全部已提交(见 `git log`)。P9 阶段 A+B 的落地细节
(索引脚本怎么解析转录稿、踩过的名称解析坑、9 只 bestiary 条目的改判理由)已随
commit 059ba63 落地,理由本身也直接写在了改动的文件里(各 bestiary 条目的 header、
脚本的函数注释),不在这里重复背一份——要看当时怎么想的,`git show 059ba63` 或翻
对应文件即可。开一段新的维护会话、做了还没提交的改动时,在这里加一条(格式参考
`core/15-close-session.md`);一旦对应 commit 落地,收尾时把这条记录删掉,不留存档。
