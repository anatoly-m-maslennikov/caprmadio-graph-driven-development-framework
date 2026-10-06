---
cce_version: cce_1
cce_form: prohibition
subjects:
  governs: "Atom/Content Role: Plan/Type: Plan/Blocking"
  depends_on:
    - "Atom/Content Role: Plan/Type: Plan"
    - "Atom/Content Role: Plan/Type: Plan/Decomposition"
    - "Atom/Content Role: Plan/Type: Plan/Status: Done"
    - "Hub Atom"
version: 1
updated_at: "2026-09-22 14:41:44 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {"relates_to": ["CA-R-1580", "CA-R-1583", "CA-R-1538"]}
---
# Keep Plan completion prerequisites acyclic

Plan execution **must not** contain a cycle of completion prerequisites, including one formed jointly by `BLOCKS` **and** the requirement **to** complete decomposed work **before** its Hub can be Done.
