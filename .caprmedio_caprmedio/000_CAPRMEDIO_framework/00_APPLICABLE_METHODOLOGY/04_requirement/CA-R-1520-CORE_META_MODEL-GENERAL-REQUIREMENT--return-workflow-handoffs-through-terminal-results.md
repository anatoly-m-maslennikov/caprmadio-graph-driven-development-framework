---
subjects:
  governs: "Workflow Run"
  depends_on:
    - "Workflow"
    - "Step"
    - "Action"
    - "Artifact/Revision"
    - "Operator"
    - "Journal"
    - "Status"
version: 5
updated_at: "2026-10-03 00:01:28 +0400"
relations: {"relates_to": ["CA-R-1510", "CA-R-1513", "CA-R-1519", "CA-R-1720"]}
atom_id: "CA-R-1520"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 10
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1520-CORE_META_MODEL-GENERAL-REQUIREMENT--return-workflow-handoffs-through-terminal-results.md
  source_atom_id: CA-R-1520
  source_atom_revision: 5
  source_sha256: 04bb2d029a169948a60b06d9a2f49736ce0f4e57029ee2791fa725aca8edb294
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Return Workflow handoffs through terminal results

## Scope

Workflow handoffs to another Workflow.

## Claim

**when** a Workflow declares a handoff **to** another Workflow, its Run **must** end with a terminal result sufficient for the executor **to** evaluate **and** start the continuation separately.

## Details

### Handoff result

- identify the completed Run, the reason for handoff, **and** the continuation Workflow **or** the methodology rule that selects it.
- provide the target identities **and** observed Revisions, required inputs **and** parameters, proposed changes, completed checks **and** their applicability, **and** a complete account of effects already performed, **if** **any**.
- distinguish a requested continuation from an authorized, started, **or** completed continuation. an incomplete result **must not** trigger guessed execution.

### Run boundary

- the ending Run does **not** call the continuation Workflow, wait for it, **or** resume its own normal Steps afterward.
- the executor retains the original request **and** the association between predecessor **and** successor Runs; it rechecks applicable authority **and** input freshness **before** starting the successor.
- ending the predecessor **must not** report the requested work as complete **when** a required continuation is still pending, blocked, **or** failed.
- the handoff outcome does **not** itself add a Status value. a chain of handoffs **must not** bypass approval, refresh an exhausted retry allowance, **or** create an unbounded loop.

the handoff is a result between distinct Runs, **not** an ON_RESULT edge between Steps of different Workflows.
