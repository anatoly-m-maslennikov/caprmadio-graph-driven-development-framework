---
cce_version: cce_1
cce_form: separation
subjects:
  declared:
    continuant:
      - authority
tier: core
version: 9
updated_at: 2026-08-23 15:00:38
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CA-M-001-PRINCIPLE-METHOD--mece_mutually-exclusive-collectively-exhaustive
---
# Separate authority applicability and currentness

Authority is an Artifact's governed capacity to establish meaning of a declared kind. Applicability determines whether that meaning governs a particular structural scope, selected capability, environment, version, time boundary, or other declared context. Currentness determines which exact applicable Artifact revision is presently effective in that context.

These properties are orthogonal. An authoritative Artifact MAY be inapplicable to a given context; an applicable historical revision MAY no longer be current; and a current Projection MAY accurately report state without possessing semantic authority. Acceptance, provenance, implementation, evidence, and evaluation do not silently establish authority, applicability, or currentness.

Precedence and conflict resolution select among otherwise authoritative and applicable claims; they do not merge these properties. GOVERNANCE owns the concrete rules and generated views used to resolve and report them.
