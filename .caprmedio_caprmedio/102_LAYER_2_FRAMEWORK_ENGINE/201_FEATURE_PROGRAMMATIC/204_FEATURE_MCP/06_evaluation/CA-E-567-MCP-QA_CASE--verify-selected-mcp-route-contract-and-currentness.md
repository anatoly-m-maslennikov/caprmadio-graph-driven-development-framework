---
atom_id: CA-E-567
content_role: Evaluation
type: QA Case
current_scope_unit: MCP
claim_target_scope_unit: MCP
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 4
updated_at: "2026-10-05 02:00:00 +0400"
subjects:
  governs: "MCP/selected Workflow route contract"
  depends_on: [MCP, Tool, Workflow, Action, Operator, Run, Journal]
relations:
  evaluation_for: [CA-R-1847, CA-R-1848]
---
# Summary

Verify selected MCP route contract and currentness

## Scope

Functional MCP request/response validation for all fifteen selected route
registrations, their one closed current binding manifest, and current
preview/authorized execute handoffs.

## Claim

Every realization **must** demonstrate the exact selected route registry, stable existing helpers, and source-bound request/result envelope before runtime acceptance.

## Details

Start the current reloadable server against a functional isolated Project fixture.
Assert the manifest's canonical digest and all fifteen unique route entries. For
the original thirteen, compare the full Workflow, ordered Step, ordered Action,
source-path, Version, and digest pins to CA-A-1142 v2. For
`find_and_fetch_artifacts` compare the exact CA-P-1532@2 acceptance pin and
CA-O-158/159/160@2 pins; for `find_and_fetch_journal_events` compare the exact
CA-P-1535@2 acceptance pin and CA-O-161/162/163@2 pins. Assert that the two
query admissions are inside the same canonical manifest, not a second registry,
manifest, parser, or executor. Assert that the eight pre-existing helpers remain
registered and each of the fifteen names in R1847 is registered once with no
extra generic mutation route.

For every selected name, send a schema-valid preview with exactly one outer
`definition_manifest` (`manifest_ref`, `manifest_digest`) and required
source/definition/currentness refs; assert a prepared, deferred, or
implementation-gap result is truthful, mutation-free, and identifies the
selected capability. For each query route, assert default IDs, selected fetches,
CA-R-1850 literal-grammar diagnostics, and secret exclusion; preview creates no
Run or Event. Do not count a route declaration as an executing capability.

For one implemented mutation-capable fixture, retain a preview then send exact
Operator authorization and unchanged sealed refs with `mode: execute`. For each
implemented read-only query fixture, use its exact admission/manifest pins and
explicit `mode: execute` without conferring mutation authority. In the Journal
case, assert capture of the CA-O-163 source byte-prefix precedes its own
Workflow/Action Run recording and that the returned result cannot include those
later Events. Assert the adapter forwards each admitted request once to shared
support and returns the exact Run/Action Run, result/output/event/report refs,
and source-currentness it receives. Query the returned Run and Action Run and
compare their status, lineage, and references without dispatch. Repeat after
changing a bound source/frontier/target/manifest/admission ref: it must block
before dispatch and identify the changed binding. Separately omit any route
binding, alter a pin or canonical digest, make any source/admission pin stale,
or supply `source_freshness.definition_manifest_ref` or
`.definition_manifest_digest` (with either matching or different digest): each
is rejected before shared support, with no Run, Action Run, worker, effect, or
Journal event.

Acceptance compares MCP tool inventory, annotations, full envelopes, service-call trace, mutation trace, and returned references. This carrier specifies functional proof; it is not a runtime pass.

### Sources

- CA-R-1847 v4; CA-R-1848 v4; CA-D-547 v5; CA-A-1142 v2; CA-P-1532 v2; CA-P-1535 v2; CA-D-527 v3; CA-R-1850 v2; CA-R-1866 v2; CA-R-1867 v1.
