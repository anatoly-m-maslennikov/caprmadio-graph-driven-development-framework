---
atom_id: CA-P-1686
content_role: Plan
type: Plan
label: Task
work_sequence_number: 5
current_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
autonomous_confidence_threshold: 90
status: Done
subjects:
  governs: "Implement bound Methodology source delivery"
  depends_on: [Workflow, Action, Tool, Manifest, Methodology, Evaluation]
version: 1
updated_at: "2026-10-05 05:44:17 +0000"
relations:
  is_decomposition_of: [CA-P-1643]
  blocks: [CA-P-1644]
---
# Summary

Implement bound Methodology source delivery

## Objective

Within <=15 minutes, implement bound Methodology source delivery.

## Details

Own only new RELEASE_VERSION/release_delivery.py and focused tests/test_release_delivery.py. Golden first, from accepted D561/D566/D567/D571, current O165@2/O166@2 and the actual compiler-to-stager pipeline. Consume typed locally ValidatedCandidate, recheck its actual currentness, and copy the entire canonical Methodology source tree with exact bytes/modes to the fixed derived 101_LAYER_1_FRAMEWORK_METHODOLOGY/sources target. No mutable path override or authority_path repointing. Return locally validated SealedSourceCopy only after actual complete digest proof. Handle safe first delivery, same-byte idempotence, stale/partial/collision/unsafe-path refusal. For a different existing derived delivery, replace only if ownership and its exact predecessor bytes are proven from the retained executing-N package; preserve N and repairable failure context. Never delete/overwrite unknown ownership or canonical Projection/source authority. Reuse private compiler/handoff validators rather than a second compiler or snapshot schema.

No repo actual release, source/Plans/Git/manifest/runtime/image or denied-operation workaround. Tests use disposable Project fixtures in the existing development worker only. No credential reads. Preserve every other Agent's work; choose best authorized options and record uncertainty instead of asking the Operator.

## Definition of Done

Actual full-copy/idempotence/refusal cases and exact helper/test hashes are saved. This completes one native phase helper, not the whole release, image, installation or shared Run gate.

## Result

Implemented deliver_release_sources(ValidatedCandidate) -> SealedSourceCopy. release_delivery.py `979f457f1217e28749ee5420377cc65f81fc2452944cc1873584044b0a011f1c`; tests `eb1e95907ba165f65519eb0b8be6c89961a837a43d6383f9667c3e846b81cdd8`. Twelve delivery cases, five compiler regressions and two pipeline regressions pass in disposable development fixtures: complete bytes/modes/empty directories, idempotence, exact retained-N ownership, actual delivery-renderer-stager, stale/partial/collision/symlink/tampered-package refusals and injected failure recovery. Replacement retains the whole predecessor; ReleaseDeliveryError exposes recovery_paths. No actual repository Release, installation, image or shared Run gate was executed.
