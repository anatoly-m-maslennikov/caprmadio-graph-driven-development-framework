---
subject_scopes:
  - artifact-catalog
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  replacement_of:
    - CAPRMEDIO-GOV-REQU-434--release-plan-is-maintained-definition
  child_of:
    - CAPRMEDIO-META-REQU-102--freeze-a-version-only-at-release
---
# Register Release Record as an Ops subtype

GOV registers `release_record` as a direct subtype of the internal Ops Atom
Type.

A Release Record is emitted only by the project's configured successful release
event. It identifies the released version and binds an exact manifest of the
applicable normative Atom revisions, realized Implementation and Delivery
revisions, Evaluation and Ops records used for readiness, release identifier,
and canonical Git commit or tag.

Planning allocation, release-candidate naming, pull-request creation, or
implementation completion cannot emit a Release Record. A correction after
release requires another governed Atom; the released historical fact is not
rewritten.

## Rationale

The subtype gives the factual release boundary a precise carrier without
conflating mutable delivery planning, readiness judgment, or publication
mechanisms with the event that actually froze the version.
