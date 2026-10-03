+++
artifact_subtype = "defect"
semantic_id = "CAPRMEDIO-SPEC-SKILLS-CONC-080--session-handoff-terminalization"
revision_mode = "atomic"
content_role = "observation"
governance_origin = "external"
relation_shape = "standalone"
status = "accepted"
priority = "high"
authority = "external:skill-refactor-audit"
claim = "Wrapper instructions call terminal runtime finish before every handoff, so a successful specialist transition can complete the shared session and force the next skill into a new session."
version = 1
updated_at = "2026-08-17 19:36:01"
llm_session_ids = ["codex:019f591f-04f6-70f2-8de7-828b7cccc69d"]
rationale = "The command surface contradicts the accepted session-continuity requirement and loses chain identity across the exact handoff it is meant to preserve."
promotion = {}

[[relations]]
type = "child_of"
target = "CAPRMEDIO-REQUIREMENT-SKILL-009"
+++

# Defect — Handoff terminalizes the shared session

The wrappers do not distinguish an active handoff from a terminal stop. The
default successful finish completes the session, and the next directly invoked
specialist resolves a different session ID.

This emitted Problem atom is immutable. Resolution requires implementation,
proof, and an append-only lifecycle event.
