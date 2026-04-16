# CLAUDE.md — Agent Instructions

## Engagement Overview

- **Client code:** Corcept
- **CI question:** When will Trodelvy and Dato-DXd become standard of care (SoC) for 1L mTNBC across US, UK, France, Germany, Italy, Spain, and Canada — and what does this mean for Corcept's Phase 3 enrollment viability?
- **Deliverable type:** Timeline projection tool (Excel workbook, charts, assumptions log)
- **Consultancy:** Eradigm Consulting — Life Sciences Competitive Intelligence

---

## Working Rules

- **US English** throughout all documents, code, and agent communication.
- **London timezone (Europe/London)** for all timestamps.
- **Professional consulting register** for all client-facing output. Confident, precise, appropriately hedged where data is incomplete. Prefer "data as of [date]" over "we cannot be sure."
- **Citation standard:** Every factual claim must trace to a Tier 1 or Tier 2 source. See source hierarchy below.
- **Never fabricate.** If you are not certain of a fact, say so explicitly. Do not infer or extrapolate without flagging it. In life sciences CI, incorrect pipeline stages, wrong clinical trial phases, or misattributed drug mechanisms directly mislead client strategy.

---

## Source Hierarchy

| Tier | Source type | Examples | Use for |
|------|-------------|----------|--------|
| 1 | Regulatory filings | FDA/EMA submissions, NDA/BLA, EPAR | Approval status, label claims |
| 1 | Clinical trial registries | ClinicalTrials.gov, EudraCT | Trial status, endpoints |
| 1 | Company filings | 10-K, 10-Q, investor presentations | Pipeline, strategy |
| 1 | Peer-reviewed literature | PubMed, NEJM, Lancet | Mechanism, efficacy |
| 2 | Conference abstracts | ASCO, ASH, ESMO | Early data |
| 2 | Press releases | Company IR pages | Headline results |
| 3 | Secondary analysis | Analyst reports | Context, sizing |
| 4 | AI synthesis | Agent-generated | Drafting only — never cite as source |

**Never cite an AI-generated summary as a source.** Mark unverified agent-generated claims as `[UNVERIFIED]` or `[REQUIRES VERIFICATION]` in working documents.

---

## Key Constraints

- **Stay within the defined scope.** Assets: Trodelvy (ASCENT-03, ASCENT-04), Dato-DXd (TROPION-Breast02, TROPION-Breast05). Analogs: Enhertu 2L+ HER2+ mBC, Trodelvy 3L+ mTNBC. Do not add assets or analogs not listed unless explicitly asked.
- **Markets:** US, UK, France, Germany, Italy, Spain, Canada. Do not expand without instruction.
- **Date verification:** All pipeline stages, regulatory decisions, and HTA dates must be verified against a primary source before inclusion in client deliverables. Note the retrieval date for time-sensitive data.
- **Confidence levels:** Apply to every analytical judgment — Known / High / Moderate / Low / Gap.
- **Do not commit client data** to public or shared repositories.

---

## Analytical Framework

- **Analog-based lag projection:** FDA approval = T=0. Derive per-milestone lags from two analogs (Enhertu optimistic, Trodelvy 3L+ conservative). Apply to target drug FDA anchor dates.
- **Three scenarios:** Optimistic (min lag), Base (average), Conservative (max lag).
- **SoC integration:** Defined as max(guideline inclusion, national reimbursement/access). Germany exception: access at EMA approval (free-pricing period under AMNOG). US exception: no HTA gate, SoC = max(NCCN, commercial launch).

---

## Project Structure

```
Trodelvy-and-Dato-DXd-AdHoc/
├── CLAUDE.md              (this file — agent instructions)
├── README.md              (project overview)
├── Ways of Working_ US.md (Eradigm CI working practices)
├── scripts/
│   └── generate_all.py    (main orchestrator)
├── src/
│   ├── models.py          (data model: Milestone, DrugProgram, etc.)
│   ├── data/
│   │   ├── analog_data.py        (hard-coded analog milestones)
│   │   ├── forward_looking_data.py (target asset anchors)
│   │   └── assumptions.py        (central assumptions registry)
│   ├── projection/
│   │   ├── lag_calculator.py     (analog lag derivation)
│   │   ├── scenario_engine.py    (3-scenario projection)
│   │   └── soc_integration.py    (SoC date computation)
│   └── output/
│       ├── excel_writer.py       (openpyxl workbook generation)
│       ├── chart_generator.py    (matplotlib swimlane/SoC charts)
│       └── assumptions_renderer.py (markdown assumptions doc)
├── output/                (generated files)
│   ├── drug_approval_timelines.xlsx
│   ├── swimlane_timeline.png
│   └── soc_comparison.png
└── docs/
    └── assumptions_log.md
```

Run: `python scripts/generate_all.py`

---

## Known Issues and Agent Corrections

1. **Health Canada dates must be verified against the Drug Product Database (DPD).** The DPD requires interactive search and does not have stable direct URLs. Previous agent session used incorrect dates (Trodelvy HC was listed as Jul 2022, corrected to Sep 2021; Enhertu HC was listed as Feb 2023, corrected to ~Jun 2022). Always cross-reference HC dates with the Summary Basis of Decision portal.
2. **MHRA dates require interactive lookup.** The MHRA products database (products.mhra.gov.uk) does not have stable deep links. MHRA dates in this project are estimated from EMA reliance pathway precedent and should be flagged as `[REQUIRES VERIFICATION]`.
3. **Excel number formatting:** When writing numeric values to openpyxl cells, always use `float()` explicitly. Writing `None` (not empty string `""`) for blank numeric cells. Writing `""` to a numeric column causes Excel's "number stored as text" green triangle warning.
4. **ESMO CPG date (PubMed 34678411) predates both analog FDA approvals.** This is correct — the October 2021 guideline referenced pre-approval trial data. Do not assume guidelines always post-date approval.
5. **NCT number confusion:** ASCENT-03 = NCT05382299, ASCENT-04 = NCT05382286, TROPION-Breast02 = NCT05374512, TROPION-Breast05 = NCT06103864. These were previously swapped — always verify against ClinicalTrials.gov.
6. **Registered PCDs vs. data readouts:** ClinicalTrials.gov registered PCDs for ASCENT-03/04 are for final OS analysis, not the PFS readouts that support regulatory submission. Do not confuse them.
7. **Do not generate generic URLs.** If you cannot verify a URL points to the specific document cited, omit it and state the source description only. Generic search page URLs (e.g., MHRA search, Health Canada DPD search) are worse than no URL.
