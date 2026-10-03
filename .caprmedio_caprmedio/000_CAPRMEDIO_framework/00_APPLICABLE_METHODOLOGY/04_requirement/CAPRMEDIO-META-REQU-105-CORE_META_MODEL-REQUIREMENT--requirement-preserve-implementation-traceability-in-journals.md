---
atom_id: CAPRMEDIO-META-REQU-105
cce_version: cce_1
cce_form: obligation
subjects:
  governs:
    continuant:
      - lifecycle-traceability
version: 7
updated_at: 2026-09-06 01:45:12 +0400
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-META-REQU-091-CORE_META_MODEL-CORE-REQUIREMENT--normative-atoms-are-the-caprmedio-specification
    - CAPRMEDIO-META-REQU-107-CORE_META_MODEL-CORE-REQUIREMENT--bind-traceability-to-exact-claims-and-revisions
    - CAPRMEDIO-META-REQU-158-CORE_META_MODEL-CORE-REQUIREMENT--make-journals-canonical-for-governed-provenance
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CAPRMEDIO-META-REQU-105-CORE_META_MODEL-REQUIREMENT--requirement-preserve-implementation-traceability-in-journals.md
---
# Requirement — Preserve implementation traceability in Journals

**every** structural scope that realizes normative Atoms maintains an append-only Implementation Journal. Its admitted records bind exact Requirement, Method, Evaluation, **and** Delivery Atom revisions to the native implementation targets that declare their realization.

The Journal is canonical for the declared implementation relationship. Native source, configuration, executable evaluation mechanisms, packages, **and** delivery automation remain canonical for the operative realization itself. Ops evidence **and** Verification remain the authorities for what occurred **and** whether the realization is sufficiently assured. Recording an implementation relationship never proves correctness **or** successful operation.

An implementation binding **must** survive ordinary Git history transformations such as squash merges, rebases, cherry-picks, **and** repository migration. The binding therefore identifies **every** source Atom by stable artifact identity plus revision digest **and** **every** native implementation target by a stable locator plus content digest. Git commits, pull requests, authors, sessions, **and** signatures remain useful provenance but are **not** the sole semantic identity of the binding.

Corrections, replacements, target removal, **and** changed implementation coverage append new records; accepted Journal records are never edited, reordered, **or** deleted. The effective implementation frontier is derived from the complete ordered record sequence.

Implementation-role Projections are regenerated from the Journal **and** its declared current source **and** target frontier. They **may** present implementation coverage, mappings, missing realization, **and** potentially stale bindings, but they remain rebuildable **and** non-authoritative over the Journal, normative Atoms, native implementation, **or** evaluation conclusions.

## Primary claim

**every** implementing scope preserves squash-resistant traceability from exact normative Atom revisions to native implementation targets **in** an append-only Implementation Journal **and** derives implementation Projections from that Journal.
