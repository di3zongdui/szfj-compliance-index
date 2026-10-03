# -*- coding: utf-8 -*-
"""独立校验 SZFJ Compliance Index 数据集。

设计目标：**不依赖任何私有源数据**。任何人 clone 本仓库后运行本脚本，
即可独立复算全部聚合数字、复核派生字段、验证文件完整性。

用法（在仓库根目录）：
    python scripts/verify_dataset.py

任一项不通过即退出码 1。
"""
from __future__ import print_function

import collections
import csv
import hashlib
import io
import json
import os
import re
import statistics
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, 'data')
JSON_PATH = os.path.join(DATA, 'szfj-compliance-index-v1.0.json')
CSV_PATH = os.path.join(DATA, 'szfj-compliance-index-v1.0.csv')
JSONL_PATH = os.path.join(DATA, 'szfj-compliance-index-v1.0.jsonl')
FACETS_PATH = os.path.join(DATA, 'szfj-compliance-index-v1.0-facets.json')
MANIFEST = os.path.join(ROOT, 'MANIFEST.sha256')

FIELDS = [
    'id', 'level', 'band', 'name', 'host', 'province', 'partner', 'mode',
    'admission_mode', 'tuition_year', 'certificates', 'moe_code',
    'program_type', 'qs_rank_partner', 'competitive_level', 'risk_level',
    'risk_notes', 'sources', 'mode_family', 'degree_type',
]

# 对外发布稿件中出现的数字，须与本数据集一致
ARTICLE_EXPECT = [
    ('高风险 52', 52),
    ('不授予中方学位 110', 110),
    ('双学位 9', 9),
    ('培养模式 2+2 = 81', 81),
    ('培养模式 3+1 = 34', 34),
    ('培养模式 4+0 = 6', 6),
    ('英国方向 80', 80),
    ('澳大利亚 16', 16),
    ('学费中位数 65000', 65000),
    ('学费 Q1 48950', 48950),
    ('学费 Q3 78000', 78000),
    ('学费 P10 35000', 35000),
    ('学费 P90 88000', 88000),
]

COUNTRY_KEYWORDS = ['英国', '美国', '新西兰', '新加坡', '澳大利亚', '加拿大',
                    '俄罗斯', '马来西亚', '泰国', '日本', '法国', '德国',
                    '韩国', '爱尔兰', '意大利', '荷兰', '西班牙', '瑞士',
                    '白俄罗斯', '乌克兰', '波兰', '匈牙利']

RESULTS = []


def check(label, ok, detail=''):
    RESULTS.append((bool(ok), label, detail))


def norm(v):
    """把不同格式的取值归一为可比较的字符串。"""
    if v is None:
        return ''
    if isinstance(v, list):
        return '|'.join(str(x) for x in v)
    if isinstance(v, bool):
        return 'true' if v else 'false'
    if isinstance(v, int):
        return str(v)
    return str(v).strip()


# ---------------------------------------------------------------- 派生逻辑
# 与数据集构建时使用的实现保持一致。这两段是「可独立复算」的核心：
# 输入全部来自已发布字段，不依赖任何私有数据。
def recompute_mode_family(mode):
    m = str(mode or '')
    for k in ('2+2', '3+1', '4+0', '1+', '2+1', '3+0'):
        if m.startswith(k):
            return k if k != '1+' else '1+N'
    if m.startswith('灵活'):
        return '灵活'
    return '其他'


def recompute_degree_type(certificates, risk_notes):
    t = str(certificates or '') + str(risk_notes or '')
    if '双学位' in t or '双证' in t or '双文凭' in t:
        return 'dual'
    if '无中方学位' in t or '不颁发中方' in t or '仅外方' in t:
        return 'single'
    return 'other'


def tuition_list(recs):
    out = []
    for r in recs:
        m = re.findall(r'([0-9][0-9,]{3,})', str(r.get('tuition_year') or ''))
        c = [int(x.replace(',', '')) for x in m]
        c = [x for x in c if 10000 <= x <= 800000]
        if c:
            out.append(min(c))
    return sorted(out)


# ---------------------------------------------------------------- 载入
def load_all():
    with io.open(JSON_PATH, encoding='utf-8') as f:
        pkg = json.load(f)
    j_recs = pkg['records']

    c_recs = []
    with io.open(CSV_PATH, encoding='utf-8-sig', newline='') as f:
        for row in csv.DictReader(f):
            for intf in ('qs_rank_partner', 'competitive_level'):
                row[intf] = int(row[intf]) if row[intf] != '' else None
            src = row.get('sources') or ''
            row['sources'] = [x for x in src.split('|') if x]
            for f_ in ('band', 'host', 'moe_code', 'program_type',
                       'risk_notes', 'degree_type'):
                if row.get(f_) == '':
                    row[f_] = None
            c_recs.append(row)

    l_recs = []
    with io.open(JSONL_PATH, encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line:
                l_recs.append(json.loads(line))

    with io.open(FACETS_PATH, encoding='utf-8') as f:
        facets = json.load(f)
    return pkg, j_recs, c_recs, l_recs, facets


def main():
    pkg, j_recs, c_recs, l_recs, facets = load_all()

    # ---- 0. 文件完整性 ----
    if os.path.exists(MANIFEST):
        bad = []
        with io.open(MANIFEST, encoding='utf-8') as f:
            for line in f:
                line = line.rstrip('\n')
                if not line.strip():
                    continue
                h, rel = line.split('  ', 1)
                p = os.path.join(ROOT, rel.replace('/', os.sep))
                if not os.path.exists(p):
                    bad.append('%s 缺失' % rel)
                    continue
                with open(p, 'rb') as fh:
                    actual = hashlib.sha256(fh.read()).hexdigest()
                if actual != h:
                    bad.append('%s sha256 不符' % rel)
        check('MANIFEST.sha256 全部匹配', not bad, '; '.join(bad))
    else:
        check('MANIFEST.sha256 存在', False, '文件缺失')

    # ---- 1. 三种格式记录一致 ----
    check('记录数 587', len(j_recs) == 587, 'JSON 实际 %d' % len(j_recs))
    check('CSV 行数一致', len(c_recs) == len(j_recs),
          'CSV %d vs JSON %d' % (len(c_recs), len(j_recs)))
    check('JSONL 行数一致', len(l_recs) == len(j_recs),
          'JSONL %d vs JSON %d' % (len(l_recs), len(j_recs)))

    diffs = []
    for a, b, c in zip(j_recs, c_recs, l_recs):
        for f_ in FIELDS:
            if not (norm(a.get(f_)) == norm(b.get(f_)) == norm(c.get(f_))):
                diffs.append('%s.%s: json=%r csv=%r jsonl=%r'
                             % (a.get('id'), f_,
                                norm(a.get(f_))[:30], norm(b.get(f_))[:30],
                                norm(c.get(f_))[:30]))
    check('三格式逐字段一致', not diffs, '; '.join(diffs[:5]))

    check('id 唯一', len(set(r['id'] for r in j_recs)) == len(j_recs))

    # ---- 2. 派生字段可独立复算 ----
    mf_bad, dt_bad = [], []
    for r in j_recs:
        if recompute_mode_family(r.get('mode')) != r.get('mode_family'):
            mf_bad.append(r['id'])
        if r.get('level') in ('L2', 'L3', 'L4'):
            exp = recompute_degree_type(r.get('certificates'), r.get('risk_notes'))
            if exp != r.get('degree_type'):
                dt_bad.append('%s 应 %s 实 %s' % (r['id'], exp, r.get('degree_type')))
        elif r.get('degree_type') is not None:
            dt_bad.append('%s 为 L1 却带 degree_type' % r['id'])
    check('mode_family 可复算', not mf_bad, ','.join(mf_bad[:5]))
    check('degree_type 可复算', not dt_bad, '; '.join(dt_bad[:5]))

    # ---- 3. 聚合口径可复算 ----
    non = [r for r in j_recs if r.get('level') in ('L2', 'L3', 'L4')]
    n = len(non)
    check('计划外项目 137', n == 137, '实际 %d' % n)

    risk = collections.Counter(r.get('risk_level') for r in non)
    deg = collections.Counter(r.get('degree_type') for r in non)
    mode = collections.Counter(r.get('mode_family') for r in non)
    check('风险分布复算一致',
          dict(risk) == facets['by_risk'],
          '复算 %s vs 已发布 %s' % (dict(risk), facets['by_risk']))
    check('学位结构复算一致',
          dict(deg) == facets['by_degree_type'],
          '复算 %s vs 已发布 %s' % (dict(deg), facets['by_degree_type']))
    check('培养模式复算一致',
          dict(mode) == facets['by_mode_family'],
          '复算 %s vs 已发布 %s' % (dict(mode), facets['by_mode_family']))

    geo = lambda r: str(r.get('name') or '') + ' ' + str(r.get('partner') or '')
    cc = collections.OrderedDict()
    for k in sorted(COUNTRY_KEYWORDS, key=lambda x: -sum(
            1 for r in non if re.search(x, geo(r)))):
        v = sum(1 for r in non if re.search(k, geo(r)))
        if v:
            cc[k] = v
    pub = dict((k, v['records'])
               for k, v in facets['partner_direction']['counts'].items())
    check('对接方向复算一致', cc == pub, '复算 %s vs 已发布 %s' % (dict(cc), pub))

    tv = tuition_list(non)
    q = statistics.quantiles(tv, n=4)
    t = facets['tuition_cny']
    for label, exp, act in [
            ('学费样本数 121', len(tv), t['parsed_records']),
            ('学费中位数', int(statistics.median(tv)), t['median']),
            ('学费 Q1', int(q[0]), t['q1']),
            ('学费 Q3', int(q[2]), t['q3']),
            ('学费 P10', tv[int(len(tv) * 0.1)], t['p10']),
            ('学费 P90', tv[int(len(tv) * 0.9)], t['p90']),
            ('学费最小值', tv[0], t['min']),
            ('学费最大值', tv[-1], t['max'])]:
        check('%s 复算一致' % label, exp == act, '复算 %s vs 已发布 %s' % (exp, act))

    # ---- 4. 与已发布稿件数字交叉核对 ----
    article = {
        '高风险 52': risk.get('high', 0),
        '不授予中方学位 110': deg.get('single', 0),
        '双学位 9': deg.get('dual', 0),
        '培养模式 2+2 = 81': mode.get('2+2', 0),
        '培养模式 3+1 = 34': mode.get('3+1', 0),
        '培养模式 4+0 = 6': mode.get('4+0', 0),
        '英国方向 80': cc.get('英国', 0),
        '澳大利亚 16': cc.get('澳大利亚', 0),
        '学费中位数 65000': int(statistics.median(tv)),
        '学费 Q1 48950': int(q[0]),
        '学费 Q3 78000': int(q[2]),
        '学费 P10 35000': tv[int(len(tv) * 0.1)],
        '学费 P90 88000': tv[int(len(tv) * 0.9)],
    }
    for label, exp in ARTICLE_EXPECT:
        check('稿件口径 %s' % label, article[label] == exp,
              '实际 %s' % article[label])

    # ---- 5. 排除字段确实不存在 ----
    leaked = [r['id'] for r in j_recs
              if 'faculty_score' in r or 'faculty_summary' in r]
    check('排除字段未泄露', not leaked, ','.join(leaked[:5]))

    # ---- 输出 ----
    print('=' * 72)
    print('SZFJ Compliance Index 独立校验  |  数据版本 %s' % pkg['meta']['version'])
    print('=' * 72)
    fail = 0
    for ok, label, detail in RESULTS:
        if ok:
            print('  PASS  %s' % label)
        else:
            fail += 1
            print('  FAIL  %s   %s' % (label, detail))
    print('-' * 72)
    print('  合计 %d 项，通过 %d，失败 %d' % (len(RESULTS), len(RESULTS) - fail, fail))
    if fail:
        sys.exit(1)
    print('  数据集自洽，且与已发布稿件数字一致。')


if __name__ == '__main__':
    main()
