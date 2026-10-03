---
subject_scopes:
  - interaction
version: 2
updated_at: 2026-08-21 00:21:06
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  replacement_of:
    - CAPRMEDIO-GOV-REQU-422--development-and-release-readiness-modes
  child_of:
    - CAPRMEDIO-META-REQU-094--mechanism-neutral-evaluation-atoms
    - CAPRMEDIO-META-REQU-102--freeze-a-version-only-at-release
---
# Separate development and release-readiness flows

Development is the default flow:

```text
active atomic authority
→ QA Cases
→ Implementation, including executable Tests and Evaluations
→ factual Ops records
→ development Verification
```

Development consumes active atomic authority plus any enabled current
Projections. It does not require every enabled Projection to refresh after
every new Atom unless that Projection's own gate requires currentness.

Release readiness is mandatory before a Version can be declared ready:

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

Conflict resolution never edits an accepted atom. Any applicable code,
configuration, Test, Evaluation, or Projection change after an evaluation
run makes the affected release evidence stale.

The Project Configuration Atom records `development` as the default workflow selection and `release_readiness` as the mandatory pre-release mode. Project Graph State Projections may expose the effective mode but cannot select it.

## Rationale

The successor removes retired compilation and Evergreen terminology while
preserving the different currentness needs of ordinary development and
release.
