---
subjects:
  governs: "Implementation Binding"
  depends_on:
    - "Work Journal"
    - "Scope Unit"
    - "Atom/Revision"
    - "Implementation"
    - "Projection"
    - "Verification"
version: 19
updated_at: "2026-10-03 02:10:09 +0400"
relations:
  child_of:
    - "CA-R-1682"
    - "CA-R-1697"
    - CA-R-1720
atom_id: "CA-R-1695"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
---
# Summary

Preserve Implementation traceability in the shared Project Journal

## Scope

structural Scope Units that realize RMED Atoms.

## Claim

**every** structural Scope Unit that realizes RMED Atoms **must** record its Implementation Bindings **in** the shared Project Work Journal. its admitted Records establish, replace, correct, **or** remove Implementation Bindings **and** bind exact Requirement, Method, Evaluation, **and** Delivery Atom Revisions **to** the native implementation targets that declare their realization.

the Journal is canonical for the declared implementation relationship. native source, configuration, executable evaluation mechanisms, packages, **and** delivery automation remain canonical for the operative realization itself. Operations evidence **and** Verification remain the authorities for what occurred **and** whether the realization is sufficiently assured. recording an implementation relationship never proves correctness **or** successful operation.

an Implementation Binding **must** survive transformations **or** migration of secondary storage history. the binding therefore identifies **every** source Atom by stable artifact identity plus revision digest **and** **every** native implementation target by a stable locator plus content digest. secondary storage records, review records, Authors, sessions, **and** signatures remain useful provenance but are **not** the sole semantic identity of the binding.

corrections, replacements, target removal, **and** changed implementation coverage append new records; accepted Journal records are never edited, reordered, **or** deleted. the effective implementation frontier is derived from the complete ordered record sequence.

Implementation-role Projections are regenerated from the Journal **and** its declared current source **and** target frontier. they **may** present implementation coverage, mappings, missing realization, **and** potentially stale bindings, but they remain rebuildable **and** non-authoritative over the Journal, normative Atoms, native implementation, **or** evaluation conclusions.

## Details

**every** implementing Scope Unit **must** preserve storage-independent traceability from exact normative Atom Revisions **to** native implementation targets **in** the shared Project Work Journal **and** derive Implementation Projections from that Journal.
