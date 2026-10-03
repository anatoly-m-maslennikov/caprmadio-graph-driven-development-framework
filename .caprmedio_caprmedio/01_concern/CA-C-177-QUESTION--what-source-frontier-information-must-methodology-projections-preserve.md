---
cce_version: cce_1
cce_form: concern_question
subjects:
  governs: "Projection"
  depends_on:
    - "Methodology"
    - "Artifact/Revision"
    - "Journal"
priority: medium
version: 2
updated_at: "2026-09-17 19:50:53 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {}
---
# What source-frontier information must Methodology Projections preserve?

does METHODOLOGY-REQU-630 require faithful derivation from the selected source frontier, stored source-frontier provenance, **or** both for particular registered Projection jobs?

## Evidence

REQU-630 requires current, non-authoritative, mechanically reproducible Methodology Projections that preserve source identity, source frontier, **and** authored Relation meaning. R-1494 requires persisted dependency provenance **only** **when** the registered job needs it **and** rejects a blanket persisted source frontier. REQU-630 does **not** explicitly say persisted, so a storage conflict cannot be proved merely from the words source frontier. deleting the phrase could instead erase an intended completeness **or** reproducibility condition.

## Principle check

CA-M-002 rejects independent duplicate source authority; CA-M-005 requires necessary representation **only**; CA-M-006 requires faithful Projections **and** coherent provenance obligations; CA-R-1490 preserves the useful reproducibility condition. these separate derivation fidelity from storage but do **not** establish which representation this legacy Claim intended.

## Disposition

preserve REQU-630 until its frontier-preservation condition is stated unambiguously. apply R-1494's registered-job boundary **without** inventing universal stored metadata, a new Projection, **or** an output format. do **not** report this lexical ambiguity as proof of a persisted-provenance failure **or** as complete conformance.

## Inspected source Revisions

- `CAPRMEDIO-METHODOLOGY-REQU-630@11`: `.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/04_requirement/CAPRMEDIO-METHODOLOGY-REQU-630-FRAMEWORK_METHODOLOGY-CORE-REQUIREMENT--govern-current-non-authoritative-projections.md`; SHA-256 `92f21a2b1a9f1b4444b474492e8559f69c140ff36ce02881ea980024c6f6deb1`.
- `CA-R-1494@1`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1494-CORE_META_MODEL-GENERAL-REQUIREMENT--record-projection-dependency-provenance-only-when-required.md`; SHA-256 `feb801116ac608934f692020374e3c5e6a55511b5a110891d8bebf8c83459014`.
- `CA-M-002@15`: `.caprmedio_caprmedio/05_method/CA-M-002-PRINCIPLE-METHOD--dry-don-t-repeat-yourself.md`; SHA-256 `943be84418b6f865e85d172845892c58187917d22dad56bb6103c5ded7cc6834`.
- `CA-M-005@8`: `.caprmedio_caprmedio/05_method/CA-M-005-PRINCIPLE-METHOD--add-complexity-only-when-necessary.md`; SHA-256 `cd4f3ec4fa61d979997600fbcdb2e96865da694ba1f49fcd391232b72664fd1b`.
- `CA-M-006@8`: `.caprmedio_caprmedio/05_method/CA-M-006-PRINCIPLE-METHOD--keep-the-whole-project-coherent.md`; SHA-256 `f34990465205ac3e655d83b1e3b5dcd66c8c93d2e5287cedbcb9dd38a432bd1f`.
- `CA-R-1490@1`: `.caprmedio_caprmedio/04_requirement/CA-R-1490-PRINCIPLE-REQUIREMENT--preserve-valuable-information.md`; SHA-256 `af65fc105597d5966efaa59d663d452dfa7d0376ad9ebe7bb2b521077ccafb65`.

## Generic Projection Tool consumers

R-1061 **and** R-1062 require the literal `source_frontier` field for rebuilding **and** checking a generic Projection. unlike faithful derivation alone, this is explicit persisted metadata. R-1494 rejects a blanket stored frontier but retains admitted job-specific provenance; D-310 owns `updated_at` encoding **and** prohibits treating the timestamp alone as proof of currentness. determine which registered jobs require which provenance **and** where its Carrier is specified **before** removing useful currentness evidence **or** imposing a universal replacement schema.

R-1061 also combines a capability outcome, exact fields, atomic publication, **and** Journal recording. map those contributions losslessly **to** R/D/O authority. R-1062's separate Content Role error is corrected: a Projection has its admitted Projection Type, **not** an Atom Content Role. this correction does **not** certify the remaining frontier policy **or** authorize a rebuild.

## Additional inspected source Revisions

- `CA-R-1061@10`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/04_requirement/CA-R-1061-TOOLS-REQUIREMENT--rebuild-one-programmatic-projection.md`; SHA-256 `c3643eda4f8de616b3f3a1f6a0cb930a14e0f216651e832c5eba9586f159d302`.
- `CA-R-1062@12`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/04_requirement/CA-R-1062-TOOLS-REQUIREMENT--validate-projection-currentness.md`; SHA-256 `35133ee5ffa0fd28cbebc671fc855ff92ffed5bd7a1d446b2ec2edce928505a2`.
- `CA-R-1494@1`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1494-CORE_META_MODEL-GENERAL-REQUIREMENT--record-projection-dependency-provenance-only-when-required.md`; SHA-256 `feb801116ac608934f692020374e3c5e6a55511b5a110891d8bebf8c83459014`.
- `CA-D-310@8`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/07_delivery/CA-D-310-CORE_META_MODEL-DELIVERY--serialize-projection-updated-at.md`; SHA-256 `9e898f2ce639cb30459e65924ef9714c97113e57e4d9cdf65ec6c5485538a6b0`.
- `CA-R-1493@1`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1493-CORE_META_MODEL-GENERAL-REQUIREMENT--identify-how-each-projection-is-rebuilt.md`; SHA-256 `641de6dbf00981ed4e384f4fc770cb085829267729c53a346130da5c7230637d`.
- `CAPRMEDIO-META-REQU-657@15`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CAPRMEDIO-META-REQU-657-CORE_META_MODEL-CORE-REQUIREMENT--define-projection-artifact-form.md`; SHA-256 `c996dd4ef8fdf7a5c9e8fef82a2929c874015d6e4ffd9d8363ddb767027975ff`.
