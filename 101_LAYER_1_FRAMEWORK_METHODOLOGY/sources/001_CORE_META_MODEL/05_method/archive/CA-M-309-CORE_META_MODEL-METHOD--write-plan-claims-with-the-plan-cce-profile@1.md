---
cce_version: cce_1
cce_form: method
subjects:
  governs: "CCE/Role Profile: Plan"
  depends_on:
    - "Atom/Content Role: Plan"
    - "Atom/Content Role: Plan/Type: Plan"
    - "Atom/Content Role: Plan/Type: Plan/Definition of Done"
    - "CCE Operator"
version: 1
updated_at: "2026-09-22 18:51:52 +0400"
relations:
  child_of:
    - CA-M-307
  relates_to:
    - CA-M-123
    - CA-M-306
    - CA-R-1575
    - CA-R-1581
---
# Write Plan Claims with the Plan CCE Profile

**to** write a Plan Claim with the Plan CCE Role Profile, the Author **must** perform **all** of:

1. state the Plan's primary contribution as intended work, an intended outcome, **or** their governed composition under CA-M-306.
2. **if** the Plan has own work, identify the action, its object, intended result, Assignee, **and** applicable boundary explicitly. modality, condition, temporal, quantification, logical, restriction, predicate, **and** comparison Operators **may** qualify that intended work.
3. **if** the Plan is supported **only** by decomposition, state its intended outcome **without** inventing own work.
4. keep reusable procedure authority, normative product boundaries, current realization facts, **and** reusable operational behavior outside the Plan's primary contribution.
5. write the Definition of Done as the subordinate falsifying Condition Expression under CA-M-123. condition, temporal, quantification, logical, predicate, restriction, **and** comparison Operators **may** occur **in** that slot **only** to determine whether the Plan remains not Done.
6. keep optional Details subordinate **to** the same intended work **or** outcome; Details **must not** introduce another intended outcome **or** a second Definition of Done.

an action word **in** a Plan identifies intended work. it does **not** define a reusable Operations Action.
