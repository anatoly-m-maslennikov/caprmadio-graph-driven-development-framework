+++
semantic_id = "CAPRMEDIO-SPEC-SKILLS-REQU-573--configure-governance-surfaces-wrapper"
revision_mode = "atomic"
content_role = "definition"
governance_locus = "internal"
status = "accepted"
priority = "high"
authority = "operator:anatoly-m-maslennikov"
claim = "DSET publishes one thin dset-configure skill for status, activation, deactivation, and recommendations instead of separate enable and disable skills."
version = 1
updated_at = "2026-08-17 19:36:01"
llm_session_ids = ["codex:019f591f-04f6-70f2-8de7-828b7cccc69d"]
rationale = "One configuration entrypoint keeps the public skill surface small and lets the deterministic tool own mechanical settings changes."

[promotion]
affected_children = ["implementation", "operations"]
applies_unchanged = true
local_context_required = false

[[relations]]
type = "child_of"
target = "CAPRMEDIO-SPEC-TOOLS-REQU-553--configure-governance-surfaces"

[[relations]]
type = "relates_to"
target = "CAPRMEDIO-REQUIREMENT-SKILL-002"
+++

# Requirement — Publish one dset-configure wrapper

`dset-configure` is one supplemental public skill with four operator intents:
status, activate, deactivate, and recommend. Separate `dset-enable` and
`dset-disable` skills are forbidden.

The wrapper resolves the target project's local governance, reports current
surface state, and invokes the deterministic `dset configure` command. It owns
no surface catalog, heuristic, threshold, settings-editing logic, or fallback
methodology.

Activation and deactivation require explicit write authorization and use the
tool's preview before execution. Recommendation remains read-only and advisory.
The wrapper stops after reporting the result; it does not create a selected
surface or perform another workflow automatically.
