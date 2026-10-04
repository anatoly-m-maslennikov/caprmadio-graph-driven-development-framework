---
atom_id: CA-E-567
content_role: Evaluation
type: QA Case
current_scope_unit: MCP
claim_target_scope_unit: MCP
local_tier: Standard
global_tier: 11
status: Archived
author: Anatoly Maslennikov
version: 3
updated_at: "2026-10-04 19:21:30 +0000"
subjects:
  governs: "MCP/selected Workflow route contract"
  depends_on: [MCP, Tool, Workflow, Action, Operator, Run, Journal]
relations:
  evaluation_for: [CA-R-1847, CA-R-1848]
---
# Summary

Verify selected MCP route contract and currentness

## Scope

Functional MCP request/response validation for all thirteen selected route registrations, their one closed current binding manifest, and one current preview/authorized execute handoff.

## Claim

Every realization **must** demonstrate the exact selected route registry, stable existing helpers, and source-bound request/result envelope before runtime acceptance.

## Details

Start the current reloadable server against a functional isolated Project fixture. Assert the manifest's canonical digest and all thirteen unique route entries; for each entry compare its full Workflow, ordered Step, ordered Action, source-path, Version, and digest pins to the current source fixture. Assert that the eight pre-existing helpers remain registered and each of the thirteen names in R1847 is registered once with no extra generic mutation route. For every selected name, send a schema-valid preview with exactly one outer `definition_manifest` (`manifest_ref`, `manifest_digest`) and required source/definition/currentness refs; assert a prepared, deferred, or implementation-gap result is truthful, mutation-free, and identifies the selected capability. Do not count a route declaration as an executing capability.

For one implemented mutation-capable fixture, retain a preview then send exact Operator authorization and unchanged sealed refs with `mode: execute`. Assert the adapter forwards the request once to shared support and returns the exact Run/Action Run, result/output/event/report refs, and source-currentness it receives. Query the returned Run and Action Run and compare their status, lineage, and references without dispatch. Repeat after changing a bound source/frontier/target/manifest ref: it must block before dispatch and identify the changed binding. Separately omit any route binding, alter a pin or canonical digest, make any source pin stale, or supply `source_freshness.definition_manifest_ref` or `.definition_manifest_digest` (with either matching or different digest): each is rejected before shared support, with no Run, Action Run, worker, effect, or Journal event.

Acceptance compares MCP tool inventory, annotations, full envelopes, service-call trace, mutation trace, and returned references. This carrier specifies functional proof; it is not a runtime pass.

### Sources

- CA-R-1847 v3; CA-R-1848 v3; CA-D-547 v3; CA-A-1142 v2; CA-D-527 v3.
