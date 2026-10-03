+++
artifact_subtype = "defect"
semantic_id = "CAPRMEDIO-SPEC-TOOLS-CONC-060--conflict-source-truth"
revision_mode = "atomic"
content_role = "observation"
governance_origin = "internal"
relation_shape = "standalone"
status = "accepted"
priority = "high"
authority = "repository:fpf-review"
claim = "Conflict resolution accepts caller-asserted authority facts that should be derived from repository truth."
version = 1
updated_at = "2026-08-17 19:36:01"
llm_session_ids = ["codex:019f591f-04f6-70f2-8de7-828b7cccc69d"]
rationale = "A caller must not be able to fabricate role, immutability, lifecycle, scope, priority, or precedence and thereby select a winner."
promotion = {}

[[relations]]
type = "relates_to"
target = "CAPRMEDIO-REQUIREMENT-GOV-020"
+++

# Defect — Conflict facts are caller-controlled

The conflict candidate currently carries role, immutability, externality,
scope, relation, and precedence assertions that the resolver can trust without
resolving both parties against canonical repository data.

## Completion condition

Both party IDs resolve before classification. The resolver derives available
role, lifecycle, scope, source/projection/replacement, priority, and registered
precedence facts from repository truth. Any irreducible concern or effective-
time assertion is evidence-bound and included in freshness.
