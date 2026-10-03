---
atom_id: "CA-D-510"
content_role: "Delivery"
current_scope_unit: "PROMPTS"
claim_target_scope_unit: "PROMPTS"
local_tier: "Standard"
global_tier: 11
status: Archived
author: "Anatoly Maslennikov"
version: 1
updated_at: "2026-10-03 06:25:11 +0400"
subjects:
  governs: "Evaluation/Report/Carrier"
  depends_on:
    - "Evaluation"
    - "Atom"
    - "Atom/Identifier"
    - "Atom/Revision"
    - "Workflow Run"
    - "Property"
    - "Prompt"
relations:
  relates_to:
    - CA-D-496
    - CA-R-1802
---
# Summary

Serialize review coverage and correction outcomes separately

## Scope

temporary JSON reports **and** progress records emitted by the RMED review prompt Implementation.

## Claim

the Implementation **must** serialize initial check evidence, applied corrections, **and** derived completion **in** separate fields within the report layout governed by CA-D-496-CORE_META_MODEL--store-one-review-report-per-source-atom.

## Details

| Record | Field | Encoding |
|---|---|---|
| report | `source` | object containing the checked path, Version, **and** SHA-256 digest |
| report | `atom_id` | checked Atom ID |
| report | `checks` | object keyed by `properties`, `cce`, `scope`, `claim`, `details`, **and** `summary`; **every** entry carries `status` **and** evidence **or** a reason |
| report | `findings`, `blockers` | separate arrays of confirmed findings **and** incomplete check coverage |
| report | `corrections`, `rejected_findings`, `unresolved_findings` | separate arrays retaining the disposition of findings; a completed fix carries an explicit empty `unresolved_findings` array |
| report | `result` | recorded check **or** fix result |
| progress item | `reported_result` | retained report result |
| progress item | `check_complete` | Boolean for completion of **all** required initial checks |
| progress item | `complete` | Boolean for completion of this Atom's admitted work |
| progress item | `state` | derived state that retains `blocked` for unresolved coverage **or** findings |
| progress total | `total`, `reported`, `checked`, `completed`, `complete`, `states` | selection size, report count, complete-check count, completed-Atom count, aggregate Boolean, **and** state counts |

initial check outcomes remain preserved **after** correction. `fixed_not_rechecked` **or** an approved `replaced_not_rechecked` result does **not** overwrite blocked check evidence **or** independently set `complete` **to** true.

