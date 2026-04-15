# Trodelvy & Dato-DXd — 1L mTNBC Approval Timeline Projections

Forward-looking timeline hypotheses for when **Trodelvy** (sacituzumab govitecan) and **Dato-DXd** (datopotamab deruxtecan / Datroway) are expected to be approved, reimbursed, and integrated into standard of care (SoC) for **first-line metastatic triple-negative breast cancer (1L mTNBC)** across seven geographies.

Built to inform **Corcept's Phase 3 inclusion criteria and trial start timing** by identifying when and where these TROP2 ADCs will become SoC, which determines viable enrollment geographies.

---

## Markets Covered

| Market | Regulatory Body | HTA / Reimbursement | Guideline Reference |
|--------|----------------|--------------------|--------------------|
| US | FDA | N/A (commercial) | NCCN |
| UK | MHRA | NICE | ESMO |
| France | EMA | HAS (Transparency Committee) | ESMO |
| Germany | EMA | G-BA (AMNOG) | ESMO |
| Italy | EMA | AIFA | ESMO |
| Spain | EMA | AEMPS / IPT | ESMO |
| Canada | Health Canada | CADTH / pCODR | NCCN |

---

## Assets & Trials Tracked

### Target Assets (Forward-Looking Projections)

| Drug | Indication / Population | Trial | Status |
|------|------------------------|-------|--------|
| **Trodelvy** (monotherapy) | 1L mTNBC, BRCA-wt, PD-L1 CPS<10 | ASCENT-03 | NCCN Category 1 preferred; Gilead targeting FDA H2 2026 |
| **Trodelvy + Keytruda** | 1L mTNBC, PD-L1 CPS>=10 | ASCENT-04 | NCCN Category 1 preferred; NEJM published Jan 2026 |
| **Dato-DXd** (monotherapy) | 1L mTNBC, BRCA-wt, PD-L1 CPS<10 | TROPION-Breast02 | NCCN Category 2A preferred; FDA Priority Review, PDUFA Q2 2026 |
| **Dato-DXd +/- Durvalumab** | 1L mTNBC, PD-L1 CPS>=10 | TROPION-Breast05 | PCD ~18 months out (~Oct 2027); earliest FDA ~2029 |

### Analogs (Timeline Bracketing)

| Analog | Role | FDA Approval | Rationale |
|--------|------|-------------|-----------|
| **Enhertu** (2L+ HER2+ mBC) | Optimistic anchor | Aug 2022 | Practice-changing, strong HTA outcomes, fast uptake |
| **Trodelvy** (3L+ mTNBC) | Conservative anchor | Apr 2021 | Same TROP2 ADC class, more challenging HTA path |

---

## Methodology

The projection uses **analog-based lag estimation** across four layers:

### Layer 1 — Regulatory Approval Lags
Using FDA approval as T=0, observed lags to EMA, MHRA, and Health Canada approvals from the two analogs provide an optimistic-to-conservative range for each market.

### Layer 2 — Reimbursement & HTA Timelines
Country-by-country HTA decision timelines (NICE, G-BA, HAS, AIFA, AEMPS, CADTH) derived from analog precedent. Lag ranges account for differences in evidence strength, CDF routing (UK), and AMNOG free-pricing periods (Germany).

### Layer 3 — Guideline Inclusion
NCCN (US/Canada) and ESMO (EU + UK) guideline inclusion timelines. Notably, both Trodelvy and Dato-DXd have already been added to NCCN guidelines for 1L mTNBC **ahead of regulatory approval** — an unusual precedent.

### Layer 4 — SoC Integration
Defined as: **the later of guideline inclusion and national reimbursement/access.**

Market-specific rules:
- **US**: SoC = max(NCCN guideline, commercial launch). No HTA gate.
- **Germany**: Access at EMA approval (free pricing period). G-BA does not gate access.
- **UK/France/Italy/Spain/Canada**: SoC = max(guideline, HTA decision).

### Scenarios
Three scenarios are generated for each drug/population:
- **Optimistic**: Uses Enhertu analog lag (faster HTA, stronger clinical signal)
- **Base**: Average of both analog lags
- **Conservative**: Uses Trodelvy 3L+ analog lag (slower HTA, CDF pathway)

---

## Outputs

Running the pipeline produces four deliverables:

### 1. Excel Workbook (`output/drug_approval_timelines.xlsx`)

**9 tabs:**

| Tab | Contents |
|-----|----------|
| Analog - Enhertu | Known milestone dates for Enhertu 2L+ HER2+ mBC across all 7 markets, with lags from FDA and confidence coding. **Source column cells are clickable hyperlinks** to official regulatory/HTA databases. |
| Analog - Trodelvy | Same structure for Trodelvy 3L+ mTNBC |
| Derived Lags | Side-by-side lag comparison from both analogs per milestone per geography, with optimistic/base/conservative ranges |
| Trodelvy 1L CPS<10 (ASCENT-03) | Forward projections with 3 scenarios, known NCCN data, and confidence flags |
| Trodelvy 1L CPS>=10 (ASCENT-04) | Same for the Trodelvy + Keytruda combination |
| Dato-DXd 1L CPS<10 (TB02) | Forward projections for Dato-DXd monotherapy |
| Dato-DXd 1L CPS>=10 (TB05) | Forward projections — significantly later timeline (PCD ~2027) |
| Assumptions & Gaps | All 30 assumptions with impact levels — all 7 original data gaps resolved through primary research |
| Enrollment Implications | Corcept Phase 3 enrollment window analysis mapping SoC dates to geography recommendations |

**Color coding:**
- No background = Known/confirmed date
- Green = High confidence
- Yellow = Moderate confidence
- Orange = Low confidence
- Red = Data gap

### 2. Swimlane Timeline Chart (`output/swimlane_timeline.png`)

Full milestone timeline showing all 4 drug/population combinations across 7 geographies. Each lane shows regulatory approvals, HTA decisions, guideline inclusion, and SoC integration dates with:
- Color-coded markers by milestone type
- Opacity indicating confidence level
- Horizontal bars showing optimistic-to-conservative range for projected dates
- Red dashed "today" line

### 3. SoC Comparison Chart (`output/soc_comparison.png`)

Focused view comparing only SoC integration dates across all drugs and geographies, making it easy to identify which markets shift to SoC earliest and where enrollment windows are widest.

### 4. Assumptions Log (`docs/assumptions_log.md`)

Structured markdown document with all assumptions categorized by type (methodology, regulatory, trial, guideline, reimbursement, strategic), impact levels, and a priority data gaps section.

---

## Project Structure

```
Trodelvy-and-Dato-DXd-AdHoc/
|-- README.md                          # This file
|-- scripts/
|   |-- generate_all.py                # Main entry point
|
|-- src/
|   |-- models.py                      # Core data model (Milestone, DrugProgram, etc.)
|   |-- data/
|   |   |-- analog_data.py             # Hard-coded Enhertu & Trodelvy 3L+ milestone dates
|   |   |-- forward_looking_data.py    # Trodelvy 1L & Dato-DXd 1L known anchors
|   |   |-- assumptions.py             # Central assumptions registry (30 assumptions)
|   |-- projection/
|   |   |-- lag_calculator.py          # Computes lags from analog data
|   |   |-- scenario_engine.py         # Generates optimistic/base/conservative projections
|   |   |-- soc_integration.py         # SoC date logic (max of guideline + reimbursement)
|   |-- output/
|       |-- excel_writer.py            # Multi-tab Excel workbook with hyperlinks & formatting
|       |-- chart_generator.py         # Swimlane + SoC comparison charts (matplotlib)
|       |-- assumptions_renderer.py    # Markdown assumptions log generator
|
|-- output/                            # Generated deliverables
|   |-- drug_approval_timelines.xlsx
|   |-- swimlane_timeline.png
|   |-- soc_comparison.png
|
|-- docs/
|   |-- assumptions_log.md             # Generated assumptions document
```

---

## Prerequisites

- Python 3.11+
- Required packages: `openpyxl`, `matplotlib`, `python-dateutil`

Install dependencies:
```bash
pip install openpyxl matplotlib python-dateutil
```

---

## Usage

Generate all outputs:
```bash
python scripts/generate_all.py
```

Custom output directory:
```bash
python scripts/generate_all.py --output-dir my_output/
```

The script prints a full SoC integration summary to the console after generating files.

---

## Key Findings (Base Scenario)

| Market | Trodelvy CPS<10 | Trodelvy CPS>=10 | Dato-DXd CPS<10 | Dato-DXd CPS>=10 |
|--------|:--------------:|:----------------:|:---------------:|:----------------:|
| **US** | Q4 2026 | Q4 2026 | Q3 2026 | Q1 2029 |
| **UK** | Q2 2028 | Q2 2028 | Q1 2028 | Q3 2030 |
| **Germany** | Q3 2027 | Q4 2027 | Q2 2027 | Q1 2030 |
| **France** | Q4 2027 | Q1 2028 | Q3 2027 | Q2 2030 |
| **Italy** | Q2 2028 | Q2 2028 | Q1 2028 | Q3 2030 |
| **Spain** | Q3 2028 | Q3 2028 | Q2 2028 | Q4 2030 |
| **Canada** | Q4 2027 | Q4 2027 | Q3 2027 | Q1 2030 |

### Corcept Enrollment Implications

- **US**: SoC integration at commercial launch (H2 2026) for both CPS<10 drugs. Narrow enrollment window.
- **Germany**: Earliest EU5 market due to free-pricing access at EMA approval. SoC shift Q2-Q4 2027.
- **France/Italy/Spain**: Longest reimbursement timelines (18-27 months post-FDA). **Widest pre-SoC enrollment windows** for Corcept's Phase 3.
- **Dato-DXd CPS>=10 (TROPION-Breast05)**: Significantly behind — PCD ~Oct 2027, FDA ~2029. Extended enrollment window in all markets through at least 2029.
- **Implication**: Geographies with longer HTA timelines (Italy, Spain, France) offer the widest pre-SoC enrollment windows and should be prioritized for Corcept's Phase 3 site selection.

---

## Data Gaps — Status

All **7 original data gaps have been resolved** through primary research:

| Gap | Status | Resolution |
|-----|--------|------------|
| **G-BA (Germany)** | Resolved | Enhertu Beschluss 2 Feb 2023 (D-836); Trodelvy Beschluss 19 May 2022 (D-750). Sourced from g-ba.de |
| **HAS (France)** | Resolved | Enhertu CT opinion 22 Feb 2023; Trodelvy CT opinion 6 Apr 2022. Sourced from has-sante.fr |
| **ClinicalTrials.gov PCDs** | Resolved | ASCENT-03 PCD Jul 2028 (OS); ASCENT-04 PCD Feb 2027 (OS); TROPION-Breast05 PCD Jul 28, 2027. NCT numbers corrected. |
| **TROPION-Breast05** | Resolved | NCT06103864, registered PCD Jul 28, 2027. Status: Recruiting |
| **AIFA (Italy)** | Resolved | Enhertu GU n.153 on 3 Jul 2023 (~5 months post-EMA); Trodelvy GU n.185 on 9 Aug 2022 (~9 months post-EMA). Sourced from gazzettaufficiale.it |
| **AEMPS (Spain)** | Resolved | Both Enhertu and Trodelvy approved by CIPM on 28 Oct 2022 (same session). Sourced from Spanish Ministry of Health |
| **ESMO** | Resolved | Both drugs included in ESMO mBC CPG published 19 Oct 2021 (Annals of Oncology). Predates Enhertu FDA full approval. |

---

## How to Update Data

All milestone data is defined in Python files under `src/data/`. To update:

1. **Add or correct a known date**: Edit the relevant `Milestone()` entry in `analog_data.py` or `forward_looking_data.py`. Change `Confidence.LOW` to `Confidence.KNOWN` when filling a gap.
2. **Add a new assumption**: Add an `Assumption()` entry to `src/data/assumptions.py`.
3. **Regenerate outputs**: Run `python scripts/generate_all.py`.

The Excel hyperlinks, assumptions log, and charts will all regenerate from the updated data.
