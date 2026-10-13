"""Build the public reading list and indexes from the curated catalog.

Render paper descriptions, resource links, and release announcements.
"""
from __future__ import annotations
import json
import re
from pathlib import Path
from build_catalog_charts import render as render_charts

ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/'resources/catalog.json'
NEWS=ROOT/'resources/news.json'
PUBLIC_FIELDS={'paper_id','arxiv_id','title','authors','year','submitted',
               'paper_url','description','objective','mechanism','home',
               'code_urls','code_status','source_version','latest_version'}
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


def guide_table(headers, rows):
    """Use native cell widths so guides fill a README but shrink on phones."""
    lines=['<table>', '<thead><tr>']
    lines += [f'<th align="left" width="440">{header}</th>' for header in headers]
    lines += ['</tr></thead>', '<tbody>']
    for row in rows:
        lines += ['<tr>', *(f'<td>{value}</td>' for value in row), '</tr>']
    return '\n'.join(lines + ['</tbody>', '</table>'])


def render():
    catalog=json.loads(DATA.read_text());papers=catalog['papers']
    for paper in papers:
        if set(paper)-PUBLIC_FIELDS:
            raise ValueError('Unsupported catalog fields for '+paper['paper_id'])
        if 'latest_version' in paper:
            aid = paper.get('arxiv_id')
            latest = paper['latest_version']
            if not aid or not isinstance(latest, str) or not re.fullmatch(
                re.escape(aid) + r'v[1-9]\d*', latest
            ):
                raise ValueError('Invalid latest_version for '+paper['paper_id'])
    ids=[r['paper_id'] for r in papers]
    if len(ids)!=len(set(ids)):raise ValueError('Duplicate catalog IDs')
    date=catalog['updated_on'];ordered=sorted(papers,key=lambda r:(r['submitted'],r['paper_id']),reverse=True)
    code_count=sum(bool(r['code_urls']) for r in papers)
    parts=['<a id="readme-top"></a>', '',
           '<p align="center">',
           '  <a href="https://nick7nlp.github.io/OPDHub/">',
           '    <picture>',
           '      <source media="(prefers-color-scheme: dark) and (max-width: 600px)" srcset="assets/reading-room-mobile-dark.svg">',
           '      <source media="(max-width: 600px)" srcset="assets/reading-room-mobile-light.svg">',
           '      <source media="(prefers-color-scheme: dark)" srcset="assets/reading-room-dark.svg">',
           '      <img src="assets/reading-room-light.svg" width="1200" alt="Awesome LLM On-Policy Distillation — learning from teachers on the student’s own trajectories.">',
           '    </picture>',
           '  </a>',
           '</p>', '',
           '<p align="center">',
           '  <a href="https://arxiv.org/abs/2604.00626"><strong>Read the survey</strong></a> &nbsp;·&nbsp; '
           '<a href="https://nick7nlp.github.io/OPDHub/"><strong>Explore OPDHub ↗</strong></a> &nbsp;·&nbsp; '
           '<a href="#browse-the-literature">Browse papers</a> &nbsp;·&nbsp; <a href="#citation">Cite</a>',
           '</p>', '',
           f'<p align="center"><sub>{len(papers)} entries · {code_count} with code · '
           f'Updated&nbsp;{date.replace("-", "&#8209;")}</sub></p>', '',
           'A reading companion to **[A Survey of On-Policy Distillation for Large Language Models](https://arxiv.org/abs/2604.00626)**.', '',
           '<a id="a-few-good-starting-points"></a>', '',
           '## Start reading', '',
           guide_table(['Follow a question', 'Start with'], [
               ('<strong>How does the student learn?</strong><br><sub>Sampling, divergence, and the policy update.</sub>',
                '<a href="https://arxiv.org/abs/2306.13649">GKD</a> · <a href="https://arxiv.org/abs/2306.08543">MiniLLM</a>'),
               ('<strong>Where does supervision come from?</strong><br><sub>Solutions and feedback as teacher context.</sub>',
                '<a href="https://arxiv.org/abs/2601.18734">OPSD</a> · <a href="https://arxiv.org/abs/2601.20802">SDPO</a>'),
               ('<strong>What transfers, and what does not?</strong><br><sub>Reasoning compatibility, skills, and knowledge.</sub>',
                '<a href="https://arxiv.org/abs/2604.13016">Rethinking OPD</a> · <a href="https://arxiv.org/abs/2610.09639">Skills vs. Knowledge</a>'),
               ('<strong>How do multiple agents learn?</strong><br><sub>Joint trajectories and merging distilled experts.</sub>',
                '<a href="https://arxiv.org/abs/2609.34234">MAS-OPD</a> · <a href="https://arxiv.org/abs/2609.34225">USA</a>'),
           ]), '',
           '**[Follow the full reading paths →](resources/reading-order.md)**', '',
           '<a id="the-collection"></a>', '<a id="find-your-question"></a>', '',
           '## Browse the literature', '',
           'Expand a topic to read the paper summaries, or '
           '**[search and filter on OPDHub ↗](https://nick7nlp.github.io/OPDHub/)**. '
           'Entries are ordered newest first within each topic.', '']
    for home,label in SECTIONS:
        group=[r for r in ordered if r['home']==home]
        parts+=['',f'<a id="{heading_id(home)}"></a>','',
                f'<a id="{label.lower().replace(",", "").replace(" ", "-")}"></a>', '',
                f'<details><summary><strong>{label}</strong>&nbsp;·&nbsp;{len(group)}</summary>', '',
                f'*{QUESTIONS[home]}*', '']
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
        parts+=['[↑ Back to topics](#browse-the-literature)', '', '</details>']
    parts+=['', '<details><summary>About the collection</summary>', '',
            'The central topic is research that improves, explains, or implements teacher-to-student transfer '
            'on student-generated states. Direct matching, hybrid training, teacher-mediated RL, and related '
            'comparators are labeled separately. Each topic brings together mechanisms and evidence; '
            'it is a reading guide rather than a performance ranking.', '',
            'Dates denote first public release. Code links identify associated resources; unofficial '
            'reproductions are labeled. The public survey is arXiv v4; the reading list includes later work.', '',
            '</details>', '',
            '## Research tools', '',
            guide_table(['Compare and understand', 'Implement and evaluate'], [
                ('<strong><a href="resources/method-comparison.md">Method comparison</a></strong><br><sub>Supervision requirements and practical trade-offs.</sub>',
                 '<strong><a href="resources/codebases.md">Code index</a></strong><br><sub>Implementations and associated resources.</sub>'),
                ('<strong><a href="resources/loss-taxonomy.md">Objectives</a> · <a href="resources/key-equations.md">Key equations</a></strong><br><sub>Targets, gradients, and sampling assumptions.</sub>',
                 '<strong><a href="resources/benchmarks.md">Evaluation guide</a></strong><br><sub>Benchmarks, costs, and transfer diagnostics.</sub>'),
                ('<strong><a href="resources/related-surveys.md">Related surveys</a></strong><br><sub>Connections to the broader literature.</sub>',
                 '<strong><a href="CONTRIBUTING.md">Suggest a paper or correction</a></strong><br><sub>Help keep the reading list useful.</sub>'),
            ]), '',
            '<a id="updates"></a>', '<a id="visual-reference-snapshots"></a>', '',
            '## The collection in view', '',
            '<img src="assets/catalog-overview.svg" width="1200" alt="Current collection by reading topic and paper role; every entry is counted once in each panel.">', '',
            '<img src="assets/catalog-timeline.svg" width="1200" alt="First-release dates of papers in this collection; the current month is incomplete.">', '',
            'These figures use the [current catalog](resources/catalog.json). '
            'The [chart data](resources/chart-data.json) provide the exact counts and definitions. '
            'Roles describe how papers fit into the collection; they are not loss-function classes.', '',
            '<details><summary>Latest additions and survey releases</summary>', '']
    for item in json.loads(NEWS.read_text())['items'][:2]:
        parts.append(f'- **{item["date"]}** — {item["text"]} [{item["label"]}]({item["url"]})')
    parts += ['', '[All updates and survey releases](CHANGELOG.md)', '', '</details>', '',
            '<details><summary>A direct-matching loop</summary>', '',
            '<img src="assets/catalog-learning-loop.svg" width="1200" alt="A student generates trajectories, a teacher supplies targets on the visited prefixes, and an optimizer updates the student; the loop then repeats.">', '',
            'One direct-matching example. See the [objective index](resources/loss-taxonomy.md) '
            'and [equation guide](resources/key-equations.md) for method-specific losses and feedback.', '', '</details>', '',
            '<details><summary>Archived exploratory visualizations</summary>', '',
            '[June 2026 model atlas](assets/model-atlas-heatmap.png) · '
            '[Earlier loss-label distribution](assets/loss-distribution.png) · '
            '[Earlier loss-label evolution](assets/loss-evolution.png)', '',
            'The atlas contains unverified model aliases and may count repeated model-pair mentions. '
            'The earlier loss plots mix overlapping objective labels. These archived exploratory '
            'visualizations are not reliable model-pair statistics or current collection counts. '
            'Use the current figures and method-specific indexes above.', '', '</details>', '',
            '## Citation','', '```bibtex','@misc{song2026surveyonpolicydistillationlarge,',
            '  title = {A Survey of On-Policy Distillation for Large Language Models},',
            '  author = {Mingyang Song and Mao Zheng},',
            '  year = {2026},',
            '  eprint = {2604.00626},',
            '  archivePrefix = {arXiv},',
            '  primaryClass = {cs.LG},',
            '  url = {https://arxiv.org/abs/2604.00626},','}','```','',
            'For corrections, provide the paper version and the primary source supporting the change. '
            'See [CONTRIBUTING.md](CONTRIBUTING.md).', '',
            '[MIT License](LICENSE) · [↑ Back to top](#readme-top)']
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
    render_charts()
    print(f'Rendered {len(papers)} catalog records and {sum(bool(r["code_urls"]) for r in papers)} linked-code records.')


if __name__=='__main__':render()
