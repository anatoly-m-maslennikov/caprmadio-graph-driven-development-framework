---
subjects:
  governs: "Atom/Content Role: Plan/Type: Plan/Autonomous Confidence Threshold/Carrier"
  depends_on:
    - "Atom/Content Role: Plan/Type: Plan"
    - "Autonomous Confidence Threshold"
    - "Hub Atom"
    - "File Carrier"
    - "Atom/Content Role: Plan/Type: Plan/Definition of Done"
version: 3
updated_at: "2026-09-22 23:02:20 +0000"
relations: {"relates_to": ["CA-M-271", "CA-R-1428", "CA-D-470", "CA-D-460"]}
---
# Summary

Serialize explicit Plan confidence overrides

## Claim

an explicit Plan Autonomous Confidence Threshold override **must** use the top-level integer frontmatter field `autonomous_confidence_threshold` **in** that Plan Atom's own mandatory Markdown File Carrier.

- a Hub uses that same file, **not** a separately identified Objective **or** Epic settings file.
- omit an unselected override **without** copying its inherited value; the mandatory file requirement does **not** turn inheritance into a local selection.
- retain an explicit override even **when** it equals the inherited value.
- `epic_overrides` is **not** an alternative canonical encoding.
