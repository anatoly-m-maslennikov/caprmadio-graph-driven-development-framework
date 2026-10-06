---
subjects:
  governs: "AI Agent/authorization"
  depends_on:
    - "Atom/Revision/Author"
    - "Operator"
    - "AI Agent"
    - "AI Agent/Confidence"
    - "Atom/Content Role: Plan/Type: Plan/Autonomous Confidence Threshold"
    - "Spec"
    - "Atom"
    - "Atom/Content Role: Plan/Type: Plan"
    - "Atom/Content Role: Evaluation"
    - "Atom/Content Role: Requirement"
    - "Atom/Content Role: Method"
    - "Atom/Content Role: Delivery"
    - "Project"
    - "Implementation Workflow"
version: 5
updated_at: "2026-10-03 00:22:56 +0400"
relations: {"child_of":["CA-M-261"],"relates_to":["CA-R-1591","CA-R-1552","CA-R-1080","CA-M-262"]}
atom_id: "CA-R-1559"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 10
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1559-CORE_META_MODEL-GENERAL-REQUIREMENT--gate-governing-atom-changes-during-implementation.md
  source_atom_id: CA-R-1559
  source_atom_revision: 5
  source_sha256: 6b93c0d6ecdc0820018f9debc4f0b24b1d8f2e6794dc741c9f1c66b58c6952cd
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Gate governing Atom changes during implementation

## Scope

changes to governing RMED Atoms during implementation.

## Claim

authorization **to** change a governing RMED Atom during implementation **must** satisfy the following Actor policy:

- resolve the Atom's effective Author **before** the proposed change, its governing permissions, the effective Plan Autonomous Confidence Threshold under CA-R-1591, **and** **all** additional Operator rules.
- obtain Operator approval **before** changing an Operator-authored Atom.
- request Operator disposition **before** changing an AI-authored Atom **when** confidence is below the threshold **or** an additional rule requires approval.
- an AI-authored Atom **may** change autonomously **only** **when** confidence is at **or** above the threshold **and** **all** applicable permissions **and** Operator rules allow it.
- a prohibition remains a prohibition; authorship **or** confidence **must not** create permission.
- a missing **or** unresolved Author **must not** be treated as proof of AI authorship; apply the Author default under CA-R-1080.
- an authorized RMED change establishes a new baseline under CA-M-262, **and** the applicable work **and** Evaluations **must** be resolved again against it.

## Details
