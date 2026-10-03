---
atom_id: CA-P-106
cce_version: cce_1
cce_form: obligation
subjects:
  governs:
    continuant:
      - Applicable Methodology/Sources/Local Configuration
    occurrent:
      - Configuration Authority Reconciliation
  depends_on:
    occurrent:
      - CA-P-105
version: 4
updated_at: 2026-08-27 01:31:00 +0400
autonomous_confidence_threshold: 99
relations: {}
---
# Reconcile Local Configuration Authority

**when** CA-P-105 is Done, **then** the Assignee **must** reconcile 003_LOCAL_CONFIGURATION as the Project-owned authority that identifies the current Project and selects CORE_META_MODEL and LOCAL_CONFIGURATION as the only Source Layers for Applicable Methodology compilation.

## Scope

`((all active and draft Atoms, configurations, manifests, and provenance records in the frozen CA-P-102 source frontier that govern current Project identity, Installed Extension selection, Project Customization, replacement, priority, compatibility resolution, local Tool, MCP, and App modes, and Applicable Methodology source selection) union (their exact accepted successors produced by CA-P-103 through CA-P-105 and CA-P-112) union (the authority Carriers required to record the Operator-approved CORE_META_MODEL plus LOCAL_CONFIGURATION source selection))`

## Definition of Done

the Task is **not done if** (Local Configuration does not identify exactly one current Project **or** it cannot determine CORE_META_MODEL followed by LOCAL_CONFIGURATION as its complete ordered source frontier **or** an Installed Extension contributes to Applicable Methodology **or** a Project Customization does not identify exactly one customized source revision **or** a Project Customization modifies Core Meta-Model or Extension authority **or** a current replacement, priority, compatibility, or local mode decision lacks Project-owned authority **or** Local Configuration duplicates immutable Core Meta-Model or Extension content **or** one decision requires unfinished compiled output to establish its own validity).

## Details

represent every local modification as a separate Project Customization Atom with an exact reference to the one source revision it customizes. keep every selection and resolution decision Project-owned. the Operator decided that this migration selects exactly CORE_META_MODEL followed by LOCAL_CONFIGURATION, selects zero Installed Extensions, and selects no local Tool, MCP, or App mode. do not duplicate or mutate CORE_META_MODEL or immutable installed Extension authority. CA-P-107 owns the compiler algorithm and output.

## Task Scope Resolution

the Assignee used the completed CA-P-102 frozen frontier, CA-P-103 target topology, CA-P-112 Job reconciliation, CA-P-104 Core Meta-Model reconciliation, and CA-P-105 empty Installed Extensions reconciliation. `caprmedio_framework_settings.toml` and its resolved `CAPRMEDIO-I-001` binding identify CAPRMEDIO as the current Project. CA-P-105 established that CAPRMEDIO-specific authority remains Project Local Configuration; it is not an Installed Extension and no Extension package is created in this Task. [CA-P-106 Local Configuration reconciliation](../execution_evidence/CA-P-106-local-configuration-reconciliation.projection.json) records the exact selection and its verification.

## Completion Record

PASS. CA-R-1223 identifies CAPRMEDIO as the one current Project. CA-R-1224 selects CORE_META_MODEL followed by LOCAL_CONFIGURATION as the only Applicable Methodology source Layers. CA-R-1225 selects zero Installed Extensions, consistent with the CA-R-1221 empty Candidate Catalog. CA-R-1226 requires every future Project Customization to reference exactly one source revision without modifying it. CA-R-1227 selects no local Tool, MCP, or App mode. CA-R-1176@2 now describes the accepted two-source composition. No Core Meta-Model or Extension Carrier was modified, no Extension was activated, no final Carrier was moved, and no decision depends on compiled output. Every Definition-of-Done condition passes at 99 percent execution confidence.
