# SZFJ Compliance Index

> A compliance registry of Sino-foreign cooperative undergraduate programs in China.
> **587 records** | 450 degree-granting institutions + 137 non-planned programs | v1.0 | CC BY 4.0

数据集中文说明见 [README.md](README.md)（主文档）。
This file is an English summary for international citation; the authoritative
documentation is the Chinese [README.md](README.md).

---

## What this dataset is

A registry of **587 records** covering undergraduate-level Sino-foreign
cooperative education in mainland China:

| Level | Definition | Records | Default risk |
|---|---|---|---|
| **L1** Planned (national admission) | Admitted through the national college entrance exam (gaokao) or official comprehensive evaluation | 450 | none |
| **L2** MOE-registered, non-planned | Filed with the Ministry of Education but self-recruiting, outside the gaokao application system | 7 | low |
| **L3** CSCSE programs | International undergraduate / SQA 3+1 programs under the Chinese Service Center for Scholarly Exchange | 77 | medium |
| **L4** Inter-institutional, unregistered | Bilateral university cooperation with no MOE filing and outside the CSCSE system | 53 | high |

## What this dataset is **not**

- **Not a ranking.** It does not answer "which university is better". It only
  answers "is this program genuine, and what is its actual degree/certificate
  pathway".
- **Not an official registry.** The publisher is a private research body. This is
  not a publication of the Ministry of Education or any government agency.
- **Not complete.** 137 non-planned programs is a verifiable subset, not the
  national total.

## Headline figures (reproducible from the shipped data)

- Of 137 non-planned programs, **52 (38.0%)** are flagged high risk.
- **110 (80.3%)** do not award a Chinese degree.
- **80 (58.4%)** involve UK partner institutions. This is the only
  single-direction figure that can be quoted directly; other direction counts
  are keyword hits and **must not be summed**.
- Domestic-stage annual tuition: median **CNY 65,000** (lower-bound estimate,
  121 of 137 records parseable).

## Files

| Path | Description |
|---|---|
| `data/szfj-compliance-index-v1.0.csv` | 587 rows, 20 columns, UTF-8 BOM |
| `data/szfj-compliance-index-v1.0.json` | Full package (meta, level definitions, stats, facets, records) |
| `data/szfj-compliance-index-v1.0.jsonl` | One JSON object per line |
| `data/szfj-compliance-index-v1.0-facets.json` | Derived aggregates |
| `schema/szfj-compliance-index.schema.json` | JSON Schema (draft-07) |
| `schema/datapackage.json` | Frictionless Data Package |
| `docs/codebook.md` | Field dictionary |
| `docs/methodology.md` | Classification rules |
| `docs/limits.md` | Known limitations (read before citing) |
| `docs/citation.md` | Citation formats |

## Download

| Use | URL |
|---|---|
| Pinned version (use this when citing) | `https://github.com/di3zongdui/szfj-compliance-index/releases/download/v1.0.4/<filename>` |
| Follow the latest release | `https://github.com/di3zongdui/szfj-compliance-index/releases/latest/download/<filename>` |
| Latest corrections | `https://raw.githubusercontent.com/di3zongdui/szfj-compliance-index/main/<path>` |
| China mirror (ModelScope) | `https://modelscope.cn/datasets/di3zongdui/szfj-compliance-index` |
| China mirror (Heywhale) | `https://www.heywhale.com/mw/dataset/6ac0979b6e0ebe066408e053` |

## Distribution

The **authoritative source** is the GitHub repository tag `v1.0.4`. The dataset is
mirrored on two China-accessible platforms; **file contents are byte-identical**,
and the shipped `MANIFEST.sha256` matches across all three.

| Platform | URL | Purpose |
|---|---|---|
| GitHub (primary) | <https://github.com/di3zongdui/szfj-compliance-index> | authoritative version, git history, release archive |
| ModelScope 魔搭 | <https://modelscope.cn/datasets/di3zongdui/szfj-compliance-index> | China access, in-browser preview, SDK download |
| ModelWhale 和鲸社区 | <https://www.heywhale.com/mw/dataset/6ac0979b6e0ebe066408e053> | China access, mount directly into an online notebook and re-run the verification script |

> **Do not use `v1.0.0`.** Its data files are equivalent to this release
> (`data/*.csv` and `data/*.jsonl` are byte-identical; `data/*.json` differs only
> in two `meta` fields), but its bundled README has a delivery-mode table whose
> rows sum to 135 instead of the actual 137 non-MOE programs. See
> [CHANGELOG.md](CHANGELOG.md).

> **This dataset is distributed only from the official URLs above. Third-party
> mirrors and proxies are not authorized.** Mirrors may lag behind or alter
> encoding, so a copy obtained that way cannot be matched to a released version.
> If these domains are unreachable from your network, open an Issue and we will
> provide an offline copy.

## Citation

```text
Li, Hong. 2026. SZFJ Compliance Index: A Compliance Registry of Sino-Foreign
    Cooperative Undergraduate Programs in China, Version 1.0.
    Shanghai Sino-Foreign Joint Admissions Data Research Center.
    https://github.com/di3zongdui/szfj-compliance-index
```

Full formats (GB/T 7714, APA, Chicago, BibTeX) in [docs/citation.md](docs/citation.md).
A **Cite this repository** button is available in the GitHub sidebar, powered by
[CITATION.cff](CITATION.cff).

## License

Data: **CC BY 4.0** — free to use, modify and redistribute with attribution.
Scripts: MIT.

## Contact

Corrections are prioritised over defence. Open an
[issue](https://github.com/di3zongdui/szfj-compliance-index/issues) or email
15618198831@163.com.
