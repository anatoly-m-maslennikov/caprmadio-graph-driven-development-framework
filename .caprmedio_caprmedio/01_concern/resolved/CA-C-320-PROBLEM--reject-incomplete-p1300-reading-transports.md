---
atom_id: CA-C-320
content_role: Concern
type: Problem
current_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
status: resolved
subjects:
  governs: "Native evidence transport completeness"
  depends_on:
    - "Artifact"
version: 2
updated_at: "2026-10-04 14:07:05 +0400"
relations:
  concern_about:
    - CA-P-1300
    - CA-P-1304
---
# Summary

Reject incomplete packet reading transports

## Concern

Three P1300 read attempts were rejected before admitting source reading: an oversized combined output and two invalid script-input attempts. The initial generic guard did not distinguish their failure reasons.

## Evidences

The root rejected nonzero or truncated outputs before parsing or counting their text. It then decoded serialized JSON explicitly and split native reads into three whole-record groups of nine. All27 whole texts and original parts, plus all nine bound full antecedents, were successfully loaded. No failed read became an evidence disposition or pass. Native/saved proof still governs final admission.

## Blast radius

P1300 reading only. Corrected transports restored complete access; no source was unavailable, no snapshot changed, and no framework Tool or runtime code was modified. The original execution clock was not reset.

### P1304 recurrence and recovery

The initial combined metadata/binding view exceeded the output budget and was rejected without any source-reading coverage. A guessed C320 filename lookup also failed; the exact existing path was then resolved and read. All53 native selected/context records were extracted with successful complete raw/text hash checks and read in bounded whole-record views. The original09:57:24UTC execution clock is unchanged. No missing source, current Tool defect or new lifecycle policy is inferred from these transport/lookup failures; one native/saved proof governs terminal admission.

Terminal receipt: 2026-10-04 10:07:05 UTC. Actual elapsed 581 seconds from unchanged 2026-10-04 09:57:24 UTC. Full frozen-prefix/native/saved 21 records/32 contexts and original parts, aggregates, actual next27/27/full following L9937, disjoint selections and29 governing source hashes passed. Shared strict147 Plans/106 supporting carriers and completion/BLOCKS DAG passed. This is persistence/provenance proof, not a second semantic review; Git/recovered Journal follows separately.
