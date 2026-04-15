"""
Known anchors and forward-looking data for Trodelvy and Dato-DXd in 1L mTNBC.

These are the TARGET assets whose timelines we are projecting.
Known data points (NCCN status, FDA Priority Review, company guidance) are
hard-coded. Projected milestones will be filled by the projection engine.

Key context (from NCCN Version 2.2026 & 1.2026):
- Trodelvy ASCENT-03: Category 1 preferred 1L, BRCA-wt/PD-L1 CPS<10
- Trodelvy ASCENT-04 + Keytruda: Category 1 preferred 1L, PD-L1 CPS>=10
- Dato-DXd TROPION-Breast02: Category 2A preferred 1L, BRCA-wt/PD-L1 CPS<10
- Dato-DXd TROPION-Breast05: Not yet listed (PCD ~18 months out)
"""
from datetime import date
from src.models import (
    DrugProgram, Milestone, MilestoneType, Market, Confidence
)


def build_trodelvy_ascent03() -> DrugProgram:
    """Trodelvy monotherapy in 1L mTNBC (BRCA-wt, PD-L1 CPS<10) — ASCENT-03."""
    program = DrugProgram(
        drug_name="Trodelvy (SG)",
        indication="1L mTNBC (BRCA-wt, PD-L1 CPS<10)",
        trial_name="ASCENT-03",
        sponsor="Gilead Sciences",
    )

    milestones = [
        # ── Trial ──
        # Note: NCT05382299 is ASCENT-03. Registered PCD Jul 2028 is for final OS analysis.
        # PFS interim data already read out and supports regulatory submission.
        Milestone(
            MilestoneType.TRIAL_PCD, Market.US,
            date(2028, 7, 1), Confidence.KNOWN,
            "ClinicalTrials.gov NCT05382299 — registered PCD",
            "Registered PCD Jul 2028 is for final OS analysis. PFS interim already read out.",
            source_url="https://clinicaltrials.gov/study/NCT05382299",
        ),
        Milestone(
            MilestoneType.TRIAL_READOUT, Market.US,
            date(2025, 12, 1), Confidence.HIGH,
            "Gilead presentations / regulatory submission",
            "PFS data already presented; supports sBLA filing. Trial status: Active, Not Recruiting (623 enrolled).",
        ),

        # ── Regulatory (known anchors) ──
        Milestone(
            MilestoneType.FDA_SUBMISSION, Market.US,
            date(2026, 2, 1), Confidence.HIGH,
            "Gilead Q4 2025 Earnings guidance",
            "sBLA submission expected early 2026 based on ASCENT-03 data",
            source_url="https://www.gilead.com/news-and-press/financial-information",
        ),
        Milestone(
            MilestoneType.FDA_APPROVAL, Market.US,
            date(2026, 9, 1), Confidence.HIGH,
            "Gilead guidance: accelerated 1L launch H2 2026",
            "Assumes standard sBLA review (~6-8 months) or Priority Review (~6 months)",
            source_url="https://www.gilead.com/news-and-press/financial-information",
        ),

        # ── NCCN (already listed pre-approval) ──
        Milestone(
            MilestoneType.NCCN_GUIDELINE, Market.US,
            date(2026, 1, 15), Confidence.KNOWN,
            "NCCN Breast Cancer v1.2026",
            "Category 1 preferred 1L mTNBC BRCA-wt/PD-L1 CPS<10 — listed AHEAD of approval",
            source_url="https://www.nccn.org/guidelines/guidelines-detail?category=1&id=1419",
        ),
        Milestone(
            MilestoneType.NCCN_GUIDELINE, Market.CA,
            date(2026, 1, 15), Confidence.KNOWN,
            "NCCN Breast Cancer v1.2026",
            "NCCN also referenced in Canadian practice",
            source_url="https://www.nccn.org/guidelines/guidelines-detail?category=1&id=1419",
        ),

        # ── Commercial Launch (US) ──
        Milestone(
            MilestoneType.COMMERCIAL_LAUNCH, Market.US,
            date(2026, 10, 1), Confidence.HIGH,
            "Gilead guidance: accelerated launch H2 2026",
            "Targeting rapid launch post-approval",
            source_url="https://www.gilead.com/news-and-press/financial-information",
        ),
    ]

    program.milestones = milestones
    return program


def build_trodelvy_ascent04() -> DrugProgram:
    """Trodelvy + Keytruda in 1L mTNBC (PD-L1 CPS>=10) — ASCENT-04."""
    program = DrugProgram(
        drug_name="Trodelvy (SG) + Keytruda",
        indication="1L mTNBC (PD-L1 CPS>=10)",
        trial_name="ASCENT-04",
        sponsor="Gilead Sciences",
    )

    milestones = [
        # ── Trial ──
        # Note: NCT05382286 is ASCENT-04. Registered PCD Feb 2027 is for final OS analysis.
        # PFS data already published in NEJM Jan 2026.
        Milestone(
            MilestoneType.TRIAL_PCD, Market.US,
            date(2027, 2, 1), Confidence.KNOWN,
            "ClinicalTrials.gov NCT05382286 — registered PCD",
            "Registered PCD Feb 2027 is for final OS analysis. PFS data published NEJM 21 Jan 2026.",
            source_url="https://clinicaltrials.gov/study/NCT05382286",
        ),
        Milestone(
            MilestoneType.TRIAL_READOUT, Market.US,
            date(2026, 1, 21), Confidence.KNOWN,
            "NEJM publication — 21 Jan 2026",
            "Full ASCENT-04 PFS dataset published; supported NCCN Category 1 upgrade. Trial: Active, Not Recruiting (443 enrolled).",
            source_url="https://www.nejm.org/",
        ),

        # ── Regulatory ──
        Milestone(
            MilestoneType.FDA_SUBMISSION, Market.US,
            date(2026, 3, 1), Confidence.HIGH,
            "Gilead guidance",
            "sBLA for Trodelvy + Keytruda combo in 1L CPS>=10",
            source_url="https://www.gilead.com/news-and-press/financial-information",
        ),
        Milestone(
            MilestoneType.FDA_APPROVAL, Market.US,
            date(2026, 10, 1), Confidence.HIGH,
            "Projected based on Gilead H2 2026 launch target",
            "May come slightly after ASCENT-03 monotherapy approval",
            source_url="https://www.gilead.com/news-and-press/financial-information",
        ),

        # ── NCCN (already listed) ──
        Milestone(
            MilestoneType.NCCN_GUIDELINE, Market.US,
            date(2026, 1, 15), Confidence.KNOWN,
            "NCCN Breast Cancer v1.2026",
            "Initially Category 2A preferred; upgraded to Category 1 in v2.2026",
            source_url="https://www.nccn.org/guidelines/guidelines-detail?category=1&id=1419",
        ),
        Milestone(
            MilestoneType.NCCN_GUIDELINE, Market.CA,
            date(2026, 1, 15), Confidence.KNOWN,
            "NCCN Breast Cancer v1.2026",
            source_url="https://www.nccn.org/guidelines/guidelines-detail?category=1&id=1419",
        ),

        # ── Commercial Launch (US) ──
        Milestone(
            MilestoneType.COMMERCIAL_LAUNCH, Market.US,
            date(2026, 11, 1), Confidence.HIGH,
            "Gilead guidance: accelerated launch H2 2026",
            "Combo launch may follow monotherapy by ~1 month",
            source_url="https://www.gilead.com/news-and-press/financial-information",
        ),
    ]

    program.milestones = milestones
    return program


def build_dato_tb02() -> DrugProgram:
    """Dato-DXd in 1L mTNBC (BRCA-wt, PD-L1 CPS<10) — TROPION-Breast02."""
    program = DrugProgram(
        drug_name="Dato-DXd (Datroway)",
        indication="1L mTNBC (BRCA-wt, PD-L1 CPS<10)",
        trial_name="TROPION-Breast02",
        sponsor="Daiichi Sankyo / AstraZeneca",
    )

    milestones = [
        # ── Trial ──
        Milestone(
            MilestoneType.TRIAL_PCD, Market.US,
            date(2025, 3, 1), Confidence.MODERATE,
            "ClinicalTrials.gov NCT05104866 (estimated)",
            "TROPION-Breast02 primary completion estimate",
            source_url="https://clinicaltrials.gov/study/NCT05104866",
        ),
        Milestone(
            MilestoneType.TRIAL_READOUT, Market.US,
            date(2025, 6, 1), Confidence.HIGH,
            "Data presented at major congress",
            "Primary data supported sBLA submission",
        ),

        # ── Regulatory ──
        Milestone(
            MilestoneType.FDA_SUBMISSION, Market.US,
            date(2025, 12, 1), Confidence.KNOWN,
            "Daiichi Sankyo announcement",
            "sBLA accepted by FDA with Priority Review",
            source_url="https://www.daiichisankyo.com/media/press-releases/",
        ),
        Milestone(
            MilestoneType.FDA_APPROVAL, Market.US,
            date(2026, 6, 1), Confidence.HIGH,
            "PDUFA Q2 2026 under Priority Review",
            "Priority Review granted Feb 2026; PDUFA target date Q2 2026",
            source_url="https://www.fda.gov/drugs/development-approval-process-drugs/drug-approvals-and-databases",
        ),

        # EMA submission
        Milestone(
            MilestoneType.EMA_APPROVAL, Market.DE,
            date(2026, 9, 1), Confidence.MODERATE,
            "Daiichi Q3 FY2025 Earnings: EU approval projected Q3 2026",
            "Based on regulatory submission accepted Dec 2025",
            source_url="https://www.daiichisankyo.com/investors/",
        ),
        Milestone(
            MilestoneType.EMA_APPROVAL, Market.FR,
            date(2026, 9, 1), Confidence.MODERATE,
            "Daiichi Q3 FY2025 Earnings",
            source_url="https://www.daiichisankyo.com/investors/",
        ),
        Milestone(
            MilestoneType.EMA_APPROVAL, Market.IT,
            date(2026, 9, 1), Confidence.MODERATE,
            "Daiichi Q3 FY2025 Earnings",
            source_url="https://www.daiichisankyo.com/investors/",
        ),
        Milestone(
            MilestoneType.EMA_APPROVAL, Market.ES,
            date(2026, 9, 1), Confidence.MODERATE,
            "Daiichi Q3 FY2025 Earnings",
            source_url="https://www.daiichisankyo.com/investors/",
        ),

        # ── NCCN (already listed) ──
        Milestone(
            MilestoneType.NCCN_GUIDELINE, Market.US,
            date(2026, 1, 15), Confidence.KNOWN,
            "NCCN Breast Cancer v1.2026",
            "Category 2A other recommended; upgraded to Category 2A preferred in v2.2026",
            source_url="https://www.nccn.org/guidelines/guidelines-detail?category=1&id=1419",
        ),
        Milestone(
            MilestoneType.NCCN_GUIDELINE, Market.CA,
            date(2026, 1, 15), Confidence.KNOWN,
            "NCCN Breast Cancer v1.2026",
            source_url="https://www.nccn.org/guidelines/guidelines-detail?category=1&id=1419",
        ),

        # ── Commercial Launch (US) ──
        Milestone(
            MilestoneType.COMMERCIAL_LAUNCH, Market.US,
            date(2026, 7, 1), Confidence.HIGH,
            "Projected post-PDUFA",
            "Expected rapid US launch following FDA approval",
            source_url="https://www.daiichisankyo.com/media/press-releases/",
        ),
    ]

    program.milestones = milestones
    return program


def build_dato_tb05() -> DrugProgram:
    """Dato-DXd +/- durvalumab in 1L mTNBC (PD-L1 CPS>=10) — TROPION-Breast05."""
    program = DrugProgram(
        drug_name="Dato-DXd (Datroway) +/- Durvalumab",
        indication="1L mTNBC (PD-L1 CPS>=10)",
        trial_name="TROPION-Breast05",
        sponsor="Daiichi Sankyo / AstraZeneca",
    )

    milestones = [
        # ── Trial ──
        Milestone(
            MilestoneType.TRIAL_PCD, Market.US,
            date(2027, 7, 28), Confidence.KNOWN,
            "ClinicalTrials.gov NCT06103864 — registered PCD",
            "TROPION-Breast05. Status: Recruiting. Study completion: Sep 2030.",
            source_url="https://clinicaltrials.gov/study/NCT06103864",
        ),
        Milestone(
            MilestoneType.TRIAL_READOUT, Market.US,
            date(2028, 3, 1), Confidence.LOW,
            "Estimated: ~5 months post-PCD for major congress presentation",
            "Assumes data maturation + congress cycle",
        ),

        # ── Regulatory (all projected) ──
        Milestone(
            MilestoneType.FDA_SUBMISSION, Market.US,
            date(2028, 6, 1), Confidence.LOW,
            "Projected: ~3 months post-data readout",
        ),
        Milestone(
            MilestoneType.FDA_APPROVAL, Market.US,
            date(2029, 1, 1), Confidence.LOW,
            "Projected: ~6-10 months post-submission",
            "Assumes standard or Priority Review",
        ),

        # ── Commercial Launch (US) ──
        Milestone(
            MilestoneType.COMMERCIAL_LAUNCH, Market.US,
            date(2029, 2, 1), Confidence.LOW,
            "Projected post-FDA approval",
        ),
    ]

    program.milestones = milestones
    return program
