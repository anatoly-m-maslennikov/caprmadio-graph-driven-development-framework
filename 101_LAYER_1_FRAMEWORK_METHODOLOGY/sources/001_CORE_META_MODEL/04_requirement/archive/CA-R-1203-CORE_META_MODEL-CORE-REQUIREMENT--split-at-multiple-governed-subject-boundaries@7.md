---
atom_id: CA-R-1203
cce_version: cce_1
cce_form: requirement
subjects:
  governs: "Atom/Claim"
  depends_on:
    - "GOVERNS"
    - "Subject"
version: 7
updated_at: "2026-09-14 04:00:22 +0400"
relations: {}
---
# Split at Multiple Governed Subject Boundaries

an Atom **must** be split **if** its Claim governs **`>1`** canonical targets through GOVERNS Subject Relations, whether those targets are Entities, Actions, **or** Processes.
