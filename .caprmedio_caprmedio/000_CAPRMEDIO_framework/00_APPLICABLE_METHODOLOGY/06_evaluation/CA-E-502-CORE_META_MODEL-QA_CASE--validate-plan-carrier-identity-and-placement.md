---
subjects:
  governs: "Atom/Content Role: Plan/Type: Plan/Carrier"
  depends_on:
    - "Atom/Content Role: Plan/Type: Plan"
    - "File Carrier"
    - "Directory Carrier"
    - "Atom/Revision/Authoritative Carrier Bundle"
    - "Atom/Identity"
    - "Atom/Summary"
    - "Atom/Content Role: Plan/Type: Plan/Work Sequence Number"
    - "Atom/Content Role: Plan/Type: Plan/Label"
    - "Atom/Content Role: Plan/Type: Plan/Status"
    - "Atom/Content Role: Plan/Type: Plan/Definition of Done"
version: 5
updated_at: "2026-09-30 19:57:34 +0000"
relations: {"evaluation_for": ["CA-D-460", "CA-D-461", "CA-D-469", "CA-D-470", "CA-D-472", "CA-D-475", "CA-R-1534", "CA-R-1599", "CA-R-997"]}
atom_id: "CA-E-502"
content_role: "Evaluation"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
type: "QA Case"
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/06_evaluation/CA-E-502-CORE_META_MODEL-QA_CASE--validate-plan-carrier-identity-and-placement.md
---
# Summary
Validate Plan Carrier identity **and** placement

## Scope
Plan Carrier identity **and** placement.

## Claim
the Plan Carrier Evaluation **must** reject Carrier facts that create duplicate identity **or** contradict the shared Plan model.

- accept a mandatory Markdown file **with** **or** **without** a matching optional Hub directory under `CA-D-460-CORE_META_MODEL-CORE-DELIVERY--serialize-plan-atom-carrier-bundles`; reject a directory **without** that file.
- count a matching pair once; reject two IDs, divergent stems, conflicting Status, a separate Epic identity, **or** an Objective file that claims **to** be another Atom for the same Hub.
- require DoD **in** **every** supplied Plan file, even **when** it carries a pure Hub **or** explicit overrides.
- validate leading navigation numbers **before** Atom IDs, their local uniqueness, mutable Label tokens, **and** canonical Summary slugs. changing a number **or** Label **must not** change identity **or** scheduling.
- read Plan Status from its own file **and** check its local placement; moving a Hub into `done` **must not** silently mark its decomposed Plans Done. reject an ungoverned cascade.
- accept root Backlog Plans **in** `03_plan/001_backlog`; reject `031_backlog` as the canonical new encoding **and** reject a `version-<VERSION>` directory substituted for a Version-labeled Plan identity.
- retain one identity **when** decomposed work is added, removed, **or** reordered; a changed Summary follows Atom replacement authority rather than independent filename editing.

report the invalid Carrier Bundle, source fact, **and** violated Delivery rule.

## Details
