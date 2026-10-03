+++
semantic_id = "CAPRMEDIO-FIELD-EVAL-061--canonical-health-path-order-test-case"
revision_mode = "atomic"
content_role = "method"
governance_origin = "internal"
relation_shape = "standalone"
status = "accepted"
priority = "high"
authority = "operator:anatoly-m-maslennikov"
claim = "Deterministic verification proves that project-health source entries use case-sensitive POSIX relative-path ordering rather than host-native Path ordering."
version = 1
updated_at = "2026-08-17 19:36:01"
llm_session_ids = ["codex:019f591f-04f6-70f2-8de7-828b7cccc69d"]
promotion = {}

[[relations]]
type = "check_of"
target = "CAPRMEDIO-FIELD-METH-071--canonical-health-path-order"

[[relations]]
type = "check_of"
target = "CAPRMEDIO-CONTRACT-TOOL-001"
+++

# Test Case — Enforce canonical project-health path ordering

Create a governed fixture containing relative paths whose case-sensitive POSIX
order differs from Windows-native Path order. The source-entry sequence must
use the POSIX text order and the rendered health digest must remain stable.

Run the focused project-health suite, the complete DSET verification suite, and
fresh hosted Linux, macOS, and native-Windows jobs. The platform gate closes
only when the exact pull-request head passes on every hosted runner.

This emitted Test atom is immutable. Later correction requires a successor Test
and append-only lifecycle event.
