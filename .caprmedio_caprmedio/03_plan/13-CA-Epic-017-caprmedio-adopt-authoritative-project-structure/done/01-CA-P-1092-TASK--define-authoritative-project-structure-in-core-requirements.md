---
atom_id: CA-P-1092
cce_version: cce_1
cce_form: obligation
author: Operator
assignee: AI Agent
autonomous_confidence_threshold: 99
subjects:
  governs: "Scope Unit"
  depends_on:
    - "Artifact"
    - "Atom"
    - "Operator"
    - "AI Agent"
    - "Autonomous Confidence Threshold"
version: 2
updated_at: "2026-09-15 00:13:02 +0000"
relations: {}
---
# Define authoritative Project Structure in Core Requirements

the Assignee **must** establish the Requirement authority for Project Structure as an authoritative non-Atom Artifact rather than a derived Projection.

## Scope

CORE_META_MODEL at `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL`; active R Atoms governing Structural Entities, Scope Units, their properties, structural sources of truth, Goal ownership, Settings boundaries, **and** structural Projections.

## Definition of Done

the Task is **not** Done **if** (Project Structure remains classified as a derived source **or** a child requires a Name/Order Atom **or** a Goal **to** establish its structural identity **or** concrete structural values have multiple authoritative owners **or** the distinction between declaration **and** observed materialization is absent).

## Details

the latest Operator design governs this Epic: **every** Project has its own authoritative `project_structure.toml`; Scope Unit Names, parentage, Type, Label, structural Local Order, navigation number, **and** explicit authority/Implementation Folder bindings are declared there. Goal Atoms remain independent R authority for purposes assigned by the parent; the structural declaration does **not** replace Goal content **or** the Scope Unit's Spec. an existing unit with no Active Goal remains visible as a unit with a Goal gap, **not** silently discarded.

retain `structural_level` **and** `authority_path` for readability under deterministic consistency rules. parentage determines Structural Level; the root has level 0. `PROJECT` is a reserved reference **to** the owning Project root, **not** its literal Name; other parent references resolve unique Scope Unit Names. retain Ordered/Unordered Type independently of Label **and** navigation. an explicit per-unit `authority_mode` is stored once **in** Project Structure, with omission inheriting Framework Instance Settings; the same override **must not** remain authoritative **in** both places. Project identity **and** prefix stay **in** Project Settings. preserve general D Carrier rules while moving concrete path bindings out of D Atoms.

review CA-R-626, CA-R-862, CA-R-926, CA-R-947, CA-R-1430, CA-R-1470/1471 **and** related authority; anchors are **not** an exhaustive inventory. preserve unrelated Claims **and** history. this Task updates model content **only**; no manifest, Tool code, runtime, folder migration, **or** generated output is changed. coordinate overlaps with CA-P-1086 **without** executing **or** rewriting other Epics.

execute **only** after the direct prerequisite is Done **when** one is declared. **if** confidence is below the effective Autonomous Confidence Threshold, check Project Principles first **and** ask the Operator **if** uncertainty remains. preserve unrelated working-tree changes **and** historical records. creating this Task authorizes no execution by itself.

completion evidence: 12 existing Core Requirement Atoms were reconciled **and** 3 Requirement Atoms were added (CA-R-1483–1485). Project Structure owns declarations; Goal coverage **and** physical materialization remain independent. concrete bindings **and** explicit per-unit Authority Mode overrides have one owner. 15 current source files **and** 12 byte-exact prior revisions passed integrity checks; no Tool, manifest, physical structure, **or** Projection was changed by this Task.
