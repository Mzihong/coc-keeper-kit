# Update Plan — 低成本地图方案

> 日期:2026-08-02
> 状态:阻塞(等 Keeper 定视觉风格与 DSL 范围)
> 来源:从 `Archived/2026-08-02-conventions-gaps.md` §4 拆出独立跟踪(2026-08-02)
> 关联:`2026-08-02-cult-doc-integration.md` 第三章 E 项(邪教关系图是本计划 mermaid 的样例用例)

## 问题

模组需要图,但纯 token 生成位图或精细 SVG **成本高且不可维护**——图一改就得整张重生,
diff 不可读,三模型(Claude / Gemini / ChatGPT)之间也无法复用。

## 方案:数据与渲染分离

模型只产出几行结构化数据,渲染交给确定性工具。token 成本 ≈ 写一张小表。

| 图类型 | 方法 | 成本 |
|---|---|---|
| 场景网 / 区域关系 / 势力图 | **mermaid**(GitHub 与 Artifact 原生渲染,repo 内直接可见) | 几行文本 |
| 建筑平面图 | 小 DSL(JSON:房间名 + 矩形坐标 + 门窗)+ `scripts/render-map.py` 确定性渲染 SVG | 模型只写坐标 JSON |
| 手绘感调查地图 | 不生成,产出"给 Keeper 的手绘要点清单"(哪些地标、比例、标注) | 几行文本 |

## 待 Keeper 拍板(卡着定稿)

1. **视觉风格** — SVG 平面图要什么观感?纯线框(最省)/ 带填充与阴影 /
   仿手绘(粗糙线条、羊皮纸底)。风格决定 `render-map.py` 的复杂度
2. **DSL 范围** — 只支持矩形房间 + 门窗,还是要走廊、楼梯、多层、家具图标?
   范围越大,模型每次要写的 JSON 越长,就越接近"直接画 SVG"那条被否掉的路
3. **是否值得做** — 若 Keeper 实际跑团用手绘/现成图,只保留 mermaid 一项即可,
   DSL + 渲染器整块可以砍掉

## 改动清单(定稿后执行)

- [ ] 原型验证:挑 beidaihe-winter 一个场景,试做 mermaid 关系图 +
      DSL→SVG 平面图各一张,确认效果/成本后再定稿惯例
      (顺带拿 P1 第三章的邪教关系图当第二个样例)
- [ ] `scripts/render-map.py` — DSL→SVG 渲染器(无外部依赖,stdlib 即可)
- [ ] `templates/location.md` / `scene.md` — 增加可选 "Map" 一节
      (mermaid 块或 DSL JSON 块)
- [ ] `core/03-build-world.md` / `core/09-description.md` — 各加一行:
      何时附图、用哪种
- [ ] 无文件系统的环境(ChatGPT 网页)降级:只出 mermaid 与文字键位图

## 备忘

- 拆分时(2026-08-02)repo 内**没有**任何原型产物:无 `scripts/render-map.py`,
  campaigns 下无示例图。原 P3 状态表写的"4 原型已做"与 repo 实况不符,
  本计划按"原型未落盘"记录
- ~~环境限制:本机无 Python 解释器可用~~ —— **2026-08-02 更正**:本机有
  `python 3.14.5`(`C:\Users\User\.local\bin\python.exe`),P8 已实跑
  `render-investigator.py` 证实。`render-map.py` **写完可以直接跑**,
  不必靠人工复核代码。这降低了本计划的实现风险,但不解决"风格未定"这个真阻塞点
