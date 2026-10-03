+++
semantic_id = "CAPRMEDIO-SPEC-SKILLS-EVAL-055--session-handoff-terminalization-test-case"
revision_mode = "atomic"
content_role = "method"
governance_origin = "external"
relation_shape = "standalone"
status = "accepted"
priority = "high"
authority = "external:skill-refactor-audit"
claim = "An end-to-end wrapper test proves handoff keeps one explicit session active across specialist context resolution and only a true terminal outcome completes or stops it."
version = 1
updated_at = "2026-08-17 19:36:01"
llm_session_ids = ["codex:019f591f-04f6-70f2-8de7-828b7cccc69d"]
promotion = {}

[[relations]]
type = "check_of"
target = "CAPRMEDIO-REQUIREMENT-SKILL-009"
+++

# Test Case — Preserve session identity through handoff

The command-level fixture starts `dset`, records a successful handoff without
terminalizing the session, resolves a specialist with the same session ID, and
then proves explicit completion closes it. Ambiguous or absent continuity must
stop rather than silently create a new chain.

This Test definition is immutable. Runs and evidence are separate.
