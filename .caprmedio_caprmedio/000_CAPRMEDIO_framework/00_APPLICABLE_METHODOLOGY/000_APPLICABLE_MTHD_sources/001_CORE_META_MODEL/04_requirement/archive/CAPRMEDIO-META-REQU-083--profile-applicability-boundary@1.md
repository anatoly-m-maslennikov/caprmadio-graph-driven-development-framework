---
subject_scopes:
  - scope-topology
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-META-REQU-088--meta-eligibility-rule
    - CAPRMEDIO-META-REQU-129--separate-authority-applicability-and-currentness
---
# Requirement — Bound profiles and applicability

A Profile is a reusable Method specialization for a declared scope. It may
select applicable tools, thresholds, durability behavior, language rules,
artifact governance, proof, or operational mechanisms. Once selected, its
applicable rules become part of the Method portion of the full current
Specification.

A profile must not:

- weaken or redefine a META invariant;
- change the meaning of a routing axis or layer;
- infer applicability from convenience alone; or
- require dummy artifacts for non-applicable concerns.

Non-applicability is explicit and reasoned. Project settings select allowed
profiles and routes but do not become a second source for their meanings.

## Primary claim

Profiles specialize Method and applicability without weakening META invariants,
redefining routing semantics, or requiring placeholder artifacts for
non-applicable concerns.
