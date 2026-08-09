# References & Inspiration — 树线之外（Beyond the Treeline）

Everything this campaign draws on or points to. Keep links and citations here so material
elsewhere can stay lean.

## Rulebooks & modules

- **《克苏鲁的呼唤》第七版守秘人规则书**（Chaosium）—— 所有检定、理智、战斗、生命值的权威。
- **《Cthulhu Through the Ages》**，「克苏鲁黑暗时代」章（原书 15–21 页）+ 共享附录
  「剑见箭 Swords and Arrows」（原书 31–33 页）—— 本战役的年代包来源，经由
  `../../reference/rules/eras/dark-ages.md` 使用。**路径 A，书本背书**：数字有出处，
  本战役不构造 `rules-era.md`。
- 未使用任何已出版模组。

## Kit reference used

- Rules: `../../reference/rules/` —— 基准本 `character-creation.md`、`combat.md`；
  年代差集 `eras/dark-ages.md`（先读 `eras/README.md` 的加载顺序，差集不单独读）
- Craft: `../../reference/craft/` —— `town-anatomy-zh.md`（韦尔加谷的建镇顺序：§一 分区四维、
  §二 条目体例与编号抽象、§三 神话层怎么埋进世俗名录、§四 三档密度与 NPC 落点）；
  `diagram-conventions-zh.md`（区域 mermaid 图与地图的墙/门/窗体例）。
  **`cult-design-zh.md` 刻意未取用**——本战役没有邪教。
- Bestiary: `../../reference/bestiary/` —— 尚未取用；「迁徙而来的存在」由
  `core/07-create-monster.md` 现做
- Mythos: `../../reference/mythos/` —— **未取用，且刻意不取用**。掷出的角度是「迁徙」，
  不指向任何具名旧日支配者或外神，因此不读 `great-old-ones/`，也不跑 `cult-goals`；
  `cthulhu-cult-history-zh.md` 同理不用于本战役的时间线
- Tables: `../../reference/tables/` —— intake 掷了 `hooks` / `locations` / `mythos-angles` /
  `complications`；建 world 时另掷 `locations`（×2）与 `town-institutions`（×8）。
  **所有掷骰的原始记录在本战役的 `rolls.log`**，由 `scripts/roll.py` 自动追加
- Decks & sourcebooks: `../../reference/decks/`、`../../reference/sourcebooks/` ——
  7e 的数值经由 `reference/rules/` 的 cheat-sheet 使用，其转录源是
  `sourcebooks/keeper-rulebook-7e-zh.md`。**数字可以拿，人不可以拿**——不把任何已出版
  NPC 的姓名、身世或秘密带进本战役。`decks/` 本轮未取用（`miseries-zh.md` 是后续备课时
  变数的备选深堆，用时**挑牌不抽牌**）
- Glossary: `../../reference/glossary-zh.md` —— 术语锁；本战役新造的专名同步记进
  `canon-log.md` → Standing canon

## Real-world background

- **10–11 世纪欧洲的技术与常识水平**（经 `eras/dark-ages.md`「技术与常识水平」一节）：
  识字集中在修道院与座堂学校；出行靠步行或骑马；消息以周到月为单位传递；世界观建立在宗教
  秩序而非「永恒的科学法则」之上——**这一条直接决定了本战役的表层描述怎么写**：目睹异常的
  角色更可能把它理解为神迹、恶魔或鬼魂，而不是外来的物件。
- 铁在前工业社会的稀缺性 —— 谷里的铁主要靠从遗迹里剜骨铁重锻，这把 `dark-ages.md` 的武器
  价格表接到了遗迹经济上。`core/03-build-world.md` 跑的时候把这条落实成一个具体行当。

## Tone touchstones

- **《NieR Replicant ver.1.22474487139...》**（守秘人指定）—— 要的是它的**结构性反讽**：
  一个看上去是中世纪奇幻的世界，其实是文明倒退后的废土；玩家先于角色认出脚下的东西是什么；
  角色用错误的词汇准确地描述了正确的东西。
  > **取技法，不取文本。** 按 `core/00-how-to-run.md` 的引用规则，已出版虚构作品在
  > `campaigns/` 里只提供技法，不提供文字——不搬用它的角色、地名、剧情、台词或专有名词。
  > 本战役所有专名（韦尔加、长林、不生原、守井宅、守望年）均为自造。
- 与之配套的两条自家规约，见 `CLAUDE.md` → Tone & style：**双层地点描述（表/里）** 与
  **转译规约**。触感参考只是来源，落到桌面上的是那两条规约。

## Maps & assets

- `scripts/render-map.py` 渲染的地图**就放在它所属的地点/场景旁边**（`world/`、`scenes/`），
  玩家版放 `handouts/`。本战役目前地图还少，不在这里另立索引。
- **渲染器天生就是本战役「表/里」规约的实现。** 一份 DSL 渲两版：不加旗标的是**守秘人版**
  （全渲染，含秘密）；`--player` 按 `secret: true` 过滤，并用 `player_name` / `player_label`
  把里层的真名换成谷里的叫法。**同一份 JSON 出两张图，永远不要手写两份**——会漂。
- **玩家版是需要报价的单独产物。** 按 `core/09-description.md` → Output：家具层 + `--player`
  约为守秘人版的 **3–5 倍** token 开销（贵在模型读房间、摆家具、打标签，不在渲染器），
  **生成前必须先报价并等守秘人确认**，产出物落 `handouts/` 并附一份说明用途的 `.md` 包装，
  过 `core/11-review.md` 的剧透检查后才上桌。
- 旧「石哨」守秘人版平面图随该地点一并删除（重构 2026-08-08 定，08-09 落地；石哨的功能并入
  守井宅）。**本战役现在没有任何地图。** 下一轮最值得画的候选是那处继承来的房产
  （`world/inherited-holding.md`）。
