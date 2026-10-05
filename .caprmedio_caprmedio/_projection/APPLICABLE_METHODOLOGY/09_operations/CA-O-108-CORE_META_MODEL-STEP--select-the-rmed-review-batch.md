---
atom_id: CA-O-108
content_role: Operations
type: Step
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 6
updated_at: "2026-10-03 16:23:03 +0400"
subjects:
  governs: "RMED Review Selection Step"
  depends_on:
    - "Step"
    - "Action"
    - "Step/Agentic Execution Context"
    - "Workflow Run"
    - "Step Run"
    - "Journal"
    - "Evaluation/Report"
relations: {"relates_to":["CA-O-105"]}
projection:
  source_carrier_path: ../../../000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/09_operations/RMED_ATOM_REVIEW/CA-O-108-CORE_META_MODEL-STEP--select-the-rmed-review-batch.md
  source_atom_id: CA-O-108
  source_atom_revision: 6
  source_sha256: 741aa7ecef3eb1c00d0e70e2d72d77f42416e7062b29b7fe31e4ebdbc55bbee6
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Select the RMED review batch

## Operation

RMED Review Selection Step **means** the Workflow node invoking **`=1`** Action, CA-O-105, **in** Integrated context.

- bind the active RMED request, carried source inventory, selection data, compact `atom_local` rule pack, **and** temporary output directory.
- carry the caller's Workflow name, Run ID, full report location, **and** shared Journal reference with the selected queue, including an empty **or** blocked result.
- record the original selected queue, source observations, **and** pending work **in** **`=1`** progress list.
- pass the full selection **and** shared rules **to** the caller for dispatch **in** the check phase; native file **and** session capabilities are sufficient.

## Details

the Step selects work **without** modifying source Atoms. it does **not** load global Entity **or** relation graphs for evaluation.
