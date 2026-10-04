---
subjects:
  governs: "Confidence Threshold/resolution"
  depends_on:
    - "Atom/Content Role: Plan/Type: Plan"
    - "Confidence Threshold"
    - "Operator"
    - "Hub Atom"
    - "Framework Instance Settings"
    - "Property"
    - "AI Agent"
version: 8
updated_at: "2026-09-29 22:34:37 +0000"
relations:
  child_of:
    - "CA-R-1428"
atom_id: "CA-M-271"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-271-CORE_META_MODEL-METHOD--resolve-confidence-thresholds-by-source-precedence.md
---
# Summary
Resolve confidence thresholds by source precedence

## Scope
resolution of a Confidence Threshold.

## Claim
**to** resolve an effective Confidence Threshold, select the first applicable explicit source **in** this precedence:

1. direct Operator input for the current decision context.
2. an explicit value on the current Plan.
3. the nearest Hub with an explicit value, walking `IS_DECOMPOSITION_OF` from nearest **to** farthest; read its own current Plan File Carrier under `CA-D-472-CORE_META_MODEL-DELIVERY--serialize-explicit-plan-confidence-overrides`, **not** a separate Objective targeting a folder.
4. the Framework Instance Settings default.

### resolution constraints

- an omitted optional override preserves inheritance; another explicit field does **not** stop lookup for the omitted field. a missing mandatory Plan file is invalid, **not** an inherited-setting selection.
- use current Plan Revisions, **not** historical Carrier copies **or** unrelated nearby files; a Label is **not** an override source.
- **if** a reached source is invalid **or** ambiguous, **or** no source supplies a value, request Operator disposition **before** the affected autonomous action; do **not** invent a value **or** silently fall through past invalid authority.
- direct Operator input applies **only** within its stated context.
- do **not** copy inherited values into Plan overrides. preserve an explicit selection even **when** it **`=`** the inherited value; a later upstream change **must not** overwrite it.
- this resolution **must not** create another Atom, settings file, **or** execution permission.

## Details
