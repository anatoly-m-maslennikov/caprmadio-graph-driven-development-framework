---
cce_version: cce_1
cce_form: obligation
subjects:
  governs: "Tool/COMPILE_APPLICABLE_METHODOLOGY"
  depends_on:
    - "Applicable Methodology/Compilation Output"
    - "Applicable Methodology/Sources/Project Configuration"
version: 6
updated_at: "2026-09-11 23:47:49 +0400"
relations: {}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Require Conflict-Gated Applicable Methodology Compilation

the `COMPILE_APPLICABLE_METHODOLOGY` Tool **must** dry-run the complete eligible Source Frontier before every apply, report every governed conflict with one deterministic Candidate resolution, and leave generated output unchanged unless each conflict has exactly one durable Operator approval in `003_PROJECT_CONFIGURATION/applicable_methodology_conflict_approvals.toml` whose schema, conflict ID, source-frontier digest, selected Source Carrier path, and Operator identity exactly match the dry-run report.
