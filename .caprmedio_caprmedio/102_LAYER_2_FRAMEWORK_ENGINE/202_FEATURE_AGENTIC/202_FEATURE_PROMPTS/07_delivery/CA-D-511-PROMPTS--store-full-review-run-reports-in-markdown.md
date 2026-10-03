---
atom_id: "CA-D-511"
content_role: "Delivery"
current_scope_unit: "PROMPTS"
claim_target_scope_unit: "PROMPTS"
local_tier: "Standard"
global_tier: 11
status: "Active"
author: "Anatoly Maslennikov"
version: 1
updated_at: "2026-10-03 16:23:03 +0400"
subjects:
  governs: "Evaluation/Report/Carrier"
  depends_on:
    - "Workflow"
    - "Workflow Run"
    - "Atom"
    - "Atom/Revision"
    - "Evaluation"
    - "Journal"
    - "Journal/Record"
    - "File Carrier"
relations:
  relates_to:
    - CA-D-496
    - CA-D-510
    - CA-R-1803
---
# Summary

Store full review Run reports **in** Markdown

## Scope

the human-readable full report Carrier for an RMED Atoms Base Revise Run.

## Claim

the full report **must** be **`=1`** Markdown File Carrier at repository-relative `tmp/<workflow name>/<workflow run id>.md`, with the following registered sections.

## Details

| Section | Contents |
|---|---|
| `# Run` | Workflow name, Run ID, definition binding, start **and** latest report times, execution outcome, **and** evidence-recording state |
| `## Selection` | original request, selected Atom list with source observations, selection limits, **and** exclusions |
| `## Rules` | exact checking-rule bindings **and** references **to** the shared rule content |
| `## Results` | reports received, initial checks completed, Atoms completed, **and** counts by saved outcome |
| `## Atom Reports` | **`=1`** subsection per selected Atom containing its full saved report: **all** **`=6`** check outcomes, evidence, findings, corrections, rejections, unresolved findings, **and** before/after source observations; pending Atoms remain explicitly pending |
| `## Remaining Work` | blockers, unperformed work, handoff context, **and** any requested Operator decision |
| `## Journal` | shared Journal reference, Run correlation, confirmed Event references, **and** any unconfirmed append **or** recording failure |

- bind the path from the supplied Workflow name **and** Run ID. the Workflow name for this report is `RMED Atoms Base Revise`; retain **`=1`** report path through context handoffs. path components stay within the admitted temporary root; invalid components remain an explicit output-binding blocker.
- render the full saved per-Atom evidence **without** replacing it with totals, selected examples, **or** truncated excerpts. rule bodies **may** remain shared **and** referenced; source passages that support findings remain **in** the report.
- the Markdown file is the assembled human-readable representation of the saved Run evidence under CA-D-496-CORE_META_MODEL--store-one-review-report-per-source-atom **and** CA-D-510-PROMPTS--serialize-review-coverage-and-correction-outcomes-separately. its rendering does **not** rerun checks **or** create independent findings.
- updating this Run report preserves its original findings **and** adds their actual dispositions. another Run uses another Run ID **and** report file.
