---
atom_id: CA-P-1680
content_role: Plan
type: Plan
label: Task
work_sequence_number: 3
current_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
autonomous_confidence_threshold: 90
status: Active
subjects:
  governs: "Propagate sealed compiler frontier to package staging"
  depends_on: [Tool, Manifest, Implementation, Evaluation]
version: 1
updated_at: "2026-10-05 04:46:05 +0000"
relations:
  is_decomposition_of: [CA-P-1643]
  blocks: [CA-P-1644]
---
# Summary

Propagate sealed compiler frontier to package staging

## Objective

Within <=10 minutes, propagate the accepted compiler frontier into the existing package consumer.

## Details

Root found release_packaging._complete_rows still compares the actual report frontier to the canonical full-tree digest, so accepted actual compilation cannot stage. Own only release_packaging.py and a focused real compiler-to-staging integration test. Compare canonical tree only to its canonical snapshot/currentness fields and compiler frontier to the sealed authority's compiler frontier. Keep all existing source/row/selector/structure/settings/entrypoint/output checks. Prove an actual compiler handoff with distinct hashes reaches complete idempotent non-active staging; forged frontier and stale inputs refuse without selector change. Existing development worker only; no source, code outside these files, manifest, runtime/image or denied-operation workaround.

## Definition of Done

Saved exact hashes and passing real disposable-project compiler-to-package integration plus existing compiler/handoff/packaging cases. This is not release promotion, full-suite or actual image/MCP evidence.

