---
subjects:
  governs: "Workflow"
  depends_on:
    - "Entity"
    - "Artifact"
    - "Atom"
    - "Atom/Content Role"
    - "Type"
    - "Status"
    - "Structural Entity"
    - "Scope Unit"
    - "Atom Collection"
    - "Carrier"
version: 4
updated_at: "2026-10-03 00:01:51 +0400"
relations: {"relates_to": ["CA-R-1519"]}
atom_id: "CA-R-1521"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 10
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1521-CORE_META_MODEL-GENERAL-REQUIREMENT--resolve-lifecycle-changes-from-applicable-status-models.md
  source_atom_id: CA-R-1521
  source_atom_revision: 4
  source_sha256: 68e37f2d0c8e75cdf5caf5bb9304ffac9f7e8f58fdc06c89c2debe69c8cb966c
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Resolve lifecycle changes from applicable Status models

## Scope

Workflows that change an Entity's Status.

## Claim

a Workflow for changing an Entity's Status **must** admit **any** requested Status allowed by that Entity's applicable status model **and** transition rules, rather than a fixed list built into the Workflow.

## Details

- resolve the model using the actual Entity kind **and**, for an Atom, its qualified Content Role **and** Type.
- apply the same model-driven rule **to** a Scope Unit **or** Atom Collection **when** a status model is defined for it.
- preserve the model's authorization, transition conditions, **and** applicable Carrier rules; support for **any** admitted Status does **not** authorize arbitrary values **or** transitions.
- changing the admitted values **within** the supported model **must not** require a separate Workflow for **every** value. unsupported model capabilities **must** be reported rather than silently approximated.
- a missing status model **must not** be replaced with an invented universal Draft, Active, **or** Archived lifecycle for **all** Artifacts **and** Structural Entities.
