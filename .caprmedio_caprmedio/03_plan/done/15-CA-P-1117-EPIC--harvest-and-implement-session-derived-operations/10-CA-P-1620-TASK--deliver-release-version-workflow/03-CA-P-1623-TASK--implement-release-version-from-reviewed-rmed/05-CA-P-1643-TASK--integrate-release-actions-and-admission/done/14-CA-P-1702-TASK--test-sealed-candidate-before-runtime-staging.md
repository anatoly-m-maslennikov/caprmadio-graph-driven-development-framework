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
status: Done
subjects:
  governs: "Test sealed candidate before runtime staging"
  depends_on: [Tool, Manifest, Runtime, Test Suite, Evaluation]
version: 1
updated_at: "2026-10-05 07:34:12 +0000"
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

### Current bounded completion

release_suite.py fd03813c8066dda50631b64257800ba970fdbd19e10f4a13acc9e0700a953549 and testsac6a39a6ae4f011f8bd77fdd2019b3494ebda532bd1f2c49b1cc4675cb8feebc pass21 suite cases; downstream image37 and promotion14 cases also pass in the designated development worker. Exact source/compiled candidate rows permit the suite before installation; absent package/Skill remain absent, unsafe/tampered existing packages and stale/missing compiled inputs refuse. Later image build still refuses before Docker until the complete physical package exists. No actual repository Release or image work is claimed.
