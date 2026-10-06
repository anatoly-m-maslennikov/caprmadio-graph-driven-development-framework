---
cce_version: cce_1
cce_form: obligation
subjects:
  governs: "Atom/Content Role: Plan/Type: Plan/Autonomous Confidence Threshold/Carrier"
  depends_on:
    - "Atom/Content Role: Plan/Type: Plan"
    - "Autonomous Confidence Threshold"
    - "Hub Atom"
    - "File Carrier"
    - "Atom/Content Role: Plan/Type: Plan/Definition of Done"
version: 1
updated_at: "2026-09-22 14:41:44 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {"relates_to": ["CA-M-271", "CA-R-1428", "CA-D-470", "CA-D-460"]}
---
# Serialize explicit Plan confidence overrides

an explicit Plan Autonomous Confidence Threshold override **must** use the top-level integer frontmatter field `autonomous_confidence_threshold` **in** that Plan Atom's own File Carrier.

- a Hub uses the optional File Carrier of its own Carrier Bundle, **not** a separately identified Objective **or** Epic settings file.
- omit an unselected override **without** copying its inherited value.
- a folder-only Hub supplies no file-based override; do **not** create a file merely **to** materialize inheritance.
- a supplied File Carrier still requires its Definition of Done under CA-D-470.
- `epic_overrides` is **not** an alternative canonical encoding.
