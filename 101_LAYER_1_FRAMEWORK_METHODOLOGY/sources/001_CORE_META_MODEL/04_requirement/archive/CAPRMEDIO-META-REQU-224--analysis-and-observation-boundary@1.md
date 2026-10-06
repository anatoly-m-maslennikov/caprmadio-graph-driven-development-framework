---
subject_scope: artifact-model
priority: high
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: relates_to
    targets:
      - CAPRMEDIO-META-REQU-223--streamlined-content-role-cycle
---

# Requirement — Separate Analysis from factual Observation

Observation records what occurred, was measured, or was reported, with its
available provenance and context. Examples include logs, complaints, tickets,
errors, execution outputs, measurements, and externally received reports.

Observation does not explain causes, justify a choice, synthesize implications,
or prescribe a desired state or method.

Analysis interprets Inquiries, Observations, Definitions, Methods, or
Implementations. It may compare alternatives, investigate causes, synthesize
findings, explain implications, and provide rationale for a Definition or
Method.

When one carrier mixes factual input with interpretation, the factual
Observation and interpretive Analysis are separate governed artifacts linked
by explicit relations.

## Rationale

Separating reported or measured facts from interpretation preserves evidence
provenance and makes later reasoning reviewable without rewriting the original
Observation.
