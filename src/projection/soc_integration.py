"""
Computes SoC (Standard of Care) integration dates per market.

SoC integration = the LATER of:
  (a) Guideline inclusion (NCCN for US/CA, ESMO for EU/UK)
  (b) National reimbursement/HTA decision

Market-specific exceptions:
  - US: No HTA gate. SoC = max(NCCN guideline, commercial launch)
  - Germany: Access at EMA approval (free pricing period). SoC = max(ESMO, EMA approval)
  - UK (NICE via CDF): CDF access is interim, not full SoC; flagged in notes
"""
from datetime import date
from typing import Optional
from src.models import (
    DrugProgram, Milestone, MilestoneType, Market, Confidence,
    MARKETS, GUIDELINE_MILESTONE, HTA_MILESTONE, REGULATORY_MILESTONE
)


def compute_soc_date(program: DrugProgram, market: Market) -> Optional[Milestone]:
    """
    Compute SoC integration date for a drug program in a specific market.
    Returns a new SOC_INTEGRATION Milestone, or None if insufficient data.
    """
    guideline_type = GUIDELINE_MILESTONE.get(market)
    hta_type = HTA_MILESTONE.get(market)
    reg_type = REGULATORY_MILESTONE.get(market)

    # Get guideline date
    guideline_m = program.get_milestone(guideline_type, market) if guideline_type else None
    guideline_date = guideline_m.date_value if guideline_m else None

    # Market-specific logic
    if market == Market.US:
        # US: SoC = max(NCCN, commercial launch)
        launch_m = program.get_milestone(MilestoneType.COMMERCIAL_LAUNCH, Market.US)
        launch_date = launch_m.date_value if launch_m else None

        if guideline_date and launch_date:
            soc_date = max(guideline_date, launch_date)
            notes = f"US SoC = max(NCCN {guideline_date}, launch {launch_date})"
        elif launch_date:
            soc_date = launch_date
            notes = f"US SoC = launch date {launch_date} (NCCN already included)"
        elif guideline_date:
            soc_date = guideline_date
            notes = f"US SoC = NCCN date {guideline_date} (launch date unknown)"
        else:
            return None

    elif market == Market.DE:
        # Germany: Access at EMA approval. SoC = max(ESMO, EMA approval)
        reg_m = program.get_milestone(MilestoneType.EMA_APPROVAL, Market.DE)
        reg_date = reg_m.date_value if reg_m else None

        if guideline_date and reg_date:
            soc_date = max(guideline_date, reg_date)
            notes = f"DE SoC = max(ESMO {guideline_date}, EMA {reg_date}). G-BA does not gate access."
        elif reg_date:
            soc_date = reg_date
            notes = f"DE SoC = EMA approval {reg_date}"
        else:
            return None

    else:
        # All other markets: SoC = max(guideline, HTA/reimbursement)
        hta_m = program.get_milestone(hta_type, market) if hta_type else None
        hta_date = hta_m.date_value if hta_m else None

        if guideline_date and hta_date:
            soc_date = max(guideline_date, hta_date)
            notes = (
                f"{market.value} SoC = max(guideline {guideline_date}, "
                f"HTA {hta_date})"
            )
        elif hta_date:
            soc_date = hta_date
            notes = f"{market.value} SoC = HTA date {hta_date} (guideline unknown)"
        elif guideline_date:
            # For UK and Canada, NCCN/ESMO might be available but HTA not yet
            soc_date = guideline_date
            notes = f"{market.value} SoC = guideline {guideline_date} (HTA date unknown — likely later)"
        else:
            return None

    # Check if any component was projected
    is_projected = True
    if guideline_m and not guideline_m.is_projected:
        if market == Market.US:
            launch_m2 = program.get_milestone(MilestoneType.COMMERCIAL_LAUNCH, Market.US)
            if launch_m2 and not launch_m2.is_projected:
                is_projected = False
        elif hta_m and not hta_m.is_projected:
            is_projected = False

    # Confidence = lowest confidence of inputs
    input_confidences = []
    if guideline_m:
        input_confidences.append(guideline_m.confidence)
    if market == Market.US:
        launch_m3 = program.get_milestone(MilestoneType.COMMERCIAL_LAUNCH, Market.US)
        if launch_m3:
            input_confidences.append(launch_m3.confidence)
    elif hta_type:
        hta_m2 = program.get_milestone(hta_type, market)
        if hta_m2:
            input_confidences.append(hta_m2.confidence)

    confidence_order = [
        Confidence.KNOWN, Confidence.HIGH, Confidence.MODERATE,
        Confidence.LOW, Confidence.GAP
    ]
    worst_confidence = Confidence.LOW
    for c in input_confidences:
        if confidence_order.index(c) > confidence_order.index(worst_confidence):
            worst_confidence = c

    return Milestone(
        milestone_type=MilestoneType.SOC_INTEGRATION,
        market=market,
        date_value=soc_date,
        confidence=worst_confidence,
        source="Derived: max(guideline, reimbursement/access)",
        notes=notes,
        is_projected=is_projected,
    )


def compute_all_soc_dates(program: DrugProgram) -> DrugProgram:
    """Compute and add SoC integration milestones for all markets."""
    for market in MARKETS:
        soc = compute_soc_date(program, market)
        if soc:
            program.add_milestone(soc)
    return program
