---
atom_id: CA-C-364
content_role: Concern
type: Problem
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
status: resolved
subjects:
  governs: "F18 exact saved-section coverage check"
  depends_on: [Analysis, "Atom/Content Role: Plan"]
version: 2
updated_at: "2026-10-04 13:09:29 +0000"
relations:
  concern_about: [CA-P-1363, CA-A-1081]
---
# Summary

Correct F18 saved-section locator spelling

## Concern

The first actual saved-carrier/coverage gate failed because two report-level section locators in P1363/A1081 used Results wording without the exact colon-separated A1063 locator strings. This is a narrow saved-reference serialization issue, not an omitted candidate, current taxonomy defect or changed finding disposition.

## Evidences

At 2026-10-04 13:06:51 UTC the check exited 1 at its exact_saved_section containment assertion. The bounded diagnostic showed R0323/S074, R0346/S079 and R0377/S085 matched; R0465/S107 “Results: Reusable intent groups” and R0466/S108 “Results: earlier overlapping provisional retrieval groups” did not. Both complete saved candidate sections had already been read without embedded native evidence.

At 13:07:27 UTC the Plan and Analysis strings were corrected to those exact locators. No extra source, candidate or Operation was added and no disposition changed. At 13:09:29 UTC the actual saved-carrier/coverage recheck returned PASS / exit 0, including all five exact register entries/sections, five MM/three FX subjects, eight current source Operation revisions, saved Analysis revisions, unique owned IDs/sequence, headings/type/EOF and the acyclic local completion graph. The issue is resolved; no Done claim relies on the failed check.

## Blast radius

Only P1363/A1081's exact five-entry receipt and closure gate. Parents, sources, RMED, implementation, settings, native sessions, Git and Journal are unaffected. First actual clock remains 2026-10-04 12:58:57 UTC, including diagnosis/recovery; it is not reset.
