---
atom_id: CA-R-1317
cce_version: cce_1
cce_form: condition
subjects:
  governs:
    occurrent:
      - Applicable Methodology Compilation/Conflict Resolution
  depends_on:
    continuant:
      - Local Configuration/Operator Approval
      - Applicable Methodology/Source Frontier Digest
version: 2
updated_at: 2026-08-29 01:16:37 +0400
relations: {}
---
# Fail Closed on Unresolved Methodology Conflicts

**if** an Applicable Methodology conflict lacks one exact Operator approval recorded **in** source authority **and** bound to the exact conflict **and** source-frontier digest, **then** compilation **must** fail **without** changing Applicable Methodology membership.
