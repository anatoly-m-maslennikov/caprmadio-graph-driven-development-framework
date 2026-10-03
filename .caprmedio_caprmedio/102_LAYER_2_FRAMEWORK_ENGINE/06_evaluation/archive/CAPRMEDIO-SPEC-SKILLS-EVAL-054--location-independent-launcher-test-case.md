+++
semantic_id = "CAPRMEDIO-SPEC-SKILLS-EVAL-054--location-independent-launcher-test-case"
revision_mode = "atomic"
content_role = "method"
governance_origin = "external"
relation_shape = "standalone"
status = "accepted"
priority = "high"
authority = "external:skill-refactor-audit"
claim = "Deterministic installation tests require one package-local launcher identity for every executable DSET instruction and prove shell-safe macOS, Linux, native Windows, and WSL rendering without ambient PATH."
version = 1
updated_at = "2026-08-17 19:36:01"
llm_session_ids = ["codex:019f591f-04f6-70f2-8de7-828b7cccc69d"]
promotion = {}

[[relations]]
type = "check_of"
target = "CAPRMEDIO-SPEC-SKILLS-REQU-568--shared-skill-runtime"
+++

# Test Case — Prove one portable installed launcher

Rendered wrapper and governance instructions must contain no bare executable
fallback. Exact argv or host-native launcher forms must remain correct for
paths with spaces and shell metacharacters on every declared platform.

This Test definition is immutable. Runs and evidence are separate.
