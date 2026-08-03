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
  ├ rules/          kit 自己写的 7e 速查:**数字**(原创、进 bundle)
  ├ craft/          kit 自己写的手法提炼稿:**写法**(原创、进 bundle)
  ├ bestiary/ mythos/ tables/   原创可复用素材
  ├ decks/          官方卡组转录(第三方、带引用出处、不进 bundle)
  ├ sourcebooks/    官方书籍全文转录(同上,体量更大)
  ├ index.json      七个目录的反向索引 + 校验(脚本生成,各目录另有一份)
  ├ og_Norval/      洛夫克拉夫特全集 82 篇 → 提炼稿 craft/lovecraft-zh.md
  └ glossary-zh.md  中文术语锁,写中文必查(脊梁文件,故意留在根目录)
campaigns/          一战役一目录,_template-campaign/ 是模板
update_plan/        P1–P9 改动计划 + 完结清单;README.md 是状态索引
scripts/            build-bundle.sh · render-investigator.py · build-reference-index.py
dist/bundle.md      构建产物:整个 kit 拼成一份,给没有仓库的 ChatGPT/Gemini
```

## 硬约定(踩了就是 bug)

1. **改行为改 `core/`,不改根适配器**;但 `CLAUDE.md`/`GEMINI.md`/`AGENTS.md` 三份必须一致,
   只存在于一份里的指令本身就是 bug。
2. **动过 `core/`/`templates/`/`reference/` 必须重跑 `bash scripts/build-bundle.sh`**,
   `dist/bundle.md` 和源文件同一个 commit。不重建,ChatGPT 用户就永远用着旧规则。
3. **每次改动在 `CHANGELOG.md` 追加**;同一天合并进同一条,不新开。
4. **文件名一律英文 ASCII `kebab-case.md`**,哪怕内容是中文。
5. **输出语言按战役声明**,kit 脚手架和文件名保持英文;写中文查 `reference/glossary-zh.md`。
6. **转载规则(2026-08-02 改)**:kit *生成*的内容不含任何受版权原文;官方资料**可以收录**
   进 `reference/decks/`、`sourcebooks/`,但文件末尾必须有 `## 引用出处` 表,且生成器
   **只取结构和数值刻度,不取文字**。规则本体在 `core/00-how-to-run.md` → ground rules。
7. **归档件不进 bundle**,所以任何 spec 引用它们都要写成可选("if present locally")。

## 当前状态(2026-08-03)

计划 P1–P9 的权威状态在 `update_plan/README.md` 的状态索引表,**不要在这里读状态**,
只记几条容易漏的:

- **P2/P3/P4/P6 均已归档,P1 阶段 0-2 已归档、阶段 3 拆成独立计划仍待执行。**
  2026-08-02 那批 16 个 commit(P1-P4 相关全部内容)与 2026-08-03 的收尾 commit
  均已提交,`git status` 干净。**不存在"待提交"的改动**——下一个会话不用再找
  scratchpad 或未提交的工作区改动。
- **P1 第四章的两个硬前置(P4、P7)现在都已解除,且 P7 本身也已完成**——新增
  `reference/rules/magic.md`,`core/02`/`core/07`/`reference/mythos/README.md` 已接线。
  P1 阶段 0-2 已归档,只剩阶段 3 收尾(`update_plan/2026-08-02-cult-doc-wrapup.md`)。
- **`reference/sourcebooks/keeper-rulebook-7e-zh.md`(规则书全文重译,17470 行)已确认
  可读**——P7 落盘时发现它比 grand-grimoire 更权威地给出了魔法书研读机制(CMI/CMF/MR
  三值、泛读/精读两阶段、重复精读耗时翻倍),`magic.md` 的魔法书章节改成从这份规则书
  抽样 20+ 本典籍算出的真实区间,而不是估算。之前"当前状态"没点名这份文件,接手时
  别漏看。
- **P8 投资者卡渲染缺口也已完成**——`scripts/render-investigator.py`/`templates/investigator.md`
  补全全部缺失字段,加了硬性算术+阈值型双层自校验;`core/13`/`character-creation.md`/
  `core/01`(新增问题 14)已接线。现在 P1–P8 只剩 P1 阶段 3(纯收尾)未动,P5/P9 等 Keeper。
- **P9 怪物模板的"来源红线"部分有答案** —— 转载规则已改,且
  `reference/sourcebooks/malleus-monstrorum-zh.md` 已可读;剩下要 Keeper 定的是范围。
- **三份 sourcebook 的手动重译已随第六轮批量提交落地**(9c47d98);误建的空文件
  `reference/sourcebooks/新建 Text Document.txt` 已核实不存在(已清理或从未提交)。
  仍未清的账:P7 计划第 5 行的行数(写 13731,现为 5365)、`sourcebooks/index.json`
  的行数字段、三份文件头部的"转录质量"警示按新文本复核(malleus 开头仍有噪声)。

`update_plan/README.md` 末尾还有一张**按可动性排序的表**(哪个计划现在能动、卡在等谁),
接手时先看那张。

---

## 会话记录

### 2026-08-02 — reference/ 归档体系

**做了什么**

1. **改了 kit 的转载规则。** 原规则一刀切"不复制任何受版权文本",把官方卡组这类有用的
   取材源挡在门外。新规则见上面硬约定第 6 条。同步改了 `core/00`、`CLAUDE.md`、
   `CONTRIBUTING.md`、`README.md` 免责声明——原本这几处都写着与新事实不符的话。
2. **`reference/` 根目录 7 份散落的 md 全部归位**,分成两类:

   | 目录 | 收了什么 |
   |---|---|
   | `decks/` | 好事者、恐惧症、惨事、武器与造物 4 份官方卡组 |
   | `sourcebooks/` | 7e 规则书、魔法大典、怪物之锤 3 份整书转录(共约 5.4 万行) |

   每份都改成英文 `kebab-case.md`、LF、加头部导读(含已知转录缺陷警示)、加 `## 引用出处`。
   两份 PDF 也从 `rules/` 挪到 `sourcebooks/` 与转录稿同名并列。
3. **反向索引** `scripts/build-reference-index.py` → `reference/index.json` 及各目录
   `index.json`。出处从各文件的 `## 引用出处` 表**解析**而来(引用块是唯一真源),
   引用关系靠全仓库扫描,精确到行号。脚本同时是校验器:缺引用块、缺行、或归档件没人引用
   都会报错。**改归档件后重跑它。**
4. **归档流程规范化** `core/14-archive-reference.md` + 技能 `archive-reference`,
   七步清单(分类→命名→头部→引用→接线→重建索引→收尾),已在三份适配器路由表登记。
5. **接线**:7 份资料接进 `core/02/04/06/07/13`、`reference/rules|tables|bestiary|mythos`。
   顺带解除 P7 阻塞、更新 P6/P9 的相关条目。

**为什么这么分**

`decks/` 与 `sourcebooks/` 分开,是因为用法不同:卡组是现成条目、随取随用;书是深查、
为一个数字翻一章。合成一个目录会让"我该读哪份"变模糊。
`rules/` 保持只放 kit 原创速查——它进 bundle,而转录件不进。

**留下的判断**

- **`glossary-zh.md` 故意留在 `reference/` 根目录**,不归任何子目录。它有 26 处引用、
  21 个文件,其中三处是硬依赖(`build-bundle.sh` 白名单、两个战役的 `CLAUDE.md`、
  `benchmark.json`);更重要的是它的角色是**脊梁文件**,和 `README.md` 同级,不是某个
  分类下的一份资料。为它单开只装一个文件的目录,只有改名成本没有分类收益。
  这条判断记在 `reference/index.json` 的 `kit_original_loose_files` 里。
- `og_Norval/`(82 篇洛氏原作)也是第三方资料,但它是公共领域且已自成目录,这轮没并进
  归档体系,只在 `reference/index.json` 的 `third_party_elsewhere` 里登记了位置。
  以后若要统一到一个 `source/` 伞下,那是一次独立的大改名。
- 仓库是公开的,收录 7 份官方资料原文是 Keeper 明确拍板的决定。标注出处解决了署名与
  可追溯,但不等于取得授权;`README.md` 免责段已加"版权方可开 issue 要求下架"。

**同日第二轮:新增 `reference/craft/`**

`lovecraft-craft-notes-zh.md` → `craft/lovecraft-zh.md`。理由不是"根目录要干净",而是
**P1 已经排好了它的同类**:`update_plan/2026-08-02-cult-doc-integration.md` 第三章 A 项
要产出邪教设计手法稿,计划里写明"定位对标 lovecraft 笔记"。不建目录,它就会再落到根下。
该计划的落点已同步改成 `craft/cult-design-zh.md`。

`craft/` 与 `rules/` 的分工:**rules 管数字,craft 管写法**。两边都是 kit 原创、都进 bundle,
但一个错了数值不对,另一个错了文字平庸。

顺手修了一个既有 bug:`core/09-description.md` 把这份笔记当硬依赖("Both draw on…"),
但它**从来不在 `dist/bundle.md` 里**——用 bundle 的 Keeper 被指去读一份拿不到的文件。
已把 `reference/craft/*.md` 加进 bundle 白名单。

索引脚本同时扩到七个目录(原本只索引 decks/sourcebooks),kit 原创目录不校验引用出处、
只做 orphan 检查;`bestiary/`、`mythos/` 是内容库,没人引用属正常,不计为错误
(`ORPHAN_IS_ERROR`)。

**同日第三轮:新增 `close-session` 技能**

背景:上一轮(第二轮,新增 `craft/`)的会话记录写完之后,`WORKLOG.md`、`CHANGELOG.md`、
`reference/README.md`、`scripts/build-reference-index.py` 的文档字符串**五处地方都写着
"六个目录"**,但脚本实际输出是 `indexed 20 files across 7 directories`——加了 `craft/`
之后没人回头拿实际输出核对过这句话。下一个会话靠 grep 字面量 `六个目录`/`six indexed`
才一次性挖出全部五处并改成"七个"。

这次改动**不是修那五处**(已经在上一步顺手修完),而是把"改完顺手核对一遍数字"这件事
本身变成一条**收尾流程**,不再只靠"记得回头查"。新增:

- `core/15-close-session.md` + 技能 `close-session`:给**没有对应 `update_plan/` 计划文件、
  也不是走 `core/14` 归档third-party 资料**的临时维护会话用的收尾清单。核心是它比
  `update_plan/README.md` 完结清单多一步——**回头 grep 核对**这轮日志里写的每一个数量词
  /枚举/路径,而不是凭记忆或抄上一条记录。
- 已在 `core/00`、`CLAUDE.md`(技能表)、`GEMINI.md`、`AGENTS.md` 四处路由表登记,
  三份适配器的 Maintenance 小节都加了一句指向它。

**为什么单开一个 skill,而不是把这条核对规则塞进 `update_plan/README.md` 的完结清单**:
那份清单是给**正式计划(P1–P9)**收尾用的,今天这种"没有计划文件、纯粹改 kit 结构"的会话
不会走那条流程,之前完全没有强制收尾步骤——`WORKLOG.md` 头部那句"手工维护,过期比不存在
更糟"只是提醒,不是清单。`core/14` 归档流程第 7 步是同类思路,但只覆盖归档第三方资料这一种
场景。`core/15` 补的是这两者之间的空白,并且明确写清楚三者的边界,避免以后出现第三套互相
打架的收尾规矩。

**同日第四轮:魔法大典重译稿通读 + 法术整合规划(纯规划,除本日志外未动任何文件)**

背景:Keeper 手动重译了三份 sourcebook(工作区未提交,行数现为 grand-grimoire 5365、
keeper-rulebook 17469、malleus 8759)。本轮口头任务说的是"malleus 的魔法转译完毕",
**实际核对法术全在 `grand-grimoire-zh.md`**——"深层魔法"在 grand 出现 121 处、在 malleus
0 处;malleus 仍是怪物图鉴,且开头仍有转录噪声。接手时别被文件名带偏。

**做了什么**:通读魔法大典重译稿,确认结构可机器解析:

- 条目格式书内自述在 578–592 行:法术名〔分类码〕英文名 → 消耗 → 施法用时 → 描述 →
  深层魔法(可选)→ 别名 → 附录(表 4-N / 属性块)。
- 结构标记规整:行首"消耗"443 处 = 行首"别名/另名"443 处(≈条目数;书封面称 550+,
  合并条目后实际约 443)。17 个分类码清单在 504–520 行(驱召战交梦附环续民害支造他保时变旅),
  法术名后另有(幻梦境)(民俗)(怪物名)三种限定标记。
- 前三章是施法通则(精神状态/施法区域/天象/牺牲的本质/地脉节点/请神-联络-召唤三分法),
  正是 P7 速查表该提炼的骨架素材。

**规划结论**(只存在于会话与此处,Keeper 拍板后再落成 P7 扩充或新计划文件):

1. **四层架构**:L0 原文(已有,只读)→ L1 法术索引 JSON(新脚本生成,兼校验器:
   名称/英文名/别名数组/分类码/消耗拆 mp-pow-san/用时归档/深层魔法与附表有无/行号指针,
   与 `build-reference-index.py` 的行号惯例同族)→ L2 `rules/magic.md`(P7 既定产出,
   只写惯例与数值区间,进 bundle)→ L3 `mythos/spells/` 战役用到才按需自写条目。
   转载红线由分层守住:索引只存结构与数值刻度 + 行号,原文永远只被指过去。
2. **标签**:结构标签机器提取;语义标签用封闭受控词表、五轴(实体/机制/叙事功能/
   征兆/强度),别名与实体译名挂 `glossary-zh.md`;搜索只对名称+别名+标签匹配,不对全文。
3. **叙事接线**:"仪式拆解"模式——仪式前置条件→事件钟阶段、获取痕迹→线索表行、
   打断后果→触发表、〔驱〕〔保〕类反查公平出路;`tables/mythos-angles.md` 20 个角度
   逐条映射法术引擎(别名系统天然支撑 angle 12 的"误译执行"、瑕疵法术支撑 angle 15);
   深层魔法当 06/07 的难度旋钮;阵营对抗 = 两条仪式争夺同一稀缺前置(节点/天象/典籍/祭品)。
4. **执行顺序**:P7 速查 → 索引脚本 → 标签词表 → 04/05/06/07 接线 → 常规收尾。

**留下的判断**:重译遗留的账(P7 行数、`sourcebooks/index.json`、头部警示复核、
误建空文件)统一归到**提交这批重译的那个会话**清,本轮不代办——见"当前状态"新增条目。

**第四轮补充(同一会话,Q3 深化)**

1. **战役形态不做枚举清单,做三旋钮组合空间**:时态(未施/进行中/已施成/需按期重施)×
   施术方(教团/孤狼/先民遗产/调查员被迫)× 法术的故事身份(目标/手段/凶器/环境/商品/
   传染源)。除原三种外由此再得六种:余波型、维护型、传染型、纵贯型(灵魂分配术的
   藏脏器=天然章节结构)、中咒型(被诅咒的眼自带 1D6+1 天倒计时)、典籍追逐型
   (别名系统支撑"两个名字是同一条法术"的中盘转折)。拟做成 `tables/` 可掷表,
   与 mythos-angles 同哲学。
2. **intake 转换管线**:灵感词 → 同义映射层(新增物,挂标签词表 spec)→ 受控标签 →
   索引检索,按强度分档取 3–5 条候选,每条给一行"当引擎时战役长什么样";无命中兜底
   两条路(退轴级浏览 / 按 `magic.md` 区间自造入 `mythos/spells/`)。`all auto` 走反向:
   随机抽仪式级法术,用拆解模式反推战役。
3. **强度档合成规则**(机器推导列+人工覆写列,进索引脚本):输入按权重为
   POW 消耗>MP 消耗、施法用时档、前置门槛数、可否群体施放、深层魔法有无、不可逆性;
   产出小术/中术/大术/仪式级四档,同一法术允许"基础档+深层档"双值。
4. **Keeper 提出"代价越大越适合主心骨",采纳并修正为必要非充分**:
   主心骨适性 = 强度档 × 前置条件数(可拆成钟)× 征兆数(可拆成线索);
   高代价瞬发无征兆的法术是暗算武器不是主心骨。强度↔位置映射:仪式级=主心骨、
   大术=章节转折/反派招牌(喂 P4)、中术=NPC 日常与征兆来源、小术=氛围线索与
   调查员公平出路。**设计铁律(进 magic.md):反制法术的代价必须比被反制法术低至少一档**,
   否则出路是纸面的。
5. **本轮顺带发现**:`update_plan/README.md` 的复杂度排序表与依赖图自 97c87d8 创建后
   从未更新——39d1625 只同步了状态索引。过期处:P7 行"现在能动 ❌ 等 Keeper 交付"
   (实际阻塞已解除)、P8 行"2 个已实测确认的缺陷"(状态索引为 1/2/4 共 3 个)、
   P4 行"等 3 个拍板"(现为 1/3/5/8 共 4 个)、依赖图 KeeperDoc 节点仍是"⏳ 等交付"。
   **根因:复杂度表在任何清单里都没被点名**(完结清单第 1 节只点名状态索引表);
   依赖图虽有规则(完结清单第 6 节"去掉箭头")但只在**计划完结**时触发,
   而 39d1625 是归档会话,走的 core/14 流程不含第 6 节——"外部交付解除阻塞"
   这条路径两张图都没人管。与"六个目录"同类:无规则覆盖的重复状态必然漂移。
   修法待 Keeper 选:给两处补"阻塞状态变化时同步"的规则,
   或删掉"现在能动"列改为只查状态索引。

### 2026-08-02 — 第五轮:P4 反派强度预算(人类侧)落盘 + P1 第三章落盘

背景:Keeper 直接要求"继续完 P4 和 P1 内容"。P4 在计划文件里其实已经推进到
第四轮定案(1/2/3/4/5/9 均已定案),只剩待讨论 8(基线内容已定,只差点名落点文件)
和待讨论 7(暂缓待 P9)——但 `update_plan/README.md` 状态索引仍写着旧的"2、4 已定案",
是又一次和第四轮记录的"复杂度表漂移"同类问题:进展只写进了计划文件本身,没有回填状态表。

**做了什么**

1. **P4 待讨论 8 拍板:落点跟着待讨论 1、3,同落
   `reference/rules/character-creation.md`**(新增 §11)。内容:普通人类基线 = 照
   `busybodies-zh.md` 校准;首领 = 基线 + 增量,增量二选一(法术型按资历掷法术数量,
   数值查 `grand-grimoire-zh.md`;非法术型按装备总价,查 `weapons-and-artifacts-zh.md`);
   技能**选哪些**由背景决定,**给多高**由致命性倒推(不是背景越硬数值越高——这条分工
   若不写清楚,`core/11` 审计员两种说法都能自圆其说);原设想的技能点预算带表和四组
   预设数组**确认作废**,反派与调查员共用同一套标准创建流程,不单独开小灶。
   `core/02`(登记入口)、`core/06`(首领生成指路)、`core/07`(占位句:人类反派不走
   这套 type/threat 标尺)、`core/11`(致命性倒推审计题)四处接线。
2. **顺带修了 P4 计划文件里两处指向不存在的"待讨论 6"的悬空引用**——那个子标题从来
   没真正开过,内容早已并进文末"已拆出→P9"一节,原文只是没跟着改指向。
3. **P1 第三章(设计一个克苏鲁邪教方法论)落盘**:`reference/craft/cult-design-zh.md`
   (§一为何是最好的反派、§二克苏鲁教团的独特性——含"预言可自由解释"这个手法本身、
   §三十一步有序设计流程、§四财源即线索引擎六项、§五弱点与敌人"平淡才可信")。
   配套四张骰表:`cult-goals.md`(愿望 1D10 × 手段 1D8,两表相乘才是完整目标;源表
   标称手段 1D10 实际只有 8 条,骰值区间已诚实重建为 1D8)、`cult-leader-positions.md`
   (首领社会定位 1D10,每条保留"带来什么便利")、`cult-power-sources.md`(力量来源
   1D4)、`npc-appearance.md`(外貌/气质 1D20,与既有 `npc-quirks.md` 分工:quirks 管
   怎么演,这张管长什么样)。新增 `templates/cult.md`,字段对齐 `core/03` 既有 faction
   结构。原书示范用的三个虚构邪教案例(雷切尔/安德鲁/查德)按计划确认不收录。
4. **`core/03`/`core/04`/`core/06` 三处接线**:`03` 加邪教子路径(指向 cult-design-zh
   §一–§三 + 两张骰表 + `templates/cult.md`);`04` 的三线索规则一节加子项,指向 §四
   六项财源当独立线索来源;`06` 加 `npc-appearance.md`(外貌骰表)与邪教首领指向
   `cult-leader-positions.md` + `character-creation.md` §11 两处指路。
5. **`update_plan/README.md` 状态索引、依赖图、建议执行顺序、复杂度排序表四处同步**:
   P4 从"待讨论"改"进行中(内容已落盘,等提交)";P1 反映第三章已落盘;依赖图去掉
   KeeperCall(P4 待讨论 8)与 KeeperDoc(P7,上一轮已解除但图里没删)两个节点,标注
   第四章两个硬前置均已解除;复杂度表移除已完成的 P4 行,P7/P1 行的"现在能动"列同步。

**为什么这么分工**

P4 的落点没有另开新文件——`reference/rules/character-creation.md` 已经是"KP 专用的
角色数值工具"这条判断在待讨论 1 就定过了,反派强度预算是同一件事的延伸,不必为了
"听起来该独立"而多开一份只有增量规则、离了基线看不懂的速查。
P1 第三章的"关系图"(§三第 11 步)和 D 项第二条(campaign `Threat` 字段)**没有**在
本轮落地——前者依赖 P5(仍阻塞在等 Keeper 定视觉风格),后者是阶段 2 的动作,
`templates/cult.md` 已经把两处结构留好占位,不需要提前抢做。

**留下的判断**

- **intake 的新增问题这次没有直接改 `core/01-intake.md`。** P4 待讨论 9(生成首领时
  是否强化战斗的开关)本该落进 intake,但 P1 阶段 2 也要新增一问("The threat"),
  两次分别改 intake 编号和"never invent a fourteenth question"这类字面引用,不如
  一次做完。已在两个计划文件里互相记了一笔,阶段 2 执行时一起接。
- **两个计划的内容都已落盘,但都没有提交。** 状态表和计划文件头按规则不能写
  "已完成(<commit>)"(hash 提交后才有)——P4 用"进行中(内容已落盘,等提交)"、
  WORKLOG 本节和 CHANGELOG 的日期标题都标了"待提交"。等 Keeper 决定是否提交,
  提交后需要一次回填:两个计划文件头的状态行、`update_plan/README.md` 状态表的
  commit 列、CHANGELOG 标题的 commit 列、P4 归档进 `Archived/`。

### 2026-08-02 — 第六轮:P1 第一/二章落盘 + 全天积压批量提交

背景:新会话接手,`update_plan/2026-08-02-cult-doc-integration.md` 记录第三章的 docx
转换稿"存于会话 scratchpad,不进仓库"——但 scratchpad 是**会话级临时目录**,换了新会话
它就已经不在了。核对当天所有临时目录(`AppData/Local/Temp/claude/...`)确认无残留,
只能从原始 `克苏鲁教团.docx`(桌面)重新提取。**教训记一笔:如果转换稿要跨会话复用,
不能只放 scratchpad——起码要放进本仓库某个不进 bundle 的临时目录,或者接受每次重新提取
的成本。** 这次重新提取沿用了第一轮记录的同一套手法(unzip + Node 脚本解析
`word/document.xml`,styleId `1`–`8` = heading 1–8,`a3` 是正文不是 heading),没有新坑。

**做了什么**

1. **P1 第一章(克苏鲁邪教的历史)落盘。** 27 条史料型条目压缩成表格(不用叙事散文重述,
   理由见下),拆成两个文件:`reference/mythos/great-old-ones/cthulhu.md`(克苏鲁本体的
   setting 级 lore)与 `reference/mythos/cthulhu-cult-history-zh.md`(历史条目表 + 三条
   贯穿线索:永生大师线、黑翼者线、深潜者混种线)。原文的两层虚构手记叙事外壳
   (施瓦茨 1939 / 埃伯哈特 2017)确认不收录——那是原文档的呈现方式,不是可复用素材。
2. **P1 第二章(五个教团)落盘。** `reference/mythos/cults/` 新增五个全档:
   `order-of-morpheus`、`louisiana-swamp-cult`、`society-of-the-divine-children`、
   `esoteric-order-of-dagon`、`church-of-perfect-science`。每档保留起源/首领/组织/财源/
   弱点/敌人/成员钩子/故事灵感/替换项,**成员范例只留人物钩子,不转录技能列表和法术表**
   ——那是 `core/13-create-investigator.md` 按需生成的事,塞进 lore 文件只会让文件臃肿
   且很快过期。原文附带的完整冒险案例(每教团 2 个)压成一句话钩子,不逐段重述。
3. **发现并修了 `scripts/build-reference-index.py` 的一个真实 bug**:`mythos/README.md`
   写明的子目录结构(`great-old-ones/<name>.md`、`cults/<name>.md`)在索引脚本里根本不
   支持——`ORIGINAL_DIRS` 那组用的是 `os.listdir()`,只扫顶层,不像 `ARCHIVE_DIRS` 那组
   用 `os.walk()` 递归。落盘 `cthulhu.md` 后重建索引才发现它完全没被收录、连 orphan 都
   算不上(因为压根不在扫描范围里)。改成新增的 `list_md_files_recursive()` 递归扫描,
   `find_references` 同时匹配全路径与叶子文件名,让子目录里的文件也能被"谁引用了我"检索到。
4. **全天积压的未提交改动一次性梳理并分批提交。** 工作区里堆了当天前几轮(close-session
   技能、P1 第三章、P4)的产出,加上 Keeper 手动完成的三份 sourcebook 重译,全部还没提交。
   逐文件核对 `git diff` 后按内容归属分成约 6 个 commit(而不是一个大杂烩),对确实分不开
   的共享文件(`core/03-build-world.md` 被 ch3 与 ch1/ch2 各加了一段、双方文字挨在一起,
   `index.json` 系列本就是全量重新生成)如实在 commit message 里写清楚归属。

**为什么这么分**

第二章"成员范例"原文每人都带完整技能百分比与法术列表,五个教团十几个角色全转录的话,
体量会超过教团本身的设定内容,而且这批数值本就是"论坛数字",按计划要求本该先过
`core/02-rules-reference.md` 校验才能用——提前转录等于把未校验的数字焊死在 lore 文件里。
只留人物钩子,把"要不要造一张满卡"这个决定留给使用现场,是唯一不会过期的做法。

**留下的判断**

- **scratchpad 不是跨会话存储**,这条已经在本节开头记了教训,但没有改任何流程文件——
  是否要为"转换稿需要跨会话保留"这类场景另开一个不进 bundle 的暂存约定,留给 Keeper 拍板,
  不在本轮擅自决定。
- **本轮提交没有逐条回填 commit hash 进计划文件头**(P1、P4 状态行仍写"等提交"字样)——
  按上一轮记的规则,这该是拿到 hash 后的*下一步*,不是本轮的一部分;是否补一个回填 commit
  留给这批提交完成后决定。
- **第四章(邪教徒原型/怪物/造物)未动。** 体量与第二章相当或更大,且是本计划最后一块硬骨头,
  Keeper 已确认下一步继续做。

### 2026-08-02 — 第七轮:P1 第四章落盘,阶段 1 全部完成

紧接第六轮的同一会话,提交完积压后继续做第四章。这一章和前三章性质不同:前三章是
"提炼手法/lore",数值能省则省;第四章原文明确是**可直接拿来用的数值范型**(11 个
人类邪教徒原型 + 变体、8 只怪物,类比已归档的 `busybodies-zh.md` 官方 NPC 卡组),
省数值会违背这一章存在的意义。落盘前先把"人类邪教徒"12 组基础数值(HP/伤害加值/
体格/魔法值)逐条按 7e 公式手算核对——全部正确,没有一处需要修正,是四章里源数据
质量最好的一次。

**做了什么**

1. **12 组人类邪教徒范型 + 祝福菜单 + 永生大师工具包落盘** `reference/tables/cultist-archetypes.md`。
   邪教徒原样保留可用数值(不是叙事,是速查表);"永生大师"部分只留角色定位、常见/
   独特异能菜单和一个具名范例(慧强,呼应第一/二章已经用过的同一个角色)。
2. **发现并剔除一处版权问题**:原文档给的第二个永生大师范例是"卡尔·斯坦福"——
   混沌元素官方战役《犹格-索托斯之影》(1982)里的具名角色,原文自己都提醒"如果玩家
   跑过经典战役,用这个角色要小心"。这和全篇其余内容的"论坛汇编、取结构不取文字"
   性质不同,是**命名角色绑定具体商业产品**的版权问题,直接不收录,只留基础模板供
   自行设计第二个范例。
3. **8 只怪物落盘进 `reference/bestiary/`**:黑翼者、费尔罗克、猩红者、弗米森蠕虫、
   塞德西姆(完美科学教会"处理"终点)、混种深潜者、克苏鲁受祝者、克苏鲁之隶。按
   `templates/monster.md` 的形状写(Reveal/数值/战斗/异能/行为与弱点/Lore),英文,
   与已有的 `the-bell-keeper.md` 同一约定。
4. **造物落点改了**:原计划写"怪物/造物 → bestiary",但拉莱耶偶像、克苏菇、处理器、
   非欧几里得建筑学、黑滴、疼痛诱导器这六样有的是道具、有的是空间规则、有的是毒药,
   硬塞进"生物图鉴"文体不对,改开 `reference/mythos/artifacts-zh.md` 单独收。
5. **法术范围明确缩小**:没有等 P7 完整的 550+ 法术速查,只把第四章自己要用的 7 个
   新法术(请神术达贡/海德拉变体、狂喜术、沉默之油、四只新怪物各自的召唤/束缚术)
   落进 `reference/mythos/spells/`,跟着对应怪物条目走。P7 本身仍待执行,但不再是
   本计划的前置。
6. **`core/06-create-npc.md` 加一行**指向邪教徒范型表。`reference/glossary-zh.md`
   补了 Hydra、Immortal Master、Black Wing、Fellrock、Scarlet Orb、Vermisyn Worm、
   Sedecim、Thrall of Cthulhu、Cthulhu-Blessed 九个新词——部分(Hydra、Immortal Master)
   其实第一/二章就在用,当时漏加,这轮一并补上。

**为什么这么分**

第一/二/三章("lore/方法论")与第四章("速查数值")该用不同的压缩策略,不是偷懒少写
——一份克苏鲁邪教的历史条目表被塞进具体数值只会显得突兀,而一张"造无名邪教徒 NPC"
的速查表如果连数值都没有,就完全没用。判断哪种内容该留数值、哪种该只留钩子,标准是
"这份文件在桌面上要解决什么问题",不是"原文有没有给数字"。

**留下的判断**

- **P1 阶段 1(四章提炼)到此全部完成**,剩阶段 2(`core/01-intake.md` 新增"The threat"
  问题 + campaign `Threat` 字段)和附加项(NPC 互动史)。两者都无外部依赖,可以直接接。
- **精英邪教徒满卡化(复用 `templates/investigator.schema.json`)本轮没做**——这是
  第四章清单里唯一留白的条目,判断是"真正需要一张具名精英卡时按需生成",不是提前
  批量造卡占地方。P6/P1 都已就绪,不构成阻塞。
- **本批改动尚未提交**——按上一轮的教训,commit hash 回填留给提交完成后处理。

### 2026-08-02 — 第八轮:P1 阶段 2 + NPC 互动史附加项落盘,只剩阶段 3

紧接第七轮提交完第四章后,同一会话继续做阶段 2(敌对势力 intake 问题)和挂在本计划
里的附加项(NPC 互动史)。Keeper 明确要求这两块做完,阶段 3 收尾留到下次。

**做了什么**

1. **`core/01-intake.md` 新增两问**:第 9 问"The threat"(威胁背后是邪教/独行术士
   或家族/独立怪物/场所本身/自然或宇宙现象,auto 默认掷 `mythos-angles.md` 再反推
   属于哪一类——两张表不是一一对应,是"掷出来的角度暗示了哪种威胁类型"这一步需要
   模型自己判断,不是查表映射);第 10 问"人类反派首领是否默认强化战斗能力"(默认
   否)。两问紧邻插在 B 组之后,C/D/E 组问题编号整体顺移(9→11 … 15→17),
   "never invent a fourteenth question" 跟着改成"a sixteenth"。
2. **`campaigns/_template-campaign/CLAUDE.md` 新增 `## The threat` 字段**:类别 + 
   人类反派战斗强度 + 名字/一句话身份 + 指向 `world/` 全档的链接,结构对齐
   `templates/cult.md` 的身份/力量来源/目标三行。
3. **`core/04-design-scenario.md`/`core/03-build-world.md` 各加半句**:声明了 Threat
   字段的战役,写 truth 和造 faction 都要读它、顺着它走,不重复提问、不另起炉灶。
   `core/03` 这半句是阶段 2 才补上的——第三章接线核心 faction 分支时还没有这个字段,
   补丁挂在这里而不是回头改第三章的 commit。
4. **NPC 互动史**:`templates/npc.md` 加一个新的 KEEPER ONLY 节(当前态度覆盖式 +
   逐场追加式的一行日志);`core/06-create-npc.md` 提一句新建 NPC 只填中性默认态度;
   `core/12-canon-update.md` 的更新清单加一整节 `npcs/<name>.md`,并在 Quality bar
   里加了对应检查项——这条明确按 Keeper 原话"必须写成流程,不写就没人更新"处理,
   不是可选建议。
5. **重跑了 bundle 与索引**,两者都干净通过。

**为什么这么分**

第 9、10 两问挨在一起插入,是为了只改一次问题编号——如果分两轮做,C/D/E 组的编号
要跟着改两次,`update_plan/2026-08-02-antagonist-budget.md` 待讨论 9 早就预见到这
个问题并明确要求"与 The threat 一问一起接线"。

`core/03` 补的那句不属于阶段 2 清单原文,是执行时发现的真实缺口:Threat 字段存在
的意义是"造世界的时候别答非所问",但第三章接线 faction 分支时这个字段还不存在,
没有理由预判到要写这句话——这类"下游动作暴露上游遗漏"的缺口,发现了就地补,不用
为了"改动归属于哪一轮"而拖延。

**留下的判断**

- **P1 现在只剩阶段 3(收尾)**:`reference/README.md` 登记新增的
  `reference/mythos/artifacts-zh.md`/`reference/mythos/spells/`/`reference/tables/
  cultist-archetypes.md`/八个 bestiary 条目、走一遍 `review-material` 审计新增内容、
  归档进 `Archived/`。Keeper 已表示这部分留到下次会话。
- **第三章 D 第二项(campaign `Threat` 字段)随阶段 2 一并完成**,原计划文件里
  "留给阶段 2"的标注现在可以勾掉了;E 项(关系图惯例)仍然卡在 P5。
- **本批改动尚未提交。**

### 2026-08-02 — 第九轮:P1 归档拆分 + `update_plan/Archived/README.md` 新惯例

Keeper 直接要求把 P1 拆成"已完成部分归档 + 未完成部分新计划",并把归档计划的详细
描述从主索引挪出去,理由是归档条目只会越攒越多,`update_plan/README.md` 每次都要
整段读进去,token 成本会一直涨。

**做了什么**

1. `update_plan/2026-08-02-cult-doc-integration.md`(原 P1)`git mv` 进 `Archived/`,
   文件头状态改成"阶段 0-2+附加项已完成,阶段 3 拆分为独立计划";阶段 3 清单本身
   删掉,只留一句指向新文件,不在归档记录里继续挂未勾选的待办。
2. 新建 `update_plan/2026-08-02-cult-doc-wrapup.md` 承接阶段 3(收尾)的执行清单
   (README 登记、`review-material` 审计、提交),内容原样搬自归档文件,不重复背景说明。
3. **新增 `update_plan/Archived/README.md`**:归档计划的范围描述、设计理由从今往后
   记在这里,不进主索引。`update_plan/README.md` 的状态索引表对归档条目(现含 P1/P2/P3)
   只留"名称+链接+极简状态",详情指针指向 `Archived/README.md`。同步改了完结清单
   第 7 条("移进 Archived/ 时也要在 Archived/README.md 加一行")和末尾"已完成归档"
   说明段。

**为什么这么分**:归档不等于内容消失——`Archived/` 里的文件仍是完整的设计记录,
只是**主索引不再复述它们**。这条分工只影响"哪份文件装描述",不改变"归档=完结的
只读记录"这条既有铁律。往后新计划归档时,记得两处都改:移文件 + `Archived/README.md`
加一行;漏了后者会导致归档文件"查无索引"。

### 2026-08-03 — 第一轮:P4/P6 收尾回填 + changelog/WORKLOG 漂移修正

新的一天,新会话接手,Keeper 要求"继续执行计划"。核对 `update_plan/README.md` 时发现
P4 的执行清单其实已经全部做完(最后一项 intake 提问已随 P1 阶段 2 在 66d32d2 接线),
但状态表、计划文件头、`CHANGELOG.md`、`WORKLOG.md` 四处都还停在"等提交"/"待提交"的
措辞——git log 显示昨天(2026-08-02)16 个 commit 早就全部落地(`git status` 干净),
这些措辞纯粹是**没人回头做完结清单第 7 步"回填 commit"**留下的漂移,同类问题第四轮
记录里已经点过名(复杂度表/依赖图漂移),这次是同一根因在 changelog/WORKLOG 上的另一
处发作。P4 走完收尾流程后,顺着复杂度排序表第 1 条继续做 P6 收尾,发现 P6 剩下的两条
待办也都已经有定论(见下),同一并处理。

**做了什么**

1. **P4 走完完结清单并归档**:计划文件头加回填记录、勾掉最后一项执行清单
   (标注 commit)、`git mv` 进 `Archived/`,`Archived/README.md` 加一行范围描述,
   `update_plan/README.md` 状态表行改成指针形式,依赖图 P4 节点文字同步。
2. **`CHANGELOG.md` 2026-08-02 条目头部的 commit 列表从占位的
   `(713cd1c, e0d026b, aceddf9, 待提交)` 补全成那天全部 16 个 commit**(用
   `git log --since/--until` 核实,不是凭记忆列)。
3. **`WORKLOG.md` 的"当前状态"节整段重写**——原文写的"P4/P1 第三章尚未提交"、
   "三份 sourcebook 手动重译在工作区未提交"三条,在本轮开始前其实早就是假的
   (2026-08-02 第六轮批量提交时就已清空);顺手核实了同一节提到的误建空文件确实
   已不存在,不再留悬空提醒。
4. **P6 走完完结清单并归档**:剩下的两条待办都已经有事实依据可以直接下结论,
   不需要再等 Keeper——
   - 跨 P1 项("精英邪教徒复用 schema"):P1 第四章早已落盘并明确判断"按需生成、
     不预造"(WORKLOG 第七轮已记),这条本就不需要 P6 再做什么,直接勾掉。
   - `roster.csv`:核对唯一在跑的战役 `campaigns/beidaihe-winter/`,发现连
     `investigators/` 目录都不存在、零份投资者档案——花名册索引此刻没有对象可索引,
     判断"暂不做",字段形状已经记在文件里,真有需求时直接照抄开一份 CSV 即可。
   同样走 `git mv` 进 `Archived/`,`Archived/README.md`、状态表、依赖图、建议执行
   顺序、复杂度排序表五处同步。

**为什么这么分**:P4 的回填没有新建一份"回填流程"文档——完结清单第 7 步已经写了
这条规则,缺的不是规则而是**执行**。真正暴露的问题是:归档/批量提交类的收尾动作
(第六轮那种"全天积压一次性提交")容易只顾着让 commit 落地,不回头把"待提交"这三个
字从文档里摘掉。这轮没有加新规则,只是把欠的账还了——如果之后还反复出现,才值得
考虑在完结清单里加一条强制项。
P6 的 `roster.csv` 判断没有去问 Keeper,是因为答案能从仓库现状直接读出来
(零份投资者档案),不是一个需要 Keeper 偏好的问题;真正需要 Keeper 判断的是
"以后有没有需求"这种未来的事,而"现在有没有对象可用"是可核实的事实,能自己查清楚
的事不该升级成提问。

**留下的判断**

- **P4/P6 是本轮唯一有实质内容变动的计划**;P1/P2/P3 的状态表与归档记录核对后确认
  commit hash 和措辞都已经是对的,没有需要回填的漂移。
- **`roster.csv` 的"暂不做"是可逆判断,不是关闭功能**——字段形状留在归档文件里,
  没有删除任何设计,以后有战役需要时不必重新讨论。
- **接下来按 `update_plan/README.md` 复杂度排序表第 1 条(P8 卡渲染缺口)继续**——
  P4/P6 完结后表格前移一位,P8 现在是"现在能动"里最简单的一项。

### 2026-08-03 — 第二轮:P7 魔法速查落盘(与另一会话并行执行 P8)

背景:Keeper 同时开了两段会话,一段跑 P8(卡渲染缺口),本轮跑 P7(魔法速查)。两段
会话共享同一个工作区(没有用 worktree 隔离),这带来一个新问题:生成产物
(`dist/bundle.md`、`reference/**/index.json`)由双方各自的重跑脚本共同写入,任何一方
提交这些文件都会把对方**未完成**的改动一起带进自己的 commit。

**做了什么**

1. **`reference/rules/magic.md` 落盘**:施法通则(消耗记法、施法用时的 DEX+50/N轮 规则、
   POW 对抗检定、SAN 是定值不是 X/Y)、按 `grand-grimoire-zh.md` 抽样约 300 条法术条目
   得出的四档消耗区间(小术/中术/大术/仪式级,与规划记录第四轮定下的档位名对齐)、法术
   设计的成本换算惯例(含上一会话第四轮 Q3 定下但一直没有落处的"设计铁律:反制法术的
   代价必须比被反制法术低至少一档")、魔法书研读机制。`core/02`/`core/07`/
   `reference/mythos/README.md` 三处接线。
2. **发现 `reference/sourcebooks/keeper-rulebook-7e-zh.md` 已可用**,魔法书章节改用它
   的真实数据(CMI/CMF/MR + 泛读/精读机制)而不是"规则书之外只能现编"——见"当前状态"
   新增条目。
3. **重跑 `build-bundle.sh` 与 `build-reference-index.py` 确认无误**(索引脚本报告
   "nothing orphaned"),但**没有提交这两个生成文件**——此刻它们的 diff 里混着 P8
   会话对 `core/13`/`core/01`/`character-creation.md`/`templates/investigator.md`/
   `scripts/render-investigator.py` 等文件的未提交改动(`reference/index.json` 一份就有
   397 行变化,远超 magic.md 一个文件该有的量)。提交它们等于替 P8 提前定稿一份它自己
   还没写完的东西。
4. **提交范围限定为本计划确实拥有的文件**:`reference/rules/magic.md`(新增)、
   `core/02-rules-reference.md`、`core/07-create-monster.md`、
   `reference/mythos/README.md`、两份 `update_plan/` 文件、`CHANGELOG.md`、本节。
   逐一用 `git diff` 核对这几个文件的改动范围确实只有本轮内容,没有被 P8 会话污染。

**为什么这么分**:`git add -A` 或提交 `dist/`/`index.json` 在单会话场景下是完结清单要求
的标准步骤,但两个会话共享工作区时,生成产物不再是"谁改了源文件就该谁提交"——它是两边
共同的输出。宁可这次不满足"bundle 与源文件同一个 commit"这条惯例,也不要把另一段会话
半成品的投资者卡改动焊进自己的提交历史。

**留下的判断**

- **`dist/bundle.md` 与全部 `index.json` 目前工作区有未提交改动,且这不是本轮遗漏
  ——是刻意不提交。** 等 P8 那段会话也提交完它自己的源文件改动后,需要有一次干净的
  "重跑 + 提交生成产物"收尾(可以是 P8 会话做,也可以是下一个新会话核对两边都已提交后
  再补)。**接手时看到这两类文件是 modified 但没在下面提交范围里,不是 bug。**
- **commit hash(84dba55)已回填**进计划文件头、`update_plan/README.md`、
  `Archived/README.md` 三处,作为同一次提交后的第二次小提交——完结清单第 7 步当次做完,
  没有留到下一次 touch 这些文件的时候。
- **计划文件已 `git mv` 进 `Archived/`**,`Archived/README.md` 加了一行索引。

### 2026-08-03 — 第三轮:P8 投资者卡渲染缺口落盘(与上一轮的 P7 是同一次并行,各自独立完成)

紧接第二轮记录的情况:Keeper 同时开了两段会话,本轮就是那段跑 P8 的会话。两边全程没有
碰对方的源文件,过程与结果和第二轮记录的判断一致——先只提交各自确实拥有的文件,
`dist/bundle.md`/`index.json` 等共享生成产物留到两边都提交完源文件后再统一收尾。

**做了什么**

1. **补全渲染出口(缺陷 1+4)**:`scripts/render-investigator.py` 与 `templates/investigator.md`
   一次性补齐 `spells`/`cthulhu_mythos`/`notes`/`occupation_detail`/`age_modifiers`/
   `skill_points`/`credit_rating` 细目/`gear`/`status`/`party`/`backstory_keys`/
   `experience_packages`/`mythos_encounters`/`growth_log`——全渲染,不再按 `type` 分支。
   必填形状的字段缺失仍占位 `<...>`;这批新增大多是可选数组/对象,JSON 里没有就整节
   省略,不给 pregen 卡铺一堆空标题。
2. **`core/13-create-investigator.md` 改 spec,不是改脚本**:删掉"elite-npc 跳过 Hooks"
   规则,换成"渲染永远面向 KP"的声明。顺带发现 `reference/rules/character-creation.md`
   §9 对同一件事的措辞和 `core/13` 从来没对齐过(一个说"跳过 Hooks",一个说"跳过
   backstory 提示"),两处一并统一。
3. **自校验分两层,都实测过**:硬性算术(派生值公式、点数账本平衡、每技能
   `value=base+职业+兴趣+成长`、信用评级区间)无条件跑;阈值型(创建期技能上限、
   特征取值区间)读 `campaigns/<slug>/investigators/validation.json`,没有就退回脚本内建
   默认值。默认警告但照渲,`--strict` 改拒渲。用 `templates/investigator.example.json`
   (已知算术正确的 fixture)验证零告警,又手工构造了破坏算术的 fixture 验证两种模式
   都能正确抓到、正确拒渲。
4. **`skill_cap` 阈值改成 90%,不是本计划文件早先猜的"7e RAW 75%"**——
   `reference/rules/character-creation.md` §5 已经落盘的权威数字是 90%,75% 是这份计划
   定案时的未核实猜测。同时发现默认 90% 会对每个 EDU>90 的角色的 `Own Language` 技能
   误报(Own Language 只是镜像 EDU,不是拿点数买的),加了一条豁免。
5. **`core/01-intake.md` 新增问题 14**(预制卡需求 + 校验阈值展示),插在原第 13 题
   之后,D/E 组顺移 15→18,"never invent a sixteenth question" 改成"a nineteenth"
   ——顺手发现这句话在插入前就已经和实际题数(17 题时写"sixteenth")对不上,是和
   第四轮记录的"六个目录"同类的漂移,这次一并订正。新建
   `campaigns/_template-campaign/investigators/validation.json` 作为默认阈值的唯一
   落盘副本,`core/01` 输出清单第六项改成"从这份模板复制"而不是在 spec 里重复一份
   JSON,避免两处同数字以后各自漂移。

**为什么这么分**:P6 的"审卡视图"讨论(缺陷 4 记录里提过的"第三种受众")最后没有真的
拆出player/KP/审计三套模板——Keeper 2026-08-02 就定过"受众唯一是 KP",所以这批新字段
全部挤进同一张卡,只是分节组织(`occupation_detail`/`age_modifiers`/`skill_points` 归进
一个"Creation ledger (KP audit)"标题下),不是拆文件。拆文件的成本(两份模板互相同步)
在受众已经唯一的前提下没有对应的收益。

**留下的判断**

- **`dist/bundle.md` 与全部 `reference/**/index.json` 现在可以安全地重跑并提交了**——
  第二轮记录的"等两边都提交完"的条件此刻已满足(P7 已提交 84dba55/3f7225e,P8 即本轮
  即将提交)。本轮收尾会重跑两个脚本并把结果纳入自己的提交。
- **P8 计划文件的"需要先查清的事"三条在 P7 落盘前就已查过**——当时 `reference/rules/`
  还没有 `magic.md`,答案是"两者互不阻塞";P7 落盘后复核确认两边改动的文件确实没有
  重叠,判断依然成立,原样记录在计划文件里,不追溯改写。
- **本批改动已提交(d9e1fef)并归档**——Keeper 确认后直接提交,计划文件已 `git mv`
  进 `Archived/`,hash 回填进计划文件头、`update_plan/README.md`、`Archived/README.md`
  三处,当次做完,没有留到下一次 touch 这些文件的时候。
