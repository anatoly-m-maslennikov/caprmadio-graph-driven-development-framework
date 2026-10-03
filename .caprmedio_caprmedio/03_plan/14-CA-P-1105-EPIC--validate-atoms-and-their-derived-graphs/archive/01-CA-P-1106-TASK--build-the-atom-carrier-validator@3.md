---
atom_id: CA-P-1106
content_role: Plan
type: Plan
label: Task
work_sequence_number: 1
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
autonomous_confidence_threshold: 99
status: Active
cce_version: cce_1
cce_form: obligation
subjects:
  governs: "Atom/Property/Carrier"
  depends_on:
    - "Atom"
    - "Atom/Property"
    - "Atom/Frontmatter"
    - "Atom/Claim"
    - "Atom/Summary"
    - "Relation"
    - "Tool"
    - "Evaluation"
version: 3
updated_at: "2026-09-23 23:42:09 +0000"
relations:
  is_decomposition_of:
    - CA-P-1105
  blocks:
    - CA-P-1107
---
# Summary

Build the Atom carrier validator

## Claim

the AI Agent **must** deliver a tested programmatic Tool that validates source Atom Carriers **in** a supplied folder against the current applicable Property **and** Carrier authority, **without** reconstructing Atom Properties from filename **or** directory placement.

## Definition of Done

the Plan is **not** Done **if** an applicable machine-checkable rule lacks a check **or** an explicit unsupported-rule error, **or** a required Property is accepted through filename **or** placement fallback, **or** invalid fixture cases pass, **or** valid fixture cases fail, **or** invocation **and** diagnostic results cannot be reproduced.

## Details

- implement CA-O-080 with its separate Action definitions CA-O-081–083 **and** Step bindings CA-O-084–086. O remains the operational source of truth; realize the Tool through CA-R-1622–1623, CA-M-316, CA-E-514–517, **and** CA-D-491–493. methodology Evaluation CA-E-513 checks the Workflow definition, **not** the Tool implementation.
- writing these specifications does **not** satisfy this Plan's executable Tool **and** automated-test completion conditions.
- recognize `projection.source_carrier_path` **only** as admitted metadata on Applicable Methodology projected Carriers. validate its relative resolution, selected source identity/Revision, **and** exact authored-content fidelity under CA-D-305 **and** CA-E-379; reject its use on authoritative source Atoms. this does **not** permit filename-derived Atom Properties **or** treat projected copies as independent source Atoms.
- inspect existing readers, validators, **and** model registries first; extend the canonical capability rather than introduce a parallel parser.
- resolve the admitted Property registry from current Core Meta-Model **and** applicable expansions. validate YAML syntax, duplicate keys, value types, required/optional/inapplicable Properties, unknown fields, structured section names, required sections, **and** duplicate authoritative values.
- check identity, Version, Updated At, Author, Content Role, Type, Status, tier, Scope Unit references, Subjects, **and** role-specific Properties under their actual authority; preserve governed Draft exceptions.
- check direct Relation kinds, owning direction, target existence, applicable target Status, **and** duplicate inverse storage. do **not** impose an Active-only rule on historical references **unless** their Relation authority requires it.
- use filenames **and** locations **only** for representation consistency diagnostics **after** reading internal values. report missing internal values; do **not** fill them by inference.
- accept a caller-supplied folder **and** explicit methodology context. return deterministic machine-readable findings with source locator, declared identity **when** present, Property/section, rule reference, severity, **and** failure reason; do **not** silently skip malformed files.
- add positive **and** negative fixtures for applicable roles, Types, Statuses, Drafts, Plan file/folder bundles, unknown Properties, broken YAML, body/frontmatter duplication, **and** one-way Relations.
- the Tool checks mechanically decidable conformance; Claim atomicity **and** semantic contradictions are reviewed by the later prompt, **not** claimed as proven here. add **only** missing authority needed for this capability under its declared owner.
- apply current source authority, including CA-R-1598 **and** CA-D-478–483; do **not** treat an outdated compiled copy as newer authority.
- check Project Principles **before** escalating uncertainty; ask the Operator **if** confidence remains **<99%**. do **not** silently weaken an Evaluation **or** discard a finding **to** pass.
- preserve unrelated work **and** history; follow the current revision, replacement, Summary identity, **and** approval rules.
