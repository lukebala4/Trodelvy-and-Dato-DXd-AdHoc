"""
Applies analog-derived lags to produce optimistic/base/conservative projections
for each target drug program.
"""
import copy
from datetime import date, timedelta
from typing import Optional
from src.models import (
    DrugProgram, Milestone, MilestoneType, Market, Confidence, MARKETS
)
from src.projection.lag_calculator import (
    compute_analog_lags, get_lag_range, AnalogLag, DOWNSTREAM_MILESTONES
)


def add_months(d: date, months: float) -> date:
    """Add fractional months to a date."""
    total_days = int(months * 30.44)  # Average days per month
    return d + timedelta(days=total_days)


def project_milestone(
    fda_date: date,
    lag_months: float,
    milestone_type: MilestoneType,
    market: Market,
    scenario_name: str,
) -> Milestone:
    """Create a projected milestone by applying a lag to the FDA anchor date."""
    projected_date = add_months(fda_date, lag_months)

    # Confidence based on scenario spread later; default to MODERATE for projections
    confidence = Confidence.MODERATE

    return Milestone(
        milestone_type=milestone_type,
        market=market,
        date_value=projected_date,
        confidence=confidence,
        source=f"Analog-based projection ({scenario_name}): {lag_months:.1f} months post-FDA",
        notes=f"Projected from FDA approval {fda_date.isoformat()} + {lag_months:.1f} months",
        is_projected=True,
    )


def build_scenario(
    drug_program: DrugProgram,
    all_lags: list[AnalogLag],
    scenario_name: str,  # "optimistic", "base", "conservative"
) -> DrugProgram:
    """
    Apply analog-derived lags to fill projected milestones for a drug program.

    For each downstream milestone that doesn't already have a known date,
    project it using the appropriate lag from the analog data.

    scenario_name determines which lag to use:
    - "optimistic": minimum observed lag (faster analog)
    - "base": average of analog lags
    - "conservative": maximum observed lag (slower analog)
    """
    program = copy.deepcopy(drug_program)
    fda_date = program.get_fda_approval_date()

    if fda_date is None:
        return program

    scenario_index = {"optimistic": 0, "base": 1, "conservative": 2}
    idx = scenario_index.get(scenario_name, 1)

    for mtype, markets in DOWNSTREAM_MILESTONES:
        for market in markets:
            existing = program.get_milestone(mtype, market)
            # Don't overwrite known data
            if existing and existing.date_value and not existing.is_projected:
                continue

            lag_range = get_lag_range(all_lags, mtype, market)
            lag_value = lag_range[idx]

            if lag_value is not None:
                milestone = project_milestone(
                    fda_date, lag_value, mtype, market, scenario_name
                )
                program.add_milestone(milestone)

    return program


def generate_all_scenarios(
    drug_program: DrugProgram,
    all_lags: list[AnalogLag],
) -> dict[str, DrugProgram]:
    """Generate optimistic, base, and conservative scenario projections."""
    return {
        "optimistic": build_scenario(drug_program, all_lags, "optimistic"),
        "base": build_scenario(drug_program, all_lags, "base"),
        "conservative": build_scenario(drug_program, all_lags, "conservative"),
    }
