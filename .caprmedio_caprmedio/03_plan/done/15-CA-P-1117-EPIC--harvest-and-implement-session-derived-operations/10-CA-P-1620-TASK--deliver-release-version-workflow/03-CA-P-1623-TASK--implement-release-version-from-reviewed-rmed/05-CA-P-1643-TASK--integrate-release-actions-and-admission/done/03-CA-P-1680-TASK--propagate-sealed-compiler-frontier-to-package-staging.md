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
status: Done
subjects:
  governs: "Propagate sealed compiler frontier to package staging"
  depends_on: [Tool, Manifest, Implementation, Evaluation]
version: 1
updated_at: "2026-10-05 04:49:12 +0000"
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

## Result

The stager now compares the canonical tree only with its canonical snapshot/nested currentness and compares the compiler frontier with its separately sealed authority frontier. release_packaging.py SHA-256 55971d32e044ab534f29487c1c5c90472b91f2ff839770c8600bea58a253e694; new test_release_pipeline.py 6a5d453ac91695204a136e61f4945cd7c73f2aff560015ca6738694715b9ac50. Existing development worker passed2 actual compiler-to-staging pipeline cases,5 compiler,14 codec,13 handoff and5 package cases, with no failed/skipped cases. Actual distinct hashes reach complete idempotent non-active staging; forged frontier and stale source refuse, and the selector stays unchanged. This is disposable-project evidence only, not actual project activation, full suite, image/MCP, Journal completion or retirement.
