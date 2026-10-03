---
content_role: Requirement
type: Requirement
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
author: Anatoly Maslennikov
status: Draft
cce_version: cce_1
cce_form: obligation
subjects:
  governs: "Tool/mutation completion"
  depends_on:
    - "Carrier"
    - "Journal"
    - "Operator"
    - "Tool"
version: 1
updated_at: "2026-09-23 19:20:45 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {"relates_to": ["CA-E-001", "CA-M-161", "CA-M-289", "CA-R-1064", "CA-R-1490"]}
---
# Summary

Report mutation success only after its durability boundary

## Claim

a mutating Tool **must** report successful completion **only** **after** **all** effects, child-process outcomes, **and** recovery records required by its declared completion **and** durability boundary are confirmed.

- an accepted atomicity guarantee covers **only** its declared effects **and** supported substrate; a partial operation **must not** be reported as fully atomic.
- **when** full atomicity is unavailable, the admitted recovery boundary **must** preserve enough durable identity **and** state **to** distinguish completed, incomplete, **and** uncertain effects **without** guessing which state is authoritative.
- an unmet **or** uncertain completion condition remains an explicit incomplete, failed, **or** uncertain result, **not** success **or** permission **to** repeat a non-repeatable effect.

file, subprocess, staging, **and** temporary-location techniques remain governed by CA-M-161 **and** CA-M-289. this Requirement adds no universal filesystem guarantee, retry algorithm, automatic rollback, **or** second Journal.
