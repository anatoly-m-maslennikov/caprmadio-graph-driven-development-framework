+++
semantic_id = "CAPRMEDIO-SPEC-SKILLS-EVAL-052--implementation-preparation-mode-test-case"
revision_mode = "atomic"
content_role = "method"
governance_origin = "internal"
relation_shape = "standalone"
status = "accepted"
priority = "high"
authority = "operator:anatoly-m-maslennikov"
claim = "Deterministic tests prove lazy prerequisite closure and strict implementation-only behavior from project settings."
promotion = {}
version = 1
updated_at = "2026-08-17 19:36:01"
llm_session_ids = ["codex:019f591f-04f6-70f2-8de7-828b7cccc69d"]

[[relations]]
type = "check_of"
target = "CAPRMEDIO-SPEC-SKILLS-REQU-569--implementation-preparation-mode"

[[relations]]
type = "replacement_of"
target = "CAPRMEDIO-SPEC-SKILLS-EVAL-051--lazy-implementation-preparation"
+++

# Test Case — Validate implementation preparation modes

Deterministic proof must show that a missing setting selects `lazy`; explicit
`lazy` uses the ordered decisions, proof-plan, implementation-plan, implement
closure; and explicit `strict` selects only `implement` without creating a
prerequisite child run. Invalid values must stop before a run is created.

Strict mode must report insufficient or ambiguous accepted input rather than
silently switching to lazy behavior. Both modes must preserve project-local
rule resolution, authorization, session/run identity, provenance, terminal
finish behavior, and the Verification/release stop boundary.

This Test completely replaces `CAPRMEDIO-SPEC-SKILLS-EVAL-051--lazy-implementation-preparation`. Runs and evidence are
separate.
