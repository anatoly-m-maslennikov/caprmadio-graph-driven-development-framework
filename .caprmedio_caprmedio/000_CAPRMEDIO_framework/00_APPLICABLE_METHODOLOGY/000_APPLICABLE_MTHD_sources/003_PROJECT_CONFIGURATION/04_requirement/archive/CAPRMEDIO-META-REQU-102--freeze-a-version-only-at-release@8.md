---
cce_version: cce_1
cce_form: obligation
subjects:
  governs:
    occurrent:
      - development-flow
version: 8
updated_at: 2026-08-29 09:18:56 +0400
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-META-REQU-114--preserve-content-role-boundaries-through-caprmedio-loop
---
# Requirement — Freeze a version only at release

A target version remains mutable **until** its configured release event succeeds. The event **may** be, for example, acceptance of a release pull request into the main branch, but **every** project declares its exact boundary.

Release creates one factual Ops Atom called the Release Record, whose primary claim is that the identified version was released with an exact manifest. The manifest binds the normative Atom revisions, realized implementation **and** delivery revisions, applicable evaluation **and** evidence, release identifier, **and** canonical Git commit **or** tag.

SEMANTICS owns the Release Record's freeze semantics. GOVERNANCE owns its concrete Type registration **and** carrier rules.

Planning allocation, implementation completion, pull-request creation, **or** release-candidate naming does **not** freeze the version **before** that event.

## Primary claim

A version freezes **only** **when** its configured release event creates an immutable, revision-bound Release Record with the Ops Content role **and** exact released manifest.
