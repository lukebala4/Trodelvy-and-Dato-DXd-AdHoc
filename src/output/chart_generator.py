"""
Generates swimlane/Gantt-style timeline charts using matplotlib.

Each drug x population combination gets a group of lanes (one per geography),
with color-coded markers for different milestone types. Projected dates show
optimistic-to-conservative range as horizontal bars.
"""
import matplotlib
matplotlib.use("Agg")  # Non-interactive backend
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.patches as mpatches
from matplotlib.lines import Line2D
from datetime import date, datetime
from src.models import (
    DrugProgram, MilestoneType, Market, Confidence, MARKETS
)


# Milestone type -> (color, marker shape)
MILESTONE_STYLE = {
    MilestoneType.FDA_APPROVAL: ("#1f77b4", "D"),       # Blue diamond
    MilestoneType.EMA_APPROVAL: ("#2ca02c", "D"),       # Green diamond
    MilestoneType.MHRA_APPROVAL: ("#17becf", "D"),      # Cyan diamond
    MilestoneType.HEALTH_CANADA_APPROVAL: ("#9467bd", "D"),  # Purple diamond
    MilestoneType.NCCN_GUIDELINE: ("#ff7f0e", "s"),     # Orange square
    MilestoneType.ESMO_GUIDELINE: ("#d62728", "s"),     # Red square
    MilestoneType.NICE_DECISION: ("#8c564b", "o"),      # Brown circle
    MilestoneType.GBA_DECISION: ("#e377c2", "o"),       # Pink circle
    MilestoneType.HAS_DECISION: ("#7f7f7f", "o"),       # Grey circle
    MilestoneType.AIFA_DECISION: ("#bcbd22", "o"),      # Olive circle
    MilestoneType.AEMPS_DECISION: ("#aec7e8", "o"),     # Light blue circle
    MilestoneType.CADTH_DECISION: ("#98df8a", "o"),     # Light green circle
    MilestoneType.COMMERCIAL_LAUNCH: ("#ff9896", "^"),  # Light red triangle
    MilestoneType.SOC_INTEGRATION: ("#000000", "*"),    # Black star
}

# Confidence -> alpha
CONFIDENCE_ALPHA = {
    Confidence.KNOWN: 1.0,
    Confidence.HIGH: 0.85,
    Confidence.MODERATE: 0.65,
    Confidence.LOW: 0.45,
    Confidence.GAP: 0.25,
}

# Milestones to show on the chart (most important ones)
CHART_MILESTONES = [
    MilestoneType.FDA_APPROVAL,
    MilestoneType.EMA_APPROVAL,
    MilestoneType.MHRA_APPROVAL,
    MilestoneType.HEALTH_CANADA_APPROVAL,
    MilestoneType.NCCN_GUIDELINE,
    MilestoneType.ESMO_GUIDELINE,
    MilestoneType.NICE_DECISION,
    MilestoneType.GBA_DECISION,
    MilestoneType.HAS_DECISION,
    MilestoneType.AIFA_DECISION,
    MilestoneType.AEMPS_DECISION,
    MilestoneType.CADTH_DECISION,
    MilestoneType.SOC_INTEGRATION,
]


def _date_to_num(d: date) -> float:
    return mdates.date2num(datetime(d.year, d.month, d.day))


def create_swimlane_chart(
    program_sets: list[tuple[str, dict[str, DrugProgram]]],
    output_path: str,
    scenario: str = "base",
):
    """
    Create a swimlane timeline chart.

    Args:
        program_sets: List of (label, {scenario_name: DrugProgram})
        output_path: Path for the output PNG
        scenario: Which scenario to show markers for ("base" by default)
    """
    # Build lane data
    lanes = []  # List of (label, milestones_to_plot)
    group_boundaries = []  # Y positions where groups change

    y_pos = 0
    for group_label, scenarios in program_sets:
        group_start = y_pos
        base_program = scenarios.get(scenario, scenarios.get("base"))
        opt_program = scenarios.get("optimistic")
        cons_program = scenarios.get("conservative")

        for market in MARKETS:
            lane_label = f"{market.value}"
            milestones_data = []

            for mtype in CHART_MILESTONES:
                base_m = base_program.get_milestone(mtype, market) if base_program else None
                if not base_m or not base_m.date_value:
                    continue

                # Get optimistic/conservative for range bar
                opt_m = opt_program.get_milestone(mtype, market) if opt_program else None
                cons_m = cons_program.get_milestone(mtype, market) if cons_program else None

                opt_date = opt_m.date_value if opt_m and opt_m.date_value else base_m.date_value
                cons_date = cons_m.date_value if cons_m and cons_m.date_value else base_m.date_value

                milestones_data.append({
                    "type": mtype,
                    "base_date": base_m.date_value,
                    "opt_date": opt_date,
                    "cons_date": cons_date,
                    "confidence": base_m.confidence,
                    "is_projected": base_m.is_projected,
                })

            if milestones_data:
                lanes.append((lane_label, milestones_data, group_label))
                y_pos += 1

        group_boundaries.append((group_start, y_pos, group_label))

    if not lanes:
        print("No data to chart.")
        return

    # Create figure
    n_lanes = len(lanes)
    fig_height = max(8, n_lanes * 0.55 + 3)
    fig, ax = plt.subplots(figsize=(20, fig_height))

    # Plot each lane
    for i, (lane_label, milestones_data, group_label) in enumerate(lanes):
        y = n_lanes - 1 - i  # Invert so first lane is at top

        for md in milestones_data:
            color, marker = MILESTONE_STYLE.get(md["type"], ("#333333", "o"))
            alpha = CONFIDENCE_ALPHA.get(md["confidence"], 0.5)

            base_num = _date_to_num(md["base_date"])

            # Draw range bar if projected and range exists
            if md["is_projected"] and md["opt_date"] != md["cons_date"]:
                opt_num = _date_to_num(md["opt_date"])
                cons_num = _date_to_num(md["cons_date"])
                ax.barh(y, cons_num - opt_num, left=opt_num, height=0.15,
                        color=color, alpha=0.2, edgecolor="none")

            # Draw marker
            ax.scatter(base_num, y, color=color, marker=marker,
                       s=80, alpha=alpha, zorder=5, edgecolors="black",
                       linewidths=0.5)

    # Draw group labels and separators
    for start, end, label in group_boundaries:
        y_mid = n_lanes - 1 - (start + end) / 2 + 0.5
        y_sep = n_lanes - 0.5 - end
        if end < n_lanes:
            ax.axhline(y=y_sep, color="gray", linewidth=1.5, linestyle="-", alpha=0.5)

    # Y-axis labels with group prefixes
    y_labels = []
    for i, (lane_label, _, group_label) in enumerate(lanes):
        # Add group prefix for first lane in each group
        is_first_in_group = (i == 0 or lanes[i - 1][2] != group_label)
        if is_first_in_group:
            y_labels.append(f"{group_label}\n  {lane_label}")
        else:
            y_labels.append(f"  {lane_label}")

    ax.set_yticks(range(n_lanes))
    ax.set_yticklabels(list(reversed(y_labels)), fontsize=8, fontfamily="monospace")

    # X-axis: timeline
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%b\n%Y"))
    ax.xaxis.set_major_locator(mdates.MonthLocator(bymonth=[1, 4, 7, 10]))
    ax.tick_params(axis="x", labelsize=8)

    # Today line
    today_num = _date_to_num(date(2026, 4, 15))
    ax.axvline(x=today_num, color="red", linewidth=1.5, linestyle="--", alpha=0.7)
    ax.text(today_num, n_lanes - 0.2, " Today", color="red", fontsize=8,
            va="bottom", ha="left")

    # Grid
    ax.grid(axis="x", alpha=0.3, linestyle=":")
    ax.set_xlim(
        _date_to_num(date(2026, 1, 1)),
        _date_to_num(date(2030, 6, 1))
    )
    ax.set_ylim(-0.5, n_lanes - 0.5)

    # Legend
    legend_elements = []
    seen_types = set()
    for _, milestones_data, _ in lanes:
        for md in milestones_data:
            if md["type"] not in seen_types:
                color, marker = MILESTONE_STYLE[md["type"]]
                legend_elements.append(
                    Line2D([0], [0], marker=marker, color="w", markerfacecolor=color,
                           markeredgecolor="black", markersize=8,
                           label=md["type"].value, linewidth=0)
                )
                seen_types.add(md["type"])

    # Confidence legend
    legend_elements.append(Line2D([0], [0], marker="None", color="w", label=""))
    legend_elements.append(Line2D([0], [0], marker="None", color="w", label="Confidence:"))
    for conf in [Confidence.KNOWN, Confidence.HIGH, Confidence.MODERATE, Confidence.LOW]:
        alpha = CONFIDENCE_ALPHA[conf]
        legend_elements.append(
            Line2D([0], [0], marker="o", color="w", markerfacecolor=(0.3, 0.3, 0.3, alpha),
                   markeredgecolor="black", markersize=8,
                   label=f"  {conf.value}", linewidth=0)
        )

    ax.legend(handles=legend_elements, loc="upper left", bbox_to_anchor=(1.01, 1),
              fontsize=7, framealpha=0.9, ncol=1)

    # Title
    ax.set_title(
        "Drug Approval & SoC Integration Timeline — 1L mTNBC\n"
        "Trodelvy & Dato-DXd Forward-Looking Projections (Base Scenario)",
        fontsize=12, fontweight="bold", pad=15
    )

    plt.tight_layout()
    plt.savefig(output_path, dpi=200, bbox_inches="tight", facecolor="white")
    plt.close()
    print(f"Swimlane chart saved to: {output_path}")


def create_soc_comparison_chart(
    program_sets: list[tuple[str, dict[str, DrugProgram]]],
    output_path: str,
):
    """
    Create a focused SoC integration comparison chart.
    Shows only SoC integration dates across all drugs x markets with ranges.
    """
    fig, ax = plt.subplots(figsize=(16, 8))

    colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728"]
    bar_height = 0.18

    y_labels = []
    y_pos = 0

    for market in MARKETS:
        y_labels.append(market.value)
        base_y = y_pos

        for i, (label, scenarios) in enumerate(program_sets):
            for scenario_name, offset, alpha in [
                ("optimistic", -bar_height, 0.4),
                ("base", 0, 1.0),
                ("conservative", bar_height, 0.4),
            ]:
                prog = scenarios.get(scenario_name)
                if not prog:
                    continue
                soc_m = prog.get_milestone(MilestoneType.SOC_INTEGRATION, market)
                if not soc_m or not soc_m.date_value:
                    continue

                x = _date_to_num(soc_m.date_value)
                y = base_y + (i - len(program_sets) / 2 + 0.5) * 0.25 + offset * 0.5

                marker = "D" if scenario_name == "base" else ("v" if scenario_name == "conservative" else "^")
                size = 100 if scenario_name == "base" else 50
                ax.scatter(x, y, color=colors[i % len(colors)], marker=marker,
                           s=size, alpha=alpha, zorder=5, edgecolors="black", linewidths=0.5)

        y_pos += 1

    # Formatting
    ax.set_yticks(range(len(MARKETS)))
    ax.set_yticklabels(y_labels, fontsize=10)
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
    ax.xaxis.set_major_locator(mdates.MonthLocator(bymonth=[1, 4, 7, 10]))
    ax.tick_params(axis="x", labelsize=9, rotation=45)
    ax.grid(axis="x", alpha=0.3, linestyle=":")

    # Today line
    today_num = _date_to_num(date(2026, 4, 15))
    ax.axvline(x=today_num, color="red", linewidth=1.5, linestyle="--", alpha=0.7)

    # Legend
    legend_elements = []
    for i, (label, _) in enumerate(program_sets):
        legend_elements.append(
            Line2D([0], [0], marker="D", color="w", markerfacecolor=colors[i % len(colors)],
                   markeredgecolor="black", markersize=8, label=label, linewidth=0)
        )
    legend_elements.append(
        Line2D([0], [0], marker="^", color="w", markerfacecolor="gray",
               markersize=6, label="Optimistic", linewidth=0)
    )
    legend_elements.append(
        Line2D([0], [0], marker="v", color="w", markerfacecolor="gray",
               markersize=6, label="Conservative", linewidth=0)
    )
    ax.legend(handles=legend_elements, loc="upper left", bbox_to_anchor=(1.01, 1), fontsize=8)

    ax.set_title(
        "SoC Integration Timeline Comparison — 1L mTNBC by Geography\n"
        "(Base scenario with optimistic/conservative range)",
        fontsize=11, fontweight="bold", pad=15
    )

    ax.set_xlim(
        _date_to_num(date(2026, 1, 1)),
        _date_to_num(date(2030, 6, 1))
    )

    plt.tight_layout()
    plt.savefig(output_path, dpi=200, bbox_inches="tight", facecolor="white")
    plt.close()
    print(f"SoC comparison chart saved to: {output_path}")
