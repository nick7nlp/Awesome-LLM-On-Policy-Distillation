"""Build the public reading list and indexes from the curated catalog.

The data contains verified public descriptions and source links. This renderer
does not score papers, infer metadata, or silently import private research notes.
"""
from __future__ import annotations
from collections import Counter
from html import escape
import json
from pathlib import Path
import re

ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/'resources/catalog.json'
SECTIONS=[('4','Objectives and update rules'),('5','Teacher and supervision construction'),
          ('6','Data and training dynamics'),('7','Agentic and multi-turn distillation'),
          ('8','Mechanisms, failures, and evaluation'),('9','Applications and systems'),
          ('background','Foundations and related background')]
ROLES={'direct_opd':'Direct OPD','hybrid_opd':'Mixed / replayed distillation',
       'teacher_mediated_rl':'Teacher-mediated RL','interactive_imitation':'Interactive imitation',
       'offline_distillation':'Offline comparator','analysis':'Analysis',
       'application':'Application / system report','background':'Background'}


def cell(value):
    return str(value).replace('|','&#124;').replace('\n',' ')


def heading_id(home):return 'papers-'+home


def render():
    catalog=json.loads(DATA.read_text());papers=catalog['papers']
    ids=[r['paper_id'] for r in papers]
    if len(ids)!=len(set(ids)):raise ValueError('Duplicate catalog IDs')
    main=[r for r in papers if r['home']!='background'];background=[r for r in papers if r['home']=='background']
    date=catalog['updated_on'];ordered=sorted(papers,key=lambda r:(r['submitted'],r['paper_id']),reverse=True)
    parts=['<a id="readme-top"></a>', '', '# Awesome LLM On-Policy Distillation', '',
           'A curated reading list for **[A Survey of On-Policy Distillation for Large Language Models](https://arxiv.org/abs/2604.00626)**.', '',
           '[![Stars](https://img.shields.io/github/stars/nick7nlp/Awesome-LLM-On-Policy-Distillation?style=flat)](https://github.com/nick7nlp/Awesome-LLM-On-Policy-Distillation) '
           '[![License](https://img.shields.io/badge/license-MIT-blue)](LICENSE) '
           f'![Catalog](https://img.shields.io/badge/catalog-{len(papers)}_entries-blue)', '',
           '[Search and filter on OPDHub](https://nick7nlp.github.io/OPDHub/) · '
           '[Reading paths](resources/reading-order.md) · [Method comparison](resources/method-comparison.md) · '
           '[Code index](resources/codebases.md) · [Equations](resources/key-equations.md) · '
           '[Evaluation guide](resources/benchmarks.md)', '',
           f'**Catalog checked {date}.** {len(main)} method, analysis, and application entries plus '
           f'{len(background)} foundational or related resources. Coverage through September 2026. '
           'These are reading-list entries, not a count of distinct direct-OPD algorithms. '
           'The public survey PDF is arXiv v4; this catalog includes later reviewed literature.', '',
           '## Scope and how to use the list', '',
           'The central topic is teacher-derived learning on states visited by an evolving language-model student. '
           'Direct distribution matching, mixed or replayed training, teacher-mediated rewards, analysis, and '
           'deployment reports are labeled by their actual role. Necessary off-policy comparators are identified explicitly. '
           'Inclusion requires a relevant, supported contribution; a brief entry is not a lower quality tier. '
           'Unavailable or unresolved evidence is held for review rather than presented as a verified method.', '',
           'Titles, author lists, dates, and paper links are checked against primary pages. Dates below denote first '
           'public release, rather than a venue year or the month encoded in an identifier. Repository links must '
           'both resolve and have a paper association. “No verified repository link” does not mean no code exists. '
           'A reachable repository is not an end-to-end reproduction claim.', '',
           '<p align="center"><img src="assets/opd-overview.png" width="680" alt="Conceptual teacher–student on-policy learning loop"></p>', '',
           '*Conceptual illustration of one direct-matching loop. Teacher feedback is not certified ground truth; '
           'other methods use different targets, divergences, or teacher-mediated rewards.*', '',
           '## Start here', '',
           '- [GKD](https://arxiv.org/abs/2306.13649): distinguish the sampled prefix distribution from the chosen conditional divergence.',
           '- [MiniLLM](https://arxiv.org/abs/2306.08543): follow sequence reverse KL, future returns, and the practical estimator.',
           '- [Rethinking OPD](https://arxiv.org/abs/2604.13016): examine teacher–student reasoning compatibility and failure modes.',
           '- [GAD](https://arxiv.org/abs/2511.10643): compare teacher-text-derived discriminator rewards with direct logit matching.',
           '- [MemOPD](https://arxiv.org/abs/2608.07068): inspect memory-state reconstruction before teacher scoring.', '',
           '## Browse the catalog', '']
    for home,label in SECTIONS:
        n=sum(r['home']==home for r in papers)
        parts.append(f'- [{label}](#{heading_id(home)}) — {n} entries')
    parts+=['','[Latest additions and update notes](CHANGELOG.md) · [Objective index](resources/loss-taxonomy.md) · '
            '[Related surveys](resources/related-surveys.md) · [Contributing](CONTRIBUTING.md)', '',
            '## Recent literature', '',
            'Recent release dates within the reviewed collection; this is not a ranking or an automated inclusion queue.', '',
            '| Paper | Released | Reading section |','|---|---|---|']
    for r in [r for r in ordered if r['home']!='background'][:12]:
        name=dict(SECTIONS)[r['home']]
        parts.append(f'| [{cell(r["title"])}]({r["paper_url"]}) | {r["submitted"]} | [{name}](#{heading_id(r["home"])}) |')
    for home,label in SECTIONS:
        group=[r for r in ordered if r['home']==home]
        parts+=['',f'<a id="{heading_id(home)}"></a>','',f'## {label}', '',
                '| Paper and contribution | First release | Role | Repository |','|---|---|---|---|']
        for r in group:
            resources='<br>'.join(f'[Repository {i+1}]({url})' if len(r['code_urls'])>1 else f'[Repository]({url})'
                                 for i,url in enumerate(r['code_urls'])) or '—'
            if r['code_urls'] and r['code_status'].startswith('Unofficial'):
                resources += '<br><sub>Unofficial reproduction</sub>'
            parts.append(f'| [{cell(r["title"])}]({r["paper_url"]})<br><sub>{cell(r["description"])}</sub> '
                         f'| {r["submitted"]} | {ROLES.get(r["mechanism"],r["mechanism"])} | {resources} |')
        parts+=['','[Back to top](#readme-top)']
    parts+=['','## Visual reference snapshots','',
            'The following images preserve earlier catalog snapshots. They are not statistics of the current '
            'selection and must not be used to infer the best teacher size, a universal loss ranking, or a current paper count.', '',
            '<details><summary>Teacher–student model-pair snapshot</summary>','',
            '![Historical teacher–student model-pair snapshot](assets/model-atlas-heatmap.png)','',
            'Rows and columns denote model labels. Repeated model labels do not imply identical conditioning or shared live weights.','', '</details>', '',
            '<details><summary>Earlier loss-label snapshots</summary>','',
            '![Historical loss-label distribution](assets/loss-distribution.png)','',
            '![Historical loss-label evolution](assets/loss-evolution.png)','',
            'The older display classes grouped several non-equivalent mechanisms. Use the current [objective index](resources/loss-taxonomy.md) '
            'and [equation guide](resources/key-equations.md) for method-specific descriptions.','', '</details>', '',
            '## Citation','', '```bibtex','@article{song2026opdsurvey,',
            '  title = {A Survey of On-Policy Distillation for Large Language Models},',
            '  author = {Mingyang Song and Mao Zheng},',
            '  journal = {arXiv preprint arXiv:2604.00626},','  year = {2026}','}','```','',
            'For corrections, provide the paper version and the primary source supporting the change. '
            'See [CONTRIBUTING.md](CONTRIBUTING.md).']
    (ROOT/'README.md').write_text('\n'.join(parts)+'\n')
    codes=['# Code and implementation index','', '[Catalog](../README.md) · [Contributing](../CONTRIBUTING.md)', '',
           f'Checked {date}. Links below resolve and are associated with the listed papers through a primary paper link '
           'or repository evidence. Some releases are minimal placeholders; availability is not a reproduction claim.', '',
           '| Paper | Repository |','|---|---|']
    for r in ordered:
        if r['code_urls']:
            links='<br>'.join(f'[{cell(u.split("github.com/")[-1])}]({u})' for u in r['code_urls'])
            if r['code_status'].startswith('Unofficial'):
                links += '<br><sub>Unofficial reproduction</sub>'
            codes.append(f'| [{cell(r["title"])}]({r["paper_url"]}) | '+links+' |')
    codes+=['','A dash in the main catalog means that no paper-specific repository was verified during this check. '
            'We do not substitute an unrelated framework or a cited baseline for a missing implementation.']
    (ROOT/'resources/codebases.md').write_text('\n'.join(codes)+'\n')
    objectives=['# Objective and feedback index','', '[Catalog](../README.md) · [Key equations](key-equations.md)', '',
                'Descriptions below distinguish targets, gradients and sampling. A paper can use several objectives '
                'across variants or stages; these entries are not mutually exclusive mathematical loss classes.', '',
                '| Paper | Objective or feedback | Role |','|---|---|---|']
    for r in ordered:
        if r['home']!='background':
            objectives.append(f'| [{cell(r["title"])}]({r["paper_url"]}) | {cell(r["objective"])} | {ROLES.get(r["mechanism"],r["mechanism"])} |')
    (ROOT/'resources/loss-taxonomy.md').write_text('\n'.join(objectives)+'\n')
    print(f'Rendered {len(papers)} catalog records and {sum(bool(r["code_urls"]) for r in papers)} linked-code records.')


if __name__=='__main__':render()
