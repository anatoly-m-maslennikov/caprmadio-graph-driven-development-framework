---
atom_id: CA-C-362
content_role: Concern
type: Problem
current_scope_unit: caprmedio
claim_target_scope_unit: METHODOLOGY_SOURCES
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "F16 saved-candidate evidence read-boundary failure"
  depends_on: [Operations, "Atom/Content Role: Analysis"]
version: 3
updated_at: "2026-10-04 13:13:47 +0000"
relations:
  concern_about: [CA-P-1361]
  relates_to: [CA-A-1079, CA-A-933]
---
# Summary

Retain the F16 evidence read-boundary failure

## Concern

The F16 assignment prohibited native session and raw embedded-record reads. An initial broad locator over saved A933 returned raw embedded-record text excerpts after the candidate section. This was a real intake scope failure; it cannot be undone or reported as a pristine candidate-only read.

## Evidences

The locator searched A933 for legacy/RMED/candidate terms and displayed matches beyond its line-94 raw-record heading, including embedded-record excerpt lines 1234 onward. No native session file or session index was opened. The coordinating agent was informed immediately. Subsequent A933 intake was limited to lines 1–93: the saved H07/EV03 qualifiers and W2 candidate. A1079 relies only on those saved candidate sections, A1063's exact assignment and fully read current governing sources; accidentally displayed raw excerpts are excluded from its evidentiary basis.

The same bounded preparation resolved mistaken control-directory/carrier basename lookups with exact current filenames. A broad filename filter containing “rmed” also returned unrelated source filenames because “caprmedio” occurs in every path; that locator output is not an authority comparison or evidence of full reads. Neither transport error changes the bound family or permits additional scope. Two saved gate attempts actually failed as P1130 changed v3→v4→v5 concurrently. Both changed full carriers were reread and their binding refreshed; these failed checks are not PASS evidence. First actual clock remains 2026-10-04 12:56:53 UTC.

## Blast radius

Limited to P1361 evidence-intake assurance and elapsed time, not native harvesting, source adoption, implementation or coverage counts. Nonblocking retained process Problem: the candidate's complete permitted saved section is available independently, the comparison excludes exposed raw text, and the substantive result can be checked against that section and current sources. This does not excuse the original scope violation or claim that guardrails prevented it. Root retains visibility for its independent review; no runtime/settings/Git/Journal or other agent files were changed as recovery.

The bounded saved gate passed at 2026-10-04 13:12:12 UTC, elapsed 15m19s from the unchanged first clock. Closure write 2026-10-04 13:13:47 UTC / elapsed 16m54s: actual estimate overrun is retained, not reset or presented as <=15 minutes. The earlier check exits on stale expected parent revisions were normal concurrent-control refresh, not additional substantive failures; root amendments did not change this family's inputs or gates. The actual read-boundary failure remains visible with its nonblocking exclusion/recovery disposition; the completed comparison has no concealed remainder.
