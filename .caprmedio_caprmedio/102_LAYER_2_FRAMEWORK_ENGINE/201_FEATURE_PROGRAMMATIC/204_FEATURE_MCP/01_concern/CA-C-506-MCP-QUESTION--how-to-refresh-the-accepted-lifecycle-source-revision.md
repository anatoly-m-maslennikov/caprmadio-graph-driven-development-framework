---
atom_id: CA-C-506
content_role: Concern
type: Question
current_scope_unit: MCP
local_tier: Standard
global_tier: 11
status: active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-06 17:27:56 +0000"
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

source-first repair is in progress; no actual publication or fresh release success is claimed.

