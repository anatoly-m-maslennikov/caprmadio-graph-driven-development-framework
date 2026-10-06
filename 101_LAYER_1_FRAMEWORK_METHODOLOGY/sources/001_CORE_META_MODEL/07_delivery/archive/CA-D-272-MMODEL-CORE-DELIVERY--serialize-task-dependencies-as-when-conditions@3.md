---
atom_id: CA-D-272
cce_version: cce_1
cce_form: serialization
subjects:
  governs:
    continuant:
      - "Atom/Content Role: Plan/Plan Type: Task/Dependency/Claim Serialization"
  depends_on:
    continuant:
      - "Atom/Content Role: Plan/Plan Type: Task/Dependency"
version: 3
updated_at: 2026-08-29 02:40:41 +0400
relations: {}
---
# Serialize Task Dependencies as When Conditions

**every** Task Dependency **must** be serialized **in** the dependent Task Claim as `**when** <TASK_ATOM_ID> is Done, **then** ...`.
