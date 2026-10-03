---
atom_id: CA-P-979
cce_version: cce_1
cce_form: obligation
author: Operator
assignee: AI Agent
autonomous_confidence_threshold: 99
subjects:
  governs:
    continuant:
      - "Atom/Content Role: Ops"
  depends_on:
    continuant:
      - "Atom"
      - "Atom/Claim"
      - "Atom/Content Role"
      - "Atom/Subjects"
      - "Scope Unit"
      - "Atom/Local Tier"
      - "Atom/Global Tier"
      - "Relation"
      - "Actor"
      - "Operator"
      - "AI Agent"
      - "Atom/Content Role: Plan/Type: Task"
      - "Autonomous Confidence Threshold"
version: 2
updated_at: "2026-09-13 01:25:33 +0400"
relations:
  depends_on:
    - CA-P-978
---
# Define Processes as Action-flow graphs

the Assignee **must** define a Process as a reusable flow graph whose nodes reference Actions.

## Scope

(selected Process-definition authority **and** its directly affected Content Role boundary **in** CORE_META_MODEL at `.caprmedio_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL`); the source **and** lifecycle admission boundary established by CA-P-976 applies; historical versions, generated copies, runtime, Implementation code, **and** other CAP Atoms are excluded.

## Definition of Done

the Task is **not** Done **if** ((Process nodes do **not** reference reusable Actions) **or** (the Process has no explicit control flow governing order **and** conditional selection **or** revisiting of nodes) **or** (a Process definition is conflated with a particular execution) **or** (the same reusable Action **must** be copied **or** redefined for **every** Process) **or** (accepted success, retry-budget, **or** escalation behavior is lost) **or** (illustrative Action responsibilities become an unapproved closed taxonomy) **or** (concurrency, arbitrary recursion, **or** unlimited retries are silently authorized)).

## Details

the Operator's accepted flow-diagram clarification supersedes the earlier linear-sequence restriction: **every** Process node references an Action, **and** the Process's explicit control flow **may** select **or** revisit nodes under explicit accepted conditions. doer, finder, checker/test, **and** quality-gate evaluation are illustrative Action responsibilities, **not** a closed list of Actor **or** Action Types. a checking Action **may** use an Evaluation criterion **without** turning that Spec Atom into an execution node. preserve distinct reusable definition **and** particular execution references, together with accepted success, bounded retry, **and** escalation behavior. exact relation kinds, edge cardinalities, node-reference serialization, **and** Entity/Operation domain remain with CA-P-980.

execute **only** **after** the explicit prerequisite is Done. **if** confidence **in** a decision is below the effective Autonomous Confidence Threshold, check Project Principles first **and** ask the Operator **if** uncertainty remains; do **not** silently select a new design. no migration is executed merely by creating this Task.

Completion evidence: [Process flow-graph report](../../execution_evidence/CA-P-979-process-flow-graph-report.md) **and** [exact source/Task change map](../../execution_evidence/CA-P-979-changed-source-map.projection.json). CA-R-1453 Version 1 defines the reusable Action-flow graph; CA-R-1340 Version 5 changes its residual Process-sequence wording **to** Process definition while preserving the Method role boundary. the reviewed semantic fixtures preserve Action reuse, explicit conditional flow, definition/execution separation, **and** accepted bounded retry/success/escalation behavior. the Definition of Done falsifying condition is false. the exact prior source **and** Task bytes are archived; unselected admitted sources, excluded Drafts, prior archives, frozen evidence **and** the staged index are preserved. existing Subject serialization is temporary compatibility **only**; later relation, domain, temporal **and** carrier decisions remain deferred. Git materialization under CA-D-335 remains explicitly pending.
