"""Render catalog statistics, using only the public catalog.

Run ``python scripts/build_catalog_charts.py`` from any working directory.
Requires Matplotlib; SVG text stays editable and PNGs provide portable previews.
The source date is the catalog's update date, not the time this script is run.
"""
from __future__ import annotations

import argparse
import calendar
from collections import Counter
from datetime import date
import hashlib
import json
import math
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import ticker
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

ROOT = Path(__file__).resolve().parents[1]
TOPICS = [
    ("4", "Objectives and update rules"),
    ("5", "Teacher and supervision construction"),
    ("6", "Data and training dynamics"),
    ("7", "Agentic and multi-turn distillation"),
    ("8", "Mechanisms, failures, and evaluation"),
    ("9", "Applications and systems"),
    ("background", "Foundations and related background"),
]
ROLES = [
    ("direct_opd", "Direct OPD"),
    ("hybrid_opd", "Hybrid OPD"),
    ("analysis", "Analysis"),
    ("background", "Background"),
    ("teacher_mediated_rl", "Teacher-mediated RL"),
    ("application", "Application / system report"),
    ("offline_distillation", "Offline comparator"),
    ("interactive_imitation", "Interactive imitation"),
]
PAPER = "#f6f5ef"
INK = "#294a3d"
MUTED = "#637165"
LINE = "#d7ded2"
GREEN = "#527967"
SAGE = "#8caa94"
PALE = "#e5eade"
GOLD = "#b19159"


def aggregate(catalog: dict, source_hash: str) -> dict:
    """Validate identities and dates before computing mutually exclusive totals."""
    updated = date.fromisoformat(catalog["updated_on"])
    papers = catalog["papers"]
    if not papers:
        raise ValueError("Cannot chart an empty catalog")
    ids = [paper["paper_id"] for paper in papers]
    if len(ids) != len(set(ids)):
        raise ValueError("Duplicate paper IDs in catalog")
    topic_counts = Counter(paper["home"] for paper in papers)
    role_counts = Counter(paper["mechanism"] for paper in papers)
    for counts, labels in [(topic_counts, TOPICS), (role_counts, ROLES)]:
        unknown = set(counts) - dict(labels).keys()
        if unknown:
            raise ValueError(f"Unknown chart categories: {sorted(unknown)}")
    dates = [date.fromisoformat(paper["submitted"]) for paper in papers]
    if max(dates) > updated:
        raise ValueError("A first-release date exceeds the catalog update date")
    for paper, released in zip(papers, dates):
        if paper["year"] != released.year:
            raise ValueError(f"Year and first-release date disagree: {paper['paper_id']}")
    n = len(papers)

    def rows(counts, labels):
        return [dict(key=key, label=label, count=counts[key],
                     percent=round(100 * counts[key] / n, 4))
                for key, label in labels]

    annual = Counter(d.year for d in dates)
    monthly = Counter(d.month for d in dates if d.year == updated.year)
    current_month_complete = updated.day == calendar.monthrange(updated.year, updated.month)[1]
    return {
        "schema_version": 1,
        "catalog_updated_on": updated.isoformat(),
        "catalog_sha256": source_hash,
        "source": "catalog.json",
        "total_entries": n,
        "counting_unit": "One unique catalog entry; one home topic and one role per entry.",
        "role_note": "Roles describe a paper's place in the collection, not mathematical loss classes.",
        "topics": rows(topic_counts, TOPICS),
        "roles": rows(role_counts, ROLES),
        "timeline": {
            "date_field": "submitted",
            "date_meaning": "First public release; not the date added to this collection.",
            "scope": "Entries in this collection, including foundations and related background.",
            "latest_first_release": max(dates).isoformat(),
            "year": updated.year,
            "entries_in_year": annual[updated.year],
            "entries_before_year": sum(v for k, v in annual.items() if k < updated.year),
            "annual": [{"year": year, "count": annual[year]} for year in sorted(annual)],
            "monthly": [{"month": f"{updated.year}-{month:02d}", "count": monthly[month],
                         "calendar_month_complete": month < updated.month or current_month_complete}
                        for month in range(1, updated.month + 1)],
            "coverage_note": "Collection counts do not establish complete coverage of all released papers.",
        },
    }


def configure_style():
    plt.rcParams.update({
        "font.family": "DejaVu Sans", "font.size": 11,
        "text.color": INK, "axes.labelcolor": MUTED,
        "xtick.color": MUTED, "ytick.color": MUTED,
        "figure.facecolor": PAPER, "axes.facecolor": PAPER,
        "savefig.facecolor": PAPER, "svg.fonttype": "none",
        "svg.hashsalt": "opd-catalog-charts-v1", "axes.unicode_minus": False,
    })


def heading(fig, kicker, title, subtitle):
    fig.text(.045, .941, kicker, color=MUTED, fontsize=9.5, weight="medium")
    fig.text(.045, .864, title, fontsize=25, fontfamily="DejaVu Serif")
    fig.text(.045, .804, subtitle, color=MUTED, fontsize=11)


def footer(fig, data, line1, line2=None):
    fig.add_artist(plt.Line2D([.045, .955], [.107, .107], transform=fig.transFigure,
                             color=LINE, linewidth=.8))
    fig.text(.045, .067, line1, fontsize=9, color=MUTED)
    if line2:
        fig.text(.045, .032, line2, fontsize=9, color=MUTED)
    fig.text(.955, .032, data["catalog_updated_on"], fontsize=9, color=MUTED,
             horizontalalignment="right")


def save(fig, path, description):
    fig.savefig(path.with_suffix(".svg"), metadata={"Date": None, "Title": path.stem,
                                                    "Description": description})
    fig.savefig(path.with_suffix(".png"), dpi=160,
                metadata={"Description": description})
    plt.close(fig)


def overview(data, destination):
    fig = plt.figure(figsize=(12, 7.8))
    heading(fig, "OPD / RESEARCH LIBRARY", "The collection, at a glance",
            f"{data['total_entries']} entries  ·  One home topic and one role per entry")
    maximum = max(row["percent"] for group in ["topics", "roles"] for row in data[group])
    limit = math.ceil(maximum / 10) * 10
    for left, group, title, color in [(.045, "topics", "Reading topics", SAGE),
                                      (.545, "roles", "Roles in the collection", GREEN)]:
        ax = fig.add_axes([left, .172, .409, .546])
        ax.set_xlim(0, limit)
        ax.set_ylim(-.15, 7.85)
        ax.set_axis_off()
        fig.text(left, .751, title, fontsize=14, weight="medium")
        for i, row in enumerate(data[group]):
            y = 7.4 - i
            ax.text(0, y, row["label"], va="center", fontsize=10.8)
            ax.text(limit, y, f"{row['count']}  ·  {row['percent']:.1f}%", va="center",
                    ha="right", fontsize=10, color=MUTED)
            ax.barh(y - .34, limit, height=.12, color=PALE, zorder=0)
            ax.barh(y - .34, row["percent"], height=.12, color=color, zorder=1)
        ax.text(0, -.15, "0%", va="top", color=MUTED, fontsize=9)
        ax.text(limit, -.15, f"{limit:g}% of the collection", ha="right", va="top",
                color=MUTED, fontsize=9)
    fig.add_artist(plt.Line2D([.50, .50], [.19, .765], transform=fig.transFigure,
                             color=LINE, linewidth=.8))
    footer(fig, data, "Each panel accounts for every entry once. Percentages use the full collection as the denominator.",
           "Roles are reading labels, not mathematical loss classes.  ·  Source: public catalog")
    save(fig, destination / "catalog-overview", "Topic and role counts of the public OPD catalog.")


def timeline(data, destination):
    series = data["timeline"]
    year = series["year"]
    fig = plt.figure(figsize=(12, 6.1))
    heading(fig, "OPD / RESEARCH LIBRARY", "When the papers first appeared",
            f"{series['entries_in_year']} entries first released in {year}  ·  "
            f"{series['entries_before_year']} earlier entries  ·  {data['total_entries']} in total")
    # Earlier years are separate labeled categories. Current-year bars use
    # months; neither side suggests that these are equal-duration intervals.
    older = [row for row in series["annual"] if row["year"] < year]
    ax_old = fig.add_axes([.063, .235, .235, .46])
    ax = fig.add_axes([.385, .235, .57, .46])
    fig.text(.063, .744, f"Earlier years · {series['entries_before_year']} entries", fontsize=12)
    fig.text(.385, .744, f"{year} · by month of first release", fontsize=12)
    for axis in (ax,):
        axis.spines[["top", "left", "right"]].set_visible(False)
        axis.spines["bottom"].set_color(LINE)
        axis.tick_params(axis="both", length=0, pad=7, labelsize=10)
        axis.grid(axis="y", color=LINE, linewidth=.7, zorder=0)
        axis.set_axisbelow(True)
        axis.yaxis.set_major_locator(ticker.MaxNLocator(nbins=4, integer=True))
        axis.set_ylabel("Entries", fontsize=9, labelpad=8)
    if older:
        years = [r["year"] for r in older]
        values = [r["count"] for r in older]
        ax_old.set_axis_off()
        ax_old.set_xlim(-max(values) * .29, max(values) * 1.2)
        ax_old.set_ylim(-.5, len(years) - .5)
        for i, (released, count) in enumerate(zip(years, values)):
            y = len(years) - i - 1
            ax_old.barh(y, count, height=.17, color=SAGE)
            ax_old.text(-max(values) * .05, y, str(released), ha="right",
                        va="center", fontsize=10, color=MUTED)
            ax_old.text(count + max(values) * .045, y, str(count), va="center", fontsize=10)
    else:
        ax_old.text(.5, .5, "No earlier entries", transform=ax_old.transAxes,
                    ha="center", color=MUTED)
    rows = series["monthly"]
    counts = [r["count"] for r in rows]
    bars = ax.bar(range(len(rows)), counts, width=.60, color=GREEN, zorder=2)
    labels = []
    for index, (row, bar) in enumerate(zip(rows, bars)):
        label = calendar.month_abbr[int(row["month"][-2:])]
        if not row["calendar_month_complete"]:
            bar.set_facecolor("#e6dfce")
            bar.set_edgecolor(GOLD)
            bar.set_linewidth(.8)
            bar.set_hatch("///")
            label += "*"
        labels.append(label)
        ax.text(index, row["count"] + max(counts) * .026 + .3,
                str(row["count"]), ha="center", va="bottom", fontsize=11)
    ax.set_xticks(range(len(rows)), labels)
    ax.set_xlim(-.6, len(rows) - .4)
    ax.set_ylim(0, max(counts, default=1) * 1.24 + 1)
    fig.add_artist(plt.Line2D([.339, .339], [.216, .744], transform=fig.transFigure,
                             color=LINE, linewidth=.8))
    fig.text(.063, .159, "First public release, not date added to the collection. Annual and monthly panels use separate scales.",
             fontsize=9, color=MUTED)
    partial = [r for r in rows if not r["calendar_month_complete"]]
    note = (f"* {calendar.month_name[int(partial[-1]['month'][-2:])]} is incomplete. " if partial else "")
    note += f"Latest first-release date in the catalog: {series['latest_first_release']}."
    footer(fig, data, note, "Counts describe this collection, including related background.  ·  Source: public catalog")
    save(fig, destination / "catalog-timeline", "First public release of papers in the public OPD catalog.")


def learning_loop(destination):
    """One conceptual direct-matching loop; no empirical quantities are drawn."""
    fig = plt.figure(figsize=(12, 4.8))
    heading(fig, "OPD / THE LEARNING LOOP", "Learn on the student's own trajectories",
            "A direct-matching example: collect student prefixes, obtain teacher targets, update the student.")
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_axis_off()
    blocks = [
        (.045, "01", "Student rollout", ["Generate a response", "with the current student."]),
        (.385, "02", "Teacher feedback", ["Predict next-token distributions", "on those same prefixes."]),
        (.725, "03", "Student update", ["Match student predictions", "to the teacher's soft targets."]),
    ]
    for x, number, title, lines in blocks:
        ax.add_patch(FancyBboxPatch((x, .375), .23, .325,
                     boxstyle="round,pad=0,rounding_size=.018", linewidth=.9,
                     edgecolor=LINE, facecolor=PALE))
        ax.text(x + .018, .65, number, fontsize=9, color=MUTED, va="center")
        ax.text(x + .018, .568, title, fontsize=14, va="center", color=INK)
        ax.text(x + .018, .475, "\n".join(lines), fontsize=10.2, va="center",
                linespacing=1.65, color=MUTED)
    for start, end, label in [(.285, .375, "Visited prefixes"), (.625, .715, "Soft targets")]:
        ax.add_patch(FancyArrowPatch((start, .538), (end, .538),
                     arrowstyle="-|>", mutation_scale=12, linewidth=1.3, color=GREEN))
        ax.text((start + end) / 2, .588, label, fontsize=8, ha="center", color=MUTED)
    ax.add_patch(FancyArrowPatch((.84, .366), (.16, .366),
                 connectionstyle="bar,fraction=-.125", arrowstyle="-|>",
                 mutation_scale=12, linewidth=1.2, color=GREEN))
    ax.text(.5, .225, "Repeat with the updated student", fontsize=11, ha="center", color=INK)
    ax.plot([.045, .955], [.135, .135], color=LINE, linewidth=.8)
    ax.text(.045, .082, "The teacher supplies targets; the optimizer computes the update. Teacher predictions can be imperfect.",
            fontsize=9.5, color=MUTED, va="center")
    ax.text(.045, .035, "Other OPD methods can use different losses, feedback, or mixtures of trajectories.",
            fontsize=9.5, color=MUTED, va="center")
    save(fig, destination / "catalog-learning-loop", "Conceptual direct-matching on-policy distillation loop.")


def render(catalog_path=ROOT / "resources/catalog.json", output_dir=ROOT / "assets",
           data_output=ROOT / "resources/chart-data.json"):
    raw = catalog_path.read_bytes()
    data = aggregate(json.loads(raw), hashlib.sha256(raw).hexdigest())
    output_dir.mkdir(parents=True, exist_ok=True)
    data_output.parent.mkdir(parents=True, exist_ok=True)
    data_output.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    configure_style()
    overview(data, output_dir)
    timeline(data, output_dir)
    learning_loop(output_dir)
    print(f"Rendered two charts and a learning loop from {data['total_entries']} entries; catalog updated {data['catalog_updated_on']}.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--catalog", type=Path, default=ROOT / "resources/catalog.json")
    parser.add_argument("--output-dir", type=Path, default=ROOT / "assets")
    parser.add_argument("--data-output", type=Path, default=ROOT / "resources/chart-data.json")
    args = parser.parse_args()
    render(args.catalog, args.output_dir, args.data_output)


if __name__ == "__main__":
    main()
