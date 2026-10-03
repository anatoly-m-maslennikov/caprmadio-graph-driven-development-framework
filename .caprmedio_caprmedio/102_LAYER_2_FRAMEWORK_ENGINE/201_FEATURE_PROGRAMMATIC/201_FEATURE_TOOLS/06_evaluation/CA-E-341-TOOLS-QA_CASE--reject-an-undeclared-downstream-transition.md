---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "commit-automation"
  depends_on:
    - "Action"
    - "Journal"
version: 7
updated_at: "2026-09-17 22:33:11 +0000"
relations:
  evaluation_for:
    - CA-R-1385
    - CA-R-1491
    - CA-M-182
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Reject an undeclared downstream transition

## Claim checked

a worker **or** Scheduler cannot invent downstream work outside the accepted manager-defined graph.

## Test case

return valid worker completion facts together with a requested step identity absent from the persisted declared transitions. inspect the rejected request, persisted stop state, diagnostics **and** attempted effects.

## Acceptance criteria

- completion facts remain inspectable **and** the undeclared transition is rejected; autonomous dispatch stops at the safe declared boundary.
- no undeclared executable work is queued **or** dispatched, **and** no Git **or** governed-content effect is authorized by that request.
- the bounded runtime transition that records blocked state **and** the admitted diagnostic evidence remain permitted under the existing recovery authority. recording the rejection is **not** acceptance of its requested work.
- an intact event about the rejected request remains eligible for Journal storage under CA-R-1491; accepted storage cannot certify the invalid transition **or** grant permission **to** resume.

## Failure disposition

reject invented downstream work, silent loss of the completion **or** stop reason, unauthorized effects, **or** a diagnostic-state update used **to** bypass the dispatch guard. preserve the accepted graph, requested step, completion facts **and** actual stop/effect evidence.
