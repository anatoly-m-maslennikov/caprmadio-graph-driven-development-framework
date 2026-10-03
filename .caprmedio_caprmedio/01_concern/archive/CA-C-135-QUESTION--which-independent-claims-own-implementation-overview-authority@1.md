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
version: 1
updated_at: "2026-09-17 13:42:35 +0000"
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
