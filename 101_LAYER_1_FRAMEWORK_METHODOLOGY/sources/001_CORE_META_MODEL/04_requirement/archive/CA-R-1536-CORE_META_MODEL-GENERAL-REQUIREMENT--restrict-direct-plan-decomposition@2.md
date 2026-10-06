---
cce_version: cce_1
cce_form: restriction
subjects:
  governs: "Atom/Content Role: Plan/Type: Plan/Decomposition"
  depends_on:
    - "Atom/Content Role: Plan/Type: Plan"
version: 2
updated_at: "2026-09-22 14:41:44 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {"relates_to": ["CA-R-1579", "CA-R-1576", "CA-R-1590"]}
---
# Restrict Direct Plan Decomposition

`DECOMPOSES_INTO` **must** connect **only** distinct Plan Atoms; **any** Plan **may** decompose into other Plans regardless of their Labels, **without** requiring incoming decomposition.
