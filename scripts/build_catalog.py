"""Build the public reading list and indexes from the curated catalog.

Render paper descriptions, resource links, and release announcements.
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/'resources/catalog.json'
NEWS=ROOT/'resources/news.json'
PUBLIC_FIELDS={'paper_id','arxiv_id','title','authors','year','submitted',
               'paper_url','description','objective','mechanism','home',
               'code_urls','code_status','source_version'}
SECTIONS=[('4','Objectives and update rules'),('5','Teacher and supervision construction'),
          ('6','Data and training dynamics'),('7','Agentic and multi-turn distillation'),
          ('8','Mechanisms, failures, and evaluation'),('9','Applications and systems'),
          ('background','Foundations and related background')]
ROLES={'direct_opd':'Direct OPD','hybrid_opd':'Hybrid OPD',
       'teacher_mediated_rl':'Teacher-mediated RL','interactive_imitation':'Interactive imitation',
       'offline_distillation':'Offline comparator','analysis':'Analysis',
       'application':'Application / system report','background':'Background'}
QUESTIONS = {
    '4': 'What does the student update optimize?',
    '5': 'What makes a teacher useful on student trajectories?',
    '6': 'Which states, tokens, and training stages matter?',
    '7': 'How does supervision change across actions and turns?',
    '8': 'What transfers, what fails, and why?',
    '9': 'How does distillation fit into a deployed system?',
    'background': 'Which foundations and comparators clarify OPD?',
}


def cell(value):
    return str(value).replace('|','&#124;').replace('\n',' ')


def heading_id(home):return 'papers-'+home


def render():
    catalog=json.loads(DATA.read_text());papers=catalog['papers']
    for paper in papers:
        if set(paper)-PUBLIC_FIELDS:
            raise ValueError('Unsupported catalog fields for '+paper['paper_id'])
    ids=[r['paper_id'] for r in papers]
    if len(ids)!=len(set(ids)):raise ValueError('Duplicate catalog IDs')
    date=catalog['updated_on'];ordered=sorted(papers,key=lambda r:(r['submitted'],r['paper_id']),reverse=True)
    parts=['<a id="readme-top"></a>', '',
           '<p align="center"><a href="https://nick7nlp.github.io/OPDHub/"><img src="assets/reading-room.svg" width="960" alt="On-Policy Distillation — objectives, supervision, interaction"></a></p>', '',
           '# Awesome LLM On-Policy Distillation', '',
           'How language-model students learn from teachers on their own trajectories. '
           'A reading companion to **[A Survey of On-Policy Distillation for Large Language Models](https://arxiv.org/abs/2604.00626)**.', '',
           '[![Read the survey](https://img.shields.io/badge/Survey-arXiv-315c52?style=flat-square)](https://arxiv.org/abs/2604.00626) '
           '[![Explore OPDHub](https://img.shields.io/badge/Explore-OPDHub-526c7c?style=flat-square)](https://nick7nlp.github.io/OPDHub/) '
           '[![License](https://img.shields.io/badge/License-MIT-7a7365?style=flat-square)](LICENSE)', '',
           '**[Search the collection ↗](https://nick7nlp.github.io/OPDHub/)** · '
           '[Reading paths](resources/reading-order.md) · [Method comparison](resources/method-comparison.md) · '
           '[Code](resources/codebases.md) · [Equations](resources/key-equations.md) · '
           '[Evaluation](resources/benchmarks.md)', '',
           f'<sub>{len(papers)} papers and resources · Updated {date} · '
           'The public survey is arXiv v4; the reading list includes later work.</sub>', '',
           '## Find your question', '',
           '| Learning signal | Supervision and interaction | Transfer and practice |',
           '|:---|:---|:---|',
           '| [Objectives and update rules](#papers-4) | [Teacher construction](#papers-5) | [Mechanisms and failures](#papers-8) |',
           '| [Data and training](#papers-6) | [Agents and multi-turn learning](#papers-7) | [Applications and systems](#papers-9) |', '',
           '[Foundations and related background](#papers-background) · [Related surveys](resources/related-surveys.md)', '',
           '## A few good starting points', '',
           '- **The learning problem.** [GKD](https://arxiv.org/abs/2306.13649) separates the prefix distribution from the matching loss; '
           '[MiniLLM](https://arxiv.org/abs/2306.08543) develops sequence reverse KL and its practical estimator.',
           '- **The supervision interface.** [OPSD](https://arxiv.org/abs/2601.18734) and [SDPO](https://arxiv.org/abs/2601.20802) '
           'show how solutions and feedback can turn a model into its own teacher.',
           '- **The limits of transfer.** [Rethinking OPD](https://arxiv.org/abs/2604.13016) examines reasoning compatibility; '
           '[Skills vs. Knowledge](https://arxiv.org/abs/2610.09639) separates prefix choice from divergence direction.',
           '- **Beyond one policy.** [MAS-OPD](https://arxiv.org/abs/2609.34234) studies role-specific supervision on joint agent trajectories; '
           '[USA](https://arxiv.org/abs/2609.34225) prepares distilled agent experts for merging.', '',
           'Follow a [complete reading path](resources/reading-order.md) or compare '
           '[methods by their supervision requirements](resources/method-comparison.md).', '',
           '## Updates', '']
    for item in json.loads(NEWS.read_text())['items'][:2]:
        parts.append(f'- **{item["date"]}** — {item["text"]} [{item["label"]}]({item["url"]})')
    parts += ['', '[All updates and survey releases](CHANGELOG.md)', '',
           '## The collection', '',
           'The central topic is research that improves, explains, or implements teacher-to-student transfer '
           'on student-generated states. Direct matching, hybrid training, teacher-mediated RL, and related '
           'comparators are labeled separately. Each topic brings together mechanisms and evidence; '
           'it is a reading guide rather than a performance ranking.', '',
           '<sub>Newest first within each topic. Dates denote first public release. '
           'Code links identify associated resources; unofficial reproductions are labeled.</sub>']
    for home,label in SECTIONS:
        group=[r for r in ordered if r['home']==home]
        parts+=['',f'<a id="{heading_id(home)}"></a>','',f'### {label}', '',
                f'*{QUESTIONS[home]}*', '',
                f'<details{" open" if home != "background" else ""}><summary>{len(group)} entries · expand / collapse</summary>', '']
        for r in group:
            resources=' · '.join(f'[Code {i+1}]({url})' if len(r['code_urls'])>1 else f'[Code]({url})'
                                 for i,url in enumerate(r['code_urls']))
            if r['code_urls'] and r['code_status'].startswith('Unofficial'):
                resources += ' (unofficial reproduction)'
            meta = f'{r["submitted"]} · {ROLES.get(r["mechanism"],r["mechanism"])}'
            if resources:
                meta += ' · ' + resources
            parts += [f'- **[{cell(r["title"])}]({r["paper_url"]})**  ',
                      f'  <sub>{meta}</sub>  ', f'  {cell(r["description"])}', '']
        parts+=['</details>', '', '[↑ Back to top](#readme-top)']
    parts+=['','## Visual reference snapshots','',
            '<details><summary>Teacher–student model atlas · June 2026</summary>', '',
            'Rows represent teacher models, columns represent student models, and cells show reported pair occurrences '
            'in the June 2026 catalog snapshot. Same-name models can use different conditioning information. '
            'This historical view is not a ranking of model quality or a count of the current collection.', '',
            '<a href="assets/model-atlas-heatmap.png"><img src="assets/model-atlas-heatmap.png" width="960" alt="Teacher–student model-pair matrix, June 2026 snapshot"></a>', '',
            '</details>', '',
            '<details><summary>A direct-matching loop</summary>', '',
            '<img src="assets/opd-overview.png" width="680" alt="Conceptual teacher–student on-policy learning loop">', '',
            'One direct-matching loop. Teacher feedback is not certified ground truth; other methods use '
            'different targets, divergences, or teacher-mediated rewards.', '', '</details>', '',
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
           f'Updated {date}. Implementations and resources associated with papers in the catalog. '
           'Unofficial reproductions are identified explicitly. Features and release completeness vary by repository.', '',
           '| Paper | Repository |','|---|---|']
    for r in ordered:
        if r['code_urls']:
            links='<br>'.join(f'[{cell(u.split("github.com/")[-1])}]({u})' for u in r['code_urls'])
            if r['code_status'].startswith('Unofficial'):
                links += '<br><sub>Unofficial reproduction</sub>'
            codes.append(f'| [{cell(r["title"])}]({r["paper_url"]}) | '+links+' |')
    codes+=['','Entries without a code link have no verified paper-specific repository listed.']
    (ROOT/'resources/codebases.md').write_text('\n'.join(codes)+'\n')
    objectives=['# Objective and feedback index','', '[Catalog](../README.md) · [Key equations](key-equations.md)', '',
                'Descriptions below distinguish targets, gradients and sampling. A paper can use several objectives '
                'across variants or stages; these entries are not mutually exclusive mathematical loss classes.', '',
                '| Paper | Objective or feedback | Role |','|---|---|---|']
    for r in ordered:
        if r['home']!='background':
            objectives.append(f'| [{cell(r["title"])}]({r["paper_url"]}) | {cell(r["objective"])} | {ROLES.get(r["mechanism"],r["mechanism"])} |')
    (ROOT/'resources/loss-taxonomy.md').write_text('\n'.join(objectives)+'\n')
    releases=['# Release history', '', 'Survey releases and public catalog updates.', '']
    for item in json.loads(NEWS.read_text())['items']:
        releases += [f'## {item["date"]}', '', item['text']+' '+f'[{item["label"]}]({item["url"]})', '']
    releases += ['The survey version labels refer to public arXiv releases. The reading catalog may include literature published after the latest survey PDF.']
    (ROOT/'CHANGELOG.md').write_text('\n'.join(releases)+'\n')
    print(f'Rendered {len(papers)} catalog records and {sum(bool(r["code_urls"]) for r in papers)} linked-code records.')


if __name__=='__main__':render()
