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
version: 4
updated_at: 2026-09-06 01:45:12 +0400
relations: {}
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1317-CORE_META_MODEL-CORE-REQUIREMENT--fail-closed-on-unresolved-methodology-conflicts.md
---
# Fail Closed on Unresolved Methodology Conflicts

**if** an Applicable Methodology conflict lacks one exact Operator approval recorded **in** source authority **and** bound to the exact conflict **and** source-frontier digest, **then** compilation **must** fail **without** changing Applicable Methodology membership.
