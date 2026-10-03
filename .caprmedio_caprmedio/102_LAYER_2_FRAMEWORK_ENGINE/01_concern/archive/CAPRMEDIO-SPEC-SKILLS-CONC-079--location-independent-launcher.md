+++
artifact_subtype = "defect"
semantic_id = "CAPRMEDIO-SPEC-SKILLS-CONC-079--location-independent-launcher"
revision_mode = "atomic"
content_role = "observation"
governance_origin = "external"
relation_shape = "standalone"
status = "accepted"
priority = "high"
authority = "external:skill-refactor-audit"
claim = "Installed DSET instructions rewrite only selected commands, leaving bare global dset invocations and Windows cmd.exe quoting that break location-independent host execution."
version = 1
updated_at = "2026-08-17 19:36:01"
llm_session_ids = ["codex:019f591f-04f6-70f2-8de7-828b7cccc69d"]
rationale = "The shared runtime contract is not portable when later workflow commands depend on ambient PATH or a shell dialect different from the active host."
promotion = {}

[[relations]]
type = "child_of"
target = "CAPRMEDIO-SPEC-SKILLS-REQU-568--shared-skill-runtime"
+++

# Defect — Installed commands are not fully location-independent

Rendered wrappers and resolved governance can still instruct `dset init`,
`dset runtime child`, `dset runtime closure`, or `dset rules check` through an
ambient executable. Windows rendering also emits `cmd.exe` syntax that is not a
shell-neutral PowerShell-host invocation.

This emitted Problem atom is immutable. Resolution requires implementation,
proof, and an append-only lifecycle event.
