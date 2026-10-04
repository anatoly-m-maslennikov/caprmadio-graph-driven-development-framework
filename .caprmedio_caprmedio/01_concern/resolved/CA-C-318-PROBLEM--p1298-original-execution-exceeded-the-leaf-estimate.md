---
atom_id: CA-C-318
content_role: Concern
type: Problem
label: Problem
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
status: resolved
subjects:
  governs: "CA-P-1298 elapsed execution and recovery"
relations:
  concern_about: [CA-P-1298]
version: 1
updated_at: "2026-10-04 13:41:16 +0400"
---
# Summary

P1298 original execution exceeded the leaf estimate

## Concern

The original P1298 worker started2026-10-04 09:12:48UTC but did not persist a complete result, actual continuation, Carrier proof andterminal receipt within its15-minute bound ending09:27:48UTC. A separate bounded recovery began2026-10-04 09:18:43UTC, retaining the original clock andunfinished state. The original interval is not restated as a <=15-minute successful execution.

## Evidences

Recovery fully read68whole native texts and16fullcontexts, corrected snippet dispositions into68source-specific dispositions/sixhuman chains/sixprovisionalgroups, repaired required Carrier fields andbound actualP1303/A1021. Native/saved proof passed09:27:20UTC; final closing persistence/Carrier verification occurs after theoriginaldeadline. P1298/A1016 record theactualterminalclock forbothelapsedintervals. C317 separately owns thecontext-key defect. No resets, inferred finishes, source/currentimplementation reports or partial bytes are substituted for actual completion.

### Actual terminal timing

Terminal proof2026-10-04 09:30:41UTC follows persistence09:29:29UTC: original09:12:48→09:30:41 elapsed17minutes53seconds>15; separate recovery09:18:43→09:30:41 elapsed11minutes58seconds<=15. All four owned carriers plusC317/C318 passed strict saved YAML/headings/fields/EOF/Doneplacement/localDAG. Native/saved68+16 andactual31+19/followingwhole boundary passed. The original estimate remains exceeded, qualified by the completed bounded recovery.

Final persisted receipt validation and actual terminal clock2026-10-04 09:32:49UTC: original09:12:48→09:32:49 elapsed20minutes01seconds>15; recovery09:18:43→09:32:49 elapsed14minutes06seconds<=15. The09:30:41 native/saved/Carrier result above is an earlier verification checkpoint. The final saved receipt was reopened and its clocks/Done+Active placement/headings/EOF/disposition counts passed; no next execution. A rejected oversized patch serialization made no edits; bounded hunks persisted the receipt.

## Blast radius

The original leaf estimate was exceeded; sourcecoverage/frozenwindow/authority boundaries remain intact. Resolution means the distinct recovery completed durableharvest/actualnext/localproof withinitsown15-minute interval, qualified by the preserved original overrun. Parent1128remainsActive andallstage gates/sourcefrontiers persist. No new execution is authorized by this Concern.
