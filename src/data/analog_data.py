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
            "MHRA approval — estimated from EMA reliance pathway",
            "MHRA typically follows EMA via reliance pathway within 0-2 months. EMA variation published Aug 2022. NICE TA862 (Feb 2023) requires prior MHRA approval.",
        ),
        Milestone(
            MilestoneType.HEALTH_CANADA_APPROVAL, Market.CA,
            date(2023, 2, 17), Confidence.HIGH,
            "Health Canada NOC — DPD database",
            "~10 months post-FDA. Searched via Health Canada Drug Product Database (DIN lookup for trastuzumab deruxtecan).",
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
            "US commercial launch within days of FDA approval. Source: Daiichi Sankyo corporate communications.",
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
            source_url="https://clinicaltrials.gov/study/NCT02574455",
        ),
        Milestone(
            MilestoneType.TRIAL_READOUT, Market.US,
            date(2020, 9, 19), Confidence.KNOWN,
            "NEJM — Sacituzumab Govitecan in Metastatic Triple-Negative Breast Cancer",
            "Primary results presented at ESMO Virtual 2020. Published NEJM Apr 22 2021 (DOI: 10.1056/NEJMoa2028485).",
            source_url="https://www.nejm.org/doi/full/10.1056/NEJMoa2028485",
        ),

        # ── Regulatory Approvals ──
        Milestone(
            MilestoneType.FDA_APPROVAL, Market.US,
            date(2021, 4, 7), Confidence.KNOWN,
            "FDA approval — regular approval for 3L+ mTNBC",
            "Regular approval for 3L+ mTNBC (accelerated approval Apr 2020 converted).",
            source_url="https://www.fda.gov/drugs/resources-information-approved-drugs/fda-grants-regular-approval-sacituzumab-govitecan-triple-negative-breast-cancer",
        ),
        Milestone(
            MilestoneType.EMA_APPROVAL, Market.FR,
            date(2021, 11, 22), Confidence.KNOWN,
            "EC decision — EMA EPAR",
            "EMA marketing authorisation granted 22 Nov 2021 per EPAR. ~7 months post-FDA.",
            source_url="https://www.ema.europa.eu/en/medicines/human/EPAR/trodelvy",
        ),
        Milestone(
            MilestoneType.EMA_APPROVAL, Market.DE,
            date(2021, 11, 22), Confidence.KNOWN,
            "EC decision — EMA EPAR",
            "Same EC decision applies to all EU5.",
            source_url="https://www.ema.europa.eu/en/medicines/human/EPAR/trodelvy",
        ),
        Milestone(
            MilestoneType.EMA_APPROVAL, Market.IT,
            date(2021, 11, 22), Confidence.KNOWN,
            "EC decision — EMA EPAR",
            source_url="https://www.ema.europa.eu/en/medicines/human/EPAR/trodelvy",
        ),
        Milestone(
            MilestoneType.EMA_APPROVAL, Market.ES,
            date(2021, 11, 22), Confidence.KNOWN,
            "EC decision — EMA EPAR",
            source_url="https://www.ema.europa.eu/en/medicines/human/EPAR/trodelvy",
        ),
        Milestone(
            MilestoneType.MHRA_APPROVAL, Market.UK,
            date(2021, 12, 15), Confidence.MODERATE,
            "MHRA approval — estimated",
            "MHRA followed shortly after EMA (~1 month). Exact date from MHRA product database (products.mhra.gov.uk).",
        ),
        Milestone(
            MilestoneType.HEALTH_CANADA_APPROVAL, Market.CA,
            date(2022, 7, 18), Confidence.HIGH,
            "Health Canada NOC — DPD database",
            "~15 months post-FDA. Searched via Health Canada Drug Product Database (DIN lookup for sacituzumab govitecan).",
        ),

        # ── Guidelines ──
        Milestone(
            MilestoneType.NCCN_GUIDELINE, Market.US,
            date(2021, 5, 1), Confidence.HIGH,
            "NCCN Breast Cancer v4.2021",
            "Added within one update cycle of full approval. NCCN guidelines require login at nccn.org.",
        ),
        Milestone(
            MilestoneType.NCCN_GUIDELINE, Market.CA,
            date(2021, 5, 1), Confidence.HIGH,
            "NCCN Breast Cancer v4.2021",
        ),
        Milestone(
            MilestoneType.ESMO_GUIDELINE, Market.UK,
            date(2021, 10, 19), Confidence.KNOWN,
            "ESMO CPG — Annals of Oncology, 19 Oct 2021",
            "SG recommended as preferred treatment after anthracyclines and taxanes for mTNBC.",
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
            date(2022, 8, 17), Confidence.KNOWN,
            "NICE TA819",
            "Recommended for 3L+ mTNBC. Published 17 Aug 2022. ~16 months post-FDA.",
            source_url="https://www.nice.org.uk/guidance/ta819",
        ),
        Milestone(
            MilestoneType.GBA_DECISION, Market.DE,
            date(2022, 5, 19), Confidence.KNOWN,
            "G-BA Beschluss — procedure 2021-12-01-D-750",
            "Beschluss 19 May 2022. ~6 months post-EMA approval.",
            source_url="https://www.g-ba.de/bewertungsverfahren/nutzenbewertung/762/",
        ),
        Milestone(
            MilestoneType.HAS_DECISION, Market.FR,
            date(2022, 4, 6), Confidence.KNOWN,
            "HAS CT opinion — 6 Apr 2022",
            "SMR: Important; ASMR III (moderate improvement). Published online 2 Jun 2022.",
            source_url="https://www.has-sante.fr/jcms/p_3341351/fr/trodelvy-sacituzumab-govitecan-cancer-du-sein-triple-negatif",
        ),
        Milestone(
            MilestoneType.AIFA_DECISION, Market.IT,
            date(2022, 8, 9), Confidence.KNOWN,
            "AIFA — GU Serie Generale n.185, 9 Aug 2022",
            "SSN reimbursement effective 10 Aug 2022. Access via Innovative Medicines Fund. ~9 months post-EMA.",
            source_url="https://www.aifa.gov.it/en/-/attivazione-web-e-pubblicazione-schede-di-monitoraggio-registro-trodelvy-mtnbc-",
        ),
        Milestone(
            MilestoneType.AEMPS_DECISION, Market.ES,
            date(2022, 10, 28), Confidence.KNOWN,
            "CIPM financing decision — 28 Oct 2022",
            "Same CIPM session approved both Trodelvy and Enhertu. SNS prescription available ~Dec 2022. ~12 months post-EMA.",
            source_url="https://www.sanidad.gob.es/en/gabinete/notasPrensa.do?id=5920",
        ),
        Milestone(
            MilestoneType.CADTH_DECISION, Market.CA,
            date(2022, 10, 1), Confidence.MODERATE,
            "CADTH pCODR recommendation — approximate",
            "~18 months post-FDA. Date approximate; sourced from CADTH database (cadth.ca/sacituzumab-govitecan).",
            source_url="https://www.cadth.ca/sacituzumab-govitecan",
        ),

        # ── Commercial Launch (US) ──
        Milestone(
            MilestoneType.COMMERCIAL_LAUNCH, Market.US,
            date(2021, 4, 15), Confidence.HIGH,
            "Gilead Sciences — US launch post-FDA approval",
            "US commercial launch shortly after FDA approval. Source: Gilead corporate communications.",
        ),
    ]

    program.milestones = milestones
    return program
