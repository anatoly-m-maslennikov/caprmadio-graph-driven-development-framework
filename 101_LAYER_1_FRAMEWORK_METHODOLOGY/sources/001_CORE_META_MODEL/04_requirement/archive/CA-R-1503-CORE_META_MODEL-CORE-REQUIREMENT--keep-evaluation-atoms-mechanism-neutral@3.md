---
subjects:
  governs: "Atom/Content Role: Evaluation"
  depends_on:
    - "Atom/Claim"
    - "Atom/Content Role: Implementation"
version: 3
updated_at: "2026-09-17 11:52:27 +0000"
relations: {}
atom_id: "CA-R-1503"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
type: "Requirement"
---
# Keep Evaluation Atoms mechanism-neutral

an Evaluation Atom **must** define the checked Claim, applicable conditions, acceptance criteria, **and** disposition rule **without** prescribing the mechanism that realizes its check.

automated tests, model-judged evaluations, statistical assessments, rubrics, manual reviews, **and** other implementation mechanisms **may** realize that check. choosing a mechanism does **not** change the governing Evaluation Atom's Claim.
