---
subject_scopes:
  - provenance
version: 4
updated_at: 2026-08-22 02:12:36
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
  - codex:01a01cb6-4ee4-7553-b68d-0823dda35094
relations:
  child_of:
    - CAPRMEDIO-META-REQU-105--preserve-implementation-traceability-in-journals
    - CA-R-888
  relates_to:
    - CAPRMEDIO-GOV-REQU-306--job-based-carrier-policy
    - CAPRMEDIO-GOV-REQU-313--govern-catalog-map-and-hub-projections
    - CAPRMEDIO-GOV-REQU-338--register-the-project-work-journal
---
# Register Implementation Journals and derived Projections

GOVERNANCE registers `implementation_journal` as an internal Journal Type with the semantic coordinate `journal × implementation × internal` and the four-character identity prefix `ijrn`.

Every structural scope that realizes Requirement, Method, Evaluation, or Delivery Atoms owns one logical Implementation Journal under its `08_implementation/` role folder. The Journal uses append-only NDJSON and may rotate into ordered carrier segments without changing its logical identity or rewriting admitted records.

Each record identifies:

- its stable record identity, sequence position, and recording time;
- whether it establishes, replaces or corrects, or removes an implementation binding;
- every identified source Atom by `atom_id` and exact Carrier-content digest;
- every native implementation target by target kind, stable repository-relative locator, and content digest;
- the earlier record it replaces, corrects, or removes when applicable; and
- available Git commit, pull request, author, signer, and LLM-session provenance without requiring those values to remain the binding's semantic identity.

A record may bind Requirement, Method, Evaluation, and Delivery sources together when one bounded implementation change realizes them in one structural scope. It must not claim that the targets pass their Evaluation criteria, were successfully delivered, or produced an observed result.

The effective implementation frontier is derived by replaying the complete ordered Journal. A deterministic CAPRMEDIO tool regenerates Implementation-role Catalog, Map, Hub, coverage, and dashboard Projections from that frontier plus the declared current Atom and native-target frontier. Each generated Projection records the exact Journal frontier it consumed and is replaced by regeneration rather than direct semantic editing.

The Projections may show implemented, missing, removed, and potentially stale relationships, scope summaries, coverage counts, and navigation to native targets. They do not replace the Journal, normative Atoms, native implementation, Ops evidence, or Verification.

## Rationale

One scoped Journal preserves implementation lineage across squash merges and other Git graph transformations, while deterministic Projections provide fast current views without becoming another writable traceability authority.
