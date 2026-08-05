# Update Plan — `core/` 复查:失效陈述、孤儿内容与缺失的镜像

> 日期:2026-08-04
> 状态:待执行(**两个拍板点未定**,见「待拍板」;阶段 0 不需要拍板就能动)
> 来源:Keeper 要求复查 `core/` 是否有设计不合理或 bug(2026-08-04 会话)。
> 逐条核对了 16 份 spec 的全部路径引用、跨文件一致性,以及它们对仓库实际状态的断言。
> **同日按跨计划复评瘦身一次**:原阶段 0 的一半并进 P12,原阶段 3 整块并进 P11,
> 见下方「已并出去的部分」。
> 范围:主体在 `core/`;溢出到 `.gitmodules`、`scripts/render-investigator.py`、
> `update_plan/README.md` 的完结清单、`reference/craft/README.md` 的作用域各一处。

## 这份计划要治什么

**九条问题,但只有三种病。** 逐条修完不解决复发——每一类都要配一项制度动作,
否则下一个计划完结时会再犯一遍同样的错。三类病写在「根因」一节,
每条问题的具体成因写在自己的条目里。

**本计划最该留下的产物是阶段 3 的三条制度动作,不是那几处勘误。**

## 已并出去的部分(2026-08-04 瘦身)

初稿有五个阶段。跨计划复评发现其中两块与既有计划改的是同一处文字,
**并出去比并行改安全**——两边各改一次必然打架:

| 原属本计划 | 并到哪 | 为什么 |
|---|---|---|
| 问题 2 的**语义半边**(`core/00:103` 那句「数值随便转,描述性文字保持原创」是失效的临时规则) | **P12 阶段 1.0** | P12 阶段 1.0 已经明写要把这句「整句删掉」,并把边界改成「规则条文 vs 虚构散文」。同一句话,P12 的动作是超集 |
| 问题 7(路径 C 的 Era 字段无合法值、A/B 的 slug-vs-路径不一致) | **P11 阶段 2b** | 与 2b 第三条「路径 B 有写无读」是**同一条缝**:三条路径定在 `eras/README.md`,字段合法值定在 `_template-campaign/CLAUDE.md`,两份各定义了一半。建议把 2b 第三条扩成「Era 字段的定义收口到一处」,一次修完 |

**本计划保留的是问题 2 的另一半**:那句话同时还带一个指向
`update_plan/2026-08-02-monster-templates-traits.md` 的**死链**(P9 已归档,文件已移进
`Archived/`)。死链不在 P12 的视野里,留在阶段 0。

---

## 问题清单(按严重度)

### 1. `core/07:14-15` 的断言在 P13 之后已经不成立

> it is the **only** channel a Keeper without the repo has into the 223 malleus entries
> — the transcript itself never ships. `reference/bestiary/` does ship...

`git ls-files reference/sourcebooks/` 确认 `malleus-monstrorum-zh.md` 在版本控制里;
bundle 退役后也不存在"没有仓库的 Keeper"。索引的定位应回到本职:
**223 条几百万字符的检索层**,不是分发替代品(`WORKLOG.md` 第 228 行已经这么写了)。

**为什么会漏**:P13 的扫尾动作被定义成「回收 hedge」,查的是两个具体字符串
(`if present locally` / `local only`),grep 找得到。但这句话不是 hedge,是**反向断言**
——它表达的是同一个前提的另一面,任何针对 hedge 措辞的 grep 都匹配不到它。
**根因是扫尾用字符串模式,而失效的是语义。**

**这一处不是孤例。** 同一批未清账至少还有三处(见阶段 0 的 P13 余波扫描):
`core/00:107`、**P5 阶段 3** 整节假设存在一条"无文件系统的 ChatGPT 网页链路"、
**P10 复评修订 A 的第一条理由**同样建立在"不进 bundle 等于目标用户拿不到"之上。
后两处在计划文件里,不改生产文件,但会误导执行——**P5 阶段 3 的存废影响 P10 建筑卡
那张的存废理由**,值得一次扫完再决定。

### 2. `core/00:103` 的死链(语义半边已并入 P12)

```
*Interim boundary, until P9 lands* (`update_plan/2026-08-02-monster-templates-traits.md`):
```

P9 已于 2026-08-04 完结归档,文件移进了 `Archived/`——**链接当场就烂了**。
而 `core/00` 是「压过一切」的那份文件。

**为什么会漏**:两层。
① 完结清单第 1 项「状态同步(两处)」指的是**计划文件自身 + README 索引表**,
   并不包含"这个计划在生产文件里留下的临时标记"。P9 完结时两处状态都同步了,
   清单判 pass,`core/00` 那句 `until P9 lands` 从头到尾不在清单视野内。
② 2026-08-04 因为同类悬空引用新立的约定(「不许指向 `update_plan/`」)
   只写进了 `reference/craft/README.md`,**作用域是 `craft/`**,没覆盖 `core/`
   ——而 `core/00` 早在那条约定之前就已经犯了,新约定不会回头抓存量。
**根因是完结清单缺一项反向扫描**:本计划的编号/文件名/"待 PN 定案"字样
还出现在哪些生产文件里。

### 3. `reference/external/` 不存在,两份 spec 指着它

- `core/00:107` —— "`reference/craft/` 和 `reference/external/` say so directly",
  后半句无从验证(那个目录没有 README,因为没有那个目录)。
- `core/14:38` —— 分类表把「第三方 git repo」**整类**路由到那里。

实测:目录不存在;`git ls-files -s | grep 160000` 无 gitlink;`git submodule status` 空;
但 `.gitmodules` 里 `reference/external/coc-zh` 那段还在。**子模块被摘掉了,
`.gitmodules` 没清,`core/` 也没跟着改。**

**为什么会漏**:`external/` 是 `reference/` 下**唯一不在索引脚本视野里的目录**
——`build-reference-index.py` 的 `ORIGINAL_DIRS` 和归档目录列表都不含它
(它装的是 git 子模块,不是 `.md`),`ORPHAN_IS_ERROR` 里也没有它的键。
于是删掉它不会让任何检查变红。**根因是:唯一没有自动覆盖的目录,恰好是唯一被删的目录**,
再加上删除动作没有配套的"谁还指着它"回扫。

### 4. 六份神格页是「只写不读」的孤儿目录 —— 最值得处理的一条

`reference/mythos/great-old-ones/`(`cthulhu.md` + P9 阶段 C 2026-08-04 新增 5 份)
在整个 `core/` 里只被提到**一次**:`core/07:34`,作为**归档去向**。
**没有任何 spec 说要去读它。**

而「该用哪个神话生物」的官方入口(`core/07:9-14`、`core/04` 步骤 7)是
`reference/tables/monster-index.md`,那份索引由 `build-reference-index.py` 从
malleus 转录稿 + `reference/bestiary/` 生成——grep 确认**零条 `great-old-ones` 行**。
`core/01` 问题 9(定威胁)、`core/03`(神话暗流)、`core/04` 步骤 1(真相)
三个最该读神格页的地方,一个都没接线。

**为什么会漏**:三道防线同时失效,而且各自都"有道理"。
① **P9 阶段 C 的验收标准是 `reference/` 内部自洽**——建了几份页面、
   神格页 ↔ bestiary 条目的反链是否成对。这个标准在 `reference/` 里完全闭合,
   但**没有一项要求 `core/` 里出现一条读路径**。
② **`core/14` 步骤 5「Wire it in」明确判定"没人指的归档件 = failure"**,
   但那份 spec 开篇就把自己限定为**第三方资料**:「Material the kit writes itself
   (cheat-sheets, bestiary entries, roll tables) does not come through here.」
   于是 **kit 原创内容反而没有接线要求**——最该有的那条规则,被作用域挡在门外。
③ **唯一能自动兜底的孤儿检查对 `mythos` 关掉了**
   (`ORPHAN_IS_ERROR["mythos"] = False`)。豁免理由写得清楚且合理:
   "内容库,大部分条目本来就没有 spec 引用"。但豁免是**按目录**给的,
   于是「目录里某一条没被引用」和「整个目录没有读路径」变成同一件事,
   前者的正当豁免掩护了后者。
一句话:**接线要求只写给第三方资料,原创内容靠自觉;
唯一的自动检查按目录豁免,粒度不足以区分「条目孤儿」和「目录孤儿」。**

### 5. L5 既没有模板,`core/07` 的 Output 段还和自己的归档规则打架

- `core/07:40` 无条件说 "Use `templates/monster.md`";
- 但 `core/07:34-36` 说神格页是 lore-shaped、不是 stat card,
  而 `templates/` 下**没有这个形状的模板**(现有 6 份照 `cthulhu.md` 抄,
  这件事只记在 `WORKLOG.md` 里,不在任何 spec 里);
- 更糟:`core/07` 的 **Output 段**写「Reusable, campaign-neutral →
  `reference/bestiary/<name>.md`」,**没有 L5 例外**。
  只读 Output 段的模型会把神格写进 `bestiary/`。

**为什么会漏**:`core/07` 是增量长出来的。先有"所有怪物一个模板"的世界,
P9 阶段 A 插入五级标尺,阶段 C 再插入"L5 归档到 `mythos/`"。
**两次插入都改在文件前部的 First 段**,而 Output 段在文件末尾、
语义上属于另一个话题("存哪"),没人回头对齐。
**根因是同一件事在一份 spec 里成文两次**——`core/` 每份 spec 都有
First / Output / Quality bar 三处可能重复同一条约束,改动只落在离改动点近的那处。

### 6. `core/11` 审不了 `core/04` 最严的那条要求

`core/04` 步骤 5 要求每个「必须到达」的场景 **≥3 条入边**
(与 `reference/craft/diagram-conventions-zh.md:58` 一致)。
`core/11` 的 Craft 清单只查「**至少有一个**场景可以按**多于一种**顺序到达」
——两个维度都松一档(一个 vs 每个必达场景;2 条 vs 3 条)。
同一份 `core/04` 里步骤 6 又只说 "most scenes ... more than one order",
**三处严格度互不相同**。`core/11` 存在的全部理由是审别的模型的产出,
结果生成侧最硬的一条没有审查侧对应项。

**为什么会漏**:`core/11` 的这条清单项**写在 `core/04` 引入入边规则之前**,
它对应的是步骤 6 那条旧的、松的要求。后来把入边规则写进
`diagram-conventions-zh.md` 并接到 `core/04` 时,**接线只做了生成侧单向**。
**根因是「新增一条生成要求」没有配套动作「在 `core/11` 加一条镜像审查项」**
——`core/11` 的定位要求它是所有 blocking/craft 规则的镜像,
但没有任何流程强制这个镜像关系,完结清单里也没有这一项。

### 7.(已并入 P11 阶段 2b)路径 C 的 Era 字段没有合法值

`core/01` 定义了三条路径:A(写 slug)/ B(写 `campaigns/<slug>/rules-era.md` **路径**)/
C(只留机械骨架)。但 `campaigns/_template-campaign/CLAUDE.md:25` 只枚举了
baseline / 六个 slug / 一个 path-B slug,还写着
"`core/02` 逐字读这个字段,请保持为 slug"——**路径 C 无法表达**;
A/B 之间也已经不一致(core/01 说写路径,模板说保持 slug)。

**为什么会漏**:三条路径定在 `reference/rules/eras/README.md`(负责「怎么推导」),
字段合法值定在 `_template-campaign/CLAUDE.md`(负责「怎么填」)。
**两份文件各自定义了同一个字段的一部分,没有一份定义完整**,路径 C 正好掉在缝里。

**→ 交给 P11 阶段 2b**,与那里的「路径 B 有写无读」是同一条缝,
建议把 2b 第三条扩成「Era 字段的定义收口到一处」。
**收口位置建议 `core/02`,不是 `eras/README.md`**——按硬约定「改行为改 `core/`」,
加载顺序与字段语义的权威该在 spec 里,reference 复述。
(2b 现在写的是反的:逻辑放 `eras/README.md`,`core/02` 只"同步补一句"。)

### 8. `--strict` 会在一个自称误报的检查上硬失败(溢出到 `scripts/`)

`core/13:83` 说 `--strict` 把 any violation 变成 hard failure;
`scripts/render-investigator.py:518` 是 `if (errors or warnings) and strict: sys.exit(1)`。
而属性区间那条 warning **自己的文案**就是
`(fine if point-buy or an aged/scaled NPC)`。于是一个按
`reference/rules/character-creation.md` §2 正常扣完年龄惩罚、
STR/APP 掉到 15 以下的老年调查员,在 `--strict` 下会被一条已知误报判死。

**为什么会漏**:`validate()` 分了 errors/warnings 两档,分档标准是
**"确定性 vs 可能有正当例外"**;`--strict` 的实现却是 `errors or warnings`,
**把刚分好的档又合并了**。根因是两套正交语义被当成了一套:
分档说的是「哪些可能误报」,`--strict` 说的是「把什么升级为失败」。
`core/13` 的文档**忠实地描述了实现**("any violation"),
所以文档审查也发现不了——**文档和代码一致地错**。

### 9. `core/00` 的 Layout 树漏项

缺 `reference/_source/`、`og_Norval/`、`mythos/spells/`。
`_source/` 最值得补——它有独立的 gitignore 规则,是接手会话一定会撞上的东西。

> **2026-08-04 晚更新:`_source/` 与 `og_Norval/` 两行已补进 `core/00` Layout 树**
> (随「`_source/` 改为原件不入库、文本与图入库」那批改动顺手做掉)。
> **`mythos/spells/` 仍缺**,本条未完结。
> 顺带注意:原文写的「引用保持可选」这个特殊待遇**已经不存在了**——现在只有
> `.pdf`/`.docx` 原件的引用要写成可选,`_source/` 里的 `.md` 与图都在库里。

**为什么会漏**:layout 是**手写快照,没有生成器也没有校验**。
`_source/` 是 2026-08-04 才建的,建它的会话在 `.gitignore` 和 `WORKLOG.md` 都写了,
唯独漏了 `core/00`。`core/15` 第 2 步治的"数字过期"是同一类病,
但那一步只管**数字**(六个目录 / 47 张卡),不管**结构清单**。

---

## 根因:九条问题只有三种病

| # | 病 | 中招的问题 | 缺的制度动作 |
|---|---|---|---|
| **A** | **完结清单只验"本计划要建的建了没",不验"本计划让哪些既有陈述失效了"** | 1、2、4、5 | 完结清单加一项**反向扫描**:grep 本计划的编号/文件名/"待 PN 定案"字样 + 被推翻前提的名词,人工读每一处命中 |
| **B** | **自动检查的覆盖面与人工约定的作用域都按目录切,切口正好漏掉出问题的地方** | 3、4 | 孤儿检查区分「条目孤儿」(可豁免)与「目录孤儿」(不可豁免);`external/` 纳入某种检查或整条删除;接线要求从「只管第三方」扩到「原创内容也要有读路径」 |
| **C** | **同一约束在多处成文,改动只落离改动点最近的那处** | 5、6、7 | 改一条生成要求时,配套检查同一 spec 的 First / Output / Quality bar 三处 + `core/11` 的镜像项;同一字段的合法值只允许在一处定义 |

问题 8、9 各自独立(8 是实现层的语义合并,9 是手写快照无校验),不属于上面三类。

**这三条制度动作是本计划的主要价值。** 只修九条文本,下个计划完结时还会再犯——
A 类尤其:P9 一个计划就同时踩了 1(前提失效未回扫)、2(临时标记未清)、
4(新内容没接线)、5(旧段落没对齐)。

---

## 待拍板(阶段 1 开工前需要)

**Q1 — 神格页的读路径怎么接?** 三选一或组合:
| 选项 | 做什么 | 代价 / 好处 |
|---|---|---|
| **a. 扩索引** | 改 `build_monster_index()`,把 `reference/mythos/great-old-ones/*.md` 也并进 `monster-index.md` | 改脚本 + 全表回归;好处是**现有入口不变**,`core/07`/`core/04` 一个字不用改,以后新增神格页自动进索引 |
| **b. 直接接线** | 在 `core/01` 问题 9、`core/03`、`core/04` 步骤 1 各加一条指向 `reference/mythos/great-old-ones/` 的读路径 | 纯文本;但**手工接线正是这次出问题的方式**,以后新增神格页仍靠自觉 |
| **c. 两者都做** | a 管检索,b 管"定威胁时该去读神格的 lore" | 两件事本来就不同:索引答"谁服侍 X",神格页答"X 是什么、怎么被崇拜" |
**倾向 c**,理由是 a 和 b 解决的不是同一个问题;但 a 单独做也已经堵住最大的洞。

**Q2 — L5 要不要单独的模板?**
| 选项 | 代价 |
|---|---|
| **a. 建 `templates/great-old-one.md`** | 多一份要维护的模板,但和 `core/07` 的"lore-shaped, not a stat card"对得上,也把只存在于 WORKLOG 的体例落成生产文件 |
| **b. 在 `core/07` 指名 `reference/mythos/great-old-ones/cthulhu.md` 当体例** | 零新增文件;但"拿一份内容当模板"和 `core/00` 的 "Templates in `templates/` define the shape" 打架 |
**倾向 a**。无论选哪个,`core/07` 的 Output 段都必须补 L5 例外(那条是纯 bug,不是选择)。

> **原 Q3(`--strict` 是否纳入本计划)已定案:纳入,放在阶段 3。**
> 改动是一行分档 + `core/13` 一句话,单开一条计划的开销大于改动本身。

---

## 阶段 0 — 纯勘误 + P13 余波扫描,不需要拍板

**这一阶段可以立刻动。**

- [ ] **先做一次 P13 余波扫描**(问题 1 揭示这不是孤例):
      `grep -rn "bundle\|ChatGPT\|never ships\|does ship\|拿不到\|无文件系统"` 全仓,
      **人工读每一处命中**,不看计数。已知至少四处:
      - [ ] `core/07:14-15` —— 删掉「only channel / never ships / does ship」整段框架,
            改写成索引的真实定位(检索层)
      - [ ] `core/00:107` —— 见下面 `external/` 那条
      - [ ] **P5 阶段 3** —— 整节假设存在"无文件系统的 ChatGPT 网页链路",
            而 `core/00:173` 已写死 kit 由**有文件系统的 agent 就地读**。
            **这一条不在本计划范围内改,但要把结论报给 P5**:该链路若已不存在,
            阶段 3 连同"写进 `core/00` 的链路差异说明"可能整块不必做
      - [ ] **P10 复评修订 A 的第一条理由** —— "不进 bundle 等于目标用户拿不到"已失效。
            **结论(§六 落在 `diagram-conventions-zh.md`)不变**,另外三条理由站得住,
            只是这条理由要换。同样只报不改
      > **P5 阶段 3 的存废影响 P10 建筑卡那张的存废理由**(P10 修订 B 说"砍掉它
      > ChatGPT 链路就彻底没有室内地图")。**两者要一起确认,不要分两次答。**
- [ ] `core/00:103` 删掉指向 `update_plan/2026-08-02-monster-templates-traits.md` 的死链。
      **同句的「数值随便转,描述性文字保持原创」不在本计划改** —— P12 阶段 1.0
      要把整句删掉并改成「规则条文 vs 虚构散文」,**那边是超集,等它**。
      若 P12 先落地,本条只剩"确认死链已随之消失"
- [ ] `WORKLOG.md` 硬约定 5 里同一句「过渡期边界(等 P9 定案)」——**同样等 P12**,
      本计划只负责在 P12 落地后复查它是否真的没了
- [ ] `reference/external/` 三处一起处理(先确认 Keeper 是否还要这个子模块):
      - [ ] 删 `.gitmodules` 里 `reference/external/coc-zh` 段落
      - [ ] 删 `core/14:38` 分类表那一行(或改成"第三方 git repo:当前不收,
            要收先新建目录并给 README")
      - [ ] 改 `core/00:107`,只保留 `reference/craft/`
- [ ] `core/07` Output 段补 L5 例外(→ `reference/mythos/great-old-ones/`),
      与同文件 First 段的 Filing by tier 对齐
- [x] `core/00` Layout 树补 `reference/_source/`(**2026-08-04 晚已做**;注文改成
      "转出的文本与图入库,`.pdf`/`.docx` 原件本地",原计划那句"整目录 gitignore,
      引用保持可选"已随规则变更作废)、`og_Norval/`(同批已做)
- [ ] `core/00` Layout 树补 `mythos/spells/`(**仍缺**)

## 阶段 1 — 神格页读路径 + L5 模板(需要 Q1、Q2)

- [ ] 按 Q1 定案接读路径。若含选项 a:改 `build_monster_index()`,
      **跑全表回归**(223 条 + bestiary + 新并入的 6 份,确认没有重复行
      ——`mi_match_bestiary` 的短标题盲区见 `WORKLOG.md` P9 阶段 C 那条)
- [ ] 按 Q2 定案落 L5 体例(建模板 或 在 `core/07` 指名 `cthulhu.md`)
- [ ] 验收:从 `core/01`/`core/03`/`core/04`/`core/07` 任一入口出发,
      **能在不读 WORKLOG 的前提下找到 `great-old-ones/` 并知道该拿它干什么**

## 阶段 2 — `core/11` 补齐镜像审查项

> ⚠️ **与 P11 阶段 3 撞同一个文件**(那边要给 `core/11` 加一条年代串味审查项)。
> **谁先做谁负责不打架**;建议 P11 先做,本阶段跟在它后面追加。

- [ ] Craft 清单里把「至少有一个场景可按多于一种顺序到达」升级为
      **「每个必达场景 ≥3 条入边」**,与 `core/04` 步骤 5 和
      `diagram-conventions-zh.md:58` 对齐
- [ ] 同时把 `core/04` 步骤 6 的 "most scenes ... more than one order" 措辞
      调成不与步骤 5 冲突(步骤 5 管必达场景,步骤 6 管其余)
- [ ] **回扫一遍**:`core/03`–`core/10` 里还有哪些生成要求在 `core/11` 没有镜像项
      (这一步是 C 类病的存量清理,不只补这一条)

## 阶段 3 — 制度化(本计划的主要价值)

- [ ] **A 类**:`update_plan/README.md` 完结清单加第 8 项**反向扫描**——
      grep 本计划的编号、计划文件名、`until PN`/`等 PN 定案` 字样,
      以及被本计划推翻的前提的名词;每一处命中人工读,不看 grep 计数
- [ ] **A 类**:`reference/craft/README.md` 那条「不许指向 `update_plan/`」
      **作用域从 `craft/` 扩到 `core/` + `templates/` + `reference/`**,
      落到一个所有生产文件都会读到的地方(建议 `core/00` 的 Conventions 一节)
- [ ] **B 类**:`build-reference-index.py` 的孤儿检查区分
      **条目孤儿**(`ORPHAN_IS_ERROR` 现有语义,可豁免)与
      **目录孤儿**(整个目录没有任何 spec 指向,**任何目录都不豁免**)
- [ ] **B 类**:接线要求从「只管第三方归档件」扩到「原创内容也要有读路径」
      ——`core/14` 步骤 5 那条判据搬一份进 `core/15` 的清单
      (kit 原创内容走的是 `core/15`,不走 `core/14`)
- [ ] **C 类**:`core/15` 加一步——改一份 spec 的任何一条约束时,
      检查同一文件的 **First / Output / Quality bar 三处**是否重复了这条约束,
      以及 `core/11` 是否需要一条镜像项
- [ ] **C 类 / 问题 9**:`core/15` 第 2 步的 fact-check 从「数字」扩到
      「**数字与结构清单**」,`core/00` 的 Layout 树明确点名为要核的对象之一
- [ ] **问题 8**:`render-investigator.py` 只让 errors 触发 `sys.exit(1)`
      (或给属性区间检查一个 post-age 豁免),`core/13:83` 同步改措辞

---

## 跨计划协调

本计划的复查顺带核了另外五份计划,三条与本计划直接相关的写在这里
(其余评估结论未落盘,仍在会话里):

1. **问题 2 与 P12 阶段 1.0 改同一句话** —— 见「已并出去的部分」。**P12 先做**。
2. **问题 7 与 P11 阶段 2b 是同一条缝** —— 见问题 7。**P11 先做**,
   并建议把收口位置定在 `core/02` 而不是 `eras/README.md`。
3. **阶段 2 与 P11 阶段 3 撞 `core/11`** —— 见阶段 2 的警示框。

## 收尾

走 `update_plan/README.md` 的**完结清单**(本计划改了 `core/`、`scripts/`、
`reference/`、`templates/`,六节全适用),外加本计划自己新增的第 8 项反向扫描
——**本计划是第一个该被它检验的对象**:grep `P15` / `core-spec-audit` /
「待 P15」确认没有在生产文件里留下临时标记。

特别注意:
- 阶段 3 改了完结清单本身,**改完后本计划要按新版清单再走一遍**
- 阶段 1 若动 `build_monster_index()`,`python scripts/build-reference-index.py --check`
  必须 clean,且 `monster-index.md` 行数变化要能解释清楚
- 三适配器一致性:阶段 0 和阶段 3 都可能动 `core/00` 的 Conventions/ground rules,
  那是适配器可见的顶层约定,`CLAUDE.md`/`GEMINI.md`/`AGENTS.md` 要跟着核

## 备忘

- **本计划不新增任何 kit 能力**,全部是勘误 + 制度。`CHANGELOG.md` 的条目
  应该写成"你现在不会再读到失效的说明 / 神格页现在找得到",不是列改了哪些文件
- 问题 4 是唯一会改变 Keeper 实际产出的一条(神格现在能被检索到);
  其余各条改的是"接手会话不会被误导"
- 九条问题里,**七条的根因都是"某个动作没有配套的回扫"**。
  如果时间只够做一件事,做阶段 3 的 A 类那两项
