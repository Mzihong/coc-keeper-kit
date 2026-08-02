# Update Plan — 克苏鲁教团文档整合 + 敌对势力问题

> 日期:2026-08-02
> 来源文档:`C:\Users\User\Desktop\克苏鲁教团.docx`(158 页,四章)
> 状态:待执行

## 来源与红线

来源文档是**网络论坛内容的转录/汇编**,处理规则与 `reference/og_Norval/`、
`reference/external/coc-zh` 完全一致:只读来研究,所有落盘内容**用自己的话重写提炼**,
不逐段照搬原文(见 `CLAUDE.md`:kit 不复制受版权保护的文本)。

docx 的原始转换稿放在会话 scratchpad,**不进仓库**;仓库里只留提炼后的重写内容。

## 阶段 0 — 转换与切分

- [ ] 用 pandoc(或 python-docx)把 docx 转成 Markdown,存 scratchpad
- [ ] 按四章切分;超长章节内再按小节切,逐块处理,避免上下文溢出
- [ ] 快速通读一遍目录级结构,产出四章内容清单给 Keeper 过目

## 阶段 1 — 逐章提取与内化

每章流程:**读完 → 给 Keeper 摘要 + 拟写入文件清单 → 确认 → 落盘**。
落盘前扫一遍 `reference/` 现有条目,避免与已有教派/怪物重复。

### 第一章 · 克苏鲁邪教的历史
- [ ] 提炼为 `reference/mythos/` 下的背景 lore(中文,术语过 `reference/glossary-zh.md`)
- [ ] 历史脉络中可复用的邪教/旧日支配者关系写成 setting 级条目,不带剧情

### 第二章 · 克苏鲁邪教(具体教团)
- [ ] 每个教团一档:`reference/mythos/cults/<name>.md`(中文)
- [ ] 按 `reference/mythos/README.md` 既定结构:目标、组织、成员、标志、手法、
      表面身份 vs 真实议程

### 第三章 · 设计一个克苏鲁邪教(方法论)
- [ ] 提炼为 `reference/cult-design-notes-zh.md` —— 定位对标
      `reference/lovecraft-craft-notes-zh.md`(通读后提炼的中文手法笔记)
- [ ] `core/03-build-world.md` 的 faction 分支加一行:写邪教前先读此文
- [ ] `core/04-design-scenario.md` 加一行:剧本以邪教为核心威胁时读此文

### 第四章 · 邪教徒、怪物和造物
- [ ] 邪教徒原型 → 新 roll table `reference/tables/cultist-archetypes.md`(中文)
- [ ] `core/06-create-npc.md` 加一行:造邪教徒 NPC 时滚这张表
- [ ] 怪物/造物 → `reference/bestiary/` 逐个立档(按惯例英文,标题保留中英对照)
- [ ] 所有数值**先过 `core/02-rules-reference.md` 校验/换算成正确 7e 机制**,
      论坛数字不可直接信任
- [ ] **前置依赖:** 造物若含法术/仪式,先完成 `2026-08-02-conventions-gaps.md`
      第 3 项(`reference/rules/magic.md` 速查),否则无校验依据

## 阶段 2 — 敌对势力问题(依赖阶段 1 完成)

> 排在提取内化之后:auto-fill 答"邪教"时要指向阶段 1 产出的笔记和 cults 库,
> 先有库,后有问。

- [ ] `core/01-intake.md` — B 组后新增一问 **"The threat"**:威胁背后站着什么?
      选项:邪教/组织、独行术士或家族、独立怪物、场所本身作祟、自然或宇宙现象
      (无人类反派)、auto。**默认 auto = 掷 `reference/tables/mythos-angles.md`**,
      反套路规则不变——问题给 Keeper 开正门,不给模型开"默认写邪教"的后门
- [ ] `core/01-intake.md` auto-fill 表:答"邪教"时指向
      `reference/cult-design-notes-zh.md` 与 `reference/mythos/cults/`
- [ ] `campaigns/_template-campaign/CLAUDE.md` — 新增 `Threat` 字段,
      答案落成 campaign 持久状态
- [ ] `core/04-design-scenario.md` — "First" 一节加半句:构建 the truth 前读
      campaign `CLAUDE.md` 的 Threat 字段并遵守(**不**在此 spec 加提问)
- [ ] 检查问题编号引用(如 "never invent a fourteenth question")随新增问题同步更新

## 阶段 3 — 收尾

- [ ] 更新 `reference/README.md`:登记新增的 cult-design-notes、cults 条目、
      cultist-archetypes 表
- [ ] 重跑 `scripts/build-bundle.sh` 更新 `dist/bundle.md`
- [ ] 用 `review-material` 对新增材料做一次审计(数值、剧透卫生、术语一致性)
- [ ] 按仓库维护规则填 changelog / 更新 README
- [ ] 提交:阶段 1 每章一个 commit,阶段 2 单独一个 commit

## 设计决定备忘(为什么不做成 skill)

第三、四章不做新 skill,理由:
1. skill 是动词,这两章是知识;kit 已有先例(`lovecraft-craft-notes-zh.md`
   由 `core/09`/`core/07` 在生成时去读)。
2. 新增 design-cult skill 会与 `build-world` faction 模式触发重叠,路由抖动。
3. `.claude/skills/` 只有 Claude 可见;`core/` + `reference/` 三模型共用,
   符合根适配器可移植性规则。
