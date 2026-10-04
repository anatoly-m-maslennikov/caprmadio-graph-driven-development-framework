---
atom_id: CA-C-325
content_role: Concern
type: Problem
current_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
status: resolved
subjects:
  governs: "Harvest Carrier terminal newline"
  depends_on:
    - "Artifact"
version: 1
updated_at: "2026-10-04 14:19:05 +0400"
relations:
  concern_about:
    - CA-P-1305
    - CA-P-1309
---
# Summary

Enforce one terminal newline in harvest Carriers

## Concern

The checkpoint save gate rejected two future Plan Carriers with an extra blank line at EOF. Existing shared Carrier checking did not catch the registered single-terminal-newline boundary.

## Evidences

The actual staged whitespace check returned nonzero for P1305 and P1309; no commit ran after that rejection. The root removed their final blank lines and updated updated_at without changing Version, binding records, summaries or semantic work. The corrected staged save gate must pass before the authorized commit. This retains the failure rather than treating earlier Carrier passes as complete whitespace proof.

## Blast radius

Two actual next Plan Carriers and the current checkpoint save only. Native/current-next evidence and all processed-record totals are unchanged. No delivered checker, settings or framework implementation was changed.
