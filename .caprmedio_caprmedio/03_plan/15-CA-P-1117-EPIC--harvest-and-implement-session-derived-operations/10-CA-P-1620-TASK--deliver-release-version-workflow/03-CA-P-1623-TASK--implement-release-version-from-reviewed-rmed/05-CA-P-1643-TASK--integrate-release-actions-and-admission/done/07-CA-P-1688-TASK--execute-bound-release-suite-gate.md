---
atom_id: CA-P-1688
content_role: Plan
type: Plan
label: Task
work_sequence_number: 7
current_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
autonomous_confidence_threshold: 90
status: Done
subjects:
  governs: "Execute bound Release suite gate"
  depends_on: [Workflow, Tool, Manifest, Evaluation, Test Suite, Runtime]
version: 1
updated_at: "2026-10-05 06:14:04 +0000"
relations:
  is_decomposition_of: [CA-P-1643]
  blocks: [CA-P-1644]
---
# Summary

Execute bound Release suite gate

## Objective

Within <=15 minutes, implement the bound full-suite execution phase and truthful gate evidence.

## Details

Own only new RELEASE_VERSION/release_suite.py and focused tests/test_release_suite.py. Consume the locally validated candidate and sealed compilation; revalidate sources, executing N, exact sealed suite environment and complete candidate package. Execute the declared ordered command without shell expansion in its safe bound working directory; retain actual exit/coverage and output evidence. Missing, failed, timed-out, stale, incomplete or recording-uncertain evidence never passes or exposes N+1. Do not accept caller success flags or substitute an Engine-only or mock-only suite for the declared full suite. Use existing handoff/package types rather than another registry or manifest.

Golden first with disposable real commands plus deliberate failures. Any unsupported coverage format returns incomplete rather than presumed pass. No actual repository suite/release, source/Plans/Git edits, image/environment provisioning or C447/C449 workaround. Preserve other Agents' edits. Choose the best authorized option, record uncertainty and continue.

## Definition of Done

Focused actual-execution, refusal and failure cases pass with exact source/test hashes and retained evidence. This helper is not actual Project full-suite, image or Release completion.

### Current completed result

release_suite.py `3ce3e87ec83d0e40d721a39051d2ab03216181d3a4e7b933b0e8dca0197e3f7b`; tests `8904a01865cb3d1cca24694163bf343dba9970d9cf8f830ce104c11dedae6ab3`. Thirteen development-fixture cases pass and are repeated after inventory repair. APIs execute_bound_release_suite and verify_bound_suite_evidence validate exact current candidate/package, execute sealed arguments without shell, retain/reopen output/JUnit/receipt evidence, and reject missing/partial/unsupported/failed/skipped/unbound reports, stale inputs, forged handoffs/receipts, timeout and uncertain recording. Supported runner is POSIX local-subprocess. Test-generated artifacts were verified within execution; host export was unverified. This is protocol/subprocess test proof, not the actual Project full suite or Release.
