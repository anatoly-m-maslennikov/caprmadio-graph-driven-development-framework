---
atom_id: CA-P-1712
content_role: Plan
type: Plan
label: Task
work_sequence_number: 24
current_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
autonomous_confidence_threshold: 90
status: Active
subjects:
  governs: "Canonicalize Release fixture roots"
  depends_on: [Evaluation, Carrier, Tool]
version: 1
updated_at: "2026-10-05 09:52:00 +0000"
relations:
  is_decomposition_of: [CA-P-1643]
  blocks: [CA-P-1708, CA-P-1644]
---
# Summary

Canonicalize Release fixture roots

## Objective

Within <=8 minutes, correct the Release test fixture root binding on macOS without weakening production root checks or hiding fixture permission failures.

## Details

Ownership: RELEASE_VERSION/tests/test_release_compilation.py, tests/release_handoff_fixture.py and tests/test_release_actions.py only. Fixture roots using /tmp are aliases of /private/tmp on macOS, whereas private production contexts and retained candidate roots are canonical. Resolve existing roots consistently in fixture setup and add the smallest regression assertion that protects the actual context match. Preserve all refusal checks, declared suite/Docker mocks and original cleanup.

Do not change production code, permissions, cleanup suppression, fixture destinations, source pins, Plans, Git or live images. Another worker owns selected_native_providers.py. Filesystem cleanup EPERM is a separate C449 boundary; do not repeat denied cleanup to claim a pass. Pure read-only/AST or isolated non-filesystem tests may establish limited evidence, clearly distinguished from unexecuted fixture tests. Root owns Task state and commits.

## Definition of Done

Save exact edits, hashes and genuine verification. Fixture-based verification remains unfinished until its filesystem permission boundary is cleared; static checks alone do not make this Task Done.

## Result

The assigned subagent canonicalized the existing roots with resolve(strict=True) in all three owned fixtures and added a regression asserting fixture/candidate/retained Run/Action context root equality. Original cleanup and production checks are unchanged.

AST syntax checks pass for all three files. Fixture tests were intentionally not repeated under the C449 cleanup denial. This Task remains Active pending real verification.

SHA-256: test_release_compilation.py e1495bf16fcae4e8783a19eb662a03b4b78ffdb001ddc6888c834f5919086895; release_handoff_fixture.py 14ddefc8ebfddcb93eaa37a0e963505c69a89e344d3f68660ab1bd1329f6d63c; test_release_actions.py fda28c6d2d51f14c885e7e068473e65b5e2a723c93aecfcb4f2fb3e6e1b128b0.
