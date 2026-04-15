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
        description="TROPION-Breast05 (NCT06103864) registered PCD is Jul 28, 2027. Status: Recruiting. Study completion Sep 2030. Confirmed via ClinicalTrials.gov API.",
        impact="High",
        status="Resolved",
        related_drug="Dato-DXd",
        gap_flag=False,
    ),
    Assumption(
        id="T002",
        category="Trial",
        description="ASCENT-03 (NCT05382299) registered PCD Jul 2028; ASCENT-04 (NCT05382286) registered PCD Feb 2027. Both are final OS analysis dates — PFS data already presented. Note: original NCT numbers in data were swapped, now corrected. Confirmed via ClinicalTrials.gov API.",
        impact="Medium",
        status="Resolved",
        related_drug="Trodelvy",
        gap_flag=False,
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
        description="HAS (France) decision dates confirmed: Enhertu CT opinion 22 Feb 2023, Trodelvy CT opinion 6 Apr 2022. Sourced from has-sante.fr.",
        impact="Medium",
        status="Resolved",
        gap_flag=False,
    ),
    Assumption(
        id="GAP002",
        category="Data Gap",
        description="AIFA (Italy) dates confirmed: Enhertu GU n.153 on 3 Jul 2023 (~5 months post-EMA); Trodelvy GU n.185 on 9 Aug 2022 (~9 months post-EMA). Sourced from gazzettaufficiale.it and aifa.gov.it.",
        impact="Medium",
        status="Resolved",
        gap_flag=False,
    ),
    Assumption(
        id="GAP003",
        category="Data Gap",
        description="AEMPS (Spain) dates confirmed: Both Enhertu and Trodelvy approved by CIPM on same date, 28 Oct 2022. Sourced from Spanish Ministry of Health press release.",
        impact="Medium",
        status="Resolved",
        gap_flag=False,
    ),
    Assumption(
        id="GAP004",
        category="Data Gap",
        description="G-BA AMNOG dates confirmed: Enhertu Beschluss 2 Feb 2023 (procedure D-836), Trodelvy Beschluss 19 May 2022 (procedure D-750). Sourced from g-ba.de.",
        impact="Low",
        status="Resolved",
        gap_flag=False,
    ),
    Assumption(
        id="GAP005",
        category="Data Gap",
        description="ESMO guideline dates confirmed: Both Enhertu and Trodelvy included in ESMO mBC CPG published 19 Oct 2021 (Annals of Oncology). This predates Enhertu FDA full approval (Aug 2022) — the guideline referenced DESTINY-Breast03 data pre-approval.",
        impact="Low",
        status="Resolved",
        gap_flag=False,
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
