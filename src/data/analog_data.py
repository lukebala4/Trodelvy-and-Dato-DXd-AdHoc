"""
Hard-coded known milestone dates for the two analog drugs used for timeline bracketing.

Analog 1 (Optimistic): Enhertu (trastuzumab deruxtecan) in 2L+ HER2+ mBC
  - Practice-changing, strong HTA outcomes, fast uptake
  - FDA full approval: Aug 2022 (DESTINY-Breast03)

Analog 2 (Conservative): Trodelvy (sacituzumab govitecan) in 3L+ mTNBC
  - Same TROP2 ADC class as the target assets, more challenging HTA path
  - FDA full approval: Apr 2021 (ASCENT)

Sources: FDA, EMA, MHRA, Health Canada public databases, NICE, CADTH, G-BA.
Dates marked GAP need primary research to fill.
"""
from datetime import date
from src.models import (
    DrugProgram, Milestone, MilestoneType, Market, Confidence
)


def build_enhertu_analog() -> DrugProgram:
    """Enhertu (T-DXd) in 2L+ HER2+ mBC — optimistic analog."""
    program = DrugProgram(
        drug_name="Enhertu (T-DXd)",
        indication="2L+ HER2+ mBC",
        trial_name="DESTINY-Breast03",
        sponsor="Daiichi Sankyo / AstraZeneca",
    )

    milestones = [
        # ── Trial ──
        Milestone(
            MilestoneType.TRIAL_PCD, Market.US,
            date(2022, 3, 15), Confidence.KNOWN,
            "ClinicalTrials.gov NCT03529110",
            "DESTINY-Breast03 primary analysis cutoff",
        ),
        Milestone(
            MilestoneType.TRIAL_READOUT, Market.US,
            date(2021, 9, 19), Confidence.KNOWN,
            "ESMO 2021 presentation",
            "First presentation at ESMO Congress 2021",
        ),

        # ── Regulatory Approvals ──
        Milestone(
            MilestoneType.FDA_APPROVAL, Market.US,
            date(2022, 8, 5), Confidence.KNOWN,
            "FDA approval letter",
            "Full approval for 2L+ HER2+ mBC based on DESTINY-Breast03",
        ),
        Milestone(
            MilestoneType.EMA_APPROVAL, Market.FR,
            date(2023, 1, 24), Confidence.KNOWN,
            "EC decision",
            "EMA centralized procedure; EC marketing authorization",
        ),
        Milestone(
            MilestoneType.EMA_APPROVAL, Market.DE,
            date(2023, 1, 24), Confidence.KNOWN,
            "EC decision",
            "Same EMA approval applies to all EU5",
        ),
        Milestone(
            MilestoneType.EMA_APPROVAL, Market.IT,
            date(2023, 1, 24), Confidence.KNOWN,
            "EC decision",
        ),
        Milestone(
            MilestoneType.EMA_APPROVAL, Market.ES,
            date(2023, 1, 24), Confidence.KNOWN,
            "EC decision",
        ),
        Milestone(
            MilestoneType.MHRA_APPROVAL, Market.UK,
            date(2023, 1, 24), Confidence.KNOWN,
            "MHRA GBR reliance procedure",
            "MHRA followed EMA timeline via reliance pathway",
        ),
        Milestone(
            MilestoneType.HEALTH_CANADA_APPROVAL, Market.CA,
            date(2023, 2, 17), Confidence.KNOWN,
            "Health Canada NOC",
        ),

        # ── Guidelines ──
        Milestone(
            MilestoneType.NCCN_GUIDELINE, Market.US,
            date(2022, 9, 1), Confidence.HIGH,
            "NCCN Breast Cancer v5.2022",
            "Category 1 preferred within ~1 month of FDA approval",
        ),
        Milestone(
            MilestoneType.NCCN_GUIDELINE, Market.CA,
            date(2022, 9, 1), Confidence.HIGH,
            "NCCN Breast Cancer v5.2022",
            "NCCN also referenced in Canadian practice",
        ),
        Milestone(
            MilestoneType.ESMO_GUIDELINE, Market.UK,
            date(2023, 9, 15), Confidence.MODERATE,
            "ESMO mBC Living Guideline 2023",
            "Updated recommendation following full publication",
        ),
        Milestone(
            MilestoneType.ESMO_GUIDELINE, Market.FR,
            date(2023, 9, 15), Confidence.MODERATE,
            "ESMO mBC Living Guideline 2023",
        ),
        Milestone(
            MilestoneType.ESMO_GUIDELINE, Market.DE,
            date(2023, 9, 15), Confidence.MODERATE,
            "ESMO mBC Living Guideline 2023",
        ),
        Milestone(
            MilestoneType.ESMO_GUIDELINE, Market.IT,
            date(2023, 9, 15), Confidence.MODERATE,
            "ESMO mBC Living Guideline 2023",
        ),
        Milestone(
            MilestoneType.ESMO_GUIDELINE, Market.ES,
            date(2023, 9, 15), Confidence.MODERATE,
            "ESMO mBC Living Guideline 2023",
        ),

        # ── HTA / Reimbursement ──
        Milestone(
            MilestoneType.NICE_DECISION, Market.UK,
            date(2023, 10, 25), Confidence.KNOWN,
            "NICE TA942",
            "Recommended for routine commissioning",
        ),
        Milestone(
            MilestoneType.GBA_DECISION, Market.DE,
            date(2023, 5, 1), Confidence.MODERATE,
            "G-BA AMNOG assessment",
            "GAP: Exact G-BA decision date needs verification. Considerable additional benefit; approximate date.",
        ),
        Milestone(
            MilestoneType.HAS_DECISION, Market.FR,
            date(2023, 10, 1), Confidence.LOW,
            "Estimated from typical HAS timeline",
            "GAP: Exact HAS Transparency Committee opinion date needs research",
        ),
        Milestone(
            MilestoneType.AIFA_DECISION, Market.IT,
            date(2024, 3, 1), Confidence.LOW,
            "Estimated from typical AIFA timeline",
            "GAP: Exact AIFA Gazzetta Ufficiale publication date needs research",
        ),
        Milestone(
            MilestoneType.AEMPS_DECISION, Market.ES,
            date(2024, 4, 1), Confidence.LOW,
            "Estimated from typical AEMPS/IPT timeline",
            "GAP: Exact Spanish pricing/reimbursement date needs research",
        ),
        Milestone(
            MilestoneType.CADTH_DECISION, Market.CA,
            date(2023, 6, 29), Confidence.HIGH,
            "CADTH pCODR recommendation",
            "Recommended for reimbursement with clinical criteria",
        ),

        # ── Commercial Launch (US) ──
        Milestone(
            MilestoneType.COMMERCIAL_LAUNCH, Market.US,
            date(2022, 8, 15), Confidence.HIGH,
            "Daiichi Sankyo press release",
            "US commercial launch within days of FDA approval",
        ),
    ]

    program.milestones = milestones
    return program


def build_trodelvy_3l_analog() -> DrugProgram:
    """Trodelvy in 3L+ mTNBC — conservative analog."""
    program = DrugProgram(
        drug_name="Trodelvy (SG)",
        indication="3L+ mTNBC",
        trial_name="ASCENT",
        sponsor="Gilead Sciences",
    )

    milestones = [
        # ── Trial ──
        Milestone(
            MilestoneType.TRIAL_PCD, Market.US,
            date(2020, 11, 1), Confidence.HIGH,
            "ClinicalTrials.gov NCT02574455",
            "ASCENT trial primary completion",
        ),
        Milestone(
            MilestoneType.TRIAL_READOUT, Market.US,
            date(2020, 9, 19), Confidence.KNOWN,
            "ESMO 2020 presentation",
            "Primary results presented at ESMO Virtual 2020",
        ),

        # ── Regulatory Approvals ──
        Milestone(
            MilestoneType.FDA_APPROVAL, Market.US,
            date(2021, 4, 7), Confidence.KNOWN,
            "FDA approval letter",
            "Regular approval for 3L+ mTNBC (accelerated approval Apr 2020 converted)",
        ),
        Milestone(
            MilestoneType.EMA_APPROVAL, Market.FR,
            date(2021, 11, 10), Confidence.KNOWN,
            "EC decision",
            "EMA centralized procedure; ~7 months post-FDA",
        ),
        Milestone(
            MilestoneType.EMA_APPROVAL, Market.DE,
            date(2021, 11, 10), Confidence.KNOWN,
            "EC decision",
        ),
        Milestone(
            MilestoneType.EMA_APPROVAL, Market.IT,
            date(2021, 11, 10), Confidence.KNOWN,
            "EC decision",
        ),
        Milestone(
            MilestoneType.EMA_APPROVAL, Market.ES,
            date(2021, 11, 10), Confidence.KNOWN,
            "EC decision",
        ),
        Milestone(
            MilestoneType.MHRA_APPROVAL, Market.UK,
            date(2021, 12, 15), Confidence.HIGH,
            "MHRA approval",
            "MHRA followed shortly after EMA; approximate date",
        ),
        Milestone(
            MilestoneType.HEALTH_CANADA_APPROVAL, Market.CA,
            date(2022, 7, 18), Confidence.KNOWN,
            "Health Canada NOC",
            "~15 months post-FDA",
        ),

        # ── Guidelines ──
        Milestone(
            MilestoneType.NCCN_GUIDELINE, Market.US,
            date(2021, 5, 1), Confidence.HIGH,
            "NCCN Breast Cancer v4.2021",
            "Added within one update cycle of full approval",
        ),
        Milestone(
            MilestoneType.NCCN_GUIDELINE, Market.CA,
            date(2021, 5, 1), Confidence.HIGH,
            "NCCN Breast Cancer v4.2021",
        ),
        Milestone(
            MilestoneType.ESMO_GUIDELINE, Market.UK,
            date(2022, 3, 1), Confidence.MODERATE,
            "ESMO mBC Living Guideline update",
            "Approximate timing of ESMO guideline inclusion",
        ),
        Milestone(
            MilestoneType.ESMO_GUIDELINE, Market.FR,
            date(2022, 3, 1), Confidence.MODERATE,
            "ESMO mBC Living Guideline update",
        ),
        Milestone(
            MilestoneType.ESMO_GUIDELINE, Market.DE,
            date(2022, 3, 1), Confidence.MODERATE,
            "ESMO mBC Living Guideline update",
        ),
        Milestone(
            MilestoneType.ESMO_GUIDELINE, Market.IT,
            date(2022, 3, 1), Confidence.MODERATE,
            "ESMO mBC Living Guideline update",
        ),
        Milestone(
            MilestoneType.ESMO_GUIDELINE, Market.ES,
            date(2022, 3, 1), Confidence.MODERATE,
            "ESMO mBC Living Guideline update",
        ),

        # ── HTA / Reimbursement ──
        Milestone(
            MilestoneType.NICE_DECISION, Market.UK,
            date(2023, 7, 12), Confidence.KNOWN,
            "NICE TA900",
            "Recommended via Cancer Drugs Fund; ~27 months post-FDA",
        ),
        Milestone(
            MilestoneType.GBA_DECISION, Market.DE,
            date(2022, 4, 1), Confidence.MODERATE,
            "G-BA AMNOG assessment",
            "GAP: Exact date approximate — verify against G-BA records",
        ),
        Milestone(
            MilestoneType.HAS_DECISION, Market.FR,
            date(2022, 9, 1), Confidence.LOW,
            "Estimated from typical HAS timeline",
            "GAP: Exact HAS TC opinion date for Trodelvy 3L+ needs research",
        ),
        Milestone(
            MilestoneType.AIFA_DECISION, Market.IT,
            date(2023, 3, 1), Confidence.LOW,
            "Estimated from typical AIFA timeline",
            "GAP: Exact AIFA GU publication date needs research",
        ),
        Milestone(
            MilestoneType.AEMPS_DECISION, Market.ES,
            date(2023, 7, 1), Confidence.LOW,
            "Estimated from typical AEMPS timeline",
            "GAP: Exact Spanish pricing decision date needs research",
        ),
        Milestone(
            MilestoneType.CADTH_DECISION, Market.CA,
            date(2022, 10, 1), Confidence.MODERATE,
            "CADTH pCODR recommendation",
            "Approximate date; ~18 months post-FDA",
        ),

        # ── Commercial Launch (US) ──
        Milestone(
            MilestoneType.COMMERCIAL_LAUNCH, Market.US,
            date(2021, 4, 15), Confidence.HIGH,
            "Gilead press release",
            "US launch shortly after FDA approval",
        ),
    ]

    program.milestones = milestones
    return program
