+++
semantic_id = "CAPRMEDIO-SPEC-SKILLS-EVAL-056--overview-public-entrypoint-test-case"
revision_mode = "atomic"
content_role = "method"
governance_origin = "internal"
relation_shape = "standalone"
status = "accepted"
priority = "high"
authority = "operator:anatoly-m-maslennikov"
claim = "Deterministic validation requires exactly seventeen public skill packages, an overview workflow and thin wrapper, unchanged sixteen-entry lifecycle routing, shared-runtime distribution integrity, and a read-only overview stop boundary."
version = 1
updated_at = "2026-08-17 19:36:01"
llm_session_ids = ["codex:019f591f-04f6-70f2-8de7-828b7cccc69d"]

[promotion]
affected_children = ["skill"]
applies_unchanged = true
local_context_required = false

[promotion.parent_scope]
kind = "project"
id = "dset-specs-loops-framework"

[[relations]]
type = "check_of"
target = "CAPRMEDIO-SPEC-SKILLS-METH-057--overview-public-entrypoint"
+++

# Test Case — Enforce the Overview public entrypoint

Require an exact 17-package source and distribution catalog. Resolve
`dset-overview` through the registered `overview` workflow and project-local
rules, verify its package and host-copy integrity, and require its stop boundary
to remain read-only. Separately assert that the lifecycle rule still contains
exactly the existing sixteen entrypoints and fifteen modes, with initialization
and governance repair as the only pre-resolution exceptions.

Run the skill-wrapper, lifecycle-workflow, runtime bridge, session schema,
distribution, generated-adopter, and recursive DSET validation tests.

This emitted Test atom is immutable. Later correction requires a successor Test
and append-only lifecycle event.
