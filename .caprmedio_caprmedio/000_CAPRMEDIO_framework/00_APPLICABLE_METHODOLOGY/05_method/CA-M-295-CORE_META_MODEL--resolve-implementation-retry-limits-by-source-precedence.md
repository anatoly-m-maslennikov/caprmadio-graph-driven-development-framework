---
version: 9
updated_at: "2026-09-28 15:12:22 +0400"
relations:
  child_of:
    - CA-R-1489
  depends_on:
    - CA-M-279
subjects:
  governs: "Implementation Retry Limit/resolution"
  depends_on:
    - "Atom/Content Role: Plan/Type: Plan"
    - "Implementation Retry Limit"
    - "Operator"
    - "Framework Instance Settings"
    - "Default Settings"
    - "Hub Atom"
    - "Atom/Content Role: Plan/Type: Plan/Decomposition"
    - "Atom/Content Role: Plan/Type: Plan/Carrier"
atom_id: "CA-M-295"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-295-CORE_META_MODEL--resolve-implementation-retry-limits-by-source-precedence.md
  source_atom_id: CA-M-295
  source_atom_revision: 9
  source_sha256: 2d3c0506dcedfda929c9f391340eca3afb829f93d5807bd1be5db924069ca81c
  original_relations_sha256: 0e568ddd932a6a9cb52688571f732567cbd704e78761e71bf6799c4a1827c540
---
# Summary

Resolve implementation retry limits by source precedence

## Scope

an effective Implementation Retry Limit resolved from direct Operator input, a Plan, the nearest Hub, Framework Instance Settings, **or** Default Settings.

## Claim

**to** resolve an effective Implementation Retry Limit, select the first applicable explicit source **in** this precedence:

1. direct Operator input for the current execution context.
2. the current Plan's explicit Implementation Retry Limit.
3. the nearest Hub with an explicit limit, walking `IS_DECOMPOSITION_OF` from nearest **to** farthest **and** reading its own current Plan File Carrier under CA-D-447-CORE_META_MODEL-DELIVERY--serialize-the-implementation-retry-limit-setting.
4. Framework Instance Settings, resolving an omitted instance parameter through Default Settings under CA-M-279-CORE_META_MODEL-GENERAL-METHOD--resolve-missing-framework-parameters-from-default-settings.

### resolution constraints

- an omitted optional retry override preserves inheritance; another explicit field does **not** stop this lookup. a missing mandatory Plan file is invalid, **not** an inherited-setting selection.
- determine presence, **not** truthiness: **`=0`** is an explicit limit.
- an invalid **or** ambiguous reached source requires Operator disposition **without** silent fallback; an absent effective value stops the affected retry decision.
- direct Operator input applies **only** within its stated context.
- do **not** copy inherited values **or** create separate Objective/settings files. retain explicit overrides even **when** equal **to** the inherited value.
- use the same Plan identity for a Hub's file **and** folder.
- resolution does **not** reset the consumed retry count governed by CA-O-024-CORE_META_MODEL-ACTION--control-implementation-retries.

## Details
