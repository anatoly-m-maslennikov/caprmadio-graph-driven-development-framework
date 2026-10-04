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
version: 1
updated_at: "2026-10-04 18:30:00 +0000"
subjects:
  governs: "MCP/selected Workflow route contract"
  depends_on: [MCP, Tool, Workflow, Action, Operator, Run, Journal]
relations:
  evaluation_for: [CA-R-1847, CA-R-1848]
---
# Summary

Verify selected MCP route contract and currentness

## Scope

Functional MCP request/response validation for all thirteen selected route registrations and one current preview/authorized apply handoff.

## Claim

Every realization **must** demonstrate the exact selected route registry, stable existing helpers, and source-bound request/result envelope before runtime acceptance.

## Details

Start the current reloadable server against a functional isolated Project fixture. Assert that the eight pre-existing helpers remain registered and each of the thirteen names in R1847 is registered once with no extra generic mutation route. For every selected name, send a schema-valid preview with the required exact source/definition and currentness refs; assert a prepared, deferred, or implementation-gap result is truthful, mutation-free, and identifies the selected capability. Do not count a route declaration as an executing capability.

For one implemented mutation-capable fixture, retain a preview then send exact Operator authorization and unchanged sealed refs. Assert the adapter forwards the request once to shared support and returns the exact Run/Action Run, result/output/event/report refs, and source-currentness it receives. Query the returned Run and Action Run and compare their status, lineage, and references without dispatch. Repeat after changing a bound source/frontier/target ref: it must block before dispatch and identify the changed binding.

Acceptance compares MCP tool inventory, annotations, full envelopes, service-call trace, mutation trace, and returned references. This carrier specifies functional proof; it is not a runtime pass.

### Sources

- CA-R-1847; CA-R-1848; CA-A-1141 v1 K7 and W01–W13.
