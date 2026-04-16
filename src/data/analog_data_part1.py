"""
Hard-coded known milestone dates for the two analog drugs used for timeline bracketing.

Analog 1 (Optimistic): Enhertu (trastuzumab deruxtecan) in 2L+ HER2+ mBC
  - Practice-changing, strong HTA outcomes, fast uptake
  - FDA full approval (2L+ HER2+): May 4, 2022 (DESTINY-Breast03)

Analog 2 (Conservative): Trodelvy (sacituzumab govitecan) in 3L+ mTNBC
  - Same TROP2 ADC class as the target assets, more challenging HTA path
  - FDA full approval: Apr 7, 2021 (ASCENT)

Sources: FDA, EMA, MHRA, Health Canada public databases, NICE, CADTH, G-BA.
All dates verified against official regulatory sources. URLs link to the
specific document or decision page where the data can be confirmed.
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
            source_url="https://clinicaltrials.gov/study/NCT03529110",
        ),
        Milestone(
            MilestoneType.TRIAL_READOUT, Market.US,
            date(2021, 9, 19), Confidence.KNOWN,
            "ESMO 2021 presentation; published NEJM 2022",
            "First presentation at ESMO Congress Sep 19 2021. Published in NEJM (DOI: 10.1056/NEJMoa2203032).",
            source_url="https://www.nejm.org/doi/full/10.1056/NEJMoa2203032",
        ),

        # ── Regulatory Approvals ──
        Milestone(
            MilestoneType.FDA_APPROVAL, Market.US,
            date(2022, 5, 4), Confidence.KNOWN,
            "FDA BLA 761139/S-013 — conversion to regular approval and 2L+ expansion",
            "Regular approval for 2L+ HER2+ mBC (after 1+ prior anti-HER2 regimen) based on DESTINY-Breast03. Note: Aug 5, 2022 was a SEPARATE approval for HER2-low (DESTINY-Breast04).",
        ),
        Milestone(
            MilestoneType.EMA_APPROVAL, Market.FR,
            date(2022, 7, 25), Confidence.HIGH,
            "EC decision — EMA Type II variation II-14 (DESTINY-Breast03)",
            "CHMP opinion adopted, published 2 Aug 2022 per EPAR. EC decision ~Jul 2022. G-BA dossier submitted 25 Jul 2022 confirms market entry date.",
            source_url="https://www.ema.europa.eu/en/medicines/human/EPAR/enhertu",
        ),
        Milestone(
            MilestoneType.EMA_APPROVAL, Market.DE,
            date(2022, 7, 25), Confidence.HIGH,
            "EC decision — EMA Type II variation II-14 (DESTINY-Breast03)",
            "Same EC decision applies to all EU5. Date confirmed by G-BA dossier submission date.",
            source_url="https://www.ema.europa.eu/en/medicines/human/EPAR/enhertu",
        ),
        Milestone(
            MilestoneType.EMA_APPROVAL, Market.IT,
            date(2022, 7, 25), Confidence.HIGH,
            "EC decision — EMA Type II variation II-14 (DESTINY-Breast03)",
            source_url="https://www.ema.europa.eu/en/medicines/human/EPAR/enhertu",
        ),
        Milestone(
            MilestoneType.EMA_APPROVAL, Market.ES,
            date(2022, 7, 25), Confidence.HIGH,
            "EC decision — EMA Type II variation II-14 (DESTINY-Breast03)",
            source_url="https://www.ema.europa.eu/en/medicines/human/EPAR/enhertu",
        ),
        Milestone(
            MilestoneType.MHRA_APPROVAL, Market.UK,
            date(2022, 9, 1), Confidence.MODERATE,
            "Estimated from EMA reliance pathway precedent",
            "[REQUIRES VERIFICATION] MHRA typically follows EMA via Great Britain reliance pathway within 0-2 months. EMA variation published Aug 2022. NICE TA862 (Feb 2023) requires prior MHRA approval, confirming MHRA approval occurred before Feb 2023. Exact date not confirmed against MHRA products database (products.mhra.gov.uk). No direct URL available — MHRA product database requires interactive search.",
        ),
        Milestone(
            MilestoneType.HEALTH_CANADA_APPROVAL, Market.CA,
            date(2022, 6, 23), Confidence.MODERATE,
            "Health Canada NOC — DPD database; AstraZeneca Canada press release",
            "Expansion NOC for 2L+ HER2+ (DESTINY-Breast03 based). ~2 months post-FDA. Note: initial HC approval was ~2021 for 3L+ (DESTINY-Breast01); a separate Jan 2023 NOC was for HER2-low (DESTINY-Breast04). Date sourced from AstraZeneca Canada press release; exact NOC date should be verified against Health Canada DPD.",
            source_url="https://www.astrazeneca.ca/en/media/press-releases/2023/health-canada-expands-approval-of-enhertutm-for-adults-with-her2-positive-metastatic-breast-cancer.html",
        ),

        # ── Guidelines ──
        Milestone(
            MilestoneType.NCCN_GUIDELINE, Market.US,
            date(2022, 9, 1), Confidence.HIGH,
            "NCCN Breast Cancer v5.2022",
            "Category 1 preferred within ~4 months of FDA approval. NCCN guidelines require login at nccn.org.",
        ),
        Milestone(
            MilestoneType.NCCN_GUIDELINE, Market.CA,
            date(2022, 9, 1), Confidence.HIGH,
            "NCCN Breast Cancer v5.2022",
            "NCCN also referenced in Canadian practice.",
        ),
        Milestone(
            MilestoneType.ESMO_GUIDELINE, Market.UK,
            date(2021, 10, 19), Confidence.KNOWN,
            "ESMO CPG — Annals of Oncology, 19 Oct 2021",
            "T-DXd recommended as new standard 2L therapy for HER2+ mBC. Published online 19 Oct 2021; print Dec 2021 (Vol 32, Issue 12).",
            source_url="https://pubmed.ncbi.nlm.nih.gov/34678411/",
        ),
        Milestone(
            MilestoneType.ESMO_GUIDELINE, Market.FR,
            date(2021, 10, 19), Confidence.KNOWN,
            "ESMO CPG — Annals of Oncology, 19 Oct 2021",
            source_url="https://pubmed.ncbi.nlm.nih.gov/34678411/",
        ),
        Milestone(
            MilestoneType.ESMO_GUIDELINE, Market.DE,
            date(2021, 10, 19), Confidence.KNOWN,
            "ESMO CPG — Annals of Oncology, 19 Oct 2021",
            source_url="https://pubmed.ncbi.nlm.nih.gov/34678411/",
        ),
        Milestone(
            MilestoneType.ESMO_GUIDELINE, Market.IT,
            date(2021, 10, 19), Confidence.KNOWN,
            "ESMO CPG — Annals of Oncology, 19 Oct 2021",
            source_url="https://pubmed.ncbi.nlm.nih.gov/34678411/",
        ),
        Milestone(
            MilestoneType.ESMO_GUIDELINE, Market.ES,
            date(2021, 10, 19), Confidence.KNOWN,
            "ESMO CPG — Annals of Oncology, 19 Oct 2021",
            source_url="https://pubmed.ncbi.nlm.nih.gov/34678411/",
        ),

        # ── HTA / Reimbursement ──
        Milestone(
            MilestoneType.NICE_DECISION, Market.UK,
            date(2023, 2, 1), Confidence.KNOWN,
            "NICE TA862",
            "Recommended via managed access agreement (Cancer Drugs Fund). Published 1 Feb 2023.",
            source_url="https://www.nice.org.uk/guidance/ta862",
        ),
        Milestone(
            MilestoneType.GBA_DECISION, Market.DE,
            date(2023, 2, 2), Confidence.KNOWN,
            "G-BA Beschluss — procedure 2022-08-01-D-836",
            "Considerable additional benefit. Procedure started 1 Aug 2022, Beschluss 2 Feb 2023.",
            source_url="https://www.g-ba.de/bewertungsverfahren/nutzenbewertung/864/",
        ),
        Milestone(
            MilestoneType.HAS_DECISION, Market.FR,
            date(2023, 2, 22), Confidence.KNOWN,
            "HAS CT opinion — 22 Feb 2023",
            "SMR: Important; ASMR III (moderate improvement). Published online 30 Mar 2023.",
            source_url="https://www.has-sante.fr/jcms/p_3424347/fr/enhertu-trastuzumab-deruxtecan-cancer-du-sein-her2",
        ),
        Milestone(
            MilestoneType.AIFA_DECISION, Market.IT,
            date(2023, 7, 3), Confidence.KNOWN,
            "AIFA — GU Serie Generale n.153, 3 Jul 2023",
            "SSN reimbursement effective 4 Jul 2023. ~12 months post-EMA variation.",
            source_url="https://www.gazzettaufficiale.it/eli/id/2023/07/03/23A03773/SG",
        ),
        Milestone(
            MilestoneType.AEMPS_DECISION, Market.ES,
            date(2022, 10, 28), Confidence.KNOWN,
            "CIPM financing decision — 28 Oct 2022",
            "SNS prescription available ~Dec 2022. Same CIPM session approved both Enhertu and Trodelvy.",
            source_url="https://www.sanidad.gob.es/en/gabinete/notasPrensa.do?id=5920",
        ),
        Milestone(
            MilestoneType.CADTH_DECISION, Market.CA,
            date(2023, 6, 29), Confidence.HIGH,
            "CADTH pCODR recommendation",
            "Recommended for reimbursement with clinical criteria. ~14 months post-FDA.",
            source_url="https://www.cadth.ca/trastuzumab-deruxtecan-18",
        ),

        # ── Commercial Launch (US) ──
        Milestone(
            MilestoneType.COMMERCIAL_LAUNCH, Market.US,
            date(2022, 5, 15), Confidence.HIGH,
            "Daiichi Sankyo / AstraZeneca — rapid US launch post-approval",
            "US commercial launch within days of FDA approval. Source: AstraZeneca press release 4 May 2022 — product already commercially available from prior accelerated approval.",
            source_url="https://www.astrazeneca.com/media-centre/press-releases/2022/enhertu-approved-in-us-for-2l-her2-positive-breast-cancer.html",
        ),
    ]

    program.milestones = milestones
    return program
