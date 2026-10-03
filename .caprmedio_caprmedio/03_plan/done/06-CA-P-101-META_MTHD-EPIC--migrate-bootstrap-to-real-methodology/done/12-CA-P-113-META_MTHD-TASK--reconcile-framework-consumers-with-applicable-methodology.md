---
atom_id: CA-P-113
cce_version: cce_1
cce_form: obligation
subjects:
  governs:
    continuant:
      - CAPRMEDIO Framework Consumer
    occurrent:
      - Framework Consumer Reconciliation
  depends_on:
    occurrent:
      - CA-P-110
version: 2
updated_at: 2026-08-27 21:45:57 +0400
autonomous_confidence_threshold: 99
relations: {}
---
# Reconcile Framework Consumers with Applicable Methodology

**when** CA-P-110 is Done, **then** the Assignee **must** make every in-scope Framework consumer use the final ownership roots and generated Applicable Methodology Atom Carriers.

## Scope

`((the generated Applicable Methodology RMEDO Atom Carriers) union (the current Framework and Project settings, discovery, resolution, validation, Projection, Tool, MCP, App, and Skill consumers that reference a pre-migration authority root or Applicable Methodology) union (the minimum governed retrieval Tool and its RMED authority and Evaluations) union (representative Subject and Process retrieval cases))`

## Definition of Done

the Task is **not done if** (any current in-scope consumer reads governing authority from `.caprmedio`, `.caprmedio_install`, or `.caprmedio_runtime` **or** any current in-scope consumer uses `.caprmedio_project` instead of `.caprmedio_<project_name>` **or** Framework authority is read outside `.caprmedio_framework` **or** CAPRMEDIO Project authority is read outside `.caprmedio_caprmedio` **or** the durable running Engine installation is treated as authority instead of `.caprmedio_install` **or** ephemeral state is stored outside `.caprmedio_runtime` **or** mapped `.caprmedio` Bootstrap history or evidence is treated as governing authority **or** a generated Applicable Methodology Atom Carrier is treated as editable authority **or** subject- or process-scoped retrieval does not seed matching `subjects.governs` Subject Paths and close prerequisites transitively through `subjects.depends_on` **or** retrieval does not preserve generated compilation order and exact Source Carrier provenance **or** retrieval stores a persistent Subject Index Carrier **or** a conflict is resolved or Source authority is changed without exact Operator approval **or** a representative Subject or Process request cannot retrieve complete applicable authority from its exact Source frontier **or** deleting a derived cache prevents complete regeneration).

## Details

use `.caprmedio_framework` for Framework authority and methodology, `.caprmedio_caprmedio` as this Project's instance of the generic `.caprmedio_<project_name>` governed carrier root, `.caprmedio_install` for the durable running FRAMEWORK_ENGINE installation, and `.caprmedio_runtime` for logs, caches, processes, locks, and temporary state. retain `.caprmedio` only as mapped Bootstrap history, Plans, evidence, and structure. reconcile only current live consumers that actually reference a pre-migration authority root or methodology. derive Subject indexes in memory from generated projected current RMEDO Atom Carriers and their relative `projection.source_carrier_path` values; do not create a monolithic methodology JSON or persistent Subject Index Carrier. record exact mechanical retrieval failures and stop for Operator authority instead of inserting hidden inference or changing Source authority.
