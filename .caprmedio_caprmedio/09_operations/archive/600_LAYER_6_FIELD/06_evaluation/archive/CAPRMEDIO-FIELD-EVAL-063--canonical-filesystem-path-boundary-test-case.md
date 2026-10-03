+++
semantic_id = "CAPRMEDIO-FIELD-EVAL-063--canonical-filesystem-path-boundary-test-case"
revision_mode = "atomic"
content_role = "method"
governance_origin = "internal"
relation_shape = "standalone"
status = "accepted"
priority = "high"
authority = "operator:anatoly-m-maslennikov"
claim = "Deterministic verification proves that repository path aliases compare by resolved identity and that a Windows relative Path becomes canonical POSIX repository text without weakening string validation."
version = 1
updated_at = "2026-08-17 19:36:01"
llm_session_ids = ["codex:019f591f-04f6-70f2-8de7-828b7cccc69d"]
promotion = {}

[[relations]]
type = "check_of"
target = "CAPRMEDIO-FIELD-METH-073--canonical-filesystem-path-boundary"

[[relations]]
type = "check_of"
target = "CAPRMEDIO-CONTRACT-TOOL-001"
+++

# Test Case — Enforce canonical repository path identity

Create a directory alias and require layout discovery, containment, evidence,
and archive operations to compare the alias and target by resolved identity.
Pass a representative Windows relative Path and require POSIX repository text;
continue rejecting a string containing backslashes.

Run the focused layout/archive/evidence suites, the complete DSET verification
suite, and fresh hosted Linux, macOS, and native-Windows jobs. The platform gate
closes only when the exact pushed head passes on every hosted runner.

This emitted Test atom is immutable. Later correction requires a successor Test
and append-only lifecycle event.
