# 变更记录

本文件记录数据集发布的全部版本。数据文件与站点展示的版本号对应关系见各条目。

**两个版本号不是一回事**：`v1.0` 是**数据版本**（数据文件命名与站点展示），
`v1.0.x` 是**发布 tag**（下载地址与引用指向）。历史条目按当时口径书写，不追改。

## v1.0.3 - 2026-10-03

**校验范围更正。** `MANIFEST.sha256` 此前把 `.gitattributes` 也算作发布内容，
而实测**魔搭 CLI 会往该文件追加自己的 LFS 规则**（本地 478 字节，魔搭上 706 字节）。
后果是：任何人从魔搭下载副本、按 README 指引执行 `sha256sum -c MANIFEST.sha256`，
都会看到一条「`.gitattributes` 校验失败」——**而那条警报是假的**。

一个会把正常副本误报为「被改动」的校验脚本，与一个永远报绿的校验脚本一样有害：
两者都在摧毁「你可以自己核对」这件事的可信度。现改为只覆盖
「在任何平台都应当逐字节相同」的文件，共 **20** 项（排除 `MANIFEST.sha256` 自身、
`.gitattributes`、`.ms_upload_cache`）。README 已同步说明这两个文件的排除理由。

**同时修正的还有本仓库自己的核验脚本**：`scripts/verify_dataset_public.py` 的
资产清单与 tag 常量此前写死为 `v1.0.0`；`scripts/verify_dataset_modelscope.py`
新增的逐字节回读核验里，`get_dataset_files()` 返回的是**普通 dict** 而非对象，
我按对象去取字段得到空集，于是「下载并比对」这一步在**一个文件都没比**的情况下
报了 PASS。已在脚本内断言「实际比对文件数 == 期望文件数」，杜绝这类空循环假绿灯。

**引用影响：无。** 587 条 `records`、`facets`、`stats`、`compliance_levels` 未变，
`data/*.csv` 与 `data/*.jsonl` 逐字节未变。

## v1.0.2 - 2026-10-03

**版本指向更正。** v1.0.1 修正了文档内容，却没有同步修正「指向哪个版本」的说明 ——
于是修好的说明本身指向了**未修正的 v1.0.0**。本版本补上这一环。

**更正：v1.0.1 条目中的文件计数错误**

v1.0.1 条目称「只有 3 个文件发生变化」，实际为 **5 个**（经 GitHub compare API
逐文件核对 `78c960bb3d...ede551352cd7`）：

| 文件 | 变化 |
|---|---|
| README.md | +26 / -7 |
| docs/statistics.md | +4 / -1 |
| MANIFEST.sha256 | +4 / -4 |
| CHANGELOG.md | +39 / -0 |
| `data/szfj-compliance-index-v1.0.json` | +1 / -1 |

被漏计的是 `data/szfj-compliance-index-v1.0.json` —— 它**是数据文件，不是文档**。
该文件仅 `meta.generated_at` 一个字段变化（可复现性修复），587 条 `records` 与
`facets` / `stats` / `compliance_levels` 逐字节未变；`data/*.csv` 与
`data/*.jsonl` 经 sha256 比对确认与 v1.0.0 完全一致。漏计一个数据文件，会让
「只有文档变化」这个判断失真——而这正是引用者最需要准确知道的事。

**更正：所有「权威版本」指向**

以下位置原均指向 `v1.0.0`，即**未经本系列修正的版本**。照这些说明下载，拿到的
zip 内附 README 仍带「培养模式表相加 135≠137」的漏列问题：

| 文件 | 原值 |
|---|---|
| `README.md` / `README.en.md` | 固定版本下载地址、权威 tag 声明 |
| `CITATION.cff` | `version`、`date-released`、`identifiers.url` |
| `docs/citation.md` | BibTeX `version`、版本表、Release 链接 |
| `data/szfj-compliance-index-v1.0.json` | `meta.release_tag` |

现统一指向 `v1.0.2`。

**新增：`releases/latest/download/` 稳定别名**

README 新增一行「跟随最新发布」地址
`https://github.com/di3zongdui/szfj-compliance-index/releases/latest/download/<文件名>`。
本次缺陷的成因就是「文档里写死了具体 tag，每次发布都要手工同步」；换成稳定别名后，
只在下述固定版本行需要随版本更新。

**引用影响：无。** 587 条 `records` 未变，`facets` / `stats` / `compliance_levels`
未变，`data/*.csv` 与 `data/*.jsonl` 逐字节未变。本版本变化的只有文档、
`MANIFEST.sha256`、以及 `data/*.json` 的 2 个 `meta` 字段
（`generated_at` 确定性化、`release_tag` 版本指向）。

**资产补齐**：v1.0.1 的 Release 只上传了整包 zip，缺 4 个单文件资产（若 README
指向该 tag 的 csv 会 404）。本版本上传与 v1.0.0 对齐的 5 个资产：
`csv` / `json` / `jsonl` / `facets.json` / `zip`。

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
