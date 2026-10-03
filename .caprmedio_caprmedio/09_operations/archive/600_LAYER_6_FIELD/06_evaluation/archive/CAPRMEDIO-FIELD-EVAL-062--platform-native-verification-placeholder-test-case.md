+++
semantic_id = "CAPRMEDIO-FIELD-EVAL-062--platform-native-verification-placeholder-test-case"
revision_mode = "atomic"
content_role = "method"
governance_origin = "internal"
relation_shape = "standalone"
status = "accepted"
priority = "high"
authority = "operator:anatoly-m-maslennikov"
claim = "Deterministic verification proves that a Windows Python executable path containing backslashes and spaces remains one exact subprocess argument after command-template expansion."
version = 1
updated_at = "2026-08-17 19:36:01"
llm_session_ids = ["codex:019f591f-04f6-70f2-8de7-828b7cccc69d"]
promotion = {}

[[relations]]
type = "check_of"
target = "CAPRMEDIO-FIELD-METH-072--platform-native-verification-placeholder"

[[relations]]
type = "check_of"
target = "CAPRMEDIO-CONTRACT-TOOL-001"
+++

# Test Case — Preserve a native-Windows Python executable argument

Parse a representative verification template with `{python}` and substitute a
Windows executable path containing both backslashes and spaces. The resulting
argument vector must contain the original path byte-for-byte as its first and
only executable argument, followed by the expected module arguments.

Run the focused verifier suite, the complete DSET verification suite, and fresh
hosted Linux, macOS, and native-Windows jobs. The platform gate closes only
when the exact pushed head passes on every hosted runner.

This emitted Test atom is immutable. Later correction requires a successor Test
and append-only lifecycle event.
