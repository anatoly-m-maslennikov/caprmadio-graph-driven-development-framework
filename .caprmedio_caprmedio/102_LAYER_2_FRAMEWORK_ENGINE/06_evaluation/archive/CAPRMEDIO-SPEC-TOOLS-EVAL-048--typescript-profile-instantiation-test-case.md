+++
semantic_id = "CAPRMEDIO-SPEC-TOOLS-EVAL-048--typescript-profile-instantiation-test-case"
revision_mode = "atomic"
content_role = "method"
governance_origin = "internal"
relation_shape = "standalone"
status = "accepted"
priority = "high"
version = 1
updated_at = "2026-08-17 19:36:01"
llm_session_ids = ["codex:019f591f-04f6-70f2-8de7-828b7cccc69d"]

[[relations]]
type = "child_of"
target = "CAPRMEDIO-SPEC-TOOLS-REQU-552--typescript-profile-instantiation"
+++

# Test Case — Enforce reference and applied profile roles

Deterministic proof must require an explicit `reference` or `applied` role,
require `derived_from` only for applied instances, expose the role in read-only
inspection, reject an adopter that attempts to execute a distributed reference,
accept the same adopter after a local applied instance exists, and preserve the
complete existing profile validation and target-drift matrix.

This emitted Test definition is immutable. Test code and execution results are
separate implementation and evidence artifacts.
