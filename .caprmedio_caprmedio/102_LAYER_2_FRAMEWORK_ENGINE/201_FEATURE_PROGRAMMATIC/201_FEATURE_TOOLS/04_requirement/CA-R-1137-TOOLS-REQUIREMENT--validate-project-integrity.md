---
subjects:
  governs: "artifact-validation"
  depends_on:
    - "Project Settings"
    - "Framework Instance Settings"
    - "Atom/Content Role: Operations"
    - "Projection"
    - "Journal"
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
version: 10
updated_at: "2026-09-17 19:56:38 +0000"
---
# Validate project integrity

the framework **must** provide one deterministic read-only Tool that validates a selected Project scope as one integrated repository.

the Tool **must** apply Carrier validation **to** **every** selected Atom **and** check **all** of the following:

- unique identity resolution;
- registered structural **and** lifecycle topology;
- registered Relation **and** authority-graph rules applicable **to** RMEDO Atoms;
- authority modes **and** applicable Settings authority;
- Projection currentness;
- Journal replay integrity;
- Revision **and** proof provenance;
- generated-data stage direction;
- control-root/runtime hygiene.

the Tool **must** emit stable diagnostics **without** mutating Project files.
