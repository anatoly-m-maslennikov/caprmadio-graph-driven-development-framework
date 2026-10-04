---
atom_id: CA-E-552
content_role: Evaluation
type: QA Case
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Archived
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-04 19:29:30 +0000"
subjects:
  governs: "Tool/PROJECT_STRUCTURE partial and recovery cases"
  depends_on: [Tool, Scope Unit, Project Structure, Carrier, Journal]
relations:
  relates_to: [CA-R-1662, CA-R-1831, CA-R-1832]
---
# Summary

Report partial Scope Unit cutover and authorized rollback

## Scope

An injected post-declaration failure inside one authorized recoverable cutover.

## Claim

The Evaluation **must** prove partial effects and rollback are reported precisely and no unapproved content is erased.

## Details

- Cause a reference-repair or explicitly included Carrier update to fail after a known declaration effect.
- Assert `partial` lists applied/unapplied effects, preservation/breakage, and only the pre-authorized recovery boundary; assert no completion claim.
- Exercise the authorized rollback and assert `rolled_back` identifies restored and still-broken members, retains required history/evidence, and never resets or overwrites concurrent work.
