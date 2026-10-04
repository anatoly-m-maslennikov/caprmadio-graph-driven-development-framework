---
subjects:
  governs: "Workflow"
  depends_on:
    - "Step"
    - "Action"
    - "Workflow Run"
    - "Step Run"
    - "Workflow/Relation Kind: On Result"
    - "Artifact/Revision"
    - "Operator"
    - "Methodology"
version: 5
updated_at: "2026-10-03 00:01:03 +0400"
relations: {"relates_to": ["CA-R-1508", "CA-R-1509", "CA-R-1510", "CA-R-1511", "CA-R-1513", "CA-R-1525"]}
atom_id: "CA-R-1519"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 10
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1519-CORE_META_MODEL-GENERAL-REQUIREMENT--require-conforming-workflow-execution.md
---
# Summary

Require conforming Workflow execution

## Scope

Workflow execution.

## Claim

an executor of a Workflow **must** conform **to** the applicable methodology execution rules rather than inventing behavior that is absent from its governing definitions.

## Details

- resolve the Workflow, referenced Actions, Step bindings, typed transitions, terminal outcomes, **and** applicable execution rules **before** their use. bind definition Revisions **and** revalidate definition changes under CA-R-1525 rather than silently resolving a different Revision during the same Run.
- preserve supplied inputs, returned results, **and** actual Run identities under CA-R-1509, CA-R-1510, **and** CA-R-1511.
- admit work **only** within the applicable authorization, Operator-approval, retry, waiting, **and** recovery conditions. a missing capability **or** unresolved rule blocks the affected execution rather than granting permission. a well-formed definition remains valid **when** a selected executor lacks a required capability; definition validation **and** execution admission are distinct checks.
- a Workflow **may** assume these declared capabilities; it **must not** require a particular executor product merely **to** define its behavior.

this conformance boundary does **not** select a server, programming language, storage technology, **or** a Workflow for building the executor itself.
