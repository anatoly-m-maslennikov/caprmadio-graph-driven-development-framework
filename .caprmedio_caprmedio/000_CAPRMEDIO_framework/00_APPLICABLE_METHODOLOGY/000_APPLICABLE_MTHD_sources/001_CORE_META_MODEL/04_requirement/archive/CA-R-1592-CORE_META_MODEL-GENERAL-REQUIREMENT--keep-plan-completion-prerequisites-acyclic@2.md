---
subjects:
  governs: "Atom/Content Role: Plan/Type: Plan/Blocking"
  depends_on:
    - "Atom/Content Role: Plan/Type: Plan"
    - "Atom/Content Role: Plan/Type: Plan/Decomposition"
    - "Atom/Content Role: Plan/Type: Plan/Status: Done"
    - "Hub Atom"
version: 2
updated_at: "2026-09-22 14:41:44 +0000"
relations: {"relates_to": ["CA-R-1580", "CA-R-1583", "CA-R-1538"]}
---
# Keep Plan completion prerequisites acyclic

Plan execution **must not** contain a cycle of completion prerequisites, including one formed jointly by `BLOCKS` **and** the requirement **to** complete decomposed work **before** its Hub can be Done.
