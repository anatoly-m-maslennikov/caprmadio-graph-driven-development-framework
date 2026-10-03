---
atom_id: "CA-E-524"
content_role: "Evaluation"
type: "QA Case"
current_scope_unit: "PROMPTS"
claim_target_scope_unit: "PROMPTS"
local_tier: "Standard"
global_tier: 11
status: "Active"
author: "Anatoly Maslennikov"
version: 2
updated_at: "2026-10-03 16:23:03 +0400"
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
    - "Journal"
    - "Journal/Record"
    - "Evaluation/Report"
relations:
  evaluation_for:
    - CA-D-509
    - CA-D-510
    - CA-D-511
    - CA-M-317
    - CA-R-1801
    - CA-R-1802
    - CA-R-1803
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
| complete initial checks with an unauthorized correction | check completion remains true; fix blockers **and** unresolved findings keep Atom completion false |
| an applied correction omits another confirmed finding | the unaccounted finding remains unresolved even **if** the report claims `fixed_not_rechecked` **and** carries an empty unresolved list |
| changed source **or** applicable checking criteria **before** correction | the earlier report stays historical; correction is blocked with the mismatch **without** an automatic recheck |
| complete fixes **after** **all** initial checks conclude | the result is `fixed_not_rechecked`; completion does **not** invent a post-fix pass |
| clean Atom | **all** required local checks pass with concrete evidence; the result is `checked_clean` **without** a source edit |
| context handoff during checking **or** fixing | continuation retains completed work **and** names unfinished work; the handoff does **not** report completion **or** repeat applied edits |
| completed, empty, **or** blocked Run | the full Markdown report exists at the registered Run path, retains **all** selected Atom reports **and** unresolved work, **and** correlates with shared Journal Records through the same Run ID |
| report-write **or** Journal-append failure | saved work remains visible; evidence recording is incomplete; no successful write, recorded Event, **or** fully recorded Run is invented |
| caller handoff **or** parallel workers | **every** result retains the same Run ID; the assembled report includes **all** received evidence **without** truncation **or** duplicate effects |

mock reports exercise encoding **and** aggregation. actual prompt executions against mock Atoms establish agentic behavior; fabricated passing reports **or** schema tests alone do **not** prove semantic review quality. implementation-test evidence remains distinct from an Evaluation of the methodology Workflow itself.

report failure for an observed contradiction **and** incomplete coverage for an unexecuted **or** unsupported scenario. retain the prompt binding, input mock, output, **and** expected-result comparison as test evidence.
