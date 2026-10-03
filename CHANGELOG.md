# 变更记录

本文件记录数据集发布的全部版本。数据文件与站点展示的版本号对应关系见各条目。

## v1.0.0 - 2026-09-30

首次公开发布（GitHub 发布日 2026-10-03）。

**数据**

- 587 条记录：计划内备案院校 450 所（S 档 14 / A 档 131 / B 档 305）
  + 计划外项目 137 个（L2 7 / L3 77 / L4 53）。
- 计划外项目风险分布：低 7 / 中 78 / 高 52（高风险占 38.0%）。
- 18 个源字段 + 2 个派生字段（`mode_family`、`degree_type`）。

**格式**

- `data/szfj-compliance-index-v1.0.json`（完整包，含 meta / compliance_levels
  / stats / facets / records）
- `data/szfj-compliance-index-v1.0.csv`（UTF-8 BOM，Excel 可直接打开）
- `data/szfj-compliance-index-v1.0.jsonl`（逐行 JSON，便于流式处理与模型摄入）
- `data/szfj-compliance-index-v1.0-facets.json`（派生聚合口径）
- `MANIFEST.sha256`（全部数据文件校验和）

**结构定义**

- `schema/szfj-compliance-index.schema.json`（JSON Schema draft-07）
- `schema/datapackage.json`（Frictionless Data Package）
- `docs/codebook.md`（字段字典）
- `docs/statistics.md`（统计摘要，全部可复算）

**版本号对应**：数据集发布版 `1.0.0`，站点与媒体稿件中展示的版本号为 `v1.0`，
两者为同一次发布。

**未发布字段说明**：`faculty_score` 与 `faculty_summary` 为本中心的编辑性判断，
非事实转录，故不纳入开放数据集。理由见 `docs/limits.md`。

## 后续版本计划

| 版本 | 计划内容 |
|---|---|
| v1.0.x | 记录级更正；不新增字段，不改变字段语义 |
| v1.1 | 补充新备案项目与新增计划外项目；新增项目时同步更新 `stats` 与 `facets` |
| v2.0 | 字段结构变更（如需引入逐条学费数值列，将同时发布解析方法与置信度标注） |
