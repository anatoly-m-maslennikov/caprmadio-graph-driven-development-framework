---
atom_id: CA-D-273
cce_version: cce_1
cce_form: serialization
subjects:
  governs:
    continuant:
      - "Atom/Content Role: Plan/Type: Task/Autonomous Confidence Threshold/Frontmatter"
  depends_on:
    continuant:
      - "Autonomous Confidence Threshold"
      - "Markdown Atom Carrier"
      - "Property"
version: 6
updated_at: "2026-09-09 02:24:28 +0400"
relations: {}
---
# Serialize explicit Task confidence-threshold overrides

**if** a Task has an explicitly selected Autonomous Confidence Threshold override, **then** its Markdown Atom Carrier **must** serialize that integer as `autonomous_confidence_threshold`; **otherwise** the Carrier **must** omit that Property **and** preserve inherited resolution.
