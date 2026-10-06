---
atom_id: CAPRMEDIO-GOV-REQU-296
cce_version: cce_1
cce_form: separation
subjects:
  governs:
    continuant:
      - provenance
version: 9
updated_at: 2026-09-07 09:59:57 +0000
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CA-R-1054
---
# Distinguish internal and external Git commits

An internal project commit uses artifact type `git_commit` **and** derives the route `atomic / implementation / internal`.

An outside-owned commit governed as an external input uses artifact type `external_git_commit` **and** derives the route `atomic / implementation / external`.

the two Types use the repository-qualified native commit SHA as identity rather than a CAPRMEDIO artifact sequence. Precise repository, author, signer, **and** source facts remain provenance. They do **not** replace the type-derived Governance locus.

## Rationale

Distinct names preserve the one-type-to-one-route invariant while retaining the native identity **and** provenance required to trace internal **and** outside-owned implementation records.
