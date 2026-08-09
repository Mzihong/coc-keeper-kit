# Changelog

本 kit 的改动记录。**每完成一个 `update_plan/` 计划(或任何改变 kit 行为的改动)必须在
此追加一条**,见 `update_plan/README.md` 的「完结清单」。

格式:按日期倒序,**同一天的所有改动合并成同一条**,标题为
`## YYYY-MM-DD (<commit>, <commit>, ...)`。正文只有两个小节(没有的省略):

- `### 修复问题` —— **一个问题一句话**,说清原来错在哪、现在怎样。
- `### 更新内容` —— **一项更新一句话**,说清 Keeper 现在能做什么/必须怎么做。

只写**面向使用者**的变化——"改了哪个 spec 的哪句话"不用写。当天已有条目时,把新改动
补进那条的对应小节并在标题追加 commit,**不要为同一天新开一条**。

**篇幅是硬约束:每条 ≤2 行**(按本文件的折行宽度算)。写不下的是背景、证据、取舍理由
——那是 `WORKLOG.md`(为什么这么分)和 commit message 的活,不是这里的。**不要照着上
一条的样子写**;条目会一次比一次长,就是因为每个会话都在模仿前一条而不是这条规则。
参照系看 `## 2026-08-02`:39 条 48 行。

---

## 2026-08-09

### 修复问题

- `WORKLOG.md` 的「还没还的债」7 条里 1 条早已还清、3 条前提或位置已失效(含一条指着已被删除的
  文件),现逐条 grep 核过:删 1 条、重写 3 条,剩 6 条,表尾标注核验日期。
- `beyond-the-treeline` 的 08-08 重构留下的残留:已答的问号仍在四份文件里当悬念、专名两种写法、
  转译词表五行漂移、一句指着已删机制的说明——全部对齐到权威文件。
- `core/15-close-session.md` 列举 ad-hoc 会话适用哪几项完结清单时漏了第 8 项「反向扫描」,
  于是没有计划文件的重构一直绕过它;现已补进适用清单。

### 更新内容

- `core/15-close-session.md` 新增 "Re-verify the debt table":收尾时必须逐条复核债表——已还的删、
  行号漂的改,并盖上核验日期。原本没有任何流程会回头查它。
- 新增 `python scripts/check-campaign-consistency.py --campaign <slug>`:6 项机械检查(专名漂移、
  词表逐行 diff、问号跨文件比对、被删设定残留、死链、路径旁的计数)。**`SKIPPED` 不等于通过。**
- 改动 ≥3 份战役文件、或动了任何已声明的规约设定,收尾**必须**跑上面那个脚本 + `core/11-review.md`,
  并把结论写进当天的 changelog 或会话日志——没有产物就没法事后核。
- **发现两份文件对同一事实说法不同时,只上报、不自己处理**:说清哪边更新、依据是什么,由守秘人裁决。
  优先级规则(战役 `CLAUDE.md` 赢)是给守秘人裁决用的判据,不是静默对齐的许可。
- `beyond-the-treeline` 定了新硬规约:**旧世界的东西一律不工作**,要让某件还在动必须先有站得住的
  理由,而且那个理由本身得是线索;不许"微弱地动",也不解释它凭什么撑一千两百年——一解释就是科幻。

## 2026-08-08 (d56c0dc, 22aaf78, 144d05f, 2075e88, dcc82c2, e46bfd8)

### 修复问题

- `core/12-canon-update.md` 要求给每个 NPC 文件追 interaction history,但两级制下 stub 没有文件——
  现改为成卡追进自己文件、stub 改花名册那一行的状态列。
- 模板战役 `sessions/README.md` 教的文件名(`session-01.md`)与 `core/` 的 `sessions/<n>-<slug>.md` 对不上,
  已按 `core/` 改正并补上「场次编号跨幕连续、不重置」。
- 模板战役的子目录 README 自初始 commit 起没动过(缺 event-clock、地图、interaction history、
  `reference/craft/` 等),已一并补齐。
- 地图上的长注释会被画到画布外看不见,现改为图上只留编号圆圈、注释移到右侧栏自动折行——旧地图重跑渲染即可。
- `core/01-intake.md` 的建目录清单漏了 `investigators/`,并补写各子目录 README 要从模板复制过去。
- 挑一只怪时没有任何路由指向索引层,`reference/bestiary/`(17 条)会被当成可用怪物清单——现在
  `core/00` 路由表把「挑」与「造」分成两行,挑怪指向 `monster-index.md` 的 223 条。
- `WORKLOG.md` 涨到 502 行、大半是已归档计划的执行史,已剪到 186 行并补立两条剪枝规则与行数上限。
- pipeline 只有 9 步而 `core/` 有 17 个文件,看着像少了 8 个——现已写明文件号 ≠ 步骤号,并列出
  4 个不在流水线里的 spec(本文、`02` 查表、`14`/`15` 维护)。

### 更新内容

- 生成默认改成「按需」:会写进 `campaigns/` 的技能开跑前先给一份 ≤15 行清单等你确认,说「全量展开」可跳过。
- NPC 分两级:默认只在 `npcs/roster.md` 留一行,真被检定、战斗或实质对话点到才升级成完整卡面。
- 场景散文默认不落盘、临场在对话里给你,场景文件的朗读正文可先留 `<pending>`。
- 备课默认只读四份文件(`CLAUDE.md`、近期 canon-log、`event-clock.md`、`roster.md`,合计 ≤400 行),
  `world/` 其余按路由表按需查;事件时钟默认只建前 3 刻。
- `review-material` 现在能分辨「按需未生成」(花名册/线索矩阵里挂了号)与真正的断链,前者不再算问题。
- `scripts/render-map.py` 新增家具层与 `--player` 玩家版开关,玩家版会先报预估 token 成本(约 3–5 倍)再等确认。
- 同一渲染器新增折线与指北针图元,`rooms` 留空即站点图模式——庄园/野外不用另开一套画法。
- 越界或互相压住的家具会被挡下来,不会静默出一张画错的图。
- 玩家版地图的注释重排为连续编号,守秘人版每条非秘密注释附一个 `(PL ②)` 对照;建议一张图 ≤8 条注释。
- 新增 `compile-module` 技能与 `core/16-compile-module.md`:把打完的一幕编译成线性可读的模组文本,
  先出缺口报告再编译(P18 阶段 1–3,计划未完结)。
- changelog 条目篇幅改成硬约束(每条 ≤2 行,背景与理由归 `WORKLOG.md`),08-05 至 08-08 四条已压回该体例。

---

## 2026-08-07 (11f90b0, 86f1335, 7731a01, 090cd3c, e40071a, c80530f)

### 修复问题

- `core/07-create-monster.md` 的 Output 段没写神格(L5)的例外,神格页会被存进 `reference/bestiary/`,已补上例外。
- 怪物索引的说明还写着 bundle 时代的旧话(「没有仓库的 Keeper 唯一能看到 223 条的渠道」),已改写成它真实的定位。
- `core/00-how-to-run.md` 与 `core/14-archive-reference.md` 指着早已摘掉的 `reference/external/` 子模块,三处一并清理。
- `core/00-how-to-run.md` 的 Layout 树漏了已在用的 `reference/mythos/spells/`,已补上。
- 六份神格页此前只能被写进去、没有流程会读它们,现已收进 `monster-index.md` 一节,起草世界观与威胁类型时会被指到。
- 卡本 `--strict` 会在一个自称「可能是误报」的检查上硬失败(正常的老年调查员被判死),现在只有硬性算术错误才中止渲染。
- `core/11-review.md` 的三线索复查只数「有没有三条」,现改为三项追溯:能否被一次性灭口、会否同一时钟腐坏、场景有无入边。
- `reference/tables/README.md` 把种子表说成含 `npc-quirks.md`,实际掷的是 `complications.md`,已按 `core/` 改正。

### 更新内容

- 新增 `templates/great-old-one.md`,照现有六份神格页的实际写法定型,不再照着一份内容文件现抄。
- 新增 `reference/tables/clue-engines.md`(十台线索引擎),设计剧本时先掷 2–3 条决定线索从哪来,不再总收敛成查账+查地产+找目击者。
- 三条线索规则新增六条设计期自查(`core/04` 第 5 步),`templates/scenario.md` 的线索地图表加门槛类型与保质期两栏。
- `core/05-event-clock.md` 新增一条 trigger:玩家卡关触发反派动手,那个动作本身就是新线索。
- `update_plan/README.md` 完结清单新增反向扫描(这个计划让哪些既有说法失效),`core/15-close-session.md` 补上对应两步。
- 新增 `reference/craft/town-anatomy-zh.md`,建 town/locale 前先读:一个区靠哪四维立住、地点条目怎么写、NPC 该挂在哪。
- 新增 `reference/tables/town-institutions.md`(1d20),掷 N 次填一个镇或一个区的机构清单,N 随规模走。
- `reference/craft/diagram-conventions-zh.md` 新增 §六 文字地图卡,跑不了渲染器时用纯文字表格写相邻关系,附三个样例。
- 新增 `scripts/render-map.py`:一份 JSON 渲出 SVG 平面图,`templates/location.md`/`scene.md` 加可选 Map 小节(暂只有守秘人版)。
- `core/04` 第 6 步接上按需掷骰:场景需要的地点若 `world/` 里没有,当场跑 `roll.py locations`。
- 新增 `reference/tables/confrontation-grounds.md`(1d20):对抗场面的地形与限制、场上能用什么、为何走不掉、怎么才算收场。
- 新增 `reference/tables/scenario-shapes.md`(1d10,十种互斥结构),`core/04` 的第一步之前先掷模组形状。

---

## 2026-08-06 (c368b90, bfc7eb5)

### 修复问题

- `chases.md` 把追逐当抽象距离比 MOV 高低,与规则书的地点+行动点体系完全不是一回事,载具速度表也是自造的,已按第七章重写。
- `madness.md` 的十条症状与规则书表VII 顺序和内容都不同(骰到 4 号是两件事),已按原表重排并补上表VIII。
- `combat.md` 的重伤阈值没写清,现明确为「伤害 ≥ 角色最大生命值的一半」。
- `sanity.md` 把疯狂发作时长写成定值 10 轮,实际是 1D10 轮且只在发作时有其他调查员在场时成立。
- `combat.md` 把全自动射击的四级难度阶梯串成了七级链,已改回普通→困难→极难→大成功→不可能。
- `skill-checks.md` 的对抗检定平手规则整条是错的(实为技能值高者胜),并补上不适用难度等级、不能孤注一掷等三条。
- 孤注一掷与幸运值的限制写窄了/写漏了(任何失败检定都能推;幸运不能用于幸运、伤害、理智检定),已按书改正。

### 更新内容

- 战斗、追逐、理智三份速查表按《守秘人规则书》第六、七、八章逐节重写,补齐战技、突袭、护甲、险境与行动点、疯狂三阶段等整块缺失,每节标了行号。
- 其余四份速查表(`skill-checks` `character-creation` `magic` `monster-scale`)同样补齐,新增社交难度、幕间成长、六套替代建卡法、施法检定、第十四章通用怪物框架。
- `reference/rules/` 全目录连同六个年代包统一改成中文正文,不再是「三份中文、其余英文」。
- 新增 `phobias.md`(表IX,100 条)、`manias.md`(表X,100 条)与 `weapons-index.md`(按威胁强度四档);
  `madness.md` 拆成即时/概括两份,否则 `roll.py` 只认得到第一张表。
- 规则书降级为本地核对底本,仓库里 8 处「回去翻原文」的引用已改指对应速查表。
- 转载边界放宽:规则条文本身可直接引用(标出处),仍只取手法不取文字的是虚构散文。
- 速查表里 13 处「指了也找不到」的引用(表XVII、表III、规则书页码)已改指仓库内文件或把规则本身写了进来。
- 新增 `reference/rules/README.md`——七个 `reference/` 子目录里此前唯一缺 README 的一个。

---

## 2026-08-05 (148bb91, 3f937f6)

### 修复问题

- 开新团时模型会跳过 intake、一句不问就把整个战役建好,现在 intake 第一步是发问后停下,除非你一开口就交出全权;三份适配器同步。
- `templates/cult.md` 与 `cult-design-zh.md` 让你照一份根本不存在的 mermaid 势力图惯例画,两处已改指 `craft/diagram-conventions-zh.md`。
- `dist/bundle.md` 漏收 `reference/bestiary/` 与 `mythos/`(打包白名单是手写的),已改成连子目录一起收。
- 「什么进 bundle」散在六七个 README 和 spec 里各说一遍且措辞不一,已统一到 `reference/README.md` 一节,其余改为指向它。
- P4/P6 的计划文件头与状态表在内容早已提交后仍写着「等提交」,已回填 commit 并归档。
- `CHANGELOG.md` 2026-08-02 条目的 commit 列表只列了 4 个(含一个占位),已核实补全为当天实际的 16 个。
- 精英 NPC 卡的法术、克苏鲁神话值、KP 备注渲染不出来,`render-investigator.py` 已补齐 P6 重建 schema 后新增的全部字段。
- `fellrock.md` 的「沉默之油」反查链接指向不含该条目的 `artifacts-zh.md`,已改指 `mythos/spells/oil-of-silence.md`。
- 建索引脚本把段内加粗小标题误认成怪物条目名,已改成整行以 `**` 收尾才算标题,223 条核对无误。

### 更新内容

- 掷骰改走 `python scripts/roll.py <表名> --campaign <战役>`,同战役内不重样(`--fresh` 跨战役避重),不许模型自己报数。
- 战役文件夹新增 `rolls.log` 记录掷过哪张表与哪一条,`review-material` 会核对,对不上号判不通过。
- `reference/_source/` 的阿卡姆转出文本与地图样本改为随仓库分发(仅 `.pdf`/`.docx` 原件留本地),规则书与怪物之锤转录稿保持入库。
- 但阿卡姆属虚构内容:造镇仍只取手法不取文字,可直接转录的始终只有规则内容且须标出处。
- 新增 5 位外神完整档案(达贡与许德拉、哈斯塔、奈亚拉托提普、莎布-尼古拉斯、犹格-索托斯)与 7 只眷族/化身 bestiary 条目。
- 上述条目全部接入 `monster-index.md` 的 `Serves` 检索,「哈斯塔的精英怪是什么」不再返回空集(P9 三阶段完成并归档)。
- 新增 `reference/craft/diagram-conventions-zh.md`(势力图/场景网/区域图 + 何时不该画),硬约定是每条连线必须写清连接二者的是什么。
- bundle 整条链路退役:不再有 `dist/bundle.md`,代价是只能上传单个文件的用法从此不受支持(codex 注意从 kit 根目录开会话)。
- 规则书、怪物图鉴、卡组可被 spec 直接依赖,不再写成「本地若有」;仍拿不到的只有不入库的 `reference/_source/`。
- 「不能搬进战役」的理由从分发改成版权+牌桌:第三方资料随便读、随便引数值,人名背景秘密永远自己写。
- `core/04` 新增场景网:节点是场景、边标签是靠哪条线索过去,任何必到场景入边少于三条就是卡点。
- 新增 `reference/rules/eras/` 六个年代包(只写与基准的差集),`character-creation.md` 首次明说自己是 1920s 基准。
- intake 报年代时明说走哪条路径(书本有的直接用/年代相近的推导 delta 并标未经背书/体系外不背书),年代串味会被 `review-material` 抓到。
- `reference/tables/` 全目录改中文(路径与 `1D10`/`STR 60` 这类记法保持英文),Keeper 手写的中文行不再和原有条目不像一批人写的。
- 不报地点开团时,默认舞台从中国改成美国、次选日本——地点跟类型走不跟语言走;并写明「默认美国不等于默认阿卡姆」。
- `glossary-zh.md` 新增「外文专名的译写」一节,`core/03`/`core/06` 取名按它,`core/11` 按它查同一个人有没有两种写法。
- 新增 `reference/rules/magic.md`:施法消耗与用时、对抗判定、新法术定价,以及魔法书研读两阶段与 CMI/CMF/MR 三值。
- `render-investigator.py` 与 `templates/investigator.md` 补齐全部缺失字段,渲染不再区分 pregen/elite-npc 受众。
- 渲染时自动核对派生值、点数账本、技能构成与信用评级,默认只警告、`--strict` 拒绝渲染,阈值可在 `validation.json` 按战役调整。
- 克苏鲁教团文档整合(P1)全部完成并归档,四章都能从 `reference/` 的 README 找到入口,无孤儿文件。
- `reference/` 自己的文件可以引用或转录官方规则内容(标明哪本书哪一章),进 `campaigns/` 的内容仍然自己写。
- kit 定位写实:面向持有正版的 KP、不盈利、不用于传播;免责段补上 `reference/sourcebooks/` 收了三本整书。
- `malleus-monstrorum-zh.md` 换成 Keeper 手工重排的转录稿,属性数值可以直接读,不用再逐条判读修复。
- 新增 `reference/rules/monster-scale.md`:五级强度阶梯 × 四档 threat 的 SAN/HP/护甲/攻击区间,数据来自全书统计而非估算。
- 新增 `reference/tables/monster-traits.md`:18 条数值词条,每条强制带一个可被发现的破解口并按等级设负载上限;`core/11` 新增两条审计题。
- `monster-scale.md` 新增一节:书上的上级/下级标签分开强度的力度大于 threat 四档的整个跨度(耐久 2–2.6 倍),取样声明改成真数 223 个属性块。
- 新增 `reference/tables/monster-index.md`,覆盖怪物图鉴全部 223 条 + 当时 9 只 bestiary 条目,每条标 `Serves` 与一句区分摘要。
- `reference/bestiary/` 当时的 9 只按新标尺重核(deep-one-hybrid 改仆从种族、fellrock 改 mythic、thrall-of-cthulhu 改 moderate),补齐 Tier 与 Serves。
- 神格文件须反向列出「眷族与仆从」,已写进 `reference/mythos/README.md` 定为新神格页的必备小节。
- `core/07` 与 `core/04` 接线:挑怪物先查 `monster-index.md` 再动手写,不用翻原文猜。


---

## 2026-08-02 (713cd1c, 9c011f3, a7cb4f6, 97c87d8, 39d1625, 0769902, 610dd3b, 9c47d98, 7e42d2a, ef4936a, e34d3db, 0c736ee, 66d32d2, d91f487, e0d026b, aceddf9)

### 修复问题

- 维护规则要求填 changelog,但仓库里没有 `CHANGELOG.md`,现已补上。
- 已归档的 P2 计划文件头与状态表不一致,现已同步为"已完成(e0d026b)"。
- Maintenance 规则此前只写在 `CLAUDE.md`,现三份适配器已同步一致。
- 投资者建卡顺序颠倒(先算技能点再定年龄,年龄会改 EDU),现改为先定年龄再算点数。
- 投资者卡渲染会丢失技能专精(两条 `Science` 渲成一样),现合成显示为 `Science (Engineering)`。
- `build-reference-index.py` 不递归扫描,`mythos/` 子目录下的文件此前完全漏检,现已改为递归扫描。

### 更新内容

- 新增 `update_plan/README.md` 的完结清单(状态同步、changelog、产物重建等七组收尾检查项)。
- 新增同一 campaign 内的多章(arc)编号与索引惯例。
- canon-log 新增 Interlude(幕间)条目,记录章节间的时间跳跃与世界变化。
- 新增平行世界分支 campaign 惯例(`Lineage` 字段 + 父线只读继承)。
- 新增章节结清后归档 event-clock 的惯例。
- 新增剧本结束时的 SAN 回复与成长判定惯例。
- 新增 `create-investigator` 技能:JSON 唯一真源 + 渲染投资者卡面。
- 新增追逐、人物创建、理智三份速查表。
- `design-scenario` 新增在既有 campaign 开新章的路径。
- 人数缩放惯例并入 `design-scenario` 与 `review-material` 的审查项。
- 投资者卡 schema 按真实车卡表重建,补齐年龄补正、点数账本、装备、背景等字段(旧记录仍合法)。
- `character-creation.md` 补齐年龄补正、Build/伤害加值、技能基础值等建卡数据,可用来审核他人交的卡。
- `create-investigator` 建卡顺序改为八步,并加上点数账本必须平的验收口径。
- 新增 `investigator.example.json` 一张字段填满、算术已核对的样卡。
- kit 转载规则改为分层:生成内容不含原文,官方资料可收录但须标注 `## 引用出处`、只取结构不取文字。
- 补上一个 bundle 缺件:洛夫克拉夫特笔法笔记此前从未进 `dist/bundle.md`,现已收进 bundle。
- 新增 `reference/craft/`(手法提炼稿),与 `reference/rules/`(数值速查)分工。
- 反向索引扩到全部七个目录,新增 orphan(无人引用)检查。
- `reference/decks/`(卡组)与 `reference/sourcebooks/`(整书)分类归位,本轮收录 7 份官方资料。
- 官方法术、怪物、规则原文本地可查(卡组/书本身不进 `dist/bundle.md`,所有引用按可选处理)。
- 新增归档第三方资料的技能 `archive-reference`,七步走完分类、命名、引用、接线、重建索引。
- 新增反向索引 `reference/index.json`(按 `## 引用出处` 解析出处、全仓库扫描引用行号)。
- P7 魔法速查阻塞解除(转换稿已归档为 `grand-grimoire-zh.md`)。
- 新增 `WORKLOG.md`,给接手会话的协作者用的结构与约定速览。
- 新增 `reference/decks/` 与首份收录件 `busybodies-zh.md`(官方好事者卡组,47 张 NPC 卡)。
- `character-creation.md` 各小节补上数据来源指路(标明取自哪个源文件/章节)。
- 新增收尾维护会话技能 `close-session`,收尾时强制 grep 核对日志里的数量词/路径。
- 新增人类反派强度预算:普通人类照官方 NPC 卡校准,首领按法术资历或装备总价加增量。
- 新增邪教设计方法论 `craft/cult-design-zh.md`,配四张骰表与 `templates/cult.md` 模板。
- 教团文档第一/二章落盘:新增克苏鲁本体 lore、历史条目表与五个具体教团全档。
- 教团文档第四章落盘(P1 四章全部完成):新增邪教徒原型速查、8 个怪物、造物与配套法术。
- intake 新增"The threat"与反派强化两问,答案写入 campaign `Threat` 字段供后续 spec 读取。
- NPC 档案新增互动史记录节(当前态度 + 逐场一行事实),`update-canon` 收尾清单纳入必需项。

---

## 2026-08-01 (d213f2e, bd7cd5a, 55d1e8e, 93f8258)

### 修复问题

- 端到端彩排暴露的四处 spec 缺陷已修复。

### 更新内容

- **所有指令收进 `core/`**,`CLAUDE.md` / `GEMINI.md` / `AGENTS.md` 降级为三份薄适配器,Claude、Gemini、ChatGPT 共用同一份来源——**改 kit 行为改 `core/`,不改根适配器**。
- `.claude/skills/` 下的技能全部改为指向 `core/` 对应 spec 的薄包装。
- `scene-description` 技能更名为 `description`。
- 新增 `dist/bundle.md`(由 `scripts/build-bundle.sh` 生成),供 ChatGPT 单文件上传。
- `reference/` 扩充:中文术语表 `glossary-zh.md`、洛氏写作笔记、怪物与神话资料。

---

## 2026-07-29 (339a89b, 4558135)

### 更新内容

- CoC 7 版 Keeper 准备工作台首次发布:intake → 世界 → 事件钟 → 卡司 → 剧本 → 审查 → canon 更新的完整流水线,以及配套技能与模板。
