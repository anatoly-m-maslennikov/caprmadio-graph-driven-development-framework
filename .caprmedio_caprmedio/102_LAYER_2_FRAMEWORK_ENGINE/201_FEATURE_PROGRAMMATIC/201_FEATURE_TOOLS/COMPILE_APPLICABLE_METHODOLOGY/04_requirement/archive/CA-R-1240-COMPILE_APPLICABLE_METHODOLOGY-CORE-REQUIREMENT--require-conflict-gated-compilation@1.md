---
atom_id: CA-R-1240
cce_version: cce_1
cce_form: obligation
subjects:
  governs:
    continuant:
      - Tool/COMPILE_APPLICABLE_METHODOLOGY
  depends_on:
    continuant:
      - Applicable Methodology/Compilation Output
      - Applicable Methodology/Sources/Local Configuration
version: 1
updated_at: 2026-08-27 21:37:28 +0400
relations: {}
---
# Require Conflict-Gated Applicable Methodology Compilation

the `COMPILE_APPLICABLE_METHODOLOGY` Tool **must** dry-run the complete eligible Source Frontier before every apply, report every governed conflict with one deterministic Candidate resolution, and leave generated output unchanged unless each conflict has exactly one durable Operator approval in `003_LOCAL_CONFIGURATION/applicable_methodology_conflict_approvals.toml` whose schema, conflict ID, source-frontier digest, selected Source Carrier path, and Operator identity exactly match the dry-run report.
