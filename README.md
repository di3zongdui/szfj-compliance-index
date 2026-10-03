# 中外合作办学项目合规名录 · SZFJ Compliance Index

> **587 条记录** | 450 所计划内备案院校 + 137 个计划外项目 | 版本 v1.0 | CC BY 4.0

**这不是一份「哪所学校好」的排行榜。它只回答一个问题：这个项目，是真的吗？**

数据可直接下载：
[CSV](data/szfj-compliance-index-v1.0.csv) |
[JSON](data/szfj-compliance-index-v1.0.json) |
[JSONL](data/szfj-compliance-index-v1.0.jsonl)

---

## 一、这个数据集填补什么缺口

中外合作办学在公开信息上长期存在一个断层：

| 已有信息源 | 覆盖范围 | 未覆盖的部分 |
|---|---|---|
| 胡润百学、HKPEP 等机构榜单 | 只评**机构**（如西交利物浦、宁波诺丁汉这类独立法人大学） | 明文不含**项目** |
| 教育部涉外监管信息网 | 只回答「**是否备案**」 | 不给分层，不含计划外项目 |
| 各类分数线聚合站 | 只给**分数** | 不查合规性 |
| 自媒体与招生中介 | 招生导向 | 立场不中立 |

而按教育部口径，本科层次中外合作办学**项目**有 1300 多个，数量远多于机构。
这些项目里，有备案的、有走中留服体系的、也有校际自主跨境无备案的，家长在
报考前很难分清三者区别。

本名录覆盖的正是这个缺口：**项目层 + 计划外**，并给出可核查的分层与风险标注。

## 二、四层合规判定

每条记录都被归入以下四层之一。分层依据是该项目的**招生录取通道与可核验的
备案状态**，不是办学质量评价。

| 层级 | 定义 | 记录数 | 风险标注 | 学历学位 |
|---|---|---|---|---|
| **L1** 计划内（统招） | 纳入国家普通高校招生计划，通过高考志愿或官方综合评价录取 | 450 | `none` | 中方学历学位证书（部分另发外方学位） |
| **L2** MOE 备案计划外 | 经教育部备案，但走自主招生、不占高考志愿 | 7 | `low` | 外方学士学位 + 中留服认证，无中方学位证 |
| **L3** 中留服项目 | 中留服体系下的国际本科 / SQA 3+1 项目，自主招生 | 77 | `medium` | 外方学士学位，需中留服认证 |
| **L4** 校际自主跨境 | 校际自主合作，无 MOE 备案、不属中留服体系 | 53 | `high` | 认证路径不确定，须逐项核实 |

L1 内部另分 S/A/B 三档（S 档 14 所、A 档 131 所、B 档 305 所）。S 档仅收录
独立法人中外合作大学；非法人中外合作机构归入 A / B 档。

## 三、关键统计

以下数字全部可用随附数据文件复算，完整版见 [`docs/statistics.md`](docs/statistics.md)。

**计划外项目（137 个）的风险分布**

| 风险等级 | 数量 | 占比 |
|---|---|---|
| 低 | 7 | 5.1% |
| 中 | 78 | 56.9% |
| 高 | **52** | **38.0%** |

**学位结构（137 个计划外项目）**

| 判定 | 数量 | 占比 |
|---|---|---|
| 不授予中方学位 | **110** | **80.3%** |
| 双学位 | 9 | 6.6% |
| 未明确 | 18 | 13.1% |

**培养模式（137 个计划外项目）**

| 模式族 | 数量 | 占比 |
|---|---|---|
| 2+2 | 81 | 59.1% |
| 3+1 | 34 | 24.8% |
| 灵活 | 7 | 5.1% |
| 4+0 | 6 | 4.4% |
| 1+N | 6 | 4.4% |
| 3+0 | 1 | 0.7% |
| 2+1 | 1 | 0.7% |
| 其他 | 1 | 0.7% |
| **合计** | **137** | **100%** |

**对接方向（关键词计数，各方向不可加总）**

| 方向 | 记录数 | 占比 |
|---|---|---|
| 英国 | **80** | **58.4%** |
| 美国 | 27 | 19.7% |
| 新西兰 | 18 | 13.1% |
| 新加坡 | 18 | 13.1% |
| 澳大利亚 | 16 | 11.7% |
| 加拿大 | 15 | 10.9% |

> 一个项目的合作院校字段常同时并列多个国家的院校，例如「2+2 国际本科
> （英新澳方向）」会同时计入英国、新西兰、澳大利亚三行，因此各行数字之
> 和大于 137。**只有「英国 80 个 / 137 = 58.4%」是单一方向口径，可直接引用。**

**国内段年学费（元，下限口径，可解析 121 / 137 条）**

| 最小值 | P10 | Q1 | 中位数 | Q3 | P90 | 最大值 |
|---|---|---|---|---|---|---|
| 12,000 | 35,000 | 48,950 | **65,000** | 78,000 | 88,000 | 130,000 |

> 学费数字来自文本解析，可能把住宿费、留学指导费等并列金额计入，是**下限
> 口径估计**而非逐条精确值。正因如此，本数据集**不提供**逐条学费数值列。

## 四、快速开始

**直接下载**：见仓库根目录 `data/` 目录，或
[Release v1.0.4](https://github.com/di3zongdui/szfj-compliance-index/releases/tag/v1.0.4)。

**下载地址**

| 用途 | 地址 |
|---|---|
| 固定版本（引用时请用这个） | `https://github.com/di3zongdui/szfj-compliance-index/releases/download/v1.0.4/<文件名>` |
| 跟随最新发布 | `https://github.com/di3zongdui/szfj-compliance-index/releases/latest/download/<文件名>` |
| 跟随最新更正 | `https://raw.githubusercontent.com/di3zongdui/szfj-compliance-index/main/<路径>` |
| 国内访问（魔搭） | `https://modelscope.cn/datasets/di3zongdui/szfj-compliance-index` |
| 国内访问（和鲸） | `https://www.heywhale.com/mw/dataset/6ac0979b6e0ebe066408e053` |

**分发平台**

**唯一权威源是 GitHub 仓库 [`di3zongdui/szfj-compliance-index`](https://github.com/di3zongdui/szfj-compliance-index) 的 tag `v1.0.4`。**

> **不要用 `v1.0.0`**。它的数据文件与本版本等价（`data/*.csv`、`data/*.jsonl`
> 逐字节相同；`data/*.json` 仅 2 个 `meta` 字段不同），但它的 zip 内附 README
> 存在培养模式表漏列（各行之相加 135，与计划外项目总数 137 不符）。版本差异见
> [CHANGELOG.md](CHANGELOG.md)。

为便于国内网络访问，本数据集另在以下平台同步发布，**文件内容逐字节相同**：

| 平台 | 地址 | 定位 |
|---|---|---|
| GitHub（主源） | <https://github.com/di3zongdui/szfj-compliance-index> | 权威版本、Git 历史、Release 归档 |
| 魔搭 ModelScope | <https://modelscope.cn/datasets/di3zongdui/szfj-compliance-index> | 国内访问、页面预览、SDK 加载 |
| 和鲸社区 ModelWhale | <https://www.heywhale.com/mw/dataset/6ac0979b6e0ebe066408e053> | 国内访问、在线 Notebook 直接挂载复算 |

三个平台随附的 `MANIFEST.sha256` 哈希值完全一致，可逐文件交叉核对。
**若某平台内容与 GitHub 主源不一致，一律以 GitHub 主源为准。**

**国内平台怎么用**

魔搭（SDK 一行加载）：

```bash
pip install modelscope
modelscope download --dataset di3zongdui/szfj-compliance-index --local_dir ./szfj-compliance-index
```

和鲸（在线复算，不用装任何东西）：

1. 打开 <https://www.heywhale.com/mw/dataset/6ac0979b6e0ebe066408e053>
2. 新建项目 → 挂载本数据集（默认挂载目录 `/home/mw/input/szfj_compliance<四位数字>/`）
3. 在 Notebook 中执行：

```python
import subprocess, os
BASE = next(p for p in __import__('glob').glob('/home/mw/input/szfj_compliance*/szfj-compliance-index-v1.0'))
print(subprocess.run(['python', os.path.join(BASE, 'scripts/verify_dataset.py')],
                     cwd=BASE, capture_output=True, text=True).stdout[-3000:])
```

> **除上述本中心自行发布的平台之外，本数据集不授权任何第三方镜像站或代理通道。**
> 原因：第三方镜像可能指向旧提交、或在转发时改动编码，导致你手上的副本与我们
> 发布的版本无法对应。一旦出现引用争议，无法追溯。若你所在网络无法直连上述
> 域名，请提 Issue 说明，我们提供离线副本。

例：下载 CSV（Release 固定版本）

```bash
curl -LO https://github.com/di3zongdui/szfj-compliance-index/releases/download/v1.0.4/szfj-compliance-index-v1.0.csv
```

**Python（pandas）**

```python
import pandas as pd

URL = ("https://raw.githubusercontent.com/di3zongdui/szfj-compliance-index/"
       "main/data/szfj-compliance-index-v1.0.csv")
df = pd.read_csv(URL, encoding="utf-8-sig")

# 只看高风险的计划外项目
high = df[(df.level != "L1") & (df.risk_level == "high")]
print(len(high), "个高风险计划外项目")

# 不授予中方学位的项目占多少
print(df[df.level != "L1"].degree_type.value_counts())
```

**命令行（curl + jq）**

```bash
curl -sL https://raw.githubusercontent.com/di3zongdui/szfj-compliance-index/main/data/szfj-compliance-index-v1.0.jsonl \
  | jq -c 'select(.risk_level=="high") | {id, name, province}' | head
```

**校验完整性**

```bash
curl -LO https://github.com/di3zongdui/szfj-compliance-index/releases/download/v1.0.4/szfj-compliance-index-v1.0.4.zip
unzip szfj-compliance-index-v1.0.4.zip
cd szfj-compliance-index-v1.0
sha256sum -c MANIFEST.sha256
```

`MANIFEST.sha256` 覆盖发布内容的全部 **20** 个文件（含本 README 与方法论文档），
逐文件比对哈希即可确认手上的副本未被改动。**请务必先解压并进入顶层目录**，
在校验文件所在目录执行，否则 `-c` 会因找不到文件而全部报错。

> **不纳入清单的两个文件**：`.gitattributes` 与 `.ms_upload_cache`。
> 前者会被托管平台改写 —— 实测魔搭 CLI 会往它**追加自己的 LFS 规则**
> （本地 478 字节，魔搭上 706 字节），因此它在不同平台上不可能逐字节相同；
> 后者是上传工具在本地的缓存。把这两个文件放进清单，只会让**每个**在魔搭
> 下载副本的人看到一条假的「校验失败」。校验清单只覆盖「在任何平台都应当
> 逐字节相同」的文件。

**独立复算全部数字**

本仓库提供校验脚本，**不需要任何私有数据**即可复算数据集中的每一个聚合数字、
复核两个派生字段、并核对三种格式是否一致：

```bash
git clone https://github.com/di3zongdui/szfj-compliance-index.git
cd szfj-compliance-index
python scripts/verify_dataset.py
```

该脚本会重算风险分布、学位结构、培养模式、对接方向、学费分位数，与已发布的
`facets` 文件逐项比对，并交叉核对对外发布稿件中的 13 个数字。全部通过才返回
退出码 0。**如果你复算出的结果与数据集不符，那是我们的问题，请提 Issue。**

## 五、文件说明

| 文件 | 内容 | 适合谁用 |
|---|---|---|
| `data/*.csv` | 587 行 × 20 列，UTF-8 BOM | Excel、SPSS、Stata |
| `data/*.json` | 完整包，含 meta、分层定义、统计、派生聚合、records | 需要元数据的程序化使用 |
| `data/*.jsonl` | 逐行 JSON，一行一条 | 流式处理、大模型摄入 |
| `data/*-facets.json` | 派生聚合口径（各分布、学费分位） | 直接引用统计数字 |
| `schema/*.schema.json` | JSON Schema draft-07 | 校验、代码生成 |
| `schema/datapackage.json` | Frictionless Data Package | 数据目录收录 |
| `docs/codebook.md` | 字段字典：类型、来源、非空率、取值域 | 理解字段含义 |
| `docs/methodology.md` | 四层分级与风险判定规则 | 判断方法是否可信 |
| `docs/limits.md` | **已知局限与不可用途** | 引用前必读 |
| `docs/citation.md` | 引用格式（GB/T 7714 / APA / BibTeX） | 写作与投稿 |
| `scripts/verify_dataset.py` | 独立校验脚本，复算全部聚合数字与派生字段 | 想核验数据的人 |
| `MANIFEST.sha256` | 全部数据文件校验和 | 校验下载完整性 |

## 六、引用方式

最短可用的中文引用：

> 李洪. 中外合作办学项目合规名录（SZFJ Compliance Index）v1.0 [DS].
> 上海中外合办升学数据研究中心, 2026.
> https://github.com/di3zongdui/szfj-compliance-index

数据集条目里写作：

> 数据来源：上海中外合办升学数据研究中心《中外合作办学项目合规名录》v1.0

GB/T 7714、APA、BibTeX 等完整格式见 [`docs/citation.md`](docs/citation.md)。
GitHub 页面右上角另有 **Cite this repository** 按钮，可直接导出。

## 七、许可

**CC BY 4.0**（Creative Commons Attribution 4.0 International）。
允许商业与非商业使用、修改、再分发，唯一要求是**保留署名**。
完整法律文本见 [`LICENSE`](LICENSE)。

随附脚本（`scripts/`）用于从源数据重建本数据集，采用 MIT 许可。

## 八、重要声明

- 本数据集为**信息整理成果**，法律性质是事实转录与分层索引，
  **不是评估、认证或排名结论**。
- 本中心是**民办研究主体**，本数据集**不是**教育部、中留服或任何政府机构的
  官方发布物，也不构成对任何项目合法性的认证。
- 数据基于公开渠道采集整理，可能存在滞后或偏差。入学决策请以
  [教育部涉外监管信息网](https://crs.jsj.edu.cn) 与各校官方渠道为准。
- 风险等级反映的是**家长事前难以察觉的信息不对称程度**，不等于项目质量评价。

完整的来源说明与免责条款见 [`NOTICE`](NOTICE)，已知局限见
[`docs/limits.md`](docs/limits.md)。

## 九、更正与联系

发现记录错误请提交
[Issue](https://github.com/di3zongdui/szfj-compliance-index/issues)，
或邮件至 15618198831@163.com。经核实的更正会在补丁版本中体现，
并记入 [`CHANGELOG.md`](CHANGELOG.md)。

**更正优先于辩解。** 数据集的公信力取决于它能否被有效地证伪。

## 十、更新节奏

| 版本 | 内容 |
|---|---|
| v1.0.x | 记录级更正，不新增字段 |
| v1.1 | 补充新备案项目与新增计划外项目 |
| v2.0 | 字段结构变更（须同步发布方法说明） |

每次发布都会更新 `MANIFEST.sha256` 与 `CHANGELOG.md`。

---

发布主体：上海中外合办升学数据研究中心
标准制定：中外合作办学名录标准委员会（内设机构，不单独登记）
研究支持：上海国际教育路径研究所（IEPI）
作者：李洪（上海中外合办升学数据研究中心 首席顾问）
