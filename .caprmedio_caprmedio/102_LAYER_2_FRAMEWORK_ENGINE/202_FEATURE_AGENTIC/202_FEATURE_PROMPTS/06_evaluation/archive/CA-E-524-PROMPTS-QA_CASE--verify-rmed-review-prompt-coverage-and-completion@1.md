---
atom_id: "CA-E-524"
content_role: "Evaluation"
type: "QA Case"
current_scope_unit: "PROMPTS"
claim_target_scope_unit: "PROMPTS"
local_tier: "Standard"
global_tier: 11
status: Archived
author: "Anatoly Maslennikov"
version: 1
updated_at: "2026-10-03 06:25:11 +0400"
subjects:
  governs: "Prompt"
  depends_on:
    - "Atom"
    - "Carrier"
    - "Property"
    - "Scope"
    - "Atom/Claim"
    - "Atom/Details"
    - "Atom/Summary"
    - "Evaluation"
    - "Workflow Run"
    - "Implementation"
relations:
  evaluation_for:
    - CA-D-509
    - CA-D-510
    - CA-M-317
    - CA-R-1801
    - CA-R-1802
---
# Summary

Verify RMED review prompt coverage and completion

## Scope

the delivered RMED review prompts **and** their report-based progress aggregation.

## Claim

the Implementation passes this Evaluation **only** **when** its observed results satisfy the following golden scenarios with the declared current source bindings.

## Details

| Scenario | Expected result |
|---|---|
| readable unheaded content with a clear single contribution | Properties reports the missing headings; content checks assess quoted readable text rather than blocking **only** because headings are absent |
| independent Claims **in** readable unheaded content | Properties reports layout defects **and** Claim reports the independently replaceable contributions |
| genuine ambiguity affecting applicability | the affected check remains blocked with the precise ambiguity; independent check results remain recorded |
| partial fixes with a skipped check **or** unresolved finding | corrections remain recorded; Atom completion **and** selection completion remain false |
| complete fixes **after** **all** initial checks conclude | the result is `fixed_not_rechecked`; completion does **not** invent a post-fix pass |
| clean Atom | **all** required local checks pass with concrete evidence; the result is `checked_clean` **without** a source edit |
| context handoff during checking **or** fixing | continuation retains completed work **and** names unfinished work; the handoff does **not** report completion **or** repeat applied edits |

mock reports exercise encoding **and** aggregation. actual prompt executions against mock Atoms establish agentic behavior; fabricated passing reports **or** schema tests alone do **not** prove semantic review quality. implementation-test evidence remains distinct from an Evaluation of the methodology Workflow itself.

report failure for an observed contradiction **and** incomplete coverage for an unexecuted **or** unsupported scenario. retain the prompt binding, input mock, output, **and** expected-result comparison as test evidence.

