---
atom_id: CA-O-153
content_role: Operations
type: Step
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 2
updated_at: "2026-10-04 17:42:12 +0000"
subjects:
  governs: "Applicable Methodology Compilation/Step: assess"
  depends_on:
    - "Workflow"
    - "Step"
    - "Action"
    - "Workflow Run"
    - "Applicable Methodology"
    - "Assess Source Conflicts"
    - "Methodology Source/Expansion Boundary"
    - "Core Meta-Model"
    - "Atom"
    - "Applicable Methodology/Conflict"
    - "Applicable Methodology/Source Frontier Digest"
relations:
  relates_to: [CA-O-011, CA-O-005]
projection:
  source_carrier_path: ../../../000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/09_operations/APPLICABLE_METHODOLOGY_COMPILATION/CA-O-153-CORE_META_MODEL-STEP--assess-applicable-methodology-source-conflicts.md
  source_atom_id: CA-O-153
  source_atom_revision: 2
  source_sha256: 7135b2a6558ea556f3182b538e03cdadd759556d9f4b14546d18db6e3ca87d87
  original_relations_sha256: 9e53cce5969842350ce25539597bb1bfbc787ff9378d7f40487b722802818257
---
# Summary

Assess Applicable Methodology source conflicts

## Operation

this Step is the assess node **of** CA-O-011, Applicable Methodology Compilation, invoking **`=1`** Action, CA-O-005, Assess Source Conflicts.

### Inputs and parameters

bind the exact selected source frontier returned by CA-O-152 and the Workflow Run's applicable Core expansion-boundary and conflict authority.

check Core expansion-boundary conformance under CA-R-1375 **and** the applicable conflict authority, including CA-R-1373; detect **every** boundary violation, duplicate selected Atom identity, unresolved replacement, incompatible retained Candidate, **and** unresolved priority. retain conflicting source Atoms rather than silently discarding them. calculate one deterministic digest of the exact selected frontier **and** report the complete deterministic conflict set **before** changing Applicable Methodology membership.

### Agentic invocation binding

for an invocation whose actual bound Action is Agentic, bind **`=1`** Integrated **or** Isolated context under CA-R-1527 from the admitted invocation's supplied `agentic_execution_context` runtime parameter **before** dispatch. missing, ambiguous **or** unsupported values, **or** unavailable required context/capability, block that Agentic invocation; do **not** default **or** silently substitute. retain the selected context with the Step Run. a Programmatic invocation does **not** acquire an Agent context **or** require this parameter. this binding grants no additional authority **and** does **not** change the Action's identity **or** behavior.

## Details
