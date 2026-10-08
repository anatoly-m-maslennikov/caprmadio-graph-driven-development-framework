---
atom_id: CA-C-513
content_role: Concern
type: Question
current_scope_unit: WORKFLOW_ORCHESTRATOR
local_tier: Standard
global_tier: 14
status: resolved
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-06 18:56:40 +0000"
subjects:
  governs: "Workflow Run/Observation"
  depends_on: [Workflow Run, Action Run, Journal, Source Carrier, Projection, Operator]
relations:
  concern_about: [CA-P-1808, CA-R-1807, CA-P-1794]
---
# Summary

Should historical Run observation require current admission

## Concern

reading the recorded N12 status fails after a legitimate canonical binding refresh because the observer applies the current-source dispatch guard to the historical frozen request.

## Evidences

the live MCP status call returns a generic error. read-only CLI diagnosis identifies SelectedExecutionError: selected definition manifest digest is stale or invalid, raised by backend._release_host_frozen calling the effect revalidator before status retrieval. N12's retained actual Events already establish its interrupted outcome.

## Blast radius

read-only Release-host status and recovery-status observation after source changes. actual dispatch and recovery must retain their current-source admission checks.

## Decision

under existing R1807, distinguish authenticated historical observation from permission to execute. preserve exact frozen Run/route/request identity, retained transport binding, namespace and availability checks for reads; keep current-source revalidation for dispatch and actual recovery. source drift never authorizes effects or replay and does not rewrite saved results.

## Result

the 15-case Release-host backend suite passes, and independent review accepts the private observation/effect split. status and recovery-status preserve exact frozen identity, retained transport/availability checks and pre-client tamper/foreign refusals; actual dispatch and recovery retain strict current-source validation. after the explicit restart of the identified idle Release-host worker, live MCP reads historical N12 with its eight completed and three interrupted terminal Runs and 22 durable receipts. scheduler SUCCESS remains distinct from the actual interrupted-pending work outcome; no replay, effect or release success is inferred.
