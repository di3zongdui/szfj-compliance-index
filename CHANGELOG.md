# 变更记录

本文件记录数据集发布的全部版本。数据文件与站点展示的版本号对应关系见各条目。

## v1.0.1 - 2026-10-03

文档与校验链更正。**587 条记录、`facets`、`stats`、`compliance_levels` 全部逐字节未变**
（已与 v1.0.0 的 `main` 分支逐字段比对确认，差异仅在 `meta.generated_at`）。
只有 3 个文件发生变化：`README.md`、`docs/statistics.md`、`MANIFEST.sha256`。

**更正：培养模式表漏列**

`README.md` 与 `docs/statistics.md` 的培养模式表中，`3+0`（1 个）与 `2+1`（1 个）
两个模式族被漏列，导致表内各行相加为 135，与计划外项目总数 137 不符。
已补全两行并新增**合计行**。

同时把生成逻辑从「硬编码 6 个模式族键」改为「按 `facets` 全量输出 + 合计断言」——
硬编码是漏列的直接原因，只补数据不改逻辑，下次新增模式族会再次静默漏掉。

**更正：MANIFEST 覆盖范围过窄**

`MANIFEST.sha256` 原先只覆盖构建脚本产出的 8 个文件，`README.md`、`NOTICE`、
`LICENSE`、`CITATION.cff`、`docs/limits.md`、`docs/methodology.md` 等人手维护的
文件**不在校验范围内**。这意味着文档被改动后校验仍显示全绿，属于假绿灯。
现改为覆盖发布目录全部文件（21 项），并排除 `__pycache__` 等本地产物。

**修正：构建不可复现**

`meta.generated_at` 原为构建时刻（`datetime.datetime.now()`），导致**同一条命令
重跑两次会产出不同的字节**，`MANIFEST.sha256` 必然失配。任何在本地重建数据集的人
都会看到「校验失败」，从而把正常的可复现流程误读为「数据被篡改」。
现改为确定性常量 `2026-09-30T00:00:00`，需要记录真实构建时间时用环境变量
`SZFJ_BUILD_TIMESTAMP` 覆盖。已验证连续两次重跑产物字节完全一致。

**新增：分发平台说明**

`README.md` 新增「分发平台」小节，说明魔搭 ModelScope 与和鲸社区 ModelWhale
为本中心**自行发布**的同步渠道（非第三方镜像），并重申唯一权威源为 GitHub tag。
三个平台的文件内容逐字节相同，可用各自的 `MANIFEST.sha256` 交叉核对。

**引用影响：无。** `records` 未变，数据结论不受影响。`v1.0.0` 的固定版本链接与
Release 资产继续有效，其记录级内容与本版本等价；仅文档表述与校验链在 v1.0.1 中修正。

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
