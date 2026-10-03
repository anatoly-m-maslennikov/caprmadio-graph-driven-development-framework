+++
artifact_subtype = "defect"
semantic_id = "CAPRMEDIO-SPEC-TOOLS-CONC-059--relation-bound-health"
revision_mode = "atomic"
content_role = "observation"
governance_origin = "internal"
relation_shape = "standalone"
status = "accepted"
priority = "high"
authority = "repository:fpf-review"
claim = "Project-health coverage can false-pass when an artifact ID is merely mentioned in prose instead of connected by a validated relation."
version = 1
updated_at = "2026-08-17 19:36:01"
llm_session_ids = ["codex:019f591f-04f6-70f2-8de7-828b7cccc69d"]
rationale = "Coverage is a claim-bound evaluation relation, not a text-search result."
promotion = {}

[[relations]]
type = "relates_to"
target = "CAPRMEDIO-REQUIREMENT-GOV-024"
+++

# Defect — Health coverage trusts loose mentions

The health generator currently counts ID substrings and same-line
co-occurrence as compilation, check, and evidence coverage. A pending or
historical prose mention can therefore make an uncovered claim appear covered.

## Completion condition

Compilation, QA, implementation, and evidence coverage derive from validated
typed relations plus current lifecycle state. Prose links remain navigation
only, and false-positive fixtures stay uncovered.
