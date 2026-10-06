---
atom_id: CA-D-444
cce_version: cce_1
cce_form: obligation
subjects:
  governs: "Project Structure"
  depends_on:
    - "Carrier"
    - "Project Structure Maintenance"
    - "Operator"
version: 1
updated_at: "2026-09-15 00:13:02 +0000"
relations:
  child_of:
    - "CA-D-440"
  relates_to:
    - "CA-O-015"
---
# Separate candidate Project Structure from active authority

a staged Project Structure candidate **must** use the filename `project_structure.candidate.toml` inside the explicitly selected migration workspace, outside the canonical active path. no ordinary consumer **may** discover it as active authority; candidate validation requires an explicit candidate path. cutover **must** install the validated candidate at the canonical path **only** after freshness, authorization, reference repairs, consumer readiness **and** recoverability checks pass. the old active bytes **must** remain recoverable through accepted change evidence **without** becoming another active structural source. the candidate **must** be retired **after** successful activation **or** rejection; failure **must not** leave two files eligible for normal authority resolution.
