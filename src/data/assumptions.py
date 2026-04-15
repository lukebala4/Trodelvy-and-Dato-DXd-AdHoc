"""
Central assumptions registry. Every assumption that drives a projection is logged here.
This is the single source of truth — the Excel tab and markdown doc are generated from this.
"""
from src.models import Assumption

ASSUMPTIONS: list[Assumption] = [
    # ── Methodology ──
    Assumption(
        id="M001",
        category="Methodology",
        description="FDA approval date is used as T=0 anchor for all market-relative lag projections.",
        impact="High",
        status="Active",
    ),
    Assumption(
        id="M002",
        category="Methodology",
        description="Two analogs bracket the projection range: Enhertu 2L+ HER2+ mBC (optimistic) and Trodelvy 3L+ mTNBC (conservative).",
        impact="High",
        status="Active",
    ),
    Assumption(
        id="M003",
        category="Methodology",
        description="SoC integration is defined as the LATER of (a) guideline inclusion and (b) national reimbursement/access.",
        impact="High",
        status="Active",
    ),
    Assumption(
        id="M004",
        category="Methodology",
        description="For Germany, SoC integration uses EMA approval date (not G-BA) as access is available during free-pricing period under AMNOG.",
        impact="Medium",
        status="Active",
    ),
    Assumption(
        id="M005",
        category="Methodology",
        description="For US, SoC integration = max(NCCN guideline inclusion, commercial launch date). No HTA gate.",
        impact="Medium",
        status="Active",
    ),

    # ── Regulatory ──
    Assumption(
        id="R001",
        category="Regulatory",
        description="EMA centralized procedure assumed for all EU5 markets; no national divergence.",
        impact="Medium",
        status="Active",
    ),
    Assumption(
        id="R002",
        category="Regulatory",
        description="MHRA assumed to follow EMA via Great Britain reliance pathway, adding 0-2 months to EMA date.",
        impact="Low",
        status="Active",
    ),
    Assumption(
        id="R003",
        category="Regulatory",
        description="Health Canada assumed to run parallel review; typically 6-15 months post-FDA based on analogs.",
        impact="Medium",
        status="Active",
    ),
    Assumption(
        id="R004",
        category="Regulatory",
        description="Dato-DXd (TROPION-Breast02) PDUFA target Q2 2026 based on FDA Priority Review grant Feb 2026.",
        impact="High",
        status="Active",
        related_drug="Dato-DXd",
    ),
    Assumption(
        id="R005",
        category="Regulatory",
        description="Trodelvy 1L (ASCENT-03) FDA approval targeted H2 2026 based on Gilead Q4 2025 Earnings guidance for accelerated launch.",
        impact="High",
        status="Active",
        related_drug="Trodelvy",
    ),
    Assumption(
        id="R006",
        category="Regulatory",
        description="Trodelvy 1L (ASCENT-04 combo) FDA approval expected H2 2026, possibly 1-2 months after ASCENT-03 monotherapy.",
        impact="Medium",
        status="Active",
        related_drug="Trodelvy",
    ),
    Assumption(
        id="R007",
        category="Regulatory",
        description="Dato-DXd EU/China approval projected as early as Q3 2026 per Daiichi Q3 FY2025 Earnings guidance, based on regulatory submission accepted Dec 2025.",
        impact="High",
        status="Active",
        related_drug="Dato-DXd",
    ),

    # ── Trial / Data ──
    Assumption(
        id="T001",
        category="Trial",
        description="TROPION-Breast05 (Dato-DXd CPS>=10) PCD estimated Oct 2027, based on '~18 months out' as of Apr 2026.",
        impact="High",
        status="Active",
        related_drug="Dato-DXd",
        gap_flag=True,
    ),
    Assumption(
        id="T002",
        category="Trial",
        description="ASCENT-03 and ASCENT-04 primary completion dates estimated mid-2025; exact dates need verification on ClinicalTrials.gov.",
        impact="Medium",
        status="Active",
        related_drug="Trodelvy",
        gap_flag=True,
    ),

    # ── Guideline ──
    Assumption(
        id="G001",
        category="Guideline",
        description="NCCN already lists both Trodelvy and Dato-DXd for 1L mTNBC pre-approval (v1.2026 and v2.2026). NCCN guideline milestone is therefore BEFORE FDA approval — unusual but confirmed.",
        impact="High",
        status="Active",
    ),
    Assumption(
        id="G002",
        category="Guideline",
        description="ESMO guideline inclusion for 1L TNBC ADCs assumed to follow within 6-12 months of FDA approval, based on analog precedent.",
        impact="Medium",
        status="Active",
    ),
    Assumption(
        id="G003",
        category="Guideline",
        description="Trodelvy Category 1 vs Dato-DXd Category 2A reflects greater evidence maturity (inc. OS data in 2L), not lack of support for Dato-DXd.",
        impact="Medium",
        status="Active",
    ),

    # ── Reimbursement ──
    Assumption(
        id="H001",
        category="Reimbursement",
        description="NICE appraisal timelines assumed 12-28 months post-FDA based on analogs. CDF route possible for Dato-DXd given weaker evidence vs Trodelvy.",
        impact="High",
        status="Active",
    ),
    Assumption(
        id="H002",
        category="Reimbursement",
        description="G-BA AMNOG assessment assumed within 3-6 months of EMA approval; does not gate market access in Germany.",
        impact="Medium",
        status="Active",
    ),
    Assumption(
        id="H003",
        category="Reimbursement",
        description="HAS (France) transparency committee opinion assumed 8-17 months post-FDA; pricing negotiation adds further time.",
        impact="Medium",
        status="Active",
    ),
    Assumption(
        id="H004",
        category="Reimbursement",
        description="AIFA (Italy) reimbursement assumed 18-24 months post-FDA; typically slowest EU5 market.",
        impact="Medium",
        status="Active",
    ),
    Assumption(
        id="H005",
        category="Reimbursement",
        description="AEMPS/Spain reimbursement assumed 20-27 months post-FDA; national + regional pricing layers add variability.",
        impact="Medium",
        status="Active",
    ),
    Assumption(
        id="H006",
        category="Reimbursement",
        description="CADTH/pCODR (Canada) recommendation assumed 12-20 months post-FDA; provincial listing adds further time.",
        impact="Medium",
        status="Active",
    ),

    # ── Data Gaps ──
    Assumption(
        id="GAP001",
        category="Data Gap",
        description="HAS (France) exact decision dates for both analogs need primary research from HAS public database.",
        impact="Medium",
        status="Active",
        gap_flag=True,
    ),
    Assumption(
        id="GAP002",
        category="Data Gap",
        description="AIFA (Italy) exact GU publication dates for both analogs need primary research.",
        impact="Medium",
        status="Active",
        gap_flag=True,
    ),
    Assumption(
        id="GAP003",
        category="Data Gap",
        description="AEMPS (Spain) exact pricing/reimbursement dates for both analogs need primary research.",
        impact="Medium",
        status="Active",
        gap_flag=True,
    ),
    Assumption(
        id="GAP004",
        category="Data Gap",
        description="G-BA exact AMNOG decision dates for both analogs need verification against G-BA public records.",
        impact="Low",
        status="Active",
        gap_flag=True,
    ),
    Assumption(
        id="GAP005",
        category="Data Gap",
        description="ESMO guideline exact update dates for both analogs are approximate; need verification against ESMO publications.",
        impact="Low",
        status="Active",
        gap_flag=True,
    ),

    # ── Competitive / Strategic ──
    Assumption(
        id="S001",
        category="Strategic",
        description="Trodelvy's Category 1 preferred NCCN status and broader 1L population coverage (CPS<10 AND CPS>=10) gives it a competitive advantage over Dato-DXd at launch.",
        impact="High",
        status="Active",
    ),
    Assumption(
        id="S002",
        category="Strategic",
        description="Both ADCs have NCCN recommendations ahead of regulatory approval — unusual precedent that may accelerate SoC integration in US.",
        impact="High",
        status="Active",
    ),
]
