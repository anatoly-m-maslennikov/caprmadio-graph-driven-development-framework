---
cce_version: cce_1
cce_form: method
subjects:
  governs: "Atom/Content Role: Plan/Type: Plan"
  depends_on:
    - "Atom/Content Role: Plan/Type: Plan"
    - "Atom/Claim"
    - "Atom/Summary"
    - "Atom/Author"
    - "Atom/Content Role: Plan/Type: Plan/Assignee"
    - "Atom/Content Role: Plan/Type: Plan/Label"
    - "Atom/Content Role: Plan/Type: Plan/Subtype"
    - "Atom/Content Role: Plan/Type: Plan/Definition of Done"
    - "Atom/Content Role: Plan/Type: Plan/Decomposition"
    - "Atom/Content Role: Plan/Type: Plan/Blocking"
    - "Autonomous Confidence Threshold"
    - "Implementation Retry Limit"
    - "Scope Unit"
    - "File Carrier"
version: 2
updated_at: "2026-09-22 17:59:17 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {"relates_to": ["CA-R-1574", "CA-R-1575", "CA-R-1576", "CA-R-1577", "CA-R-1582", "CA-R-1584", "CA-R-1588", "CA-R-1589", "CA-R-1591", "CA-R-1418", "CA-M-123", "CA-M-271", "CA-M-295", "CA-D-470", "CA-D-471", "CA-D-474"]}
---
# Author Plan Atoms

**to** author a Plan Atom, apply the common Plan authoring rules independently of Label:

1. resolve **=1** effective Author.
2. state **=1** intended work **or** outcome Claim, supported by own work, direct decomposition, **or** both under CA-R-1575.
3. derive its Summary under CA-R-1418; retain it across Revisions **unless** a new Atom identity replaces it.
4. resolve its Claim Target Scope Unit under CA-R-1588; keep narrower **or** composite work restrictions **in** the Claim, **and** do **not** target an ancestor Scope Unit.
5. **if** it has own work, resolve **=1** effective Assignee **and** assign that work **to** that Assignee. retain the leaf-work bound under CA-R-1589.
6. **if** it has a File Carrier, write **=1** Definition of Done under CA-M-123; include the decomposed completion obligations **when** applicable. a folder-only Hub derives completion under CA-R-1583.
7. use a Label **only** for navigation; apply an authoring Subtype **only** **when** explicitly governed.
8. express required start dependencies with `BLOCKS`; derive decomposition from folders **without** duplicating it **in** frontmatter. do **not** infer execution dependencies from leading numbers.
9. resolve confidence **and** retry values from their applicable sources; store **only** explicitly selected overrides on this Plan.
10. keep optional Details within the Claim **and** its restrictions **without** another intended outcome.
