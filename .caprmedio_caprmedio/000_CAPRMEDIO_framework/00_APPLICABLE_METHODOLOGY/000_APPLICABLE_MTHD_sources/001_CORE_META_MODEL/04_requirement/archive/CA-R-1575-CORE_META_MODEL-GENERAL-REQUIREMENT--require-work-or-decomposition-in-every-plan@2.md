---
subjects:
  governs: "Atom/Content Role: Plan/Type: Plan"
  depends_on:
    - "Atom/Content Role: Plan/Type: Plan"
    - "Atom/Content Role: Plan/Type: Plan/Decomposition"
    - "Atom/Summary"
    - "Atom/Claim"
version: 2
updated_at: "2026-09-22 14:41:44 +0000"
relations: {"relates_to": ["CA-R-1574", "CA-R-1579"]}
---
# Require work or decomposition in every Plan

**every** Plan Atom **must** have **>=1** of:

- its own work content;
- **>0** outgoing `DECOMPOSES_INTO` Relations **to** other Plan Atoms.

both contributions **may** be present within the same Claim; a Summary alone **without** either contribution is insufficient.
