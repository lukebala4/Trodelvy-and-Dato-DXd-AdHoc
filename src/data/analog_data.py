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
            source_url="https://clinicaltrials.gov/study/NCT03529110",
        ),
        Milestone(
            MilestoneType.TRIAL_READOUT, Market.US,
            date(2021, 9, 19), Confidence.KNOWN,
            "ESMO 2021 presentation",
            "First presentation at ESMO Congress 2021",
            source_url="https://www.thelancet.com/journals/lanonc/article/PIIS1470-2045(22)00097-3/fulltext",
        ),

        # ── Regulatory Approvals ──
        Milestone(
            MilestoneType.FDA_APPROVAL, Market.US,
            date(2022, 8, 5), Confidence.KNOWN,
            "FDA approval letter",
            "Full approval for 2L+ HER2+ mBC based on DESTINY-Breast03",
            source_url="https://www.fda.gov/drugs/resources-information-approved-drugs/fda-approves-fam-trastuzumab-deruxtecan-nxki-unresectable-or-metastatic-her2-positive-breast-cancer",
        ),
        Milestone(
            MilestoneType.EMA_APPROVAL, Market.FR,
            date(2023, 1, 24), Confidence.KNOWN,
            "EC decision — EMA EPAR",
            "EMA centralized procedure; EC marketing authorization",
            source_url="https://www.ema.europa.eu/en/medicines/human/EPAR/enhertu",
        ),
        Milestone(
            MilestoneType.EMA_APPROVAL, Market.DE,
            date(2023, 1, 24), Confidence.KNOWN,
            "EC decision — EMA EPAR",
            "Same EMA approval applies to all EU5",
            source_url="https://www.ema.europa.eu/en/medicines/human/EPAR/enhertu",
        ),
        Milestone(
            MilestoneType.EMA_APPROVAL, Market.IT,
            date(2023, 1, 24), Confidence.KNOWN,
            "EC decision — EMA EPAR",
            source_url="https://www.ema.europa.eu/en/medicines/human/EPAR/enhertu",
        ),
        Milestone(
            MilestoneType.EMA_APPROVAL, Market.ES,
            date(2023, 1, 24), Confidence.KNOWN,
            "EC decision — EMA EPAR",
            source_url="https://www.ema.europa.eu/en/medicines/human/EPAR/enhertu",
        ),
        Milestone(
            MilestoneType.MHRA_APPROVAL, Market.UK,
            date(2023, 1, 24), Confidence.KNOWN,
            "MHRA GBR reliance procedure",
            "MHRA followed EMA timeline via reliance pathway",
            source_url="https://products.mhra.gov.uk/search/?search=trastuzumab+deruxtecan",
        ),
        Milestone(
            MilestoneType.HEALTH_CANADA_APPROVAL, Market.CA,
            date(2023, 2, 17), Confidence.KNOWN,
            "Health Canada NOC",
            source_url="https://health-products.canada.ca/dpd-bdpp/dispatch-repartition?lang=eng&type=BP&term=trastuzumab+deruxtecan",
        ),

        # ── Guidelines ──
        Milestone(
            MilestoneType.NCCN_GUIDELINE, Market.US,
            date(2022, 9, 1), Confidence.HIGH,
            "NCCN Breast Cancer v5.2022",
            "Category 1 preferred within ~1 month of FDA approval",
            source_url="https://www.nccn.org/guidelines/guidelines-detail?category=1&id=1419",
        ),
        Milestone(
            MilestoneType.NCCN_GUIDELINE, Market.CA,
            date(2022, 9, 1), Confidence.HIGH,
            "NCCN Breast Cancer v5.2022",
            "NCCN also referenced in Canadian practice",
            source_url="https://www.nccn.org/guidelines/guidelines-detail?category=1&id=1419",
        ),
        Milestone(
            MilestoneType.ESMO_GUIDELINE, Market.UK,
            date(2023, 9, 15), Confidence.MODERATE,
            "ESMO mBC Living Guideline 2023",
            "Updated recommendation following full publication",
            source_url="https://www.esmo.org/guidelines/breast-cancer",
        ),
        Milestone(
            MilestoneType.ESMO_GUIDELINE, Market.FR,
            date(2023, 9, 15), Confidence.MODERATE,
            "ESMO mBC Living Guideline 2023",
            source_url="https://www.esmo.org/guidelines/breast-cancer",
        ),
        Milestone(
            MilestoneType.ESMO_GUIDELINE, Market.DE,
            date(2023, 9, 15), Confidence.MODERATE,
            "ESMO mBC Living Guideline 2023",
            source_url="https://www.esmo.org/guidelines/breast-cancer",
        ),
        Milestone(
            MilestoneType.ESMO_GUIDELINE, Market.IT,
            date(2023, 9, 15), Confidence.MODERATE,
            "ESMO mBC Living Guideline 2023",
            source_url="https://www.esmo.org/guidelines/breast-cancer",
        ),
        Milestone(
            MilestoneType.ESMO_GUIDELINE, Market.ES,
            date(2023, 9, 15), Confidence.MODERATE,
            "ESMO mBC Living Guideline 2023",
            source_url="https://www.esmo.org/guidelines/breast-cancer",
        ),

        # ── HTA / Reimbursement ──
        Milestone(
            MilestoneType.NICE_DECISION, Market.UK,
            date(2023, 10, 25), Confidence.KNOWN,
            "NICE TA942",
            "Recommended for routine commissioning",
            source_url="https://www.nice.org.uk/guidance/ta942",
        ),
        Milestone(
            MilestoneType.GBA_DECISION, Market.DE,
            date(2023, 2, 2), Confidence.KNOWN,
            "G-BA Beschluss — procedure 2022-08-01-D-836",
            "Considerable additional benefit. Decision 9 days after EMA approval.",
            source_url="https://www.g-ba.de/bewertungsverfahren/nutzenbewertung/864/",
        ),
        Milestone(
            MilestoneType.HAS_DECISION, Market.FR,
            date(2023, 2, 22), Confidence.KNOWN,
            "HAS CT opinion — ENHERTU_22022023_AVIS_CT19944",
            "SMR: Important; ASMR III (moderate improvement). Published online 30 Mar 2023.",
            source_url="https://www.has-sante.fr/jcms/p_3424347/fr/enhertu-trastuzumab-deruxtecan-cancer-du-sein-her2",
        ),
        Milestone(
            MilestoneType.AIFA_DECISION, Market.IT,
            date(2024, 3, 1), Confidence.LOW,
            "Estimated from typical AIFA timeline",
            "GAP: Exact AIFA Gazzetta Ufficiale publication date needs research",
            source_url="https://www.aifa.gov.it/en/liste-farmaci-a-z",
        ),
        Milestone(
            MilestoneType.AEMPS_DECISION, Market.ES,
            date(2024, 4, 1), Confidence.LOW,
            "Estimated from typical AEMPS/IPT timeline",
            "GAP: Exact Spanish pricing/reimbursement date needs research",
            source_url="https://www.aemps.gob.es/",
        ),
        Milestone(
            MilestoneType.CADTH_DECISION, Market.CA,
            date(2023, 6, 29), Confidence.HIGH,
            "CADTH pCODR recommendation",
            "Recommended for reimbursement with clinical criteria",
            source_url="https://www.cadth.ca/trastuzumab-deruxtecan-18",
        ),

        # ── Commercial Launch (US) ──
        Milestone(
            MilestoneType.COMMERCIAL_LAUNCH, Market.US,
            date(2022, 8, 15), Confidence.HIGH,
            "Daiichi Sankyo press release",
            "US commercial launch within days of FDA approval",
            source_url="https://www.daiichisankyo.com/media/press-releases/",
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
            "ESMO 2020 — NEJM publication",
            "Primary results presented at ESMO Virtual 2020",
            source_url="https://www.nejm.org/doi/full/10.1056/NEJMoa2028485",
        ),

        # ── Regulatory Approvals ──
        Milestone(
            MilestoneType.FDA_APPROVAL, Market.US,
            date(2021, 4, 7), Confidence.KNOWN,
            "FDA approval letter",
            "Regular approval for 3L+ mTNBC (accelerated approval Apr 2020 converted)",
            source_url="https://www.fda.gov/drugs/resources-information-approved-drugs/fda-grants-regular-approval-sacituzumab-govitecan-triple-negative-breast-cancer",
        ),
        Milestone(
            MilestoneType.EMA_APPROVAL, Market.FR,
            date(2021, 11, 10), Confidence.KNOWN,
            "EC decision — EMA EPAR",
            "EMA centralized procedure; ~7 months post-FDA",
            source_url="https://www.ema.europa.eu/en/medicines/human/EPAR/trodelvy",
        ),
        Milestone(
            MilestoneType.EMA_APPROVAL, Market.DE,
            date(2021, 11, 10), Confidence.KNOWN,
            "EC decision — EMA EPAR",
            source_url="https://www.ema.europa.eu/en/medicines/human/EPAR/trodelvy",
        ),
        Milestone(
            MilestoneType.EMA_APPROVAL, Market.IT,
            date(2021, 11, 10), Confidence.KNOWN,
            "EC decision — EMA EPAR",
            source_url="https://www.ema.europa.eu/en/medicines/human/EPAR/trodelvy",
        ),
        Milestone(
            MilestoneType.EMA_APPROVAL, Market.ES,
            date(2021, 11, 10), Confidence.KNOWN,
            "EC decision — EMA EPAR",
            source_url="https://www.ema.europa.eu/en/medicines/human/EPAR/trodelvy",
        ),
        Milestone(
            MilestoneType.MHRA_APPROVAL, Market.UK,
            date(2021, 12, 15), Confidence.HIGH,
            "MHRA approval",
            "MHRA followed shortly after EMA; approximate date",
            source_url="https://products.mhra.gov.uk/search/?search=sacituzumab+govitecan",
        ),
        Milestone(
            MilestoneType.HEALTH_CANADA_APPROVAL, Market.CA,
            date(2022, 7, 18), Confidence.KNOWN,
            "Health Canada NOC",
            "~15 months post-FDA",
            source_url="https://health-products.canada.ca/dpd-bdpp/dispatch-repartition?lang=eng&type=BP&term=sacituzumab+govitecan",
        ),

        # ── Guidelines ──
        Milestone(
            MilestoneType.NCCN_GUIDELINE, Market.US,
            date(2021, 5, 1), Confidence.HIGH,
            "NCCN Breast Cancer v4.2021",
            "Added within one update cycle of full approval",
            source_url="https://www.nccn.org/guidelines/guidelines-detail?category=1&id=1419",
        ),
        Milestone(
            MilestoneType.NCCN_GUIDELINE, Market.CA,
            date(2021, 5, 1), Confidence.HIGH,
            "NCCN Breast Cancer v4.2021",
            source_url="https://www.nccn.org/guidelines/guidelines-detail?category=1&id=1419",
        ),
        Milestone(
            MilestoneType.ESMO_GUIDELINE, Market.UK,
            date(2022, 3, 1), Confidence.MODERATE,
            "ESMO mBC Living Guideline update",
            "Approximate timing of ESMO guideline inclusion",
            source_url="https://www.esmo.org/guidelines/breast-cancer",
        ),
        Milestone(
            MilestoneType.ESMO_GUIDELINE, Market.FR,
            date(2022, 3, 1), Confidence.MODERATE,
            "ESMO mBC Living Guideline update",
            source_url="https://www.esmo.org/guidelines/breast-cancer",
        ),
        Milestone(
            MilestoneType.ESMO_GUIDELINE, Market.DE,
            date(2022, 3, 1), Confidence.MODERATE,
            "ESMO mBC Living Guideline update",
            source_url="https://www.esmo.org/guidelines/breast-cancer",
        ),
        Milestone(
            MilestoneType.ESMO_GUIDELINE, Market.IT,
            date(2022, 3, 1), Confidence.MODERATE,
            "ESMO mBC Living Guideline update",
            source_url="https://www.esmo.org/guidelines/breast-cancer",
        ),
        Milestone(
            MilestoneType.ESMO_GUIDELINE, Market.ES,
            date(2022, 3, 1), Confidence.MODERATE,
            "ESMO mBC Living Guideline update",
            source_url="https://www.esmo.org/guidelines/breast-cancer",
        ),

        # ── HTA / Reimbursement ──
        Milestone(
            MilestoneType.NICE_DECISION, Market.UK,
            date(2023, 7, 12), Confidence.KNOWN,
            "NICE TA900",
            "Recommended via Cancer Drugs Fund; ~27 months post-FDA",
            source_url="https://www.nice.org.uk/guidance/ta900",
        ),
        Milestone(
            MilestoneType.GBA_DECISION, Market.DE,
            date(2022, 5, 19), Confidence.KNOWN,
            "G-BA Beschluss — procedure 2021-12-01-D-750",
            "~6 months post-EMA approval.",
            source_url="https://www.g-ba.de/bewertungsverfahren/nutzenbewertung/762/",
        ),
        Milestone(
            MilestoneType.HAS_DECISION, Market.FR,
            date(2022, 4, 6), Confidence.KNOWN,
            "HAS CT opinion — TRODELVY_06042022_AVIS_CT19684",
            "SMR: Important; ASMR III (moderate improvement). Published online 2 Jun 2022.",
            source_url="https://www.has-sante.fr/jcms/p_3341351/fr/trodelvy-sacituzumab-govitecan-cancer-du-sein-triple-negatif",
        ),
        Milestone(
            MilestoneType.AIFA_DECISION, Market.IT,
            date(2023, 3, 1), Confidence.LOW,
            "Estimated from typical AIFA timeline",
            "GAP: Exact AIFA GU publication date needs research",
            source_url="https://www.aifa.gov.it/en/liste-farmaci-a-z",
        ),
        Milestone(
            MilestoneType.AEMPS_DECISION, Market.ES,
            date(2023, 7, 1), Confidence.LOW,
            "Estimated from typical AEMPS timeline",
            "GAP: Exact Spanish pricing decision date needs research",
            source_url="https://www.aemps.gob.es/",
        ),
        Milestone(
            MilestoneType.CADTH_DECISION, Market.CA,
            date(2022, 10, 1), Confidence.MODERATE,
            "CADTH pCODR recommendation",
            "Approximate date; ~18 months post-FDA",
            source_url="https://www.cadth.ca/sacituzumab-govitecan",
        ),

        # ── Commercial Launch (US) ──
        Milestone(
            MilestoneType.COMMERCIAL_LAUNCH, Market.US,
            date(2021, 4, 15), Confidence.HIGH,
            "Gilead press release",
            "US launch shortly after FDA approval",
            source_url="https://www.gilead.com/news-and-press",
        ),
    ]

    program.milestones = milestones
    return program
