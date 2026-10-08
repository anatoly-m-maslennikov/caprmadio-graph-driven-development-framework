---
atom_id: CA-P-1711
content_role: Plan
type: Plan
label: Task
work_sequence_number: 23
current_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
autonomous_confidence_threshold: 90
status: Done
subjects:
  governs: "Review safe exact image retirement"
  depends_on: [Image, Framework Instance Settings, Manifest, Tool, Evaluation]
version: 2
updated_at: "2026-10-05 09:45:00 +0000"
relations:
  is_decomposition_of: [CA-P-1643]
  blocks: [CA-P-1697, CA-P-1644]
---
# Summary

Review safe exact image retirement

## Objective

Within <=8 minutes, independently review only P1707's consequential exact-removal delta against accepted D573@2 and Release safety authority.

## Details

Read-only review of release_image.py SHA14d196bafe451085a3c6f7de4cd5f3fac4cec27a8deac5f1ccd848d06b1eae3c and testsbac6e8970a65510377ed45c9ac487749673e7432980e3ff043e34a8e77917b29. Current reported51 fake-image and14 promotion cases pass. Check actual digest-matched settings, successful same-candidate suite/image/promotion, required-ref/all-container observation, no candidate/unknown/tag/force/prune deletion, exact before/after CLI proof and durable concurrency/uncertain replay limits. Identify concrete counterexamples only; no broad audit or real Docker operation. Missing same-intent recording reconciliation stays explicit rather than becoming a fabricated pass.

## Definition of Done

Save exact ACCEPT/REJECT, focused evidence/confidence and blocking findings. Actual image, full Release and provider/runtime gates remain separate.

## Result

Independent read-only review: ACCEPT at96%, no blocking finding in the bounded P1707 delta. Verified release_image.py SHA-256 14d196bafe451085a3c6f7de4cd5f3fac4cec27a8deac5f1ccd848d06b1eae3c; tests bac6e8970a65510377ed45c9ac487749673e7432980e3ff043e34a8e77917b29; D573@2 5db7045ec34fbd9aea129d63262f6fce1ac5a6bff2b147af90a9fad6e560adad.

- Settings are reopened and checked against their sealed digest and exact admitted retention table.
- Successful same-candidate promotion, suite, immutable build/canary, package, selector and Skill evidence are independently reopened before removal.
- Every listed running or stopped container is inspected by immutable image ID; incomplete observation blocks removal.
- An exclusive durable intent precedes only non-forced docker image rm of the exact prior image. Candidate, unknown, mutable-tag and broad-prune targets are not admitted.
- Exact disappearance and a complete immutable inventory must agree; uncertain effects and failed recording cannot become success or implicit replay.

The reviewer ran no tests or Docker operations. Earlier51 image/14 promotion passes are historical, not refreshed execution proof. Durable same-intent recording reconciliation remains unimplemented. Actual Docker, complete Release, public/provider/runtime and restart gates remain separate. The intent is scoped to the candidate/prior pair, not a global Docker lock.
