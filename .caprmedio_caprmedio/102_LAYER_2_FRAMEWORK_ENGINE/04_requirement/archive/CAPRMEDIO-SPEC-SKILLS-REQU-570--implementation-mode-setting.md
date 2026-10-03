+++
semantic_id = "CAPRMEDIO-SPEC-SKILLS-REQU-570--implementation-mode-setting"
revision_mode = "atomic"
content_role = "definition"
governance_origin = "internal"
relation_shape = "standalone"
status = "accepted"
priority = "high"
authority = "operator:anatoly-m-maslennikov"
claim = "Each project selects lazy or strict dset-implement preparation through workflows.implement.mode in caprmedio_settings.toml, with lazy as the default."
version = 1
updated_at = "2026-08-17 19:36:01"
llm_session_ids = ["codex:019f591f-04f6-70f2-8de7-828b7cccc69d"]
rationale = "The workflow behavior remains accepted, but its source must reference the canonical settings filename and key."
promotion = {}

[[relations]]
type = "child_of"
target = "CAPRMEDIO-GOV-REQU-395--verbose-project-settings"

[[relations]]
type = "replacement_of"
target = "CAPRMEDIO-SPEC-SKILLS-REQU-569--implementation-preparation-mode"
+++

# Requirement — Select implementation preparation in canonical settings

Root `caprmedio_settings.toml` selects `lazy` or `strict` through
`workflows.implement.mode`; the default is `lazy`.

Lazy mode reconciles accepted session intent into missing atoms, completes
separate Test and applicable Evaluation definitions or plans, completes the
implementation plan when required, and then implements. It never invents
acceptance or silently resolves material ambiguity.

Strict mode performs implementation only from already sufficient accepted
inputs. It does not create, repair, or compile missing authority, QA, or plans;
missing or ambiguous inputs produce an exact stop.

Both modes resolve repository-local governance, preserve run/session and
commit provenance, obey authorization, and stop before claiming Verification
or release readiness.

## Rationale

This successor preserves the two-mode workflow while correcting the active
settings carrier reference.

This emitted Requirement atom is immutable. Later correction requires a
successor and append-only lifecycle evidence.
