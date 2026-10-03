---
atom_id: CAPRMEDIO-GOV-REQU-301
cce_version: cce_1
cce_form: separation
subjects:
  governs:
    occurrent:
      - interaction
version: 11
updated_at: 2026-09-06 01:45:12 +0400
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  replacement_of:
    - CAPRMEDIO-GOV-REQU-422--development-and-release-readiness-modes
  child_of:
    - CAPRMEDIO-META-REQU-094-CORE_META_MODEL-REQUIREMENT--requirement-keep-evaluation-atoms-mechanism-neutral-and-chains-distinct
    - CAPRMEDIO-META-REQU-102--freeze-a-version-only-at-release
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CAPRMEDIO-GOV-REQU-301-CORE_META_MODEL-REQUIREMENT--separate-development-and-release-readiness-flows.md
---
# Separate development and release-readiness flows

development is the default flow:

```text
active atomic authority
→ QA Cases
→ Implementation, including executable Tests and Evaluations
→ factual Ops records
→ development Verification
```

development consumes active atomic authority plus **any** enabled current Projections. it does **not** require **every** enabled Projection to refresh **after** **every** new Atom **unless** that Projection's own gate requires currentness.

release readiness is mandatory **before** a Version can be declared ready:

```text
all active atomic authority
→ optional atomic refactoring when overlap warrants it
→ refresh every required Projection
→ detect conflicts
→ resolve conflicts through new atomic authority
→ repeat to a fixed point
→ reconcile implementation and evaluation
→ execute Tests and Evaluations at the exact candidate head
→ fresh Ops records and Verification
→ accepted readiness Verification Record
```

conflict resolution never edits an accepted Atom. **any** applicable code, configuration, Test, Evaluation, **or** Projection change **after** an Evaluation run makes the affected release evidence stale.

the Framework Instance Settings Artifact records `development` as the default workflow selection **and** `release_readiness` as the mandatory pre-release mode. the Project Scope Unit Graph Projections **may** expose the effective mode but **must not** select it.

## Rationale

the successor removes retired compilation **and** Evergreen terminology while preserving the different currentness needs of ordinary development **and** release.
