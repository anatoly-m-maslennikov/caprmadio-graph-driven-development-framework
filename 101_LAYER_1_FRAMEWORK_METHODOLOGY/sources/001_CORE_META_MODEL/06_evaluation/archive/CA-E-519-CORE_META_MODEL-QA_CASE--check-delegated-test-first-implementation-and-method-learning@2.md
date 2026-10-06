---
atom_id: CA-E-519
content_role: Evaluation
type: QA Case
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
author: Anatoly Maslennikov
status: Active
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "Implementation Workflow"
  depends_on:
    - "Workflow"
    - "Step"
    - "Action"
    - "AI Agent"
    - "Atom/Content Role: Plan/Type: Plan"
    - "Atom/Content Role: Method"
    - "Atom/Content Role: Evaluation"
    - "Atom/Content Role: Implementation"
    - "Projection"
    - "Operator"
    - "Implementation Retry Limit"
    - "Autonomous Confidence Threshold"
version: 2
updated_at: "2026-09-24 17:18:07 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  evaluation_for:
    - CA-O-016
    - CA-O-017
    - CA-O-018
    - CA-O-019
    - CA-O-020
    - CA-O-021
    - CA-O-089
    - CA-O-090
    - CA-O-091
    - CA-O-092
    - CA-O-093
    - CA-O-094
    - CA-O-095
    - CA-O-096
    - CA-O-099
    - CA-O-100
    - CA-O-101
    - CA-O-102
    - CA-O-098
  relates_to:
    - CA-E-486
    - CA-E-473
    - CA-R-1592
    - CA-R-1599
    - CA-R-1559
---
# Summary

Check delegated test-first implementation and Method learning

## Claim

the delegated implementation **and** Method-learning Workflow check **must** reject any definition **or** Run that conflates their separate completion conditions **or** bypasses their evidence gates.

- reject missing source-bound active Method Projection, missing selected RED, stale source bindings, **or** unresolved authority. require P/Plan work, falsifiable Definitions of Done, actual dependencies, bounded delegated work, **and** native Isolated Steps; MCP is **not** required.
- check that implementation test preparation follows applicable Methods **before** behavior implementation, with **only** explicit minimum prerequisites admitted. **when** PROGRAMMATIC policy applies, require end-to-end-first golden-corpus evidence; a unit-only pass **or** mocked implementation does **not** replace it.
- exercise expected initial failure, a genuine code defect, test-code defect, an environment blocker, **and** incorrect governing expectations. require distinct diagnoses; do **not** turn every failure into a Method lesson.
- require relevant targeted reproduction/regression tests for discovered defects **and** required current-candidate end-to-end verification after repair. preserve confidence, permission, retry accounting, **and** no-progress termination.
- complete CA-O-016 with **all** required implementation work **and** checks satisfied **without** creating an M Atom. reject `methods_ready`, Method drafting, Method promotion, **or** CA-O-098 as an internal completion dependency of that graph.
- invoke CA-O-102 separately with retained issue/test/diagnosis/fix evidence. verify deduplication against existing Methods, Standard Draft creation **only** for a justified missing Method, no assigned Draft ID, **and** no automatic broader-policy generalization.
- keep a Method Draft non-authoritative **until** its correction **and** regression are verified, current authority is checked, **and** applicable confidence/permission/Operator approval gates pass. a blocked learning Run **must not** turn a completed implementation Run into an incomplete one.
- reject activation from stale evidence **or** tests alone **without** a supported lesson. a newly accepted Method changes future authority bindings; it does **not** silently reclassify old results as checked against that new authority.
- distinguish graph-definition conformance from real Run evidence; defining tests **or** Workflows is **not** proof of execution.
