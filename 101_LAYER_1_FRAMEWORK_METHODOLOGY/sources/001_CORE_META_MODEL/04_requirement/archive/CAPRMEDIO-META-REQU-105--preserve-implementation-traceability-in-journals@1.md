---
subject_scopes:
  - lifecycle-traceability
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-META-REQU-091--normative-atoms-are-the-caprmedio-specification
    - CAPRMEDIO-META-REQU-107--bind-traceability-to-exact-claims-and-revisions
    - CAPRMEDIO-META-REQU-158--make-journals-canonical-for-governed-provenance
---
# Requirement — Preserve implementation traceability in Journals

Every structural scope that realizes normative Atoms maintains an append-only Implementation Journal. Its admitted records bind exact Requirement, Method, Evaluation, and Delivery Atom revisions to the native implementation targets that declare their realization.

The Journal is canonical for the declared implementation relationship. Native source, configuration, executable evaluation mechanisms, packages, and delivery automation remain canonical for the operative realization itself. Ops evidence and Verification remain the authorities for what occurred and whether the realization is sufficiently assured. Recording an implementation relationship never proves correctness or successful operation.

An implementation binding must survive ordinary Git history transformations such as squash merges, rebases, cherry-picks, and repository migration. The binding therefore identifies each source Atom by stable artifact identity plus revision digest and each native implementation target by a stable locator plus content digest. Git commits, pull requests, authors, sessions, and signatures remain useful provenance but are not the sole semantic identity of the binding.

Corrections, replacements, target removal, and changed implementation coverage append new records; accepted Journal records are never edited, reordered, or deleted. The effective implementation frontier is derived from the complete ordered record sequence.

Implementation-role Projections are regenerated from the Journal and its declared current source and target frontier. They may present implementation coverage, mappings, missing realization, and potentially stale bindings, but they remain rebuildable and non-authoritative over the Journal, normative Atoms, native implementation, or evaluation conclusions.

## Primary claim

Each implementing scope preserves squash-resistant traceability from exact normative Atom revisions to native implementation targets in an append-only Implementation Journal and derives implementation Projections from that Journal.
