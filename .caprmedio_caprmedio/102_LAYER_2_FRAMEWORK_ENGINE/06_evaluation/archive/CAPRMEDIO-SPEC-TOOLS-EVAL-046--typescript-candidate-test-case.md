+++
semantic_id = "CAPRMEDIO-SPEC-TOOLS-EVAL-046--typescript-candidate-test-case"
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
target = "CAPRMEDIO-SPEC-TOOLS-REQU-550--typescript-candidate-profile"
+++

# Test Case — Validate the TypeScript candidate profile

Deterministic proof must validate the candidate profile's schema and identity,
the exact six gate mappings, pinned source evidence, safe relative paths,
canonical command sequence, warning-only ratchet, zero-error baseline,
candidate blocker semantics, and read-only target inspection.

Representative invalid fixtures must fail for a missing gate, unpinned source,
unsafe path, warning-count mismatch, non-zero error baseline, command absent
from the canonical sequence, active status with blockers, and target revision,
script, lockfile, or source/test-population drift.

This emitted Test definition is immutable. Runs and their evidence are
separate artifacts.
