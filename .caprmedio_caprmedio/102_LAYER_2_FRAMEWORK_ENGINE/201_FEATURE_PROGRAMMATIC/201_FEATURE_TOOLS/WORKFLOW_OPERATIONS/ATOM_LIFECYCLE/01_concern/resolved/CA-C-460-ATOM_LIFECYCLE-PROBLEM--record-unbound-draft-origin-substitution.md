---
atom_id: CA-C-460
content_role: Concern
type: Problem
current_scope_unit: ATOM_LIFECYCLE
local_tier: Standard
global_tier: 11
status: resolved
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-05 07:10:33 +0000"
subjects:
  governs: "Draft origin provenance"
  depends_on: [Atom, Carrier, History, Tool, Evaluation]
relations:
  concern_about: [CA-P-1662, CA-P-1638, CA-D-568, CA-D-570]
---
# Summary

Record unbound Draft origin substitution

## Concern

P1638 independently rejected the current Draft-promotion implementation at96% confidence. Two actual gaps remain: demoted lineage can be changed to never_identified, and a forged descriptor can select a real unrelated immutable archive with matching Role/Summary. Existing five promotion and eighteen status/demotion passing cases do not cover these two origin substitutions. P1675-P1677 repair source and implementation; P1638 must review the exact successor before the status composite closes.

## Evidences

P1638's saved rejected review and independent origin adjudication identify the exact branches and source claims. Prior partial passing evidence is retained, not converted into a clean pass.

## Blast radius

The bounded Draft identity promotion path and its source history contract. No mandatory image/permission gate is bypassed and no broad identity registry or new Journal is introduced.

## Current native review

The repaired promotion/retry lane passes eight golden cases, fourteen status cases and eight shared status/Journal cases. Current native review still REJECTS at98%: Update loads an unrelated mutable current history reference without first validating it against the target Draft. The reviewer reproduced an applied Update which appended a child to another Draft's head and left competing canonical locators. P1699 binds pre-write unique-head validation and unchanged-tree substitution/replay tests. The parent remains Active until this required repair and current review succeed.

## Resolution

Accepted D568@5/D570@4/D569@5 target-bound retained history and P1690 atomic consumption/recovery repair the two original origin substitutions. P1694 completes exact head-first promotion retry. P1699 now validates the current target head before Draft Update reserves or writes anything; independent review ACCEPT98% reproduces the formerly applied unrelated-head probe as draft-lineage-invalid with unchanged bytes. Nine native plus fourteen status tests pass, including stale/replayed Update heads; the isolated owned staged delta also passes23 while preserving external changes. This bounded Problem is resolved; image/runtime and relocation Concerns remain separate.
