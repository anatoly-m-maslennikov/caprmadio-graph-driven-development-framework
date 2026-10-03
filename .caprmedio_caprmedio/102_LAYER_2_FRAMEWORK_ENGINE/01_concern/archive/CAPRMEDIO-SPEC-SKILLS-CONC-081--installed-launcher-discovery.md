+++
artifact_subtype = "gap"
semantic_id = "CAPRMEDIO-SPEC-SKILLS-CONC-081--installed-launcher-discovery"
revision_mode = "atomic"
content_role = "observation"
governance_origin = "internal"
relation_shape = "standalone"
status = "accepted"
priority = "high"
version = 1
updated_at = "2026-08-17 19:36:01"
llm_session_ids = ["codex:019f591f-04f6-70f2-8de7-828b7cccc69d"]
+++

# Gap — Installed wrappers cannot deterministically find DSET

The distributor installs the shared runtime under the host-private package
root, while every thin wrapper invokes a bare `dset` command. Installation does
not add that launcher to `PATH` or give wrappers a deterministic package-local
resolver, so a clean host installation may not be invocable.

## Rationale

This is a missing skill-distribution capability because copy success alone does
not satisfy host discovery and invocation.
