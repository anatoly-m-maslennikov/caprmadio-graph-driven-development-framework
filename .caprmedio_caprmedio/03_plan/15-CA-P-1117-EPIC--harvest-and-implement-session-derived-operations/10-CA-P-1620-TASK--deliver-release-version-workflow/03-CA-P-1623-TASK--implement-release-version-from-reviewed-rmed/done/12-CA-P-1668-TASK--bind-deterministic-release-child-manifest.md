---
atom_id: CA-P-1668
content_role: Plan
type: Plan
label: Task
work_sequence_number: 12
current_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
autonomous_confidence_threshold: 90
status: Done
subjects:
  governs: "Bind deterministic Release child manifest"
  depends_on: [Atom, Carrier, Revision, Tool, Manifest, Evaluation]
version: 1
updated_at: "2026-10-05 04:08:40 +0000"
relations:
  is_decomposition_of: [CA-P-1623]
  blocks: [CA-P-1669]
---
# Summary

Bind deterministic Release child manifest

## Objective

Within <=15 minutes, bind deterministic Release child manifest.

## Details

Own one new Tool Delivery source CA-D-571 and one C/Question CA-C-454 only. Specify the D561 child output manifest's deterministic filename and canonical bytes before P1650 implements them. Best in-scope choice: _release_manifest.json with a versioned schema, executing compiler digest, selected candidate Release, canonical-source/frontier and derived-source-copy digests, and destination-sorted projected-output path/digest rows. The manifest must not contain its own digest, the final compiled-tree digest or candidate-manifest SHA: those cause circular expected-output checks. It is a derived compiler result, not another source authority. Reuse D566/D567 expected-versus-observed handoff and no canonical projection rewrite. Read actual compiler output rendering before final shape; choose simpler equivalent encoding if justified in C454. No code, compile, package, runtime, Journal, Plans or Git writes.

Choose the best authorized in-scope option when uncertain, record a C/Question and continue under the current Epic. You are not alone; preserve other edits and C447/C449 boundaries. Root saves completion from actual evidence only.

## Definition of Done

Save the bounded output, exact source revisions and truthful review/current frontier. This Task does not complete runtime gates or the Epic.

## Result

Saved repaired D571@2 SHA-256 24dc030c0a95dc21c72a4b054c1eae088a004550bed0efd75265c2ad95fc753c and C454@2 a56191d3cbbbfe754db8e43f87def0cbcfc055d9c83bf1fd86815c941a26eb74, with exact v1 archives. Pure pre-D566 rendering predicts child manifest/output rows/tree digest without effects; actual child rendering must match before trusted handoff. Self/cross-hash and pre-effect/post-effect cycles are excluded. P1669 independently ACCEPT95%. No compiler invocation or Release execution is claimed.
