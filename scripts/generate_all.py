#!/usr/bin/env python3
"""
Main entry point: loads data, computes projections, generates all outputs.

Usage:
    python scripts/generate_all.py [--output-dir output/]

Outputs:
    - output/drug_approval_timelines.xlsx  (multi-tab workbook)
    - output/swimlane_timeline.png         (full milestone chart)
    - output/soc_comparison.png            (SoC-focused comparison chart)
    - docs/assumptions_log.md              (markdown assumptions doc)
"""
import sys
import os
import argparse
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.data.analog_data import build_enhertu_analog, build_trodelvy_3l_analog
from src.data.forward_looking_data import (
    build_trodelvy_ascent03, build_trodelvy_ascent04,
    build_dato_tb02, build_dato_tb05,
)
from src.data.assumptions import ASSUMPTIONS
from src.projection.lag_calculator import compute_analog_lags
from src.projection.scenario_engine import generate_all_scenarios
from src.projection.soc_integration import compute_all_soc_dates
from src.output.excel_writer import create_workbook
from src.output.chart_generator import create_swimlane_chart, create_soc_comparison_chart
from src.output.assumptions_renderer import render_assumptions_markdown


def main():
    parser = argparse.ArgumentParser(
        description="Generate drug approval timeline projections for 1L mTNBC"
    )
    parser.add_argument(
        "--output-dir", default="output/",
        help="Directory for generated output files (default: output/)"
    )
    args = parser.parse_args()

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    docs_dir = Path("docs")
    docs_dir.mkdir(parents=True, exist_ok=True)

    print("=" * 70)
    print("Drug Approval Timeline Projections — 1L mTNBC")
    print("Trodelvy & Dato-DXd Forward-Looking Analysis")
    print("=" * 70)

    # ── Step 1: Load analog data ──
    print("\n[1/7] Loading analog data...")
    enhertu = build_enhertu_analog()
    trodelvy_3l = build_trodelvy_3l_analog()
    print(f"  Enhertu: {len(enhertu.milestones)} milestones")
    print(f"  Trodelvy 3L+: {len(trodelvy_3l.milestones)} milestones")

    # ── Step 2: Compute observed lags from analogs ──
    print("\n[2/7] Computing analog lags...")
    enhertu_lags = compute_analog_lags(enhertu)
    trodelvy_3l_lags = compute_analog_lags(trodelvy_3l)
    all_lags = enhertu_lags + trodelvy_3l_lags
    print(f"  Derived {len(all_lags)} lag observations from 2 analogs")

    # ── Step 3: Load forward-looking drug programs ──
    print("\n[3/7] Loading forward-looking drug data...")
    trodelvy_03 = build_trodelvy_ascent03()
    trodelvy_04 = build_trodelvy_ascent04()
    dato_tb02 = build_dato_tb02()
    dato_tb05 = build_dato_tb05()
    print("  Trodelvy ASCENT-03 (CPS<10): loaded")
    print("  Trodelvy ASCENT-04 (CPS>=10): loaded")
    print("  Dato-DXd TROPION-Breast02 (CPS<10): loaded")
    print("  Dato-DXd TROPION-Breast05 (CPS>=10): loaded")

    # ── Step 4: Generate 3 scenarios for each program ──
    print("\n[4/7] Generating scenario projections...")
    trodelvy_03_scenarios = generate_all_scenarios(trodelvy_03, all_lags)
    trodelvy_04_scenarios = generate_all_scenarios(trodelvy_04, all_lags)
    dato_tb02_scenarios = generate_all_scenarios(dato_tb02, all_lags)
    dato_tb05_scenarios = generate_all_scenarios(dato_tb05, all_lags)
    print("  3 scenarios (optimistic/base/conservative) for each of 4 programs")

    # ── Step 5: Compute SoC integration dates ──
    print("\n[5/7] Computing SoC integration dates...")
    for name, scenarios in [
        ("Trodelvy ASCENT-03", trodelvy_03_scenarios),
        ("Trodelvy ASCENT-04", trodelvy_04_scenarios),
        ("Dato-DXd TB02", dato_tb02_scenarios),
        ("Dato-DXd TB05", dato_tb05_scenarios),
    ]:
        for scenario_name, program in scenarios.items():
            compute_all_soc_dates(program)
        base = scenarios["base"]
        soc_count = sum(
            1 for m in base.milestones
            if m.milestone_type.value == "SoC Integration"
        )
        print(f"  {name}: {soc_count} SoC dates computed (base scenario)")

    # ── Step 6: Generate outputs ──
    projection_sets = [
        ("Trodelvy 1L CPS<10 (ASCENT-03)", trodelvy_03_scenarios),
        ("Trodelvy 1L CPS>=10 (ASCENT-04)", trodelvy_04_scenarios),
        ("Dato-DXd 1L CPS<10 (TB02)", dato_tb02_scenarios),
        ("Dato-DXd 1L CPS>=10 (TB05)", dato_tb05_scenarios),
    ]

    print("\n[6/7] Generating Excel workbook...")
    excel_path = str(output_dir / "drug_approval_timelines.xlsx")
    create_workbook(
        analogs=[enhertu, trodelvy_3l],
        all_lags=all_lags,
        projection_sets=projection_sets,
        assumptions=ASSUMPTIONS,
        output_path=excel_path,
    )

    print("\n[7/7] Generating charts...")
    swimlane_path = str(output_dir / "swimlane_timeline.png")
    create_swimlane_chart(
        program_sets=projection_sets,
        output_path=swimlane_path,
    )

    soc_path = str(output_dir / "soc_comparison.png")
    create_soc_comparison_chart(
        program_sets=projection_sets,
        output_path=soc_path,
    )

    # Assumptions log
    assumptions_path = str(docs_dir / "assumptions_log.md")
    render_assumptions_markdown(ASSUMPTIONS, assumptions_path)

    # ── Summary ──
    print("\n" + "=" * 70)
    print("COMPLETE. Generated outputs:")
    print(f"  Excel:         {excel_path}")
    print(f"  Swimlane:      {swimlane_path}")
    print(f"  SoC Chart:     {soc_path}")
    print(f"  Assumptions:   {assumptions_path}")
    print("=" * 70)

    # Print quick SoC summary
    print("\nSoC Integration Summary (Base Scenario):")
    print("-" * 50)
    from src.models import MilestoneType, MARKETS
    for label, scenarios in projection_sets:
        base = scenarios["base"]
        print(f"\n{label}:")
        for market in MARKETS:
            soc = base.get_milestone(MilestoneType.SOC_INTEGRATION, market)
            if soc and soc.date_value:
                q = (soc.date_value.month - 1) // 3 + 1
                print(f"  {market.value:8s}: Q{q} {soc.date_value.year} ({soc.confidence.value})")
            else:
                print(f"  {market.value:8s}: TBD")


if __name__ == "__main__":
    main()
