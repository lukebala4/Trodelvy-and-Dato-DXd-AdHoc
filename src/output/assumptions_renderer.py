"""
Renders the assumptions registry into a markdown document.
"""
from src.models import Assumption


def render_assumptions_markdown(assumptions: list[Assumption], output_path: str):
    """Generate a structured markdown assumptions log."""
    lines = [
        "# Assumptions & Data Gaps Log",
        "",
        "## Overview",
        "",
        "This document records every assumption that drives the forward-looking timeline",
        "projections for Trodelvy and Dato-DXd in 1L mTNBC. Assumptions are categorized",
        "and tracked with impact levels and data gap flags.",
        "",
        f"**Total assumptions:** {len(assumptions)}",
        f"**Data gaps requiring research:** {sum(1 for a in assumptions if a.gap_flag)}",
        "",
        "---",
        "",
    ]

    # Group by category
    categories = {}
    for a in assumptions:
        categories.setdefault(a.category, []).append(a)

    for category, items in categories.items():
        lines.append(f"## {category}")
        lines.append("")
        lines.append("| ID | Description | Impact | Drug | Gap? |")
        lines.append("|:---|:-----------|:------:|:----:|:----:|")

        for a in items:
            drug = a.related_drug or "General"
            gap = "**YES**" if a.gap_flag else "No"
            desc = a.description.replace("|", "/")
            lines.append(f"| {a.id} | {desc} | {a.impact} | {drug} | {gap} |")

        lines.append("")

    # Data gaps summary
    gaps = [a for a in assumptions if a.gap_flag]
    if gaps:
        lines.append("---")
        lines.append("")
        lines.append("## Priority Data Gaps")
        lines.append("")
        lines.append("The following gaps should be filled through primary research to improve")
        lines.append("projection confidence:")
        lines.append("")
        for a in gaps:
            lines.append(f"- **{a.id}**: {a.description}")
        lines.append("")

    with open(output_path, "w") as f:
        f.write("\n".join(lines))

    print(f"Assumptions log saved to: {output_path}")
