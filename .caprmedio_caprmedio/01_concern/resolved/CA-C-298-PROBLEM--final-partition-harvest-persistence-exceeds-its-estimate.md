---
atom_id: CA-C-298
content_role: Concern
type: Problem
current_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
status: resolved
subjects:
  governs: "Final-partition harvest execution estimate"
  depends_on:
    - "Project"
    - "Operations"
version: 1
updated_at: "2026-10-04 08:27:15 +0400"
relations:
  concern_about:
    - CA-P-1193
    - CA-P-1207
---
# Summary

Final-partition harvest persistence exceeds its estimate

## Concern

1193's hundred selected messages were fully read,but root coordination/context continuation delayed durable output beyond the original fifteen-minute estimate. Complete semantic reading is not sufficient to mark1193 Done while persistence/verification remains unfinished.

## Evidences

1193 was executing before root's2026-10-04T04:17:57Z clock; the first retained incomplete persistence clock is04:22:58Z. Exact working-time accounting was not measured; do not claim an exact elapsed pass. Root binds remaining save/check work as actual child1207 with a <=5-minute estimate and records actual results before closure. Selected100raw aggregate0a983c5940b3f1e608b44c9d2b88383fe2d6c7de03a7289152a3423f7f95bdc1 is independently reverified; no lost source fragment is asserted.

## Blast radius

Resolved scheduling disposition: root createdactualcompletionchild1207,savedA914/next1203/1129,andpassedsource/disposition/count/hash/headings/whitespace/rootparser-DAGchecks by04:27:15Z,4m17safterboundstart.1193closesascompositewithcompletedremainder;originalelapsedoverrunisnoterased.Nosourcecontentorlaterstagewasdeclaredcompletefromtimingrepair.

Only1193 persistence and its next1203 readiness. Parent1129/1118 remain Active; no authoring/implementation gate is released. Resolution requires saving/verifying the bound remainder,not a false timing receipt or reprocessing an unchanged source.
