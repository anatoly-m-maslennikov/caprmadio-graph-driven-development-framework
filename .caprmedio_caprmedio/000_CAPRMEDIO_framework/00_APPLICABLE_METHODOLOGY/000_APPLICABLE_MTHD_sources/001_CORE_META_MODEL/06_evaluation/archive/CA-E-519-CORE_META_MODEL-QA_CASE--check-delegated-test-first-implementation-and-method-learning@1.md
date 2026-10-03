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
version: 1
updated_at: "2026-09-24 01:39:33 +0000"
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
    - CA-O-097
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

the delegated implementation Workflow check **must** reject a definition **or** Run that bypasses its test-first, Plan, evidence, **or** corrective-Method gates.

- reject missing source-bound active Method Projection, missing selected RED context, stale source bindings, unresolved required authority, **or** silently applying unrelated Methods. refresh **and** revalidate after an authorized Method activation.
- require P/Plan Atoms for Tasks/subtasks, a falsifiable Definition of Done, bounded admitted work, explicit once-owned decomposition, **and** acyclic completion prerequisites. estimates target **<15** minutes where practical; invented estimates **or** omitted test work do **not** satisfy the bound.
- require delegated subagent execution for the Isolated Step bindings. a native host with subagents, file access, **and** command execution but no MCP **must** be an admitted execution option; an unavailable subagent **must not** cause a main-session fallback.
- reject implementation **before** test preparation, skipping runnable baseline tests, copied implementation behavior as expected test results, **or** a mock substituted for the implementation under test. admit **only** explicit minimum prerequisites needed **to** execute prepared tests.
- a correct initial test failing because selected behavior is absent returns expected initial failure, **not** a repair retry **or** a Method lesson. actual implementation/test-code defects require diagnosis **and** admitted retry control. an environment failure **or** incorrect governing test expectation **must not** be misclassified as a coding mistake.
- a missing corrective Method starts as an identity-compliant Standard Draft; an existing suitable Method is reused. repeated failure for the same lesson does **not** create duplicate Atoms. Drafts remain excluded from the active Method Projection.
- require evidence that the regression detects the diagnosed defect **and** passes on the fix, plus all required current-candidate checks. missing, stale, **or** failed evidence prevents activation. passing tests alone do **not** justify a wider policy **or** resolve an authority conflict.
- unmet confidence, permission, **or** required Operator approval keeps a new Method Draft non-authoritative. successful admission activates the bounded Method **and** triggers refreshed Method context **and** affected-work review; it does **not** automatically generalize policy.
- **every** actual failed-code repair goes through CA-O-024 **and** preserves retry accounting. repeated preparation with no changed work/evidence/baseline terminates blocked; a changed failure, subagent replacement, **or** new Method **must not** reset the allowance.
- reject successful completion while required P work, child Plans, current checks, Method dispositions, **or** Definitions of Done remain incomplete. distinguish definition conformance from a real execution result.
