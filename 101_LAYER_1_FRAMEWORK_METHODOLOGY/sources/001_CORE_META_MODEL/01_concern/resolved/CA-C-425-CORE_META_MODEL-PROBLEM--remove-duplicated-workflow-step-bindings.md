---
atom_id: CA-C-425
content_role: Concern
type: Problem
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
status: resolved
subjects:
  governs: "Workflow/Step binding ownership"
  depends_on: [Workflow, Step, Action]
version: 2
updated_at: "2026-10-04 17:44:00 +0000"
relations:
  concern_about: [CA-O-010, CA-O-011, CA-O-015, CA-P-1465]
---
# Summary

Remove duplicated Workflow Step bindings

## Concern

O010 v8, O011 v11 and O015 v7 independently repeat canonical Step-owned Action references and invocation parameters/input bindings in their Workflow graph Carriers. This violates `CA-R-1570-CORE_META_MODEL-GENERAL-REQUIREMENT--keep-workflow-graphs-separate-from-step-bindings` v4 and risks two competing invocation-binding authorities. Graph preservation alone does **not** establish this ownership conformance.

## Evidences

- Independent P1457 v1 F1 identified O010 v8's duplicated Action/Parameters/inputs declarations. P1465's full current reads found the same bounded issue in O011 v11's shared-Action node/transition columns and O015 v7's Action/Parameters/inputs node table.
- R1570 v4 assigns the graph scheme, entry, Step references, typed Relations, conditions and terminal outcomes to the Workflow; referenced Step Atoms exclusively own Action references, parameters and input bindings.
- P1465 binds only the three current source files and their complete verbatim predecessor snapshots. The repair removes repeated per-Step binding columns and Action labels from the graph, retaining each graph's six Step identities and all16/16/13 transitions/guards/outcomes. Saved successor Versions are O010 v9, O011 v12 and O015 v8 at 2026-10-04 17:31:25 UTC; the exact original v8/v11/v7 snapshots remain under their respective archive filenames.
- Canonical Step sources are not changed; their independent review remains separate. This Concern stays Active pending independent review of the three amended Workflows and root's disposition. The authoring save is **not** clean source acceptance, runtime proof or permission to redesign the model.

## Blast radius

### Disposition

Independent P1469 accepted O010v9/O011v12/O015v8 after P1465's repair. All eighteen Step endpoints and forty-five transition conditions/destinations/guards are preserved; repeated Step-owned Action/input bindings were removed. This graph-ownership defect is resolved. Agentic invocation context has separate C426 and is not accepted by this disposition.

The directly affected Core Workflows are generic Source Reconciliation, Applicable Methodology Compilation and Project Structure Maintenance. Their canonical Step/Action authority remains existing, their Summary/identity remains fixed and their graph behavior is preserved. P1465 owns this bounded repair; P1132 and downstream P1158/P1160 remain gated on independent amended-source review. No Action/Step/code, Project Structure, settings, Journal or Git change is authorized by this Concern.
