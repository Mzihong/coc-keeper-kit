# 7e Character Creation — cheat-sheet

> Quick-fire pregen/investigator reference. **Mechanics only** — formulas, bands, and the
> shape of each field. It is not a rules reproduction: the occupation list, the skill
> descriptions, and the phobia/mania tables stay in the *Keeper Rulebook* and
> *Investigator Handbook*. Look them up there; record the *numbers* here.
>
> The data model that holds all of this is `templates/investigator.schema.json`.
> The build order is `core/13-create-investigator.md`.
>
> **Sourcing convention:** every section below carries a **来源** line — a pointer to where
> the numbers came from, never a quote. Precision is capped at what's actually been verified:
> - Where a rulebook chapter/appendix number is cited, it's because the source material
>   itself named it explicitly (traced, not guessed).
>   Nothing here is invented as fact.
> - Everything else cites the traceable intermediate source — which sheet of the reference
>   character sheet workbook it was extracted from — and is marked **章节号未核实**
>   (rulebook chapter number not yet confirmed). Filling those in requires an actual read of
>   the *Keeper Rulebook*'s character-creation chapters, which hasn't happened yet — tracked
>   in `update_plan/2026-08-02-investigator-cards.md`. Until then, treat the sheet-level
>   citation as the honest ceiling of what's confirmed.

## 1. Characteristics

- **3D6 × 5** — STR, CON, DEX, APP, POW, and **Luck**.
- **(2D6+6) × 5** — SIZ, INT, EDU.
- Point-buy is a valid alternative when a table wants control over randomness.
- Reading the scale: 15 = feeble, 50 = average adult, 90 = the best you have ever met,
  99 = human ceiling. **SIZ and POW are the only two that may exceed 99**; EDU caps at 99.
- Luck is rolled, not derived. It is a resource in play — see
  `reference/rules/skill-checks.md`.

来源:`COC apolo.xlsx`『属性注释』sheet(章节号未核实)。

## 2. Age — pick the age first, then pay for it

Age is not flavour; it moves characteristics before anything is derived.

| Age | Physical deduction | APP | EDU | Move |
|-----|--------------------|-----|-----|------|
| 15–19 | −5 split across STR **and SIZ** | — | −5, and roll Luck **twice, keep the better** | — |
| 20–39 | — | — | 1 EDU improvement check | — |
| 40–49 | −5 split across STR/CON/DEX | −5 | 2 checks | −1 |
| 50–59 | −10 | −10 | 3 checks | −2 |
| 60–69 | −20 | −15 | 4 checks | −3 |
| 70–79 | −40 | −20 | 4 checks | −4 |
| 80–89 | −80 | −25 | 4 checks | −5 |

- **EDU improvement check:** roll D100. Over current EDU → EDU gains 1D10 (cap 99).
  Under or equal → no change. Do this *before* computing occupation skill points, since
  most occupations pay out of EDU.
- Record what was applied in `age_modifiers` — a reviewer must be able to re-derive the
  final characteristics from the rolls.

来源:`COC apolo.xlsx`『附表』sheet 的年龄补正区(隐藏 sheet;章节号未核实)。

## 3. Derived stats

| Stat | Formula |
|------|---------|
| **HP** | (CON + SIZ) ÷ 10, round down |
| **Major wound** | half maximum HP — a single hit at or above it is a major wound |
| **MP** | POW ÷ 5, round down |
| **SAN (start)** | = POW |
| **SAN (max)** | 99 − Cthulhu Mythos% |
| **Move** | 8 base; **7** if STR *and* DEX are both below SIZ; **9** if both are above; then apply the age penalty |
| **Dodge** | DEX ÷ 2 (a skill — it can be raised with points like any other) |
| **Own Language** | = EDU |
| **Build / Damage Bonus** | from STR + SIZ, below |

| STR+SIZ | Damage Bonus | Build |
|---------|--------------|-------|
| 2–64 | −2 | −2 |
| 65–84 | −1 | −1 |
| 85–124 | none | 0 |
| 125–164 | +1D4 | 1 |
| 165–204 | +1D6 | 2 |
| 205–284 | +2D6 | 3 |
| 285–364 | +3D6 | 4 |
| 365–444 | +4D6 | 5 |

Above 444, every further 80 points adds +1D6 and +1 Build.

来源:`COC apolo.xlsx`『属性注释』sheet(HP/MP/SAN/Move/Build/DB 各公式区;章节号未核实)。

## 4. Occupation — three things, always

An occupation is not a job title. It supplies exactly three mechanical things; if you invent
one, invent all three and get the Keeper's sign-off before the numbers are spent.

1. **A skill-point formula.** The families in play:
   - `EDU × 4` — the academic/professional default.
   - `EDU × 2 + X × 2` where X is the characteristic the job leans on — DEX for
     acrobats and thieves, STR for brawlers and labourers, APP for performers and
     confidence artists, POW for the devout.
   - The formula is a *ceiling*, not a target: 78 EDU on `EDU × 4` = 312 points.
2. **A Credit Rating band**, e.g. 30–60. Occupation points must bring Credit Rating to at
   least the band's **lower bound** before anything else is bought. Sitting outside the band
   is allowed when the concept demands it — a broke doctor, a rich drifter — but it is a
   deliberate call, not an accident.
3. **A skill list.** Occupation points may only be spent on this list. Most lists carry one
   or more **free-choice slots** ("any one other skill", "two personal or era specialities") —
   name them explicitly on the sheet so the Keeper can audit the card at a glance.

The occupation also implies **contacts** — the professional circle the job puts them in
touch with. That is the cheapest hook source on the whole sheet; harvest it in step 4.

来源:`COC apolo.xlsx`『职业列表』sheet(230 个职业行,含信用区间/职业属性/技能点/
本职技能/推荐关系人各列;章节号未核实)。

## 5. Skill points

- **Occupation points:** per the formula above. Occupation-list skills only.
- **Personal interest points:** **INT × 2**. Any skill.
- **Cap:** no skill exceeds **90%** at creation. Many tables announce a tighter cap up front
  (e.g. "70 occupation / 60 interest") — if the campaign declares one, put it in
  `skill_points.cap`.
- **Cthulhu Mythos** starts at **0** and is never bought at creation. Raising it lowers
  maximum Sanity permanently.
- **Credit Rating** is bought with occupation points like any other skill, from a base of 0.

**Base values.** A skill's `base` is where it starts before a single point is spent — the
ledger check in §10 needs it, so record it.

| Base | Skills |
|------|--------|
| **1%** | Anthropology · Archaeology · Artillery · Demolitions · Diving · Electronics · Hypnosis · Lip Reading · Locksmith · Medicine · Operate Heavy Machinery · Psychoanalysis · Pilot (any) · Language (Other) · Science (any) · Lore (any) |
| **5%** | Accounting · Animal Handling · Appraise · Art/Craft (any) · Computer Use · Disguise · Fast Talk · History · Law · Occult · Ride |
| **10%** | Electrical Repair · Mechanical Repair · Natural World · Navigate · Persuade · Psychology · Sleight of Hand · Survival (any) · Track |
| **15%** | Charm · Intimidate · Fighting (Axe) |
| **20%** | Climb · Drive Auto · Firearms (Handgun) · Jump · Library Use · Listen · Stealth · Swim · Throw |
| **25%** | Fighting (Brawl) · Firearms (Rifle/Shotgun) · Spot Hidden |
| **30%** | First Aid |
| **special** | Dodge = DEX ÷ 2 · Own Language = EDU · Credit Rating = 0 · Cthulhu Mythos = 0 |

来源:`COC apolo.xlsx`『技能注释』sheet,逐项技能的"基础成功率"列。这个 sheet 自己的
表头写明"详见规则书**第四章:技能**"——是源材料自带的章节引用,直接沿用,非推测。

### Umbrella skills

Art/Craft, Science, Survival, Fighting, Firearms, Pilot, Language (Other), and Lore are
**never bought generically**. Buy a named specialisation — `Science (Physics)`,
`Fighting (Brawl)`, `Language (Russian)` — and each one carries its own base value and grows
on its own.

In the JSON, put the **family** in `name` and the **specific** in `specialization`
(`name: "Science"`, `specialization: "Physics"`). Don't repeat the specialisation inside
`name`; the card renderer composes the two.

Two optional spillovers a table may run (settle before cards are built):

- **Art/Craft and Science:** taking one specialisation to 50% raises sibling specialisations
  by +10 (never past 50); at 90% they rise +10 again (never past 90).
- **Language:** the same, applied across languages in the same family.

来源:`COC apolo.xlsx`『技能注释』sheet「技能可选规则」区(专业技能可转移的优势;
章节号未核实——同一 sheet 的第四章引用是针对技能主表,不确定是否覆盖这条可选规则)。

## 6. Credit Rating → what they can actually afford

Credit Rating is the only economic stat. It converts to a lifestyle, not to a budget
spreadsheet. **1920s USD**:

| Lifestyle | CR | Cash | Assets | Casual spending |
|-----------|-----|------|--------|-----------------|
| Penniless | 0 | $0.50 | none | $0.50 |
| Poor | 1–9 | CR × 1 | CR × 10 | $2 |
| Average | 10–49 | CR × 2 | CR × 50 | $10 |
| Wealthy | 50–89 | CR × 5 | CR × 500 | $50 |
| Rich | 90–98 | CR × 20 | CR × 2,000 | $250 |
| Super rich | 99 | $50,000 | $5,000,000+ | $5,000 |

Other eras keep the same bands and rescale the multipliers — a modern-USD game runs roughly
20× the 1920s figures. Set the campaign's currency and scale once in
`campaigns/<slug>/CLAUDE.md`, then record the resulting numbers in `credit_rating`.

Below "casual spending", don't roll and don't itemise. Above it, the purchase is a scene.

来源:`COC apolo.xlsx`『资产及物价参考』sheet「资产参考表」区(CR→生活水平/现金/
其他资产/消费水平换算,含 1920s 美元/现代美元/2010s 人民币等多套换算;此表本身
章节号未核实。**注意区分**:同一 sheet 里另有一张「现代物价参考表」(单品价格,
本文件未收录)明确标注来源为『守秘人规则书:附录Ⅲ:物价表』——那条引用属于那张
单品价表,不属于这里的 CR 换算表,不要混用)。

## 7. Backstory — eight prompts, then a cut

Fill **all eight**, then keep only what this campaign can pull on:

Personal description · Ideology/beliefs · Significant people · Meaningful locations ·
Treasured possessions · Traits · Injuries & scars · Phobias & manias

Two rules that make them worth the ink:

- **Mark the key entries.** One or two entries are the ones the investigator *is* — record
  them in `backstory_keys`. Honouring a key bond restores Sanity; losing it costs Sanity for
  good. An unmarked backstory is decoration.
- **Every surviving entry names something in the campaign** — an NPC, a faction, a location,
  the central mystery. "His wife" is not a hook. "His wife, who works the switchboard at the
  cannery" is.

Insanity feeds directly off this list: madness episodes reach for significant people,
ideology, and treasured possessions by name. A thin backstory makes a thin breakdown.

来源:`COC apolo.xlsx`『人物卡』sheet「背景故事」栏(八项 + 每项旁的"关键"勾选框);
章节号未核实。

## 8. Optional pre-play history ("experience packages")

Some tables let an investigator buy a slice of history with starting Sanity — a war, a beat,
a stretch inside, a hospital ward, a Mythos brush. The shape is always the same:

**pay Sanity → gain a mechanical edge → accept a constraint and a mandated backstory entry.**

Typical trade: 1D10 Sanity for immunity to Sanity loss from corpses, plus a minimum starting
age and a mandatory war/job-related scar, phobia, or mania. A Mythos brush instead grants
Cthulhu Mythos points and mandates two backstory entries.

This is a house option, not core 7e. If the campaign uses it, declare it in the campaign's
`CLAUDE.md` and record each package in `experience_packages` — including the constraint, so a
reviewer can check the age and backstory actually honour it.

来源:`COC apolo.xlsx`『附表』sheet「经历包」表(战场/警务/罪犯/医务/神话经历包五种)。
源材料自己把这张表标成"**可选规则**:有故事的调查员"——「house option, not core 7e」
这个定性直接取自源材料的标签,不是我加的判断。规则书对应章节未核实。

## 9. Pregens vs. elite NPCs

- A **pregen** built for a specific scenario has Credit Rating, skills, and backstory hooks
  tuned to the plot. See `core/13-create-investigator.md`.
- An **elite NPC** (a named cultist, a rival investigator) reuses the same schema and sets
  `"type": "elite-npc"`. It may legitimately carry `spells`, `cthulhu_mythos`, and
  `mythos_encounters`, which a starting pregen may not. The rendered card is KP-facing for
  both types — nothing is skipped by `type`; see `core/13-create-investigator.md`.

## 10. Quality bar — the ledger has to balance

- **Point ledger:** occupation points spent = the formula's total; interest points spent =
  INT × 2. Recompute; don't eyeball. Record both in `skill_points`.
- **Per skill:** `value` = base + occupation + interest + growth. If one skill doesn't add
  up, the card is wrong.
- **Every derived stat** traces back to the final characteristics — after age modifiers, not
  before.
- **Credit Rating** sits inside the occupation's band, or the deviation is deliberate and
  noted.
- **Occupation points** touched only occupation-list skills, and free-choice slots are named.
- **No skill over the declared cap**; Cthulhu Mythos is 0 on a pregen.
- **Umbrella skills** all carry a specialisation.

## 11. Human antagonists — baseline + increment, no separate budget table

kit 里"这个反派该多强"曾经差点长出一套独立的技能点预算带(300–1000)和四组预设属性/
技能数组。**这条路已被否决**:反派(邪教徒、邪教首领、其他人类反派)走**和调查员完全
相同的创建流程**(上面 §1–§5)——3D6×5 / (2D6+6)×5 属性、标准池公式
(`EDU×4 + INT×2 + 200`,或按概念替换成对应属性组合的等价公式)、§5 的 base value 表、
90% 硬上限。不给反派开小灶,也不从一张数字表里直接抄数。

### 基线:普通人类 = busybodies 卡组

`reference/decks/busybodies-zh.md` 的 47 张已配平数值 NPC 卡就是"普通人类"的数值
参照——不必另造一张抽象的"均值 50"占位表。造一个非首领级的人类反派(普通成员、
打手、路人)时,直接照最接近职业的那张卡校准属性与技能刻度,和
`core/06-create-npc.md` 现有做法一致。

### 首领 = 基线 + 增量,增量按类型二选一

首领(以及其他"明显强于普通人"的人类反派)= 上面的基线创建流程,**再叠加一层
增量**。增量的形式由首领类型决定,二选一,不混用:

| 类型 | 增量来源 | 增量形式 |
|---|---|---|
| **法术型**(施法、通神类首领) | 按资历掷 `1D4+1`(年轻)/ `1D6+1D4+2`(标准)/ `3D6+4`(成熟)/ `4D6+10`(古老)条法术;法术本身的 MP/SAN 成本查 `reference/sourcebooks/grand-grimoire-zh.md`(若本地存在) | 法术数量 + 随之水涨船高的克苏鲁神话技能值 |
| **非法术型**(帮派头目、雇佣兵、纯世俗势力) | 装备总价定强度,直接对接 `reference/decks/weapons-and-artifacts-zh.md` 的价格栏 | 武器/防具/载具的档次 |

原始文档给出的"技能点预算带 300–1000"表、四组预设属性数组(A 平均/B 高于平均/
C 强大/D 长者)、五组预设技能点数组(A–E)**整段不落盘、不重建**——它们的历史记录
留在 [`update_plan/2026-08-02-antagonist-budget.md`](../../update_plan/2026-08-02-antagonist-budget.md),
本节是唯一落盘的生成方法。

### 技能怎么选,数值怎么定:背景选技能,致命性定数值

首领的技能列表**按故事背景分配**——当过军医的首领有 Medicine / First Aid /
Firearms,学者首领没有。但同一个技能给多高,**不由背景正推,由致命性倒推**:同样
是 Firearms,给 45% 还是 85%,取决于这个数值一旦命中调查员会造成什么后果,不是
"他当过兵所以应该很高"。背景在数值定完后**反向追加解释力**即可(例如"boss 是
老兵,但身负不可治愈的创伤"),不改变数值本身的来源。这条分工的审计口径见
`core/11-review.md`。

### 生成时是否强化战斗能力

生成首领(或同级人类反派)时,**默认不强化战斗方面能力**——技能分配走上面"背景
选技能"的路子就够。是否强化是 Keeper 的开关,但这个开关**不在这里问**:落点是
intake,一次性问、写进 campaign `CLAUDE.md` 当默认,随
`update_plan/2026-08-02-cult-doc-integration.md` 阶段 2("敌对势力问题")一起接线。

### 与人数缩放(P3 Scaling)的关系

不给换算公式。人数低于基准时优先降**数量**;数量已经降到 1 还嫌重,才去动**单体
强度**——这是判断口径,不是公式。上面"是否强化战斗"那个开关就是这条口径在生成
时的落点。

来源:kit 原创综合,定案过程见 `update_plan/2026-08-02-antagonist-budget.md`
(非规则书转录,原始素材已按上面的说明弃用)。
