+++
artifact_subtype = "problem"
semantic_id = "CAPRMEDIO-REALIZATION-CONC-083--implementation-profile-evaluation-is-deferred"
revision_mode = "atomic"
content_role = "observation"
governance_origin = "internal"
relation_shape = "standalone"
status = "accepted"
priority = "high"
authority = "operator:anatoly-m-maslennikov"
claim = "The new IMPL layer, Local Python Tools profile, relocated executable methodology, and replacement implementation Decisions do not yet have current Test/Evaluation definitions and execution evidence."
llm_session_ids = ["codex:019f591f-04f6-70f2-8de7-828b7cccc69d"]
rationale = "The operator explicitly deferred Tests and Evaluations until the real structure was finalized; preserving the gap prevents structural completion from being mistaken for evaluation."
promotion = {}

[[relations]]
type = "relates_to"
target = "CAPRMEDIO-REALIZATION-METH-062--terminal-profile-features"

[[relations]]
type = "relates_to"
target = "CAPRMEDIO-REALIZATION-REQU-582--local-python-tools-profile"

[[relations]]
type = "relates_to"
target = "CAPRMEDIO-REALIZATION-REQU-583--portable-dry-run-and-diagnostics"
+++

# Problem — Implementation Profile evaluation is deferred

The six-layer structure and `local-python-tools-v1` profile are current
authority, but their evaluation suite has intentionally not been rewritten or
executed in this structural phase.

The next evaluation phase must update layer-order and path fixtures, add profile
schema/selection and resolver coverage, re-emit QA definitions for the
replacement TOOL/IMPL Decisions, and cover mandatory dry-run behavior,
file-header documentation, actionable errors, safe debug mode, and supported-OS
transferability. It must then run deterministic Tests and applicable
Evaluations and record exact-revision evidence before this Problem is resolved.
