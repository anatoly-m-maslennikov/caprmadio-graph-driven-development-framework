---
atom_id: CA-P-1658
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
  governs: "Repair full Framework staging handoff"
  depends_on: [Atom, Status, Carrier, Tool, Manifest, Methodology, Evaluation, Journal]
version: 1
updated_at: "2026-10-05 03:59:46 +0000"
relations:
  is_decomposition_of: [CA-P-1654]
  blocks: [CA-P-1650, CA-P-1643]
---
# Summary

Repair full Framework staging handoff

## Objective

Within <=15 minutes, repair full Framework staging handoff.

## Details

Own RELEASE_VERSION/release_packaging.py and its test_release_packaging.py only. After the typed P1656 interface is available, repair P1651 findings using accepted D566/D567 and E572@2: require internal validated SealedCandidateCompilation, canonical candidate identity, complete typed package rows, source-observed digest/mode reread, no symlinked or escaping runtime staging parents, unchanged N and exact retained-package idempotency/collision behavior. Actual temporary-package golden tests, not raw fake SHA acceptance. No compile, selector, public Skill, Journal or image effects.

Read exact accepted sources and current files. You are not alone: preserve unrelated edits. Do not bypass C447/C449 or count a development worker as immutable-image/MCP/queue proof. Record actual saved output and remaining coverage.

## Definition of Done

The bounded assigned output, exact frontier and genuine focused evidence are saved. Source-only, mocked, partial or rejected work does not complete the composite, required runtime gates or Epic.

## Result

Replaced raw manifest/row staging with typed SealedCandidateCompilation. It rechecks local currentness, copy/compiler trees, actual source bytes and modes, full package inventory, runtime-parent safety, idempotency and collisions while preserving current N and public Skill. release_packaging.py SHA-256 eea888c353fbf3d850d26be49762a39755f225d8b2aad8c4a63ee5c2d7b85464; test_release_packaging.py d30b5160b2a9498ba1febd6fa8ef4d52f9c808d030aea2b37b5cf88f5709d94d. Five package tests and thirteen handoff tests pass in the existing development worker; root separately reran the five package tests. Compiler-positive evidence in these fixtures is explicitly mocked, so this proves staging mechanics only, not actual compiler/full-suite/runtime/image/promotion/Journal gates.
