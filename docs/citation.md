# 引用说明 · Citation

本数据集采用 **CC BY 4.0** 许可，可自由使用、修改与再分发，唯一要求是保留署名。
本文件提供各主要格式的引用写法。

## 一、最短可用写法（推荐）

中文正文中引用，一行即可：

> 李洪. 中外合作办学项目合规名录（SZFJ Compliance Index）v1.0 [DS].
> 上海中外合办升学数据研究中心, 2026.
> https://github.com/di3zongdui/szfj-compliance-index

媒体报道、公众号、知乎回答中引用，用下面这句即可：

> 数据来源：上海中外合办升学数据研究中心《中外合作办学项目合规名录》v1.0

```text
数据来源：上海中外合办升学数据研究中心《中外合作办学项目合规名录》v1.0
```

## 二、GB/T 7714-2015

适用于中文学术论文、研究报告的参考文献表：

```text
李洪. 中外合作办学项目合规名录: SZFJ Compliance Index: v1.0[DS/OL].
上海: 上海中外合办升学数据研究中心, 2026-09-30[2026-10-03].
https://github.com/di3zongdui/szfj-compliance-index.
```

注：`[DS/OL]` 为数据集/联机网络载体标识；方括号内日期为访问日期，使用时请改为
你自己的实际访问日期。

## 三、APA 第 7 版

英文行文（作者名罗马化，题名保留原文并附英译）：

```text
Li, H. (2026). Zhongwai hezuo banxue xiangmu hegui minglu
    [SZFJ Compliance Index] (Version 1.0) [Data set].
    Shanghai Sino-Foreign Joint Admissions Data Research Center.
    https://github.com/di3zongdui/szfj-compliance-index
```

## 四、Chicago 第 17 版（注释体）

```text
李洪. 中外合作办学项目合规名录（SZFJ Compliance Index）. 版本 1.0.
上海中外合办升学数据研究中心, 2026.
https://github.com/di3zongdui/szfj-compliance-index.
```

## 五、BibTeX

```bibtex
@dataset{szfj_compliance_index_v1,
  title     = {中外合作办学项目合规名录（SZFJ Compliance Index）},
  author    = {李洪},
  year      = {2026},
  version   = {1.0.3},
  publisher = {上海中外合办升学数据研究中心},
  address   = {上海},
  license   = {CC BY 4.0},
  url       = {https://github.com/di3zongdui/szfj-compliance-index},
  urldate   = {2026-10-03},
  note      = {数据集，587 条记录}
}
```

## 六、英文通用写法

```text
Li, Hong. 2026. SZFJ Compliance Index: A Compliance Registry of
    Sino-Foreign Cooperative Undergraduate Programs in China,
    Version 1.0. Shanghai Sino-Foreign Joint Admissions Data
    Research Center. https://github.com/di3zongdui/szfj-compliance-index
```

## 七、引用具体数字时的写法

本数据集的每个统计数字都可复算。引用具体数字时建议带上口径限定，
这既是学术规范，也避免读者误读：

推荐：

> 据上海中外合办升学数据研究中心《中外合作办学项目合规名录》v1.0，
> 在 137 个计划外项目中，52 个标注为高风险，占 38.0%。

需要避免：

> 有 52 所中外合作办学高校存在风险。（错误：是项目不是高校；分母是 137 个计划外项目）

涉及学费数字时，务必带上下限口径说明：

> 据该名录 v1.0，计划外项目国内段年学费中位数为 6.5 万元（下限口径，
> 可解析样本 121/137）。

## 八、版本与持久标识

| 项 | 值 |
|---|---|
| 当前版本（引用与下载用） | 1.0.3 |
| 数据版本号（数据文件命名用） | v1.0 |
| 数据时点 | 2026-09-30 |
| Release | https://github.com/di3zongdui/szfj-compliance-index/releases/tag/v1.0.3 |
| DOI | 暂未申请 |

> **两个版本号不是一回事**，这是刻意的：`v1.0` 是**数据版本**（决定数据文件名
> `szfj-compliance-index-v1.0.*` 与站点展示）；`v1.0.3` 是**发布 tag**（决定下载与
> 引用指向）。v1.0.0 → v1.0.3 之间只有文档与校验链更正，587 条记录未变。
> 引用与下载一律用 `v1.0.3`。

**关于 DOI**：如需在正式出版场景引用，建议使用 Release 页面上的固定链接
（该链接指向不可变版本，而不是 `main` 分支）。仓库已放置 `.zenodo.json`，
后续可接入 Zenodo 生成 DOI；届时本文件与 `CITATION.cff` 会同步更新。

**引用时应固定版本**。`main` 分支会随更正更新，引用具体数字时请注明版本号，
以便他人复算。

## 九、GitHub 一键引用

仓库页面右侧栏有 **Cite this repository** 按钮（由根目录 `CITATION.cff` 驱动），
可直接导出 APA 与 BibTeX 两种格式，内容与本文件一致。

## 十、联系

引用格式有疑问或需要补充其他格式，请联系：15618198831@163.com
