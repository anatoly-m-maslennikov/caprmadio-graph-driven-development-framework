---
atom_id: CAPRMEDIO-META-REQU-105
cce_version: cce_1
cce_form: obligation
subjects:
  governs: "Implementation Binding"
  depends_on:
    - "Work Journal"
    - "Scope Unit"
    - "Atom/Revision"
    - "Implementation"
    - "Projection"
    - "Verification"
version: 12
updated_at: 2026-09-15 05:51:38
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  child_of:
    - CAPRMEDIO-META-REQU-091-CORE_META_MODEL-CORE-REQUIREMENT--normative-atoms-are-the-caprmedio-specification
    - CAPRMEDIO-META-REQU-107-CORE_META_MODEL-CORE-REQUIREMENT--bind-traceability-to-exact-claims-and-revisions
    - CAPRMEDIO-META-REQU-158
---
# Preserve Implementation traceability in the shared Project Journal

**every** structural Scope Unit that realizes RMED Atoms **must** record its Implementation Bindings **in** the shared Project Work Journal. its admitted Records establish, replace, correct, **or** remove Implementation Bindings **and** bind exact Requirement, Method, Evaluation, **and** Delivery Atom Revisions **to** the native implementation targets that declare their realization.

the Journal is canonical for the declared implementation relationship. Native source, configuration, executable evaluation mechanisms, packages, **and** delivery automation remain canonical for the operative realization itself. Operations evidence **and** Verification remain the authorities for what occurred **and** whether the realization is sufficiently assured. Recording an implementation relationship never proves correctness **or** successful operation.

an Implementation Binding **must** survive transformations **or** migration of secondary storage history. the binding therefore identifies **every** source Atom by stable artifact identity plus revision digest **and** **every** native implementation target by a stable locator plus content digest. secondary storage records, review records, Authors, sessions, **and** signatures remain useful provenance but are **not** the sole semantic identity of the binding.

corrections, replacements, target removal, **and** changed implementation coverage append new records; accepted Journal records are never edited, reordered, **or** deleted. the effective implementation frontier is derived from the complete ordered record sequence.

Implementation-role Projections are regenerated from the Journal **and** its declared current source **and** target frontier. they **may** present implementation coverage, mappings, missing realization, **and** potentially stale bindings, but they remain rebuildable **and** non-authoritative over the Journal, normative Atoms, native implementation, **or** evaluation conclusions.

## Primary claim

**every** implementing Scope Unit **must** preserve storage-independent traceability from exact normative Atom Revisions **to** native implementation targets **in** the shared Project Work Journal **and** derive Implementation Projections from that Journal.
