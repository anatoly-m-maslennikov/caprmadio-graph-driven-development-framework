---
cce_version: cce_1
cce_form: concern_question
subjects:
  governs: "Projection/Type: Implementation Overview"
  depends_on:
    - "Projection"
    - "Journal"
    - "Implementation Binding"
    - "Carrier"
    - "Framework Instance Settings"
priority: medium
version: 2
updated_at: "2026-09-17 15:27:02 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {}
---
# Which independent Claims own Implementation Overview authority?

which existing **or** replacement Claims separately own Implementation Overview classification, its required source coverage, **and** its concrete configuration **without** duplicating its definition?

## Evidence

GOV-REQU-322 **and** META-REQU-115 define substantially the same non-authoritative current implementation view. together they require coverage, bindings, provenance, gaps, Journal-derived implementation history, exact selected sources, **and** separation from authority **and** Verification. META-REQU-115 additionally says this view requires no internal Implementation Atom **and** admits governed reasoning as a rebuilding mechanism. GOV-REQU-322 also carries `project_graph_state.artifacts.enabled_types: [implementation_record]` **and** historical rationale. these are **not** interchangeable with the current Projection classification.

## Principle check

CA-M-002 rejects competing definitions; CA-M-006 requires source selection, classification, **and** actual configuration **to** agree; CA-R-1490 protects the additional constraints **and** history. R-1460 separates derivation from Carrier materialization, **and** R-1494 rejects blanket provenance retention unless required by the registered job. a merge that silently keeps the old enabled-Type token **or** an archival that discards the unique no-Implementation-Atom condition is **not** a proven repair.

## Disposition

preserve both sources pending a complete responsibility mapping. establish the surviving definition, source/authority boundaries, independently replaceable conditions, **and** ownership of the concrete enabled-Type selection **before** replacing the pair. do **not** invent a new Settings parameter, drop a unique obligation, **or** normalize the old token by guesswork.

## Related Carrier ambiguity

CA-D-397 still serializes the old Projection Type `implementation_record` as `irec`, alongside `catalog`, `map`, **and** `hub`. its Atom identity exception says class short names rather than the canonical Content Role components. the D-397 prefix claim **must** be reconciled with the surviving Implementation Overview definition **before** deleting the old prefix **or** treating it as a silently admitted alias. the source permits no inferred renaming of existing Projection Carriers.

- `CA-D-397` Version 7: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/07_delivery/CA-D-397-PROJECT_CONFIGURATION-DELIVERY--register-caprmedio-type-prefixes.md`; SHA-256 `533eaa4a1fc5c38a8b8dbccb9b021fd583f86b96163d6f60e023eec06bd601c3`.
- `CA-D-311` Version 7: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/07_delivery/CA-D-311-CORE_META_MODEL-CORE-DELIVERY--represent-authority-without-semantic-change.md`; SHA-256 `52f2ce6780e26c3594985ea05c18a73fb2cec238a8cdea14c3ed3e1d818f4133`.
