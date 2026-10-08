---
atom_id: CA-P-1816
content_role: Plan
type: Plan
label: Task
work_sequence_number: 1
current_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
autonomous_confidence_threshold: 90
status: Done
version: 2
updated_at: "2026-10-08 15:33:32 +0000"
subjects:
  governs: "Retain per-route candidate Run evidence"
  depends_on: [Implementation, Evaluation, Source Carrier, Workflow, Action, Journal]
relations:
  is_decomposition_of: [CA-P-1124]
  relates_to: [CA-C-515]
---
# Summary

Retain per-route candidate Run evidence

## Objective

preserve already-completed disposable-fixture Run and Journal evidence needed by the final coverage matrix.

## Details

- the existing sealed harnesses assert native per-route evidence, then remove disposable fixtures; their retained JUnit reports alone do not contain exact per-route Run IDs.
- use a bounded read-only observer under .caprmedio_tmp to preserve completed graph/Run results and exact supporting Journal prefixes before cleanup. bind every copy to its original path, bytes/mode/digest, candidate and fixture-local definitions.
- this is report collection, not a product Tool or permission expansion. it dispatches no Workflow, creates no Event, changes no source/runtime and never claims a fixture-local fifteen-route manifest is the live sixteen-route binding.
- after actual harness passage, attach captured identities and receipts to the existing matrix. absent captures remain explicit gaps, never inferred success.

## Definition of Done

the confirmed defect is explained and repaired against current authority; source-equivalent focused regressions have a captured terminal result and independent review accepts the bounded change. actual full Release acceptance remains deferred to the Release milestone, not this parent's retained first-cut closure.

### Accepted retained proof collection

both actual six-route stdio and authenticated Docker HTTP artifacts are retained under `.caprmedio_tmp/epic-first-cut-20261008/`. `retained-workflow-receipts.json` has SHA-256 `9a3866d6b440584feac03a06460b2e9f4d4395a0389e47dac528ffae2ed4a244`; `http-workflow-receipts.json` has SHA-256 `adb7d7f0b08be0f58ec97afaebb1a4ae8c0d6d9f4350c8d4c49e282df71b7818`. Each indexes six observed completed Workflow and 18 completed Action terminals, their original Journal/event digests, frozen source definitions, parent lineage and result/effect references. The original retained fixture carriers and passing Terminal logs remain present and independently accepted. W09 is explicitly golden mock-Agent evidence, not a live LLM effect; no formal Release, production Run or installed-N claim is made. This closes the current parent's retained proof-collection requirement through the Operator-authorized administrative Git fallback, without creating Events.
