+++
artifact_subtype = "defect"
semantic_id = "CAPRMEDIO-SPEC-TOOLS-CONC-057--atomic-replacement-source"
revision_mode = "atomic"
content_role = "observation"
governance_origin = "internal"
relation_shape = "standalone"
status = "accepted"
priority = "high"
authority = "repository:self-host-review"
claim = "The relation validator rejects replacement_of from immutable QA atoms even though replacement is defined for every atomic successor."
promotion = {}
version = 1
updated_at = "2026-08-17 19:36:01"
llm_session_ids = ["codex:019f591f-04f6-70f2-8de7-828b7cccc69d"]
rationale = "The first QA successor authored under the typed-relation contract exposed a source restriction narrower than the governing definition."

[[relations]]
type = "relates_to"
target = "CAPRMEDIO-GOV-METH-023--typed-artifact-relations"
+++

# Defect — Atomic replacement rejects QA successors

`replacement_of` is defined as complete replacement by a new immutable atomic
artifact, but source validation currently permits only Decision atoms. A Test
or Evaluation therefore cannot replace its earlier definition even with a
matching append-only absorption event.

## Completion condition

Every semantic atom may originate `replacement_of`; non-atomic documents
remain invalid; matching absorption, cycle, and structural-exclusivity gates
remain unchanged.

## Rationale

Replacement is a lifecycle relation, not an authority grant. Restricting it to
Decisions prevents immutable QA correction and contradicts the canonical
relation definition.
