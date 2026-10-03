+++
artifact_subtype = "defect"
semantic_id = "CAPRMEDIO-SPEC-TOOLS-CONC-055--runtime-terminalization"
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

# Defect — Skill runs are started but not terminalized

Skill context starts a runtime run and persists a running checkpoint, but the
thin-wrapper path has no guaranteed finish operation. Nested calls overwrite
the single latest-run checkpoint, leaving parent runs running and later unable
to finish through the checkpoint route.

## Rationale

This is a current tool defect because normal skill invocation produces
misleading operational state and loses resumable parent identity.
