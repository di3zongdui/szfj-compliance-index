# 字段字典 · Codebook

> 中外合作办学项目合规名录 v1.0 · 共 587 条记录 · 20 个字段

字段来源分类：**transcribed**（转录公开事实）｜**classified**（按本中心公开规则判定，规则见 methodology.md）｜**derived**（由其他字段机械推导，算法见下）。

| 字段 | 中文 | 类型 | 来源 | 非空率 | 取值域 / 说明 |
|---|---|---|---|---|---|
| `id` | 记录唯一标识 | string | transcribed | 100.0% | 587 个不同值 |
| `level` | 合规层级 L1-L4 | string | classified | 100.0% | `L1`, `L2`, `L3`, `L4` |
| `band` | L1 内部档位 S/A/B | null/string | classified | 76.7% | `S` `A` `B`；仅 L1 有值 |
| `name` | 项目或机构名称 | string | transcribed | 100.0% | 587 个不同值 |
| `host` | 国内开办高校 | null/string | transcribed | 23.3% | 仅计划外项目（L2-L4）有值；L1 为院校本体故为空 |
| `province` | 所在省级行政区 | string | transcribed | 100.0% | 29 个不同值 |
| `partner` | 境外合作院校 | string | transcribed | 87.9% | 院校文本，常并列多国多校；括号内多为校名缩写而非国别码 |
| `mode` | 培养模式（原始文本） | null/string | transcribed | 96.1% | 37 个不同值 |
| `admission_mode` | 招生录取方式 | null/string | transcribed | 95.2% | 84 个不同值 |
| `tuition_year` | 国内段年学费（原始文本） | string | transcribed | 100.0% | 人类可读的原始文本，如「第一二年 ¥200,000 / 第三四年 ¥230,000」。**不提供**逐条学费数值列，原因见 docs/limits.md |
| `certificates` | 学历学位授予情况 | string | transcribed | 100.0% | 52 个不同值 |
| `moe_code` | 教育部备案编号 | null/string | transcribed | 4.6% | 教育部备案编号，仅部分记录有 |
| `program_type` | 计划外项目类型 | null/string | classified | 23.3% | `MOE备案计划外（自主招生）`, `中留服国际本科项目`, `中留服SQA 3+1项目`, `中留服SQA 3+1项目（加速班）`, `校际自主跨境项目` |
| `qs_rank_partner` | 境外合作院校 QS 排名 | integer/null | transcribed | 5.3% | 31 个不同值 |
| `competitive_level` | 竞争度标注 2-5 | integer/null | classified | 72.7% | `5`, `4`, `3`, `2` |
| `risk_level` | 合规风险等级 | string | classified | 100.0% | `none`, `low`, `medium`, `high` |
| `risk_notes` | 风险说明（转录） | null/string | transcribed | 23.3% | 单行文本，无换行符 |
| `sources` | 信息来源 | array | transcribed | 100.0% | `教育部涉外监管信息网|各校招生简章`, `教育部涉外监管信息网|中留服项目名单|各校招生简章（公开渠道采集，非官方排名）` |
| `mode_family` | 培养模式族（派生） | string | derived | 100.0% | `4+0`, `其他`, `3+1`, `2+2`, `3+0`, `1+N`, `2+1`, `灵活` |
| `degree_type` | 学位结构判定（派生，仅 L2-L4） | null/string | derived | 23.3% | 仅 L2-L4 有值；L1 为统招，不参与判定 |

## 派生字段算法

两个派生字段的解析函数**逐字复用** `scripts/verify_article_numbers.py`，以保证与已发布文章口径完全一致：

```python
# mode_family —— 严格按 mode 首段匹配
# 顺序尝试 '2+2','3+1','4+0','1+','2+1','3+0'，'1+' 归为 '1+N'；
# 前缀为「灵活」记 '灵活'；其余 '其他'

# degree_type —— 检索 certificates + risk_notes 文本
# 含「双学位/双证/双文凭」-> dual
# 含「无中方学位/不颁发中方/仅外方」-> single
# 其余 -> other
```

## 明确未发布的字段

| 字段 | 未发布理由 |
|---|---|
| `faculty_score` | 本中心自设的教学质量评分（78-94），无公开可复现的方法论，且属「评价裁定」而非「事实转录」 |
| `faculty_summary` | 多为院校招生宣传文本的转录，异质且非结构化，发布易被误读为本中心结论 |
| 逐条学费数值列 | 学费文本中常并列住宿费、留学指导费、全程总额；实测按文本取值会得出错误结果，故只在聚合层发布 |
| 逐条国别列 | `partner` 括号内多为校名缩写，仅 14.6% 含国别码，无法逐条可靠派生 |

详见 `docs/limits.md`。
