# Changelog

本 kit 的改动记录。**每完成一个 `update_plan/` 计划(或任何改变 kit 行为的改动)必须在
此追加一条**,见 `update_plan/README.md` 的「完结清单」。

格式:按日期倒序,**同一天的所有改动合并成同一条**,标题为
`## YYYY-MM-DD (<commit>, <commit>, ...)`。正文只有两个小节(没有的省略):

- `### 修复问题` —— **一个问题一句话**,说清原来错在哪、现在怎样。
- `### 更新内容` —— **一项更新一句话**,说清 Keeper 现在能做什么/必须怎么做。

只写**面向使用者**的变化——"改了哪个 spec 的哪句话"不用写。当天已有条目时,把新改动
补进那条的对应小节并在标题追加 commit,**不要为同一天新开一条**。

---

## 2026-08-04 (待回填)

### 更新内容

- **kit 不再是"只有克苏鲁"的工具了。** 新增 5 位主要外神的完整档案
  (`reference/mythos/great-old-ones/`:达贡与许德拉、哈斯塔、奈亚拉托提普、
  莎布-尼古拉斯、犹格-索托斯),每份都含苏醒/现身条件、征兆、教团崇拜方式、守秘人
  裁定空间,以及反链到具体眷族怪物的「眷族与仆从」小节。配套新增 7 只眷族/化身
  bestiary 条目(深潜者、拜亚基、哈斯塔之眷族、恐怖猎手、黑法老、黑山羊幼仔、
  犹格·索托斯之子),数值取自《怪物之锤》,文字与设计全部原创。
- **"XX 是 boss,这里的精英怪该用什么"这类问题现在真的能被回答了。** 上述新条目全部
  接入了 `reference/tables/monster-index.md` 的 `Serves` 检索——之前这张表能查到怪物,
  但除了克苏鲁外没有别的神格有对应的仆从条目可查,问"哈斯塔的精英怪是什么"会得到空集。
  P9(怪物强度标尺 + 索引层 + 神格铺设)三阶段至此全部完成并归档。

### 修复问题

- P4/P6 的计划文件头、`update_plan/README.md` 状态表在内容早已提交完成后仍停留在
  "等提交"/"进行中"措辞,现已回填 commit hash 并归档进 `update_plan/Archived/`。
- `CHANGELOG.md` 2026-08-02 条目头部的 commit 列表此前只列了 4 个(含一个"待提交"
  占位),现已核实补全为当天实际的全部 16 个 commit。
- 造精英邪教徒/反派 NPC 卡时,法术、克苏鲁神话值、KP 备注(`notes`)三个字段一律
  渲染不出来——`scripts/render-investigator.py` 直接把它们丢了,`.md` 卡面和 `.json`
  源数据不一致。P6 重建 schema 后新增的一批字段(职业细节、年龄补正、点数账本、
  信用评级细目、装备、状态、经历包、神话接触、成长记录)同样没有卡面出口。
- 怪物图鉴 `fellrock.md` 的"沉默之油"反查链接指向了 `artifacts-zh.md`,但那份文件里
  根本没有这一条——沉默之油实际是 `reference/mythos/spells/oil-of-silence.md` 的法术,
  已改正指向。
- 建索引脚本解析怪物图鉴条目名称时,把段内加粗的小标题(如"**触肢攻击**")连同后面
  无关的括号内容一起误认成条目名,导致索引表个别行显示的是攻击描述文字而不是怪物
  名——已改成要求整行以 `**` 收尾才算标题,223 条全部核对无误。

### 更新内容

- **法术、仪式、魔法书终于有了数值标尺。** 新增 `reference/rules/magic.md`:施法消耗
  (魔法值/理智值/意志值)与施法用时的记法、对抗检定怎么判、造一个新法术该怎么定价才不
  会破坏平衡,以及魔法书的研读机制(泛读/精读两阶段、CMI/CMF/MR 三值、重复精读耗时翻倍)。
  之前造 spellcaster 怪物或者写魔法书全靠现编,现在 `core/07-create-monster.md` 与
  `reference/mythos/README.md` 都指向这份速查表。
- **投资者卡渲染器补全,精英 NPC 的法术和 KP 备注终于上卡了。** `scripts/render-investigator.py`
  与 `templates/investigator.md` 一次性补齐全部缺失字段;渲染不再区分 pregen/elite-npc
  受众——工具始终是给 KP 审卡的,玩家自己建卡、KP 审后录入 JSON,预制卡需求改在
  intake 一次性问清楚(新增问题 14)。
- **渲染时自动核对算术,不用再手算点数账本对不对。** 每次渲染都会检查派生值公式、
  技能点账本是否平、每条技能的数值是否等于 base+职业+兴趣+成长、信用评级是否落在
  职业区间;还会按创建期技能上限(默认 90%)和特征取值区间给出提醒。默认只警告、
  照常渲卡;`--strict` 可以改成直接拒绝渲染。阈值可在
  `campaigns/<slug>/investigators/validation.json` 按战役调整,intake 会在新问题 14
  里先展示默认值再问是否要改。
- **克苏鲁教团文档整合(P1)全部完成并归档。** 四章内容(教团史、五个教团全档、设计
  方法论、邪教徒范型与怪物图鉴)现在都能从 `reference/README.md`/
  `reference/tables/README.md` 的目录说明里找到入口,不用翻文件树摸索;
  `reference-index` 审计确认没有孤儿文件。
- **官方数值现在可以直接抄进 `reference/` 了,不必再重写一遍。** 原规则一刀切
  "只取结构和数值刻度,不取文字",结果是查到书上的属性行也只能凭它重建一份近似值——
  怪物、法术、武器这类**本身就是规则**的内容因此永远拿不到书上的原数。现在:
  kit 自己的 `reference/` 文件**可以引用或转录官方规则内容**,在文件里标明哪本书、
  哪一章即可。**进 `campaigns/` 的内容仍然自己写**——这条没放松,但理由从版权改成牌桌:
  搬来的 NPC 是每个用同一套资料的 KP 都已经知道底牌的人。
  过渡期边界(等 P9 定完):**数值随便转,描述性文字保持原创**。
- **kit 的定位写实了:面向持有正版的 KP、不盈利、不用于传播。** 根 `README.md` 免责段、
  `CONTRIBUTING.md`、`core/00-how-to-run.md` 都已按此改写,并点明
  `reference/sourcebooks/` 收了三本整书(此前免责段只提了卡组,没提书)。
  版权方可开 issue 要求下架这条保留。
- **怪物图鉴换了一份干净得多的转录稿。** `reference/sourcebooks/malleus-monstrorum-zh.md`
  从旧的 PDF 直接提取(属性行常年断字、表格错行)换成 Keeper 手工重排版本,属性数值
  现在可以直接读,不用再逐条判读修复。
- **造非人类怪物终于有真实的强度标尺了,不再是"凭感觉"。** 新增
  `reference/rules/monster-scale.md`:五级强度阶梯(独立种族 → 仆从种族 → 唯一存在 →
  神格,人类反派另算),每级四档 threat 各自的 SAN 损失/HP/护甲/攻击技能典型区间,
  数据来自对怪物图鉴的全书统计而非估算。`core/07-create-monster.md` 里那句"人类反派
  不走这套预算"的占位话终于有了下半句:**怪物强度 = 阶梯基线 + 词条负载**。
- **怪物现在可以挂"数值词条"做强化,而且强化必须留破绽。** 新增
  `reference/tables/monster-traits.md`:18 条可挂载的数值词条(再生、分裂、免疫常规
  武器、汲取属性、疯狂凝视等),每条都强制带一个可被调查员发现的破解口,并按等级设了
  负载上限,防止一只怪物被堆到"打不过也躲不掉"。`core/11-review.md` 新增两条对应的
  审计题。
- **挑怪物强度时先看书上的「上级/下级」标签,它比自己估更准。** `monster-scale.md`
  新增一节:怪物图鉴给绝大多数种族条目标了上级或下级,而这个标签分开强度的力度**大于
  threat 四档的整个跨度**——上级组的耐久是下级组的 2–2.6 倍、攻击技能约两倍。
  用法很直接:书标下级就取该级的 trivial/moderate 两行,标上级就取 deadly/mythic 两行。
  同一轮把取样声明改成了真数(全书 223 个属性块,非"约 240"),并写明各字段的实际
  覆盖率与两处不拆的理由(护甲样本太薄、L4/L5 书上没有上下级标签)。
- **KP 现在能直接查"某神格的精英怪该用谁",不用翻一万行原文。** P9 阶段 B 落地:
  新增 `reference/tables/monster-index.md`,覆盖怪物图鉴全部 223 个条目 + 现有 9 只
  bestiary 条目,每条都标好服侍哪位神格(`Serves`)与一句区分摘要。这张表进
  `dist/bundle.md`——**ChatGPT/Gemini 链路第一次能看到怪物**,此前 `bestiary/`
  与图鉴都不在白名单里,那条链路对怪物完全空白。
- **`reference/bestiary/` 现有 9 只按新标尺重新核过一遍。** `deep-one-hybrid.md` 的
  type 从独立种族改成仆从种族(malleus 原文就是这么分类的);`fellrock.md` 的 threat
  从 deadly 改成 mythic(体型与耐久数值早已过 deadly 上限)、`thrall-of-cthulhu.md`
  从 deadly 改成 moderate(malleus 标它是"下级"仆从种族,按新标尺该取轻档);9 只都
  补齐了 Tier 与 Serves/索引摘要两个新字段。
- **神格文件现在要反向列出自己的眷族与仆从。** `cthulhu.md` 补了这一节(哪些怪物服侍
  它、哪些是它的血亲),并写进 `reference/mythos/README.md` 定为新神格文件的必备小节
  ——以后铺哈斯塔、奈亚拉托提普这些新神格(P9 阶段 C)照这个格式写,索引表才不会只有
  半条查询路径。
- `core/07-create-monster.md`、`core/04-design-scenario.md` 都接了一句:挑怪物先查
  `reference/tables/monster-index.md` 再动手写,不用翻原文猜。

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
