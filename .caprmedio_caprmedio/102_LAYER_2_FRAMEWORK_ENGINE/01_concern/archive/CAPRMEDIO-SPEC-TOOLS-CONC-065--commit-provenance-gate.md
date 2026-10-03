+++
artifact_subtype = "gap"
semantic_id = "CAPRMEDIO-SPEC-TOOLS-CONC-065--commit-provenance-gate"
revision_mode = "atomic"
content_role = "observation"
governance_origin = "internal"
relation_shape = "standalone"
status = "accepted"
priority = "high"
version = 1
updated_at = "2026-08-17 19:36:01"
llm_session_ids = ["codex:019f591f-04f6-70f2-8de7-828b7cccc69d"]
+++

# Gap — Commit provenance is derived but not enforced

Traceability can parse commit trailers into derived edges, but no gate rejects
an evergreen or implementation commit that omits a governing Decision ID.
Arbitrary uppercase IDs can also satisfy the current parser, so the repository
cannot enforce its commit-provenance rule.

## Rationale

This is a missing tool capability because a derived view cannot replace the
required delivery gate.
