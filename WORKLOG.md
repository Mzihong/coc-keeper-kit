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
      ↑ 上面五个是 kit 原创,下面两个是第三方转录——通则见 reference/README.md
  ├ index.json      七个目录的反向索引 + 校验(脚本生成,各目录另有一份)
  ├ og_Norval/      洛夫克拉夫特全集 82 篇 → 提炼稿 craft/lovecraft-zh.md
  └ glossary-zh.md  中文术语锁,写中文必查(脊梁文件,故意留在根目录)
campaigns/          一战役一目录,_template-campaign/ 是模板
update_plan/        P1–P14 改动计划 + 完结清单;README.md 是状态索引
scripts/            render-investigator.py · build-reference-index.py
```

**没有构建产物,也没有构建步骤。** kit 由能读文件的 agent 就地读取(Claude Code /
codex / gemini CLI),`dist/bundle.md` 那条单文件上传链路已于 2026-08-04 退役(P13)。

## 硬约定(踩了就是 bug)

1. **改行为改 `core/`,不改根适配器**;但 `CLAUDE.md`/`GEMINI.md`/`AGENTS.md` 三份必须一致,
   只存在于一份里的指令本身就是 bug。
2. **每次改动在 `CHANGELOG.md` 追加**;同一天合并进同一条,不新开。
3. **文件名一律英文 ASCII `kebab-case.md`**,哪怕内容是中文。
4. **输出语言按战役声明**,kit 脚手架和文件名保持英文;写中文查 `reference/glossary-zh.md`。
5. **转载规则(2026-08-02 立,2026-08-03 二次放宽,2026-08-06 P12 三次改边界)**:
   官方资料**可以收录**进 `reference/decks/`、`sourcebooks/`,文件末尾必须有
   `## 引用出处` 表。**2026-08-06 改动(P12)**:边界从"数值 vs 描述性文字"改成
   **"规则条文 vs 虚构散文"**——kit 自己的 `reference/` 文件可以引用或转录官方**规则
   条文本身的措辞**,不再局限于数值(属性行、法术耗费、武器伤害,以及定义险境/判定
   流程的整句话都可以直接引用),标明是哪本书哪一章(或节)即可;这条不再是"等 P9
   定案"的过渡期状态,P9 早已完成,现在是永久边界。**进 `campaigns/` 的内容仍然自己
   写**——这条留下来了,理由是"牌桌"(搬来的 NPC 是别人都知道底牌的人),不是版权。
   kit 的定位同时写实为:**面向持有正版的 KP、不盈利、不用于传播**。
   规则本体在 `core/00-how-to-run.md` → ground rules。
   **⚠️ 放宽只覆盖「规则条文」,不覆盖「虚构内容」。** 改完之后仓库里是三分法,别混:
   **① 规则条文**(数值、机制、条文措辞)→ 可转录,标出处;
   **② 虚构散文**(小说、战役文本、`reference/craft/` 的源材料、`external/` 的子模块)
   → 仍然**取手法不取文字**,`craft/README.md` 与 `reference/README.md` 已写明放宽不适用;
   **③ 具名角色 + 绑定商业产品**(如 `cultist-archetypes.md` 里那位"卡尔·斯坦福")
   → 仍不收录。
   **这条线管的是「能不能搬进 `campaigns/`」,不是「能不能读」**——归档件就在仓库里,
   spec 可以直接读、直接依赖(2026-08-04 P13 改)。**唯一真正拿不到的是 `.pdf`/`.docx`
   原件本身**,指向原件的引用仍写成可选;`reference/_source/` 自 2026-08-04 晚起
   **不再整目录 gitignore**(见下面「`_source/` 的入库边界」一条)。

## 当前状态(2026-08-04)

各计划的权威状态在 `update_plan/README.md` 的状态索引表,**不要在这里读状态**,
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
    `reference/tables/monster-index.md`。校验和缺引用出处同级——
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
- **P13(bundle 退役)已完成并归档(2026-08-04)。** 这条改的是 kit 的分发形态,接手时
  必须知道三件事:①**没有构建步骤了**——`scripts/build-bundle.sh` 与 `dist/` 已删,
  `.gitignore` 的 `/dist/` 一行也删了;②**硬约定重新编号**,旧 2(什么进 bundle)与
  旧 7(归档件不进 bundle)整条删除,原 3–6 上移成 2–5,**按号引用时先数一遍**;
  ③**归档件可以被 spec 直接依赖了**——全仓 10 处 `if present locally` / `local only`
  已回收,现在仍写成可选的只有指向 `.pdf`/`.docx` **原件**的引用。
  计划文件与执行记录在 `update_plan/Archived/2026-08-04-retire-bundle.md`。
  ~~**一处留给 P12 的坑**:P12 阶段 1.2 要 `git rm --cached` 规则书,那之后
  `keeper-rulebook-7e-zh.md` 又变成本地若有~~ —— **这个坑 2026-08-04 晚随 P12 已定案 ②
  被撤回而消失**:规则书不再脱离跟踪,没有任何 hedge 需要加回去。
- **P12(速查表自足化)阶段 1.0–1.2 已于 2026-08-06 落地(接手时须知)**:
  `keeper-rulebook-7e-zh.md` 已**退出查询链路,但仍在版本库里**——`core/02-rules-reference.md`
  不再说它是"最后一句话",改成"本地若有可对账,不是拿来读的";`reference/rules/*`、
  `reference/tables/*` 现在直接对着它写,每节标行号锚点方便本地核对。仓库里指它查具体规则的
  8 处引用(`magic.md`、`artifacts-zh.md`、`call-father-dagon-and-mother-hydra.md`、
  `cultist-archetypes.md`、`sourcebooks/README.md` 等)已改指对应速查表。**转载规则的边界
  同时改了**:从「数值 vs 描述性文字」改成「规则条文 vs 虚构散文」——规则条文(含条文
  本身的措辞)可直接引用/转录,虚构散文仍然只取手法不取文字,`core/00-how-to-run.md`
  → ground rules 与三份适配器已同步。
- **P12 阶段 2(其余四份速查表)已于 2026-08-06 完成,接手时须知三件事**:
  ①`skill-checks.md`/`character-creation.md`/`magic.md`/`monster-scale.md` 四份现在都
  对着规则书第三/四/五/九/十一/十二/十四章逐节核过,不再是阶段 1 之前那种"部分内容
  未核"的状态;`character-creation.md` 的技能基础值表逐条核对第四章原文全部通过,新增
  了官方六套替代建卡法;`magic.md` 补了施法检定/孤注一掷失败代价表/成为相信者/深层
  魔法这几块此前完全没有的机制;`monster-scale.md` 新增了第十四章的通用怪物框架(体格
  比较表、怪物战斗与战技规则、不死的神格、人类打得过哪些神话生物),原有的五级阶梯
  (抽样自 malleus)不变。
  ②**语言体例统一成中文正文**——这四份此前是英文正文(kit 其余脚手架的既有惯例),
  现在按阶段 1 定的新体例(中文正文 + 英文术语括注)改写,`reference/rules/` 全目录
  现在体例一致,不再是"三份中文、四份英文"的混搭。**这条连带改了 `character-
  creation.md`**——它是 P11 六个年代包的 1920s 基准本,换语言前先扫过 `eras/` 六份
  差集确认没有硬编码的英文小节标题依赖(五节体例本身是通用的,不受基准本语言影响),
  `eras/` 六份年代包与其 `README.md` 同批翻译成中文,保持整个目录体例一致。
  ③**`character-creation.md` 内部小节编号改动时刻意避开了 §11**——新增的"创建调查员
  其它方法"一节没有插在中间,而是追加成新的 §12,因为 `core/`(`06-create-npc.md`、
  `07-create-monster.md`、`11-review.md`、`02-rules-reference.md`、`01-intake.md`)、
  `campaigns/_template-campaign/CLAUDE.md`、`reference/tables/cultist-archetypes.md`、
  `reference/tables/weapons-index.md`、`reference/rules/monster-scale.md` 等多处活文件
  都硬编码引用着"`character-creation.md` §11 = 人类反派基线"——插在中间会让这些引用
  全部指错地方。**以后再动这份文件的小节顺序,先 grep 一遍 `character-creation\.md.*§`
  确认没有撞车,再动手**,这个坑本身也值得记一笔。
- **2026-08-04 当时活动计划是三条:P5 + 新立的 P10、P11。**(P11 已于 2026-08-05
  完成并归档,见上面单独一条;这里保留是当天决策背景。)P10 = 阿卡姆资料提炼成
  `craft/town-anatomy-zh.md` 城镇解剖手法稿;**P11 = 年代开放**——目标是「KP 报哪个年代
  都能开团」这项能力,不是预挑几个年代建包:`reference/rules/eras/<era>.md` 只写与
  1920s 基准的差集(书里覆盖的全建)、战役声明式加载,**外加书里没覆盖的年代按差集写法
  现场推导的兜底路径**(路径 B,`core/01` 要当场告诉 KP 走的是哪条)。
  两份都**不是**"把资料原样收进来":P10 的源材料是虚构内容,受硬约定 5 的三分法 ②③ 管,
  只能取手法;P11 的源材料是规则内容,可转录标出处。**两个计划的阶段 0 都是"转换+勘察",
  不需要 Keeper 拍板就能动。**
- **P10 阶段 0 已完成(2026-08-04,13821ac),复杂度降到三条计划里最低。** docx 已转
  `reference/_source/arkham-zh.md`(同日晚入库时由 `阿卡姆.md` 改名);勘察结论
  (章节行号表、地点条目字段体例、门牌编号法则、
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
  确认仓库里有定义**,没有就当场定义或删掉那句,**不许指向 `update_plan/`**(计划完结后
  会移进 `Archived/`,链接当场就烂)。两类条目都管。**为什么需要它:`build-reference-index.py` 与完结清单查的都是
  文件级引用与孤儿,一个没有路径的裸名词对两者都不可见**,踩了照样报 no problems。
- **P11(年代开放)已全部完成并归档(13821ac 阶段 0–2 + 2026-08-05 阶段 2b/3,
  3f937f6)**,见 `update_plan/Archived/README.md`。年代开放从计划变成了实际能用的
  六个年代包,加上 Era 字段的解析算法(未声明/`1920s` → 基准;匹配 `eras/README.md`
  索引 → 路径 A;不匹配但 `campaigns/<slug>/rules-era.md` 存在 → 路径 B;都不是 →
  路径 C)——**这份算法权威在 `core/02-rules-reference.md`,不在 `eras/README.md`**,
  后者与 `_template-campaign/CLAUDE.md` 只复述,这一条同时解掉了 P15 问题 7(路径 C
  无合法值、A/B 的 slug-vs-路径不一致)。`core/13` 不再绕过加载顺序,busybodies 卡组
  非 1920s 限定已加,`core/11` 有了年代串味审查项。踩过一次坑值得记一笔:年代文件初稿
  写成了纯中文正文,后来对照 `character-creation.md`/`magic.md` 才发现 kit 的既有惯例
  是**英文正文 + 中文术语括注**,纯中文正文违反"kit 脚手架保持英文"——已重写六份,
  接手后续年代相关改动时留意这条,别重蹈同一个错。
- **P14 于 2026-08-04 换过一次方向,文件名也换了**:原
  `2026-08-04-tables-d20-to-d100.md`(随机表 d20 → d100,约 390 条)已整份重写为
  [`2026-08-04-scenario-diversity.md`](update_plan/2026-08-04-scenario-diversity.md)。
  **推翻理由是原前提不成立**:四张种子表已是 20⁴ = 16 万种组合,"空间被 20 条封顶"是假的;
  它真正想治的"摸熟"是**采样问题**——模型口头报点数不均匀。Keeper 因此追加一条硬要求:
  **掷骰必须走 `scripts/roll.py`,不许模型自己决定点数**。新方案 = 脚本(不放回 + 跨战役
  查重 + 表行数自检)+ 两张缺表(对抗场面 / 模组形状)+ `locations` 接到场景级,扩容降为
  条件执行。**副作用:`tables/README.md`「宁可 20 条具体的」那句约定不再需要推翻,原样保留。**
  接手时注意本条记的是**方向**,`update_plan/README.md` 才是状态权威。
- **P14 阶段 1(`scripts/roll.py` 本体 + 硬约定接线)已于 2026-08-05 随 148bb91 落地**。
  两处偏离计划字面描述,接手时留意:①不放回/`--fresh` 用集合差实现,不是计划原文写的
  "重掷循环"——效果等价,池子精确报告耗尽而不是假装重试 20 次;②在计划清单之外加了
  `--check-all`(全表自检,不掷骰)和 `--spec`(标注哪个 spec 在掷)两个参数。想看当时
  怎么想的,`git show 148bb91` 或翻 `scripts/roll.py` 的文件头注释。
- **P14 阶段 2(种子表口径 bug + locations 接到场景级)已于 2026-08-07 完成,待提交**
  ——见下面「会话记录」。两张缺表(对抗场面/模组形状,阶段 3–4)与条件执行的扩容
  (阶段 5)仍没做。
- **P15(`core/` 复查勘误)已于 2026-08-07 全部完成并提交(阶段 0 `11f90b0`,阶段 1-3
  `86f1335`),归档见 `update_plan/Archived/2026-08-04-core-spec-audit.md`。** Keeper 拍板
  两个待定点:神格页读路径**两者都做**(扩 `monster-index.md` + 四处直接读路径),L5
  模板**新建** `templates/great-old-one.md`。`build_monster_index()` 新增
  `parse_great_old_one_pages()`——Cthulhu/Nyarlathotep/Yog-Sothoth/Shub-Niggurath 在
  malleus 转录稿里要么是旧式散文格式、要么根本没有战斗数值,原解析器读不出来,新表直接
  从六份神格页的 `Index summary` 字段生成一节「神格详注」。`core/11` 补了两条镜像审查项
  (puzzle 提示阶梯、event clock 双分支)并把入边审查从"至少一个场景"升级成"每个必达
  场景 ≥3 条入边"。阶段 3 的六项制度动作(完结清单加反向扫描第 8 项、`update_plan/`
  引用禁令作用域扩到 `core/`+`templates/`+`reference/`、孤儿检查区分条目/目录孤儿、
  `core/14`→`core/15` 补原创内容接线要求、`core/15` 加 First/Output/Quality bar 三处对齐
  步骤、`render-investigator.py --strict` 只让 errors 中止)全部落地。**顺带修了一处同类
  死链**:`scripts/build-reference-index.py` 两处指着 P9 计划文件的旧路径(该文件已归档到
  `Archived/`),已改成点名 `Archived/` 下的实际路径。**未处理的同类发现**:扫描时还看到
  `reference/rules/character-creation.md`、`reference/sourcebooks/keeper-rulebook-7e-zh.md`、
  `reference/sourcebooks/grand-grimoire-zh.md`、`reference/bestiary/README.md` 各一处
  同样指着已归档计划的旧路径,不在本计划范围内,留给下一个计划处理。
- **P16(线索引擎 + 三线索检验)已于 2026-08-07 全部完成并提交(`86f1335`),归档见
  `update_plan/Archived/2026-08-04-clue-engines.md`。**
  新表 `reference/tables/clue-engines.md`(d10,十条各带一条别的引擎给不了的结构属性,
  表头写死"一次只掷 2–3 条,不许全开")已接 `roll.py` 并通过 `--check-all` 自检;
  `cult-power-sources.md` 与它双向互指(造物→工艺与制造、受赐力量→身体代价默认通电)。
  `cult-design-zh.md` §四 改口径为"财源是十台里写得最细的一台",§五 的"平淡才合理"
  指回引擎 7(制度摩擦,**不是**原计划草稿设想的引擎 8/10——阶段 0 查重后更正)。
  `core/04` 第 5 步加六条检验(表格形式,压到 22 行,守住判据 B 的 25 行阈值);
  `templates/scenario.md` 的线索地图表改成"一条线索一行"以容纳新增的门槛类型/保质期
  两列,而不是把原表撑成 9 列宽表。`core/05` 加了"卡关够久→反派动手,那个动作本身是
  线索"的 trigger;`core/11` 的三线索审查换成三项追溯(正向查幽灵线索、今夜察觉测试查
  独立性、保质期查易腐)。`core/11` 三方撞车(本计划阶段 4 / P11 阶段 3 / P15 阶段 2)
  按 P11→P15→P16 顺序做完,无冲突。详见 `update_plan/Archived/2026-08-04-clue-engines.md`。
- **P10(城镇解剖手法稿)已于 2026-08-07 全部完成并提交,归档见
  `update_plan/Archived/2026-08-04-town-anatomy-from-arkham.md`。**
  新增 `reference/craft/town-anatomy-zh.md`(92 行,四节:§一 城镇部件清单——地势/建筑
  年代与样式/族裔与阶层/经济角色四维,从 9 段区导言实读出的公约数,非凭空设计;§二 地点
  条目字段体例含门牌编号法则;§三 神话层怎么不留标记地混进世俗名录——禁书类条目挂靠在
  私宅书房、大学/公共图书馆、旧书店、公寓房客私藏、神秘学社团这些**完全世俗的地点类型**
  上,反查索引也不给它们单独归类,是可执行的写法约束不是态度;§四 地点密度分三档,实测
  103/104/116 所在区段 25 条样本比例约 4:13:8,NPC 集中在密度最高的一档,不是均匀撒的)。
  `core/03-build-world.md` 的 town/locale 路径接线两处(读提炼稿哪几节 + 建镇时掷
  `town-institutions.md`,后者的调用**不并入** "First, orient" 的首次建世界掷骰行,
  是每次建镇都掷的独立指令)。
  新增 `reference/tables/town-institutions.md`(1d20,原创抽象,名字全部自拟):
  勘察阶段发现反查名录里「各行各业与专业人员」163 条占世俗层六成,分类学本身免费但这
  163 条要重新子分类才有用——已拆成 12 个互不重叠的行当(法律文书/医疗心理/治安阴影/
  学术文墨/传统匠人/店铺经纪/技术建筑/艺文表演/另类边缘知识/公职行政/日常服务/运输
  劳力),占表的 1–12 行;其余八个世俗机构类别(餐饮娱乐/旅馆公寓/教堂/俱乐部与组织/
  工厂与商业设施/杂项/殡葬墓地/医疗机构)各占一行,13–20。**神话典籍与恐怖生物两类
  (38 条/12.7%)被剔除在外**——那是「藏在镇里的东西」不是「镇上有什么」,混进同一张表
  会违反 `core/03` 的 "Ordinary first, then the crack"。落地时直接写成
  `python scripts/roll.py town-institutions ...` 最终措辞并通过 `--check-all` 自检,
  没有给 `P14` 阶段 1.2 留下待补的掷骰点措辞。
  `reference/craft/diagram-conventions-zh.md` 新增 §六 文字地图卡(无渲染器环境的兜底
  格式,跑不了 `scripts/render-map.py` 时用),3 个原创样例:4 区海港镇「黑鸥湾」+ 2 区
  矿村「铁哨谷」(故意做成不同规模,防止被当模板抄)+ 建筑级「县立档案馆」(房间/连通/
  出入口)。顺带还清该文件 §四 第 69 行一处从未被定义过的裸名词「文字地图卡」(与 P5
  阶段 0 还的是同一类债),并改 §五 表格行避免建筑卡与「建筑内部布局不归本文件管」那句
  范围声明冲突。**P5 阶段 3(降级路径)2026-08-07 已拍板砍掉不做**(见下一条),
  §六 因此不再有"P5 阶段 3 待读"这层期待,现在就是最终态,不必再跨计划指路。**
- **P5 阶段 1(功能一:场景定位图 A 档)与阶段 3 的取舍已于 2026-08-07 一并定案,
  `090cd3c`,详情见 `update_plan/2026-08-02-low-cost-maps.md`(计划仍在跑,
  阶段 2/2b 待执行,未整份归档)。**
  **阶段 3 拍板结果:砍掉,不做。** 理由是 `core/00-how-to-run.md` 现在写死"kit 由有
  文件系统的 agent 就地读……没有构建步骤,也没有单文件导出"(P13 退役 bundle 后的措辞),
  全文再没有任何地方提"ChatGPT 网页链路"——那个使用场景已经不存在。这同时回答了 P10
  修订 B 的存废理由:`diagram-conventions-zh.md` §六 建筑卡不追溯撤销(它现在是"跑不了
  `render-map.py` 时的通用兜底格式",不依赖 ChatGPT 链路是否存在),但不必再为它扩展内容。
  **阶段 1 落地:** 新增 `scripts/render-map.py`(stdlib、纯确定性,同一份 DSL 渲染两次
  输出字节完全一致)。DSL 定型为「房间数组 `{id,name,x,y,w,h,doors[],windows[]}`,门窗按
  `edge`(top/right/bottom/left)+ `pos`(0–1 分数)定位,不用绝对坐标」——共享墙靠两个
  房间的边**端点完全重合**去重(不是邻近匹配),重合则判定内墙(细线),否则外墙(粗线),
  这条约束写进了脚本文档字符串,模型写 DSL 时要让相邻房间的墙边完全对齐。门画成 "∧" 折线
  楔子(3 点 polyline,不是 SVG 弧线);窗是外墙外侧的短虚线段;楼梯是矩形 + 等距斜线阴影
  + 方向箭头;圆形房间(塔楼)直接画 `<circle>`,不接入矩形墙体系统;引线标注(`callouts`)
  支持 `secret` 字段(斜体渲染),但**阶段 1 不做过滤**——`--player` 开关是阶段 2 的活。
  **验证方式:** 原定用已删除的 `beidaihe-winter` 战役样本,Keeper 拍板改成临时 scratchpad
  (100% 原创两层楼样本「灰烬庄园」,验证完即弃、不入库、不进 `campaigns/`)。模型没有
  可视化能力,验收分两层:逐元素核对渲染出的 SVG 坐标与预期几何是否吻合(墙粗细分类、
  门缺口区间、窗位置全部用算式核对,不是目测);再发布成 Artifact 页面请 Keeper 目测确认
  视觉可读性,**Keeper 确认「达标,按此定稿」**。事后又对照
  `reference/_source/arkham-maps/interior-1.jpeg` 复核一遍,渲染要素基本吻合,**唯一没有
  复刻的是原图部分内墙用的"撕纸边缘"锯齿线**——判定属于 C/D 档已否决的手绘感装饰,
  不追加。`templates/location.md`/`templates/scene.md` 新增可选 Map 小节(内嵌 DSL JSON
  示例);`core/03-build-world.md`/`core/09-description.md` 各加一条:仅当室内布局本身
  影响判定(连通、视线)时才附图,大多数地点/场景不需要。**一份 DSL = 一层楼**,多层
  建筑写多份文件、在 location.md 里按楼层顺序连续放多个 Map 小节——"纵向堆叠"发生在
  文档阅读顺序,不要求渲染器把多层拼进同一张 SVG。
- **`reference/_source/` = 第三方**料场**(2026-08-04 建立)。入库边界当日晚被 Keeper
  改过一次,接手时按新的记:** ~~整目录 gitignore,永不入库~~ →
  **原件(`.pdf`/`.docx`)不入库,从原件转出的 `.md` 与抽出的图入库。**
  Keeper 原话:「可以 gitignore pdf,但是 md 一定要有」,担心的是 **fresh clone 出来的
  kit 是残的**。目录 README 在 `reference/_source/README.md`,细则以它为准。

  | 现有内容 | 入库? |
  |---|---|
  | `arkham-zh.md`(6723 行 / 14 万字符 / 0 图;原名 `阿卡姆.md`) | ✅ |
  | `arkham-maps/`(从**同一份 docx** 抽的 20 张,8.2 MB,P5 的视觉参照) | ✅ |
  | `阿卡姆.docx`(12 MB,上面两项的共同原件,归档时算**一个**出处) | ❌ 本地 |
  | `克苏鲁时空穿梭6.pdf`(3.9 MB,已提炼成 `rules/eras/` 六个年代包) | ❌ 本地 |

  **入库的 5 份文件名同批 ASCII 化**(硬约定 3;此前全仓 `git ls-files` 非 ASCII 文件名
  为 0,这批是第一个会破例的)——地图改成 `district-*` / `region-*` / `city-*` /
  `interior-1..4` / `exterior-1..2` / `site-crowninshield-manor`,**新旧对照表在目录
  README 里**。两份不入库的原件保留原中文名。

  **⚠️ 拿得到 ≠ 可以抄。** 这次动的是**分发面**,不是转载边界:`core/00` 的三分法
  一个字没改,`arkham-zh.md` 仍是第 ② 类虚构散文,**取手法永不取文字**;
  它也**不是归档件**(没走 `core/14`、没有自己的 `## 引用出处`、不进反向索引,
  `build-reference-index.py` 的 `ARCHIVE_DIRS`/`ORIGINAL_DIRS` 都不含 `_source/`)。
  要正式收录仍走 `core/14-archive-reference.md` 搬进 `sourcebooks/`/`decks/`。
  `.gitignore` 里 `*.docx` 那条(2026-08-04 补,此前只挡 `*.pdf`)保留——正是它在挡原件。
- **P5 三个待拍板问题已于 2026-08-04 全部定案,不再阻塞**:纯几何线框(不做仿手绘)、
  A 档先落地 / B 家具层可选 / **C 材质阴影与 D 手绘抖动完全否决**、且**拆成两个功能**
  ——功能一给 KP 的场景定位图(A 档,~400 token),功能二给 PL 的可互动场景图
  (A+B,约 3–5×,**必须 KP 主动要且生成前先告知成本**,还要过剧透审查出 player-safe 版)。
  否决理由写在计划的「已定案」一节,以后想重开 C/D 要先推翻那里的理由。
  **同日据阿卡姆地图样本又定了三件事**(样本在 `reference/_source/arkham-maps/`,
  Keeper 已筛到 20 张并按内容重命名,**当日晚入库并改成 ASCII 名**):① 书里有**三种图**
  ——城市图(斜视 + 编号圆圈)、
  室内平面图(正投影 + 粗实心黑墙 + **房间名写在房间里**)、站点/庄园图(自由轮廓 + 留白),
  阶段 1 的渲染要素逐条对着 `interior-1/2/4` 定,**不是凭空写的**;② **不建图标库**
  ——`interior-4`(密大图书馆)家具密度很高但全是几何图元 + 标签文字(书架=细长矩形、
  桌=圆),所以家具 DSL 用 `{s,x,y,w,h,label}` 而不是类型枚举,B 档少掉一半代码;
  ③ **室外站点图复用同一渲染器**(房间数组为空、只有图元层),只新增折线与指北针约 20 行,
  **不另造文字格式**——省的不只是代码,是不用再教模型第三种写法。
  **P5 阶段 0 是还债**:`templates/cult.md:42` 与 `reference/craft/cult-design-zh.md:68`
  两个生产文件把 P5 计划文件当 mermaid 规范引用,但那份规范不存在,而且计划完结后会
  移进 `Archived/`,链接当场就烂。
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
- **`monster-index.md` 与 malleus 转录稿的关系已不再是「对外通道」。** P13 之后所有
  归档件都在仓库里、spec 可以直接读,索引的作用回归本职:**223 条几百万字符的书没人
  每次整份读**,索引是那份体量的检索层,不是分发替代品。
- **三份 sourcebook 的手动重译已提交落地**(9c47d98);误建的空文件
  `reference/sourcebooks/新建 Text Document.txt` 已核实不存在(已清理或从未提交)。
  仍未清的账:P7 计划第 5 行的行数(写 13731,现为 5365)、`sourcebooks/index.json`
  的行数字段。malleus 头部的"转录质量"警示已随换稿重写,不再欠账;
  grand-grimoire/keeper-rulebook 两份头部警示仍未复核。

- **intake 现在有一条硬门禁:问完就停,Keeper 回复前不建任何文件(95dfdf2)。** 起因是
  Keeper 用 codex 测「创建新团」,模型一题没问就开建。**根因不在路由,在 `core/01-intake.md`
  的写法**:全文只有一句要求提问,而「never require an answer」「you will decide it well」、
  整节 Auto-fill + 默认值表、以及 Quality bar 那句「answered as few as zero questions and
  still has a complete campaign」四处合起来把零提问描述成合格结果,唯一的硬停还在写完文件
  之后。同一条 non-negotiable 已同步进三份适配器——**这一层才是关键**,codex 只自动加载
  适配器,不保证会打开 spec。**还没确认的一件事**:codex 当时到底读没读 `core/01-intake.md`。
  若它压根没打开 `core/` 任何文件,那是另一种病(工作目录:codex 只加载 cwd 及祖先的
  `AGENTS.md`,从 `Git Repositories/` 根起会话则本仓库的 `AGENTS.md` 不进上下文),
  95dfdf2 治不了,得先问 Keeper 的启动目录。

`update_plan/README.md` 末尾还有一张**按可动性排序的表**(哪个计划现在能动、卡在等谁),
接手时先看那张。

---

## 会话记录

本节只留**未提交**的工作;P12(速查表自足化,含阶段 0–2 与两次复审)已随 `c368b90`
提交并归档到 `update_plan/Archived/2026-08-04-cheatsheet-self-sufficiency.md`,原本记在
这里的三条会话记录已按 `core/15-close-session.md` 的 "Prune before you add" 删除——
细节要么已经折进上面"当前状态"里 P12 那条摘要,要么直接 `git show c368b90` 看。

- **2026-08-07:P14 阶段 2,未提交。** 改了五个文件:①`reference/tables/README.md`
  种子表节四张改成 hooks/locations/mythos-angles/complications(原来错写
  `npc-quirks.md`),`npc-quirks.md` 挪去「备课与临场表」节紧邻 `npc-appearance.md`,
  `complications.md` 从该节并入种子表节;②`core/04-design-scenario.md` 第 6 步新增
  一句:场景需要的地点若 `world/` 里没有,当场跑 `python scripts/roll.py locations
  --campaign <slug>`;③`reference/tables/locations.md` 说明行补上指向 `core/04` 第 6
  步的交叉引用;④`update_plan/2026-08-04-scenario-diversity.md` 阶段 2 两项打勾;
  ⑤`update_plan/README.md` 状态表 P14 行同步、`CHANGELOG.md` 补进当天(2026-08-07)
  条目。**没做**:提交、commit hash 回填(状态表与计划文件头当前写"待提交",等 Keeper
  决定要不要提交)。
- **同日:P14 阶段 3,未提交。** 新增 `reference/tables/confrontation-grounds.md`
  (d20,对抗场面成立的条件)。格式没照单格长句写,仿照 `clue-engines.md` 的多列结构
  (`场地 | 地形与限制 | 场上能用的 | 结束于`)——`roll.py` 的表格解析本就支持任意列数
  按 `— ` 拼接输出,四维分列比塞一句话里更好读也更好维护,已通过 `--check-all` 与
  `--seed` 抽样验证。接线三处:`core/04-design-scenario.md` 第 6 步(物理对抗掷这张表,
  与 `chases.md` 划清"选材 vs 机制"边界)、第 7 步(怪物的 fair out 接到掷出的结束
  条件上)、`core/09-description.md`(Mode A 场景描写照掷出的地形/可用物写);
  `reference/tables/README.md` 表清单加一行。自检结果:20 条里 2 条(卷筒机印刷厂、
  钢架施工楼顶)预设工业化年代,0 条挑国家,比例不影响可用性,不砍。`update_plan/
  2026-08-04-scenario-diversity.md` 阶段 3 全部打勾、`update_plan/README.md` 状态表、
  `CHANGELOG.md` 同步补进当天条目。**没做**:提交。
- **同一会话,同日:`update_plan/README.md` 瘦身,242 行降到约 150 行,未提交。**
  「依赖图」一节此前塞了近 70 行已归档计划(P9–P16)的历史耦合说明,「建议执行顺序」
  一节尾部也挂着同类已完成条目的详细复述——两者都和 `Archived/README.md` 重复,那份
  文件才是归档计划的权威详情记录。删法:依赖图只留活跃计划(P5/P14)的图 + 一行指路;
  「建议执行顺序」尾部同理压成一行指路;「复杂度排序」尾部三条纯指针的删除线条目
  (P10/P15/P16)直接删,`Archived/README.md` 本来就有。**唯一一条不是纯历史、被顺手
  搬家而不是删除的**:P16 落地时给 `core/04` 第 5 步留下的 clue-engines 掷骰点措辞债
  (原来挂在依赖图 P16 节),挪进了 `2026-08-04-scenario-diversity.md` 阶段 2 末尾,
  因为它是 P14 还没还的活账,不是已归档计划的历史。**新增一条执行守则**(本文件
  `update_plan/README.md` 内)防复发:依赖边解决/阶段完成时只删不留说明段落,细节权威
  在 `Archived/README.md` 或对应计划文件自己的 `- [ ]`。**没做**:提交。

---

其余已提交条目已按 `core/15-close-session.md` 的 "Prune before you add" 删除:
P13(bundle 退役)随 7f85d9b 落地,「默认舞台改为美国」随 d481713 落地,
P14 阶段 1(`scripts/roll.py`)随 148bb91 落地,`_source/` 入库边界改判随 9666499 落地
(该条此前漏剪,已清掉),P11 阶段 2b + 阶段 3(年代开放收尾)随 3f937f6 落地——
偏离计划字面描述的实现细节已经折进「当前状态」那条摘要,不在这里重复背一份。

同理,P9 阶段 A+B 的落地细节(索引脚本怎么解析转录稿、踩过的名称解析坑、9 只 bestiary
条目的改判理由)已随 commit 059ba63 落地,理由本身也直接写在了改动的文件里(各 bestiary
条目的 header、脚本的函数注释),不在这里重复背一份——要看当时怎么想的,
`git show 059ba63` 或翻对应文件即可。

开一段新的维护会话、做了还没提交的改动时,在这里加一条(格式参考
`core/15-close-session.md`);一旦对应 commit 落地,收尾时把这条记录删掉,不留存档。
