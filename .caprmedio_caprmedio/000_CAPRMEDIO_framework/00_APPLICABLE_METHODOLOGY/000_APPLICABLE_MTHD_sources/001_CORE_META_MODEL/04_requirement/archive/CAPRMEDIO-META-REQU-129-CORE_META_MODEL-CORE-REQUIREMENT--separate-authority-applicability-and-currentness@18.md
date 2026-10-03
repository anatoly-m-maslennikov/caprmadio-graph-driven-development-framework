---
cce_version: cce_1
cce_form: separation
subjects:
  governs: "authority"
  depends_on: []
version: 18
updated_at: "2026-09-09 21:56:59 +0400"
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  child_of:
    - CA-M-001
---
# Separate authority applicability and currentness

Authority is an Artifact's governed capacity **to** establish meaning of a declared kind. Applicability determines whether that meaning governs a particular structural scope, selected capability, environment, version, time boundary, **or** other declared context. Currentness determines which exact applicable Artifact revision is presently effective **in** that context.

These properties are orthogonal. An authoritative Artifact **may** be inapplicable **to** a given context; an applicable historical revision **may** no longer be current; **and** a current Projection **may** accurately report state **without** possessing semantic authority. Acceptance, provenance, implementation, evidence, **and** evaluation do **not** silently establish authority, applicability, **or** currentness.

Precedence **and** conflict resolution select among **otherwise** authoritative **and** applicable claims; they do **not** merge these properties. the owning Requirement, Method, Evaluation, **and** Delivery Atoms govern how these properties are resolved **and** reported through derived views.
