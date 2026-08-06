# tables/ — 随机表

备课和临场即兴用的掷骰表。**本目录一律用中文写**——守秘人日后要手动往表里加条目,中英
混排会让新旧条目一眼看出不是一批人写的。跨引用路径、文件名和数值记法(`1D10`、`STR 60`)
保持英文,措辞按 `reference/glossary-zh.md` 取词。

尽量保持年代无关;只在某个年代才成立的表,放进需要它的那个战役里。

格式:开头两行短引言(掷什么、什么时候掷),然后一张带 `dN` 列的表。

**怎么掷**:一律走 `python scripts/roll.py <table> --campaign <slug>`,不许模型自己报点数。
脚本自己解析每张表声明的骰面,战役内不放回、跨战役查重(`--fresh`)都由它管;两维表
(如 `cult-goals.md`)一次调用就把两张都掷了。细节见 `scripts/roll.py` 的文件头注释,
硬约定见 `core/00-how-to-run.md` → ground rules。

## 种子表——反套路的那一层

这四张**不是可选的调味**。守秘人给的输入很少或没有时,`core/01-intake.md` 强制要求掷这
四张。不掷,任何模型都会收敛到同一个战役:阿卡姆、一个邪教、一位旧日支配者正在苏醒。
掷了、**并且保留掷出的结果**,才是低信息量战役变具体的原因。

- `hooks.md`(1d20)——调查员是怎么被卷进来的。
- `locations.md`(1d20)——事情发生在哪儿;打断默认往小渔村滑的引力。
- `mythos-angles.md`(1d20)——那份"不对劲"到底是什么。四张里最要紧的一张。
- `npc-quirks.md`(1d20)——让 NPC 能被演出来的那个小动作。

## 备课与临场表

- `complications.md`(1d20)——这一场会出什么岔子;备课时掷两次。
- `madness-instant.md`(1D10)——疯狂发作·即时症状(逐轮处理时用,表VII)。
- `madness-summary.md`(1D10)——疯狂发作·概括症状(跳到之后概括推进时用,表VIII);
  与上一张同源(8.3 疯狂发作)但骰面用途不同,拆成两个文件是因为 `roll.py` 单维度
  解析一份文件只认第一张表,同一文件塞两张 1D10 就只有前一张摇得到。
- `phobias.md`(1D100)——恐惧症状表(表IX),规则书表格全量转录,和
  `reference/decks/phobias-and-manias-zh.md` 的精选卡组是两回事。
- `manias.md`(1D100)——躁狂症状表(表X),同上,与 `phobias.md` 同一原因拆成独立文件。
- `npc-appearance.md`(1d20)——第一眼的外形加脾性;`npc-quirks.md` 的姊妹表(外形对
  举止)。
- `cult-goals.md`(1D10 × 1D8)——邪教的愿望 × 手段;两张都掷,相乘才成立。见
  `reference/craft/cult-design-zh.md` §三。
- `cult-leader-positions.md`(1d10)——邪教首领的社会门面,以及这个位置换来的便利。
- `cult-power-sources.md`(1d4)——邪教声称的超自然背书从哪儿来。
- `cultist-archetypes.md`——12 组现成的低阶邪教徒数值(按角色分组,不是骰表),外加一套
  永生大师工具箱。`create-npc` 的配套件,见 `core/06-create-npc.md`。
- `monster-traits.md`——给怪物条目加挂的数值词条菜单(带负载点与破解口),配
  `reference/rules/monster-scale.md`。
- `monster-index.md`——223 条神话生物的导航表,**脚本生成,不要手改**;数据源是
  `monster-index-data.json`。
- `weapons-index.md`——表XVII 全部武器按威胁强度重排(不是骰表),给反派配装备时手选;
  和 `reference/decks/weapons-and-artifacts-zh.md` 的按品类原表分工不同,见该文件头部。

## 加新表

一张表一个文件,`kebab-case.md`。前两行就写清楚掷什么骰、什么时候掷。宁可 20 条具体的,
也不要 100 条含糊的——一张真会被读完的表,胜过一张只会被扫一眼的表。

可以考虑的选题:`rumours.md`、`investigator-names.md`、`weird-details.md`、
`what-the-cultist-carries.md`、`sounds-in-the-dark.md`。
