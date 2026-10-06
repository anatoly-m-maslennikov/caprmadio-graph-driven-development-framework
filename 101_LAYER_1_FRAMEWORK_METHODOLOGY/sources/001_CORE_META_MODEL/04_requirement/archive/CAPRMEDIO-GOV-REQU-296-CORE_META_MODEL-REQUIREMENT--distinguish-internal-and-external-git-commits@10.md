---
atom_id: CAPRMEDIO-GOV-REQU-296
cce_version: cce_1
cce_form: separation
subjects:
  governs:
    continuant:
      - "Atom/Content Role: Implementation/Type"
  depends_on:
    continuant:
      - "Atom/Identity"
      - "Governance Origin"
      - "Provenance"
version: 10
updated_at: "2026-09-10 20:54:28 +0400"
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CA-R-1054
---
# Distinguish internal and external Git commits

an internal project commit uses Type Git Commit **and** derives the route `atomic / implementation / internal`.

an outside-owned commit governed as an external input uses Type External Git Commit **and** derives the route `atomic / implementation / external`.

the two Types use the repository-qualified native commit SHA as identity rather than a CAPRMEDIO artifact sequence. precise repository, author, signer, **and** source facts remain provenance. they do **not** replace the type-derived Governance locus.

## Rationale

distinct names preserve the one-type-to-one-route invariant while retaining the native identity **and** provenance required **to** trace internal **and** outside-owned implementation records.
