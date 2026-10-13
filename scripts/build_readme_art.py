"""Rebuild the README masthead for narrow/wide screens and light/dark themes."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PALETTES = {
    'light': dict(paper='#f5f5ee', ink='#294a3d', muted='#576b5d',
                  line='#d6ded0', accent='#7a9883', soft='#e7ece0'),
    'dark': dict(paper='#192920', ink='#e5eddf', muted='#b1c3ae',
                 line='#364d3d', accent='#94b49b', soft='#263e2d'),
}


def masthead(theme, mobile=False):
    colors = PALETTES[theme]
    width, height = (640, 380) if mobile else (1200, 332)
    pieces = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
        f'viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">',
        '<title id="title">On-policy distillation — a research library for large language models</title>',
        '<desc id="desc">Learning from teachers on the student’s own trajectories: '
        'student rollout, teacher feedback, student update.</desc>',
        '<style>',
        'text{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Arial,sans-serif}',
        '.serif{font-family:Georgia,"Times New Roman",serif;letter-spacing:-2px}',
        *[f'.{name}{{fill:{value}}}' for name, value in colors.items()],
        f'.rule{{fill:none;stroke:{colors["line"]};stroke-width:1}}',
        f'.flow{{fill:none;stroke:{colors["accent"]};stroke-width:1.6;stroke-linecap:round;stroke-linejoin:round}}',
        f'.mark{{fill:none;stroke:{colors["accent"]};stroke-width:4}}',
        '</style>',
        f'<rect width="{width}" height="{height}" rx="8" class="paper"/>',
    ]
    if mobile:
        pieces += [
            '<path d="M36 32v21m8-25v28m8-23v18" class="mark"/>',
            '<text x="70" y="48" class="muted" font-size="17" letter-spacing="2">OPD / RESEARCH LIBRARY</text>',
            '<text x="33" y="137" class="serif ink" font-size="76">On-policy</text>',
            '<text x="33" y="211" class="serif ink" font-size="76">distillation.</text>',
            '<text x="36" y="258" class="muted" font-size="22">Learning from teachers on the student’s</text>',
            '<text x="36" y="287" class="muted" font-size="22">own trajectories.</text>',
            '<path d="M36 316H604" class="rule"/>',
            '<g class="muted" font-size="18">',
            '<text x="36" y="349">Student rollout</text>',
            '<text x="244" y="349">Teacher feedback</text>',
            '<text x="476" y="349">Policy update</text>',
            '</g>',
            '<path d="M193 343h26m-5-4 5 4-5 4M425 343h26m-5-4 5 4-5 4" class="flow"/>',
        ]
    else:
        pieces += [
            '<path d="M49 33v20m8-25v29m8-23v18" class="mark"/>',
            '<text x="83" y="49" class="muted" font-size="14" letter-spacing="2.4">OPD / RESEARCH LIBRARY</text>',
            '<text x="43" y="142" class="serif ink" font-size="80">On-policy distillation.</text>',
            '<text x="48" y="193" class="muted" font-size="22">Learning from teachers on the student’s own trajectories.</text>',
            '<path d="M48 234H728" class="rule"/>',
            '<text x="48" y="276" class="muted" font-size="17" letter-spacing=".3">Objectives</text>',
            '<text x="238" y="276" class="muted" font-size="17" letter-spacing=".3">Supervision</text>',
            '<text x="455" y="276" class="muted" font-size="17" letter-spacing=".3">Interaction</text>',
            '<circle cx="201" cy="270" r="2" class="accent"/>',
            '<circle cx="418" cy="270" r="2" class="accent"/>',
            '<path d="M772 40V292" class="rule"/>',
            '<text x="820" y="49" class="muted" font-size="12" letter-spacing="1.6">THE LEARNING LOOP</text>',
        ]
        for index, (y, title, detail) in enumerate([
            (103, 'Student rollout', 'Generate trajectories'),
            (181, 'Teacher feedback', 'Supervise visited states'),
            (259, 'Student update', 'Improve the policy'),
        ], 1):
            pieces += [
                f'<circle cx="834" cy="{y}" r="14" class="soft"/>',
                f'<text x="834" y="{y + 5}" text-anchor="middle" class="ink" font-size="13">{index}</text>',
                f'<text x="866" y="{y - 1}" class="ink" font-size="21">{title}</text>',
                f'<text x="866" y="{y + 22}" class="muted" font-size="15">{detail}</text>',
            ]
            if index < 3:
                pieces.append(f'<path d="M834 {y + 24}v27m-4-5 4 5 4-5" class="flow"/>')
        pieces.append('<path d="M1133 259h17q18 0 18-18V121q0-18-18-18h-17m6-4-6 4 6 4" class="flow"/>')
    pieces.append('</svg>')
    return '\n'.join(pieces) + '\n'


if __name__ == '__main__':
    for theme in PALETTES:
        for mobile in (False, True):
            suffix = ('-mobile' if mobile else '') + f'-{theme}'
            (ROOT / f'assets/reading-room{suffix}.svg').write_text(masthead(theme, mobile))
    print('Rendered four README mastheads.')
