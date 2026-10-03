---
cce_version: cce_1
cce_form: concern_question
subjects:
  governs: "Atom/Revision"
  depends_on:
    - "Atom/Identifier"
    - "Atom/Status"
    - "Artifact/Carrier"
    - "Journal"
priority: medium
version: 1
updated_at: "2026-09-17 14:38:57 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {}
---
# How should Draft Revisions retain lineage without an assigned ID?

how is an unnumbered Draft Revision associated with its already admitted Atom **when** it is proposed as that Atom's next Revision?

## Evidence

D-288 explicitly forbids an assigned Atom ID **in** a Draft filename; D-446 requires an identity-plus-Version Identifier **only** for non-Draft Revisions. the Operator also described an active current Revision, archived prior Revisions, **and** a Draft next Revision. R-366 binds exact Revision references with identity, Version, **and** Updated At. the inspected rules do **not** identify the exact admitted Carrier **or** Journal binding that distinguishes a new independent Draft from a proposed next Revision **without** restoring its forbidden Draft ID.

## Principle check

CA-M-002 requires one identity source; CA-M-006 requires Draft Carriers **and** Revision references **to** agree; CA-R-1490 protects predecessor **and** proposed-successor association. the explicit no-ID Draft decision remains authoritative. it does **not** permit a guessed filename convention, inferred lineage from matching Summary text, **or** an unregistered hidden identity field.

## Disposition

preserve D-288 **and** the non-Draft exception **in** D-446. resolve the exact Draft lineage mechanism **before** modifying their Carriers **or** declaring same-Atom next-Revision support complete. do **not** assign Draft IDs, collapse matching Drafts, invent a second identifier, **or** rewrite historical associations during this repair.
