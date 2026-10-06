---
atom_id: CA-C-506
content_role: Concern
type: Question
current_scope_unit: MCP
local_tier: Standard
global_tier: 11
status: resolved
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-06 18:38:40 +0000"
subjects:
  governs: "MCP/selected source pin refresh"
  depends_on: [Projection, Workflow, Action, Operator, Journal, Source Carrier]
relations:
  concern_about: [CA-P-1800, CA-P-1799]
---
# Summary

How to refresh the accepted lifecycle source revision

## Concern

how can the current selected binding adopt the accepted lifecycle Action revision when the existing guarded writer refreshes Release admission only?

## Evidences

the original writer preserves the fifteen non-Release route pins. the reviewed Action revision is current authority, so retaining its previous pin makes four selected routes stale; hand-editing the Projection would omit publication intent and recording.

## Blast radius

the one canonical selected binding and the four lifecycle routes using the revised Action. preserve the other twelve routes, query admission and registry evidence.

## Decision

under the Epic's autonomous best-option instruction, add the exact current registration and derive **only** its eight declared pin substitutions. reuse existing trusted Operator authorization, intent, write, readback and Journal machinery. this is an approved bounded source revision, not general graph rewriting.

## Result

the registered eight-occurrence lifecycle refresh is actually published as binding revision 8 and the normal current Release-admission refresh as revision 9. exact readback, preserved historical Journal prefixes and completed receipts are retained at journal:release-manifest:f0b7cea609921392f1059bc218f04d8d8ebf21aa55e1b433b8bfc8d5804f0c00 and journal:release-manifest:7dcde04ace60ee550b67e037978b85176ad90753c1d48147b8ef162d390eb804. twelve source-refresh regressions and independent review pass. live MCP context retrieval passes for all sixteen route names at canonical digest e26598708056b90f9bea85148a02b98bab51a74d66b987f1232ad1cb18eb77aa, without topology changes or Run execution.
