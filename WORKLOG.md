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
7. **归档件不进 bundle**,所以任何 spec 引用它们都要写成可选("if present locally")。

## 当前状态(2026-08-03)

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
  `core/01`(新增问题 14)已接线。**P1–P8 现已全部完成并归档**,活动计划只剩 P5 与 P9。
- **P9 阶段 A + B 均已完成(2026-08-03),阶段 C(神格铺设)是唯一剩下的**。
  17 项执行清单在 `update_plan/2026-08-02-monster-templates-traits.md`,分 A/B/C 三段,
  **三段全完才归档**——A/B 完成不等于计划完结,接手请直接做 C。
  - **阶段 A**(标尺与词条):`reference/rules/monster-scale.md` + 五级强度阶梯 +
    `reference/tables/monster-traits.md` 的 18 条数值词条,`core/07` 的 X 已回填。
  - **阶段 B**(索引层):扩了 `scripts/build-reference-index.py`,新增
    `parse_malleus_entries()`(从转录稿抽取全部 223 条的名称/tier/SAN/锚点)+
    `build_monster_index()`(合并 `reference/tables/monster-index-data.json` 里人写的
    223 条 `Serves`/摘要,再被匹配到的 `reference/bestiary/*.md` 条目覆盖),生成
    `reference/tables/monster-index.md`(进 bundle)。校验和缺引用出处同级——
    `Serves`/摘要留空就报错。现有 9 只 bestiary 条目已按新标尺重标(见下一条),
    `cthulhu.md` 补了反向的眷族/仆从小节,`core/07`/`core/04` 已接线检索入口。
  - **接手做阶段 C 前必看**:阶段 B 的机制(脚本)与内容(人写 223 条)**在同一个会话
    里一次做完了**,没有按原计划拆两个上下文——用 8 个并行 subagent 各分块读取转录稿、
    写 `Serves` + ≤40 字摘要草稿,汇总校验后一次性合并进
    `reference/tables/monster-index-data.json`,详情见下面「会话记录」。
    **阶段 C(铺约 6 个神格 + 8–10 眷族)现在没有任何等待项,标尺、词条、索引机制都已就绪。**
- **`reference/bestiary/` 现有 9 只的实测分布,是 P9 定案的主要依据**:threat 8/9 都是
  `deadly`(`trivial`/`mythic` 从未用过),同为 `deadly` 的 SAN 从 `0` 到 `1D4/1D10`;
  type 六类里 `beast`/`undead`/`great-old-one`/`human` 从未被单独用过,活着的两类有
  3 只被迫加括号补充。**别把这 9 只当对标样板用**——它们是在没有标尺的状态下写的,
  P9 执行清单第 9 项就是回头校准它们。
- **古神级条目住在 `reference/mythos/great-old-ones/`(现有 `cthulhu.md`),不在
  `bestiary/`。** 这条分工现在没写在任何 spec 里,P9 执行清单第 4 项负责补上。
- **kit 现在几乎是一套克苏鲁专用工具。** 在 kit 自己写的文件里统计神格提及:
  克苏鲁 **135** 次、达贡/海德拉 14/7 次(教团已立档但**神格本身没有文件**)、
  犹格-索托斯/莎布-尼古拉斯/奈亚拉托提普/伊格 各 1–2 次、**哈斯塔 0 次**。
  P9 阶段 C 是**拓宽**不是补漏,工作量按这个认。
- **`dist/bundle.md` 仍然不收 `reference/bestiary/` 也不收 `reference/mythos/`**
  (白名单只有 `core/`、`templates/`、`reference/rules|craft|tables/`,见
  `scripts/build-bundle.sh` 第 36–45 行)——但 P9 阶段 B 落地的
  `reference/tables/monster-index.md` **在** `tables/` 白名单里,已确认进 bundle。
  走 ChatGPT 链路的 KP 现在**能查到**怪物(名称/tier/SAN/服侍谁/一句摘要),但查不到
  完整 stat block(那仍然只在本地转录稿与 `bestiary/` 里)——这是设计如此,不是缺口。
- **三份 sourcebook 的手动重译已提交落地**(9c47d98);误建的空文件
  `reference/sourcebooks/新建 Text Document.txt` 已核实不存在(已清理或从未提交)。
  仍未清的账:P7 计划第 5 行的行数(写 13731,现为 5365)、`sourcebooks/index.json`
  的行数字段。malleus 头部的"转录质量"警示已随换稿重写,不再欠账;
  grand-grimoire/keeper-rulebook 两份头部警示仍未复核。

`update_plan/README.md` 末尾还有一张**按可动性排序的表**(哪个计划现在能动、卡在等谁),
接手时先看那张。

---

## 会话记录

当前没有会话记录——目前为止的改动全部已提交(见 `git log`)。P9 阶段 A+B 的落地细节
(索引脚本怎么解析转录稿、踩过的名称解析坑、9 只 bestiary 条目的改判理由)已随
commit 059ba63 落地,理由本身也直接写在了改动的文件里(各 bestiary 条目的 header、
脚本的函数注释),不在这里重复背一份——要看当时怎么想的,`git show 059ba63` 或翻
对应文件即可。开一段新的维护会话、做了还没提交的改动时,在这里加一条(格式参考
`core/15-close-session.md`);一旦对应 commit 落地,收尾时把这条记录删掉,不留存档。
