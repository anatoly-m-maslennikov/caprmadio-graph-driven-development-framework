---
atom_id: CA-C-456
content_role: Concern
type: Problem
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: resolved
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-05 04:21:12 +0000"
subjects:
  governs: "Release compiler execution identity"
  depends_on: [Atom, Carrier, Tool, Evaluation]
relations:
  concern_about: [CA-P-1650, CA-D-567, CA-D-571]
---
# Summary

Record Release compiler evidence identity mismatch

## Concern

The initial P1650 helper executed the installed compiler module but could hash different Project-declared compiler bytes in its success evidence. A disposable fixture stub would therefore be named as if it executed. The saved repair requires declared entrypoint bytes to match the actual executing module before effects; mismatched bytes refuse. The dedicated real-render corpus passes four tests, including this refusal. release_compilation.py SHA-256 is 0c7efbceba973198399a8f5dfcf43ea805868ec463b6588ccced1533be76e148. This resolves the local compiler identity gap, not actual repository Release or image acceptance.

## Evidences

The directly affected Task preserves the exact resulting files, source pins, actual focused test outputs and remaining coverage.

## Blast radius

The narrow implementation slice named above. No broader source audit, runtime promotion or denied-operation workaround is authorized by this record.
