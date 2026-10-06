---
subjects:
  governs: "Atom/Carrier"
  depends_on:
    - "Atom/Content Role"
    - "Priority"
    - "Atom/Content Role: Plan/Type: Plan"
version: 6
updated_at: "2026-09-22 14:41:44 +0000"
relations: {}
---
# Serialize Concern Priority

a Concern Atom Carrier **must** serialize **`=1`** selected Priority as `priority` with the lowercase value `high`, `medium`, **or** `low`. **every** non-Concern Content Role Atom Carrier **must** omit `priority`; virtual `highest` **must not** be stored.
