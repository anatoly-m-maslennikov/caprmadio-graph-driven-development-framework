---
atom_id: CA-P-1702
content_role: Plan
type: Plan
label: Task
work_sequence_number: 14
current_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
autonomous_confidence_threshold: 90
status: Active
subjects:
  governs: "Test sealed candidate before runtime staging"
  depends_on: [Tool, Manifest, Runtime, Test Suite, Evaluation]
version: 1
updated_at: "2026-10-05 07:19:04 +0000"
relations:
  is_decomposition_of: [CA-P-1643]
  blocks: [CA-P-1701, CA-P-1644]
---
# Summary

Test sealed candidate before runtime staging

## Objective

Within <=10 minutes, remove the suite helper's undeclared physical-installation prerequisite while preserving complete candidate validation.

## Details

Own only RELEASE_VERSION/release_suite.py and tests/test_release_suite.py. Current O174 tests before O175 staging; E572@2 permits but does not require earlier package preparation. Keep local currentness, complete exact compilation/package rows and source-file validation. If a physical retained candidate package exists, verify it strictly; absence must not cause hidden staging or an otherwise unjustified pre-suite refusal. Unsafe/symlink/tampered existing packages and stale source/compiled rows still refuse. The declared command/cwd/full six-component actual coverage and durable suite receipt remain unchanged. Later image admission and promotion still require successful suite and the complete installed candidate.

Golden-first actual disposable fresh candidate without runtime package must run the suite successfully, preserve N and keep package/Skill absent. Add no-package stale/tamper refusal and verify later staging binds identical complete bytes. Preserve others; no source/Plan/Git changes, actual repository/image operations or C447/C449 workaround. Use only the existing designated development worker.

## Definition of Done

Save exact hashes and focused no-package/retained-package/refusal results, with unchanged later actual package/image gates.
