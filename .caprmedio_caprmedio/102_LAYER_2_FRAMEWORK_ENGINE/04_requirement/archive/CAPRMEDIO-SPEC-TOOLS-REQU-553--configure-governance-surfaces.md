+++
semantic_id = "CAPRMEDIO-SPEC-TOOLS-REQU-553--configure-governance-surfaces"
revision_mode = "atomic"
content_role = "definition"
governance_locus = "internal"
status = "accepted"
priority = "high"
authority = "operator:anatoly-m-maslennikov"
claim = "The DSET CLI exposes deterministic status, activate, deactivate, and recommend operations for registered governance surfaces, previews every write by default, and writes only with explicit execution authority."
version = 1
updated_at = "2026-08-17 19:36:01"
llm_session_ids = ["codex:019f591f-04f6-70f2-8de7-828b7cccc69d"]
rationale = "A dry-run-first command makes optional governance reversible and inspectable without requiring an agent to edit TOML mechanically."

[promotion]
affected_children = ["skill", "implementation", "operations"]
applies_unchanged = true
local_context_required = false

[[relations]]
type = "child_of"
target = "CAPRMEDIO-GOV-REQU-448--governance-surface-settings"
+++

# Requirement — Configure governance surfaces deterministically

The CLI exposes:

```text
dset configure ROOT status
dset configure ROOT activate SURFACE
dset configure ROOT deactivate SURFACE
dset configure ROOT recommend
```

`status` and `recommend` are read-only. `activate` and `deactivate` print the
exact current and proposed state without writing unless `--execute` is present.
Unknown surfaces, invalid settings, competing settings carriers, or an
unresolved repository root stop with an actionable diagnostic.

The writer changes only the selected boolean and preserves the rest of
`caprmedio_settings.toml`, including comments and operator-owned values.
Deactivation never deletes a governed carrier.

Recommendations are advisory. They report the evidence and never activate a
surface automatically.
