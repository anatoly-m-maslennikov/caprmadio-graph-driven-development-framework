---
atom_id: MOCK-R-2
content_role: Requirement
type: Requirement
current_scope_unit: DEMO
claim_target_scope_unit: DEMO
local_tier: Standard
global_tier: 11
status: Active
author: Fixture Operator
version: 1
updated_at: "2026-09-25 21:01:05 +0000"
subjects:
  governs: "Widget/Color"
  depends_on: ["Widget", "Widget/Color: Blue", "Widget/Status", "Widget/Status: Active", "Widget/Status: Queued"]
relations: {}
---
# Summary

use Blue for Active or Queued Widgets on public displays

## Scope

the Color of a Widget **in** a public display **where** its Status is Active **or** Queued.

## Claim

the Color of a Widget **must** be Blue.

## Details

Blue is the admitted display value.
