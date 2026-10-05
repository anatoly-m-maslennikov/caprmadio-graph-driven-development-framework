---
version: 8
updated_at: "2026-10-01 21:24:33 +0400"
relations: {"relates_to": ["CA-D-361", "CA-R-1488", "CA-R-1489", "CA-D-408", "CA-D-460", "CA-D-470", "CA-M-295"]}
subjects:
  governs: "Implementation Retry Limit/Carrier"
  depends_on:
    - "Framework Instance Settings"
    - "Default Settings"
    - "Implementation Retry Limit"
    - "Atom/Content Role: Plan/Type: Plan"
    - "Carrier"
atom_id: "CA-D-447"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/07_delivery/CA-D-447-CORE_META_MODEL-DELIVERY--serialize-the-implementation-retry-limit-setting.md
  source_atom_id: CA-D-447
  source_atom_revision: 8
  source_sha256: 6b39f117ff6b90a81b3553bbf97b183587fda4f8be55a5701c7c62fbe6785475
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Serialize the implementation retry-limit setting

## Scope

explicitly selected Implementation Retry Limits.

## Claim

an explicitly selected Implementation Retry Limit **must** use the integer field assigned **to** its owning source Carrier:

- Framework Instance Settings TOML: `implementation.retry_limit`.
- Default Settings TOML: the same field under CA-D-408-CORE_META_MODEL-DELIVERY--reuse-framework-parameter-fields-in-default-settings.
- a Plan Atom's own File Carrier frontmatter: `implementation_retry_limit`, including a Hub's mandatory Markdown File Carrier.

## Details

### inheritance and ownership

- allowed values follow CA-R-1488-CORE_META_MODEL-REQUIREMENT--define-implementation-retry-limit; the default value is owned **only** by Default Settings.
- omitted instance values resolve under CA-M-279-CORE_META_MODEL-GENERAL-METHOD--resolve-missing-framework-parameters-from-default-settings; omitted Plan fields inherit under CA-M-295-CORE_META_MODEL-METHOD--resolve-implementation-retry-limits-by-source-precedence@7 **without** copied values. preserve explicit **=0**.
- a Hub override belongs **to** that same Plan identity, **not** a separate Objective **or** settings file; do **not** use `epic_overrides`.
- **every** Plan has its own Markdown file **and** DoD under CA-D-460-CORE_META_MODEL-CORE-DELIVERY--serialize-plan-atom-carrier-bundles **and** CA-D-470-CORE_META_MODEL-DELIVERY--serialize-plan-file-sections; its existence does **not** require a selected retry override.
