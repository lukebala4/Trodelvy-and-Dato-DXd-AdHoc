# Lessons Learned: What Went Wrong and How to Prevent It

## Context

This document is a post-mortem of the errors encountered during the initial build of the Trodelvy/Dato-DXd 1L mTNBC timeline projection tool. It is written to help you structure future AI-assisted life sciences CI projects so that these categories of error do not recur.

---

## Summary of Errors Found

### 1. Incorrect Health Canada Dates (Data Accuracy)

**What happened:** The agent populated Health Canada approval dates that were significantly wrong:
- Trodelvy 3L+ mTNBC: coded as Jul 18, 2022 (~15 months post-FDA). Actual NOC was Sep 24, 2021 (~5.5 months post-FDA) per Health Canada's Drug and Health Products Portal.
- Enhertu 2L+ HER2+: coded as Feb 17, 2023 (~10 months post-FDA). Evidence suggests the correct date is approximately Jun 2022 (~2 months post-FDA) for the DESTINY-Breast03-based indication expansion. The Feb 2023 date may have been confused with the HER2-low (DESTINY-Breast04) approval.

**Impact:** These errors cascade. The analog lag calculations for Canada were wrong, which meant all forward-looking Canadian projections were based on incorrect precedent data.

**Root cause:** The agent generated plausible-sounding dates without verifying them against a primary source. Health Canada's Drug Product Database (DPD) requires interactive search and does not have stable deep-linkable URLs, so the agent appears to have estimated dates based on typical patterns rather than looking them up. The estimates were then marked as "HIGH" confidence, which is misleading.

**How to prevent it:**
- In your CLAUDE.md, add an explicit rule: *"Do not assign Confidence.HIGH or Confidence.KNOWN unless the date is verified against a Tier 1 source (regulatory database, official press release, or published EPAR/SBD). If the source requires interactive search (e.g., Health Canada DPD, MHRA product database), mark the date as MODERATE at best and add [REQUIRES VERIFICATION]."*
- Include a verification checklist in your prompt: for each market, name the specific database the agent should consult (FDA Drugs@FDA, EMA EPAR, MHRA Products, Health Canada DPD, NICE, G-BA, HAS, AIFA GU, AEMPS CIPM, CADTH).
- Require the agent to produce a source audit table as a separate output, mapping each data point to its verification status.

---

### 2. Excel "Number Stored as Text" Green Triangle (Technical)

**What happened:** Several columns in the Excel workbook showed green triangle warnings in cells. This is Excel's indicator that a cell contains a value that looks numeric but is stored as text.

**Root cause:** Two coding errors in the openpyxl Excel generation:
1. Empty lag cells were written as `""` (empty string) instead of `None`. In a column of numeric values, Excel sees an empty string as "text in a numeric column" and flags adjacent cells.
2. Cells with no analog data were written as the string `"N/A"` in columns that otherwise contained floats.
3. Python's `round()` occasionally returns `int` instead of `float` (e.g., `round(0.0, 1)` can be stored as `0` by openpyxl when read back), which is inconsistent with float cells in the same column.

**How to prevent it:**
- In your CLAUDE.md, add a rule: *"When writing numeric data to Excel via openpyxl, always cast values to float() explicitly. Use None for empty cells in numeric columns, never empty string. Never mix string and numeric types in the same column."*
- If the project involves Excel output, include a verification step in the pipeline: after generating the workbook, programmatically scan all columns for type mismatches (string values in otherwise-numeric columns).

---

### 3. Unverifiable or Generic URLs (Source Quality)

**What happened:** Earlier versions of the codebase contained URLs that did not point to the specific document cited. Examples included:
- Generic company homepages (gilead.com, daiichisankyo.com) instead of specific press releases
- MHRA search page URLs instead of product-specific pages
- Health Canada search form URLs instead of specific DIN/NOC lookups
- A Lancet article DOI that pointed to the wrong paper

A previous session attempted to fix these, but the fix itself introduced some URLs that could not be independently verified in this environment (regulatory sites block automated access).

**Root cause:** The agent filled URL fields with plausible-looking but unverified links. When correcting these in a later session, the agent again generated URLs based on likely patterns rather than confirmed navigation. This is a form of fabrication — the URLs look authoritative but were never actually visited and confirmed.

**How to prevent it:**
- In your CLAUDE.md: *"Do not generate URLs unless you have verified they resolve to the specific document cited. If a regulatory database requires interactive search (MHRA, Health Canada DPD), omit the URL and describe the lookup path instead. A missing URL is better than a wrong URL."*
- When reviewing agent output that includes hyperlinks, spot-check at least 3-4 links manually in a browser before accepting the deliverable.
- Consider having the agent produce a separate "Source Verification Log" that explicitly states, for each URL: verified (yes/no), method of verification, date checked.

---

### 4. NCT Number Confusion (Data Entry)

**What happened:** In the initial build, the ClinicalTrials.gov NCT numbers for ASCENT-03 and ASCENT-04 were swapped. ASCENT-03 was incorrectly assigned NCT05382286 (which is ASCENT-04) and vice versa. Similarly, TROPION-Breast02 was initially assigned NCT05104866 (which is TROPION-Breast01, a different trial in HR+/HER2- breast cancer).

**Root cause:** The agent retrieved trial identifiers from memory/training data rather than looking them up on ClinicalTrials.gov. Clinical trial naming conventions (sequential NCT numbers, similar trial names within a program) make it easy to confuse related trials.

**How to prevent it:**
- In your prompt, provide the correct NCT numbers upfront if you know them, or explicitly instruct: *"Look up each trial on ClinicalTrials.gov and confirm the NCT number matches the trial name and indication before coding it."*
- Add NCT numbers as a required field in the CLAUDE.md project brief.
- After generation, include a programmatic check that fetches trial metadata from the ClinicalTrials.gov API and validates that the trial name and drug match what's coded.

---

### 5. ESMO Guideline Date Preceding FDA Approval (Misinterpretation Risk)

**What happened:** The ESMO mBC Clinical Practice Guideline (PubMed 34678411) was published October 19, 2021. For the Enhertu analog, the FDA full approval for 2L+ HER2+ was May 4, 2022. This means the ESMO guideline date appears to PREDATE the FDA approval by ~7 months, producing a negative lag.

This is actually correct — the ESMO guideline referenced DESTINY-Breast03 data presented at ESMO Congress September 2021, before the FDA acted on it. However, it initially caused confusion and was flagged as a potential data error by the agent itself in earlier sessions.

**Lesson:** In life sciences, guidelines sometimes incorporate trial data before regulatory approval. The analytical framework needs to handle negative lags gracefully rather than treating them as errors. This should be documented as an explicit assumption.

---

## Why These Errors Happened: Structural Causes

### 1. No Verification Gate Between Data Entry and Output

The pipeline goes: hard-code data -> compute lags -> project -> generate Excel. There is no intermediate step that validates source data against external databases. The agent coded dates, marked them as "Known" or "High" confidence, and the pipeline trusted them without challenge.

**Fix:** Add a `verification_status` field to the Milestone dataclass (e.g., "Verified against primary source", "Estimated from precedent", "Unverified"). Make the pipeline warn or error if any "Unverified" milestones are used in client-facing projections.

### 2. The Prompt Was Comprehensive but Lacked Verification Instructions

The original task prompt was detailed about *what* to build (data structures, projection logic, output formats) but did not include:
- Explicit instructions to verify each data point against a named primary source
- A requirement to flag uncertainty honestly rather than filling gaps with estimates
- A mandate to produce a source audit trail alongside the deliverable

**Fix:** For any CI project involving factual data, the prompt should include a section titled "Verification Requirements" that specifies: which sources to check, what constitutes sufficient verification, and how to flag gaps. See the updated CLAUDE.md in this repo for an example.

### 3. Confidence Was Cosmetic, Not Functional

The `Confidence` enum (Known/High/Moderate/Low/Gap) was used for color-coding in Excel but did not gate any behavior. A "Gap" milestone was treated identically to a "Known" milestone in the projection engine. This means the confidence system was decorative — it told the reader something was uncertain but did not prevent that uncertain data from driving projections presented alongside verified data.

**Fix:** Consider making the projection engine behave differently based on confidence. For example: "Low" or "Gap" milestones could be excluded from lag calculations, or projections based on them could be visually separated in the output. At minimum, the Enrollment Implications tab should highlight which recommendations depend on unverified inputs.

### 4. No CLAUDE.md Existed During Initial Build

The project was built without a CLAUDE.md file. This meant the agent had no project-specific rules about source verification, confidence assignment, URL generation, or life sciences domain conventions. The agent applied generic software development practices to a domain (life sciences competitive intelligence) where factual accuracy requirements are much higher.

**Fix:** Always create CLAUDE.md before the first line of code, not after. For CI projects, it must include the source hierarchy, verification rules, and domain-specific constraints listed in the Ways of Working document.

---

## Checklist for Future Life Sciences CI Projects

Before starting any agent-assisted CI engagement:

- [ ] **Define the CI question precisely** — one or two sentences, answerable, time-bounded
- [ ] **Create CLAUDE.md first** — include source hierarchy, verification rules, confidence definitions, scope boundaries
- [ ] **Provide known data points in the prompt** — NCT numbers, known approval dates, specific database URLs. The more verified inputs you give the agent, the fewer it has to look up (and potentially get wrong)
- [ ] **Require a source audit table** — every factual claim mapped to its source, verification status, and retrieval date
- [ ] **Build in a verification gate** — before generating client deliverables, run a check that all data points are verified or explicitly flagged
- [ ] **Spot-check URLs manually** — open at least 5 links in a browser before accepting any deliverable with hyperlinks
- [ ] **Separate data entry from projection** — have the agent populate data in one step, review/correct it, then run projections as a separate step. Do not let the agent go end-to-end from data entry to final output without a human review checkpoint
- [ ] **Use the agent for structure and computation, not as a source of facts** — the agent excels at building data models, writing projection logic, formatting Excel, and generating charts. It is unreliable as a primary source of regulatory dates, clinical trial details, and HTA timelines. Treat its factual claims as drafts requiring verification

---

## Was This a Prompting Problem?

Partly, yes. The original prompt was structured around *what to build* (data structures, projection logic, output tabs) but did not emphasize *how to verify*. For a software project, this would be fine — the code either works or it doesn't. For a life sciences CI project, the code can work perfectly while containing completely wrong data. The prompt needed:

1. **Explicit verification instructions** per market and per data source
2. **A mandate to flag uncertainty** rather than fill gaps with estimates
3. **A CLAUDE.md with domain rules** before the build began
4. **A two-phase workflow**: data collection/verification first, then computation/output second

Was the Ways of Working document suboptimal? Not exactly — the existing document is strong on software engineering practices (commits, testing, documentation). What was missing was the life sciences CI overlay: source hierarchy, verification discipline, and the principle that *in this domain, a confident-sounding wrong answer is worse than an honest gap*. The new consolidated Ways of Working document and CLAUDE.md now include these.

The core lesson: **the agent will match the rigor you demand.** If the prompt says "hard-code these dates," the agent will hard-code whatever it can find or infer. If the prompt says "hard-code these dates, verify each one against the named primary source, and mark any you cannot verify as [UNVERIFIED]," you get a fundamentally different — and more trustworthy — output.
