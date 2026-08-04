# Era Pack — Cthulhu Invictus (克苏鲁不败)

> **This is a delta, not a standalone document.** Read `reference/rules/eras/README.md` first
> for the loading order — read `reference/rules/character-creation.md` (the 1920s baseline)
> in full, then apply the five sections below as overrides. A section not listed here means
> "unchanged from baseline."

**Era:** the Roman Empire, roughly 1st–2nd century CE (the source gives no fixed year — the
Keeper can place it anywhere from the late Republic to the height of the Empire).
**来源:** *Cthulhu Through the Ages* 中文版(七宫涟个人汉化),「克苏鲁不败」章,原书页
7–13(本 PDF 第 4–10 页)。装备一节另外引用共享附录「剑见箭 Swords and Arrows」
(原书页 31–33,本 PDF 第 25–28 页)。

## Skill table changes

New/changed skills versus the 1920s baseline (来源同上):

- **Art/Craft (Potion) 艺术/工艺〔药剂〕** (base 05%) — identify, mix, and compound
  infusions, potions, antidotes, and hallucinogens.
- **Citizen 公民** (base 10%) — knowledge of Roman law and government; untangles political
  favours and judges whether an act is legal.
- **Drive Cart 驱车〔驾驭马车/牛车〕** (base 20%) — handling a one- or two-animal cart.
  This is this era's equivalent slot to the baseline's Drive Auto.
- **Empire Lore 帝国知识** (base 25%) — knowledge of imperial history, custom, and current
  affairs; the era's equivalent of the baseline's Own Country skill.
- **Fighting (Shield) 格斗〔盾〕** (base 15%) — using a shield offensively; can also
  substitute for Dodge in combat (see Optional rules below).
- **Outsider Lore 外邦知识** (specialisation, base 20%) — knowledge of peoples, places, and
  legends outside the Empire; invested per region/nation, never as a general "Outsider Lore."
- **Ranged Weapons 射击** (specialisation, variable%) — covers bow, crossbow, and sling;
  invested per weapon: bow 10%, crossbow 20%, sling 15%. Replaces the baseline's firearms
  specialisations for this era.
- **Mend/Mender 修造〔修理/制造〕** (base 20%) — repairs or builds simple equipment, sets
  traps; cannot repair shields or weapons.

## Equipment & weapons

The three ancient-era files (Cthulhu Invictus, Dark Ages, Mystic Iceland) share the
「剑见箭 Swords and Arrows」 combat supplement's armour/shield mechanics (来源页 31–33):

- **Armour** is variable, not a flat reduction — roll the armour die on every successful
  hit taken: plain clothing 0, heavy clothing 1D2−1, padded soft leather 1D2, padded heavy
  leather 1D3, soft leather 1D6, ring mail 1D6+1, scale mail 1D6+1, chainmail 1D8.
- **Shields** provide extra armour (see 「剑见箭」表 2). A shield-user who Dodges uses
  Fighting (Shield) instead of Dodge; on a tie or a defender's win the shield's armour still
  applies, but on a full attacker win the shield is bypassed entirely.
- **Example Cthulhu Invictus weapons** (来源页 33,货币单位 sestertii/SE): cestus
  (Fighting (Brawl), 25%, 1D6, one-handed, 50 SE); pilum (Fighting (Spear) or Throw, 15%,
  1D8, one-handed, 45 SE); gladius (Fighting (Sword), 20%, 1D6+1, one-handed, 175 SE);
  trident (Fighting (Spear) or Throw, 10%, 1D6, one-handed, 75 SE).
- **Ranged weapons cannot be dodged** — the target can only seek cover or block with a
  shield (a penalty die to the attacker, but the defender loses their next action). A
  target must be within one-fifth of the attacker's DEX to fight back against a ranged or
  thrown attack.
- **Currency:** sestertii (SE); example prices at 来源页 11 (a longsword ≈ 1200 SE, a
  chainmail shirt ≈ 2400 SE).

## Technology & common knowledge

Iron Age / Roman engineering level — roads, aqueducts, public baths, and legionary
logistics are mature, but there is no gunpowder, printing, or mechanical power. Information
travels by land courier and sea, on the order of weeks rather than days. Religion is part of
the state's order; worshipping an unofficial god — Mythos entities most of all — is
legally a betrayal of Roman order, not just a moral lapse (来源页 13).

## Occupation table

Example occupations (skill-point formula and Status range per 来源页 8–10; Status stands
in for Credit Rating, scale at 来源页 10): slinger, spy, gladiator, legionary, merchant,
scout, army physician (7 examples; three more — soothsayer, courtesan, farmer — at
来源页 6–7). Each occupation lists a fixed skill list, a point formula, and a Status range,
structurally identical to the baseline occupation model and directly usable in
`templates/investigator.schema.json`'s occupation field. Status is the numeric equivalent
of Credit Rating, but **it cannot be ticked up like an ordinary skill** — it only rises or
falls through deeds and scandal (来源页 9、11).

## Optional rules

- **Birth Omen table** (1D10, 来源页 5) replaces part of the baseline's background-generation
  flow — Romans believed the events around a child's birth shaped their whole life; roll
  once at character creation and adjust characteristics/skills per the result (e.g. "the
  temple caught fire: −10 Luck"; "parents saw a blessing on the mother: +5 STR").
- **Ideology/Beliefs (Patron God)**, **Significant People**, **Meaningful Locations**, and
  **Treasured Possessions** tables (all 1D10, 来源页 5–6) follow the baseline's table
  structure with Roman-specific entries (e.g. "Jupiter, King of the Gods"; "the Roman
  Pantheon"; "jewellery").
- Full rules for **Fighting (Shield) replacing Dodge** are under Equipment & weapons above;
  a shield-user who declares full defence for the round gets a bonus die on every
  Fighting (Shield) roll that round (来源页 26).
