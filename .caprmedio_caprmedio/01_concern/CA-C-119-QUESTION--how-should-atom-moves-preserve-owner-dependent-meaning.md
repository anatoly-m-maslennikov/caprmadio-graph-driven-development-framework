---
cce_version: cce_1
cce_form: concern_question
subjects:
  governs: "Atom/Scope"
  depends_on:
    - "Atom"
    - "Atom/Claim"
    - "Atom/Revision"
    - "Artifact/Carrier"
    - "Scope Unit"
    - "Relation"
priority: medium
version: 1
updated_at: "2026-09-17 03:02:47 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {}
---
# How should Atom moves preserve owner-dependent meaning?

how should ATOM_MOVE handle an authorized destination that changes an Atom's owning Scope Unit **and** therefore can change omitted Claim Scope Unit **or** relative-reference resolution, while current Tool authority promises byte-identical relocation?

## Evidence

- CA-R-867, CA-M-187, **and** CA-E-305 require unchanged bytes **and** filenames across relocation. CA-D-283 instead encodes the current owner **in** the filename; stable Atom ID does **not** imply a stable mutable filename suffix.
- CA-R-1433 permits Version preservation **only** **when** identity, Claim, both scope meanings, **and** direct semantic Relations are preserved under CA-D-304. CA-R-886 resolves relative Scope Unit references from the owning Scope Unit.
- the latest Operator rule restricts explicit Claim Scope Unit **to** Goal **and** Demand; CA-C-118 records the remaining targeting conflict. an ordinary Atom cannot automatically acquire that Property merely **to** freeze its former applicability.
- CA-D-421 binds the existing move capability. the original audit also identifies the CA-M-187 procedure as Operations; moving it **to** O alone would leave the semantic relocation conflict intact.

## Principle check

CA-M-002 requires canonical identity **and** representation reuse; CA-M-006 requires coherent scope **and** reference meaning; CA-R-1490 preserves valuable content. these justify rejecting unconditional filename preservation but do **not** choose whether a cross-owner request intentionally retargets its Claim, preserves applicability through another admitted representation, **or** needs an explicitly separate semantic migration. the absent authoritative Project Structure **in** CA-C-117 also prevents certifying actual ownership from folder names alone.

## Disposition

preserve the current move capability **and** its exact conflicting evidence. defer the unresolved semantic choice under the Operator's uncertainty policy; do **not** silently narrow ATOM_MOVE **to** same-owner cases, invent a new Claim Property, **or** accept changed meaning as formatting. a later gap-free correction must align R-867, the replacement O Action for M-187, E-305, D-421, filename authority, Revision handling, **and** the affected reference-resolution rules.
