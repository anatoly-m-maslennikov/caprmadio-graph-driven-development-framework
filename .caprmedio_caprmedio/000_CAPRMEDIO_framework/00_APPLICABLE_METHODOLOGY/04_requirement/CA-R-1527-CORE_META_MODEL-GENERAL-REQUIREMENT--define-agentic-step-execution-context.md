---
subjects:
  governs: "Step/Agentic Execution Context"
  depends_on:
    - "Step"
    - "Action/Execution Kind"
    - "Workflow"
    - "Step Run"
    - "AI Agent"
    - "Operator"
version: 4
updated_at: "2026-10-01 21:44:50 +0400"
relations: {"relates_to": ["CA-R-1509", "CA-R-1526", "CA-R-1525"]}
atom_id: "CA-R-1527"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 10
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1527-CORE_META_MODEL-GENERAL-REQUIREMENT--define-agentic-step-execution-context.md
  source_atom_id: CA-R-1527
  source_atom_revision: 4
  source_sha256: 54d5849f0b4603b0947e9232ba46f7be0a077f84d30a448fe4f8ba4780b587b5
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Define agentic Step execution context

## Scope

Agentic Step Execution Context selected by a Step's invocation binding for its Agentic Action.

## Claim

Agentic Step Execution Context **means** the context selected by a Step's invocation binding for its Agentic Action: Integrated **or** Isolated.

- Integrated: the current participating session receives the Action's bound inputs **and** instructions, performs the Action, **and** returns its result **to** the executor.
- Isolated: a separate AI Agent context receives the Action's bound inputs **and** instructions, performs the Action, **and** returns its result **to** the executor.
- an Agentic Step invocation resolves **`=1`** admitted context through its declared binding **before** dispatch. the binding **may** use an explicitly supplied runtime parameter; a missing **or** unsupported context blocks admission rather than causing silent substitution.
- the same Action definition **may** be reused **in** either context **when** its required capabilities are available. do **not** duplicate an Action merely **to** select another context.
- a Workflow **may** mix Programmatic Steps, Integrated Agentic Steps, **and** Isolated Agentic Steps. the context belongs **to** the invocation, **not** **to** a second Workflow classification **or** the Action's identity; it does **not** apply **to** a Programmatic Action as an Agent context.
- the actual Step Run retains its selected context. Isolated does **not** mean unrestricted, fully autonomous, concurrent, **or** unable **to** request Operator input. Integrated does **not** grant the session additional authority.

## Details
