"""
Computes observed lags from analog data and derives projection ranges.

For each analog, calculates the months between FDA approval (T=0) and every
subsequent milestone. These observed lags are then used to project timelines
for the target assets.
"""
from datetime import date
from typing import Optional
from src.models import (
    DrugProgram, AnalogLag, MilestoneType, Market, MARKETS
)


def months_between(d1: date, d2: date) -> float:
    """Calculate months between two dates (d2 - d1). Positive if d2 > d1."""
    return (d2.year - d1.year) * 12 + (d2.month - d1.month) + (d2.day - d1.day) / 30.0


# Milestone types that represent downstream market events (relative to FDA T=0)
DOWNSTREAM_MILESTONES = [
    (MilestoneType.EMA_APPROVAL, [Market.FR, Market.DE, Market.IT, Market.ES]),
    (MilestoneType.MHRA_APPROVAL, [Market.UK]),
    (MilestoneType.HEALTH_CANADA_APPROVAL, [Market.CA]),
    (MilestoneType.NCCN_GUIDELINE, [Market.US, Market.CA]),
    (MilestoneType.ESMO_GUIDELINE, [Market.UK, Market.FR, Market.DE, Market.IT, Market.ES]),
    (MilestoneType.NICE_DECISION, [Market.UK]),
    (MilestoneType.GBA_DECISION, [Market.DE]),
    (MilestoneType.HAS_DECISION, [Market.FR]),
    (MilestoneType.AIFA_DECISION, [Market.IT]),
    (MilestoneType.AEMPS_DECISION, [Market.ES]),
    (MilestoneType.CADTH_DECISION, [Market.CA]),
    (MilestoneType.COMMERCIAL_LAUNCH, [Market.US]),
]


def compute_analog_lags(analog: DrugProgram) -> list[AnalogLag]:
    """
    Given an analog DrugProgram with known milestones, compute the observed
    lag in months from FDA approval to each downstream milestone.
    """
    fda_date = analog.get_fda_approval_date()
    if fda_date is None:
        return []

    lags = []
    for mtype, markets in DOWNSTREAM_MILESTONES:
        for market in markets:
            m = analog.get_milestone(mtype, market)
            if m and m.date_value:
                lag = months_between(fda_date, m.date_value)
                lags.append(AnalogLag(
                    analog_name=f"{analog.drug_name} ({analog.indication})",
                    milestone_type=mtype,
                    market=market,
                    lag_months=round(lag, 1),
                    source=m.source,
                ))

    return lags


def get_lag_range(
    all_lags: list[AnalogLag],
    milestone_type: MilestoneType,
    market: Market,
) -> tuple[Optional[float], Optional[float], Optional[float]]:
    """
    For a given milestone type and market, return (optimistic, mid, conservative)
    lag in months from the available analogs.

    - optimistic = minimum observed lag (faster analog)
    - conservative = maximum observed lag (slower analog)
    - mid = average of the two

    Returns (None, None, None) if no analog data exists for this combination.
    """
    matching = [
        lag for lag in all_lags
        if lag.milestone_type == milestone_type and lag.market == market
        and lag.lag_months is not None
    ]

    if not matching:
        return (None, None, None)

    lag_values = [lag.lag_months for lag in matching]
    optimistic = min(lag_values)
    conservative = max(lag_values)
    mid = round(sum(lag_values) / len(lag_values), 1)

    return (optimistic, mid, conservative)


def get_all_lag_ranges(all_lags: list[AnalogLag]) -> dict:
    """
    Compute lag ranges for every milestone type x market combination.
    Returns dict keyed by (MilestoneType, Market) -> (optimistic, mid, conservative).
    """
    ranges = {}
    for mtype, markets in DOWNSTREAM_MILESTONES:
        for market in markets:
            ranges[(mtype, market)] = get_lag_range(all_lags, mtype, market)
    return ranges
