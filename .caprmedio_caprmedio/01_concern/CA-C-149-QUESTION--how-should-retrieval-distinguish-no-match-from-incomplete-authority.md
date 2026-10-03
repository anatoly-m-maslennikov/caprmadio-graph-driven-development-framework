---
cce_version: cce_1
cce_form: concern_question
subjects:
  governs: "Applicable Methodology Retrieval"
  depends_on:
    - "Applicable Methodology"
    - "Atom/Subjects"
    - "Projection"
    - "Term"
priority: medium
version: 1
updated_at: "2026-09-17 14:56:53 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {}
---
# How should retrieval distinguish no match from incomplete authority?

what evidence distinguishes a legitimate empty Subject-query result from missing, stale, unresolved, **or** incomplete governing authority?

## Evidence

M-225 returns no Atom **when** no matching GOVERNS path exists. D-336 instead fails **when** an exact requested Atom ID has zero active matches. those are different query domains; neither rule supplies a complete Subject-query result-status model. the retrieval source is Applicable Methodology, whose membership **and** source completeness cannot be inferred from an empty matching set alone.

## Principle check

CA-M-002 requires reuse of the authoritative selection **and** source binding, **not** a second registry. CA-M-006 requires coherent failure reporting. CA-R-1490 prohibits silently losing required authority. these Principles do **not** establish whether a new query with no governed Term is valid, **or** which explicit evidence proves the source complete.

## Disposition

preserve both Claims. do **not** make **every** no-match query fail, treat an empty set as proof of complete authority, infer missing definitions, **or** relax exact-ID discovery. resolve the admitted query domains **and** completeness evidence **before** changing the Retriever contract. the Method-versus-Action extraction remains the separate boundary recorded by C-141.

## Inspected source Revisions

- `CA-M-225` Version 11: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-225-CORE_META_MODEL-METHOD--retrieve-applicable-methodology-mechanically.md`; SHA-256 `ec5c52afbdf27b5403441f81bae2702b13345f022c38d142d20e16bac1a44110`.
- `CA-D-336` Version 8: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/07_delivery/CA-D-336-CORE_META_MODEL-DELIVERY--resolve-active-atoms-from-canonical-carrier-identities.md`; SHA-256 `ed7b5d8d034ffaef1e630a7cdafb28e00773ff7c074154f064b7d2a6676ed98b`.
