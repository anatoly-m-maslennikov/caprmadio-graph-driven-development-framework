---
subject_scope: relation-model
priority: high
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: child_of
    targets:
      - CAPRMEDIO-META-REQU-274--place-rationale-in-analysis
      - CAPRMEDIO-GOV-REQU-295--derive-locus-and-declare-endpoint-origins
      - CAPRMEDIO-GOV-REQU-324--register-rationale-analysis-subtype
---

# Requirement — Register the rationale_for relation

GOV registers the directed `rationale_for` relation from one Rationale Analysis Atom to one or more Requirement, Method, Evaluation, or Delivery Atoms whose selection it explains.

Only the Rationale Atom stores this relation. The inverse lookup from a specification Atom to applicable rationale is derived and must not be duplicated as a backlink in the specification carrier.

The relation conveys explanation, not authority, implementation, evaluation, evidence, precedence, replacement, or dependency. Archiving or replacing a Rationale Atom does not change the target specification unless a separate normative Atom changes it.

## Primary claim

`rationale_for` is the canonical one-way relation from optional Rationale Analysis to the specification Atoms it explains, with no stored inverse backlink.
