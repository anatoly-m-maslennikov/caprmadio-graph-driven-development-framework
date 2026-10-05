---
subjects:
  governs: "Action/Execution Kind"
  depends_on:
    - "Action"
    - "AI Agent"
    - "Tool"
    - "Operator"
version: 4
updated_at: "2026-10-03 00:06:54 +0400"
relations: {"relates_to": ["CA-R-1452"]}
atom_id: "CA-R-1526"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 10
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1526-CORE_META_MODEL-GENERAL-REQUIREMENT--define-action-execution-kind.md
  source_atom_id: CA-R-1526
  source_atom_revision: 4
  source_sha256: 2e3f06da63e0309d9f33a92630139ab5420678aa8ba42344f53976d4671b92e6
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Define Action Execution Kind

## Scope

the distinction between execution by code **and** execution requiring AI Agent judgment for an Action's declared responsibility.

## Claim

Action Execution Kind **means** the distinction between execution by code **and** execution requiring AI Agent judgment for an Action's declared responsibility.

## Details

- Programmatic: code performs the Action according **to** its specified behavior, **without** delegating interpretation **or** judgment **to** an AI Agent. programmatic interaction with the Operator does **not** by itself make the Action Agentic.
- Agentic: an AI Agent interprets the supplied context **and** instructions **to** perform the Action. the AI Agent **may** call Tools within its admitted authority.
- classify an invocation by the responsibility actually delegated, **not** by whether its transport **or** surrounding executor is implemented **in** code. code that delegates the Action's judgment **to** an AI Agent does **not** make that Action Programmatic.
- the distinction does **not** select the Agent's execution context, grant permissions, **or** change the Action's semantic boundary. Tool calls **do not** by themselves create additional Actions **or** Workflow Steps.
