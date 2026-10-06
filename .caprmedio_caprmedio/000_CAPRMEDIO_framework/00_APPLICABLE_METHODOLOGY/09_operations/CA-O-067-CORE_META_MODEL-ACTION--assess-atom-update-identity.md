---
subjects:
  governs: "Assess Atom Update Identity"
  depends_on:
    - "Action"
    - "Atom"
    - "Atom/Summary"
    - "Atom/Claim"
    - "Atom Change Classification"
    - "Artifact/Revision"
    - "Workflow"
    - "Workflow Run"
    - "Operator"
version: 6
updated_at: "2026-10-04 15:11:59 +0000"
relations: {"relates_to": ["CA-R-1432", "CA-R-1464", "CA-M-303", "CA-R-1520"]}
atom_id: "CA-O-067"
content_role: "Operations"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
type: "Action"
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/09_operations/CA-O-067-CORE_META_MODEL-ACTION--assess-atom-update-identity.md
  source_atom_id: CA-O-067
  source_atom_revision: 6
  source_sha256: 4e121c05c1749b3af447632798c3f4c939bf42302f5a3420a4e27ccc9ad71be6
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Assess Atom update identity

## Operation

Assess Atom Update Identity **means** the reusable read-only Action that compares an existing Atom with its proposed result **and** returns whether the requested update preserves its identity under CA-R-1432 **and** CA-R-1464.

### Inputs

- the exact existing Atom Revision **and** the proposed Claim, properties, **and** Summary.
- applicable change authority **and** relevant evidence for this assessment.

### Outcomes

| Condition | Returned result |
|---|---|
| the applicable change class preserves identity | the admitted change class, proposed result, **and** assessment evidence; `carrier_only` **and** equivalent `refinement` retain the target Version while refreshing Updated At, while `semantic_revision` returns the next target Revision; no presumed authorization **or** persistence |
| replacement is required, including **any** change of Summary value | replacement required, with the target Revision, proposed result, classification reason, **and** assessment evidence |
| evidence **or** classification is uncertain | unresolved, with the missing evidence **or** required Operator decision; no presumed update **or** replacement approval |

the result describes **only** the supplied proposal against the identified target Revision. it does **not** remain sufficient **when** that proposal, Revision, **or** relevant evidence changes.

this Action **must not** select a continuation Workflow, end its caller's Run, schedule another Run, authorize a mutation, **or** persist **any** change. the calling Workflow declares its routing under CA-M-303 **and** supplies its own performed-effect account **when** preparing a handoff under CA-R-1520.

## Details
