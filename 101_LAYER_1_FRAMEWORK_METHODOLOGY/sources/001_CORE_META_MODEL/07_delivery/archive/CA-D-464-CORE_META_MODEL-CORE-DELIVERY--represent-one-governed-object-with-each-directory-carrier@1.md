---
cce_version: cce_1
cce_form: cardinality
subjects:
  governs: "Directory Carrier"
  depends_on:
    - "Artifact"
    - "Structural Entity"
    - "Atom/Revision"
version: 1
updated_at: "2026-09-20 23:55:10 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {"relates_to": ["CA-D-259", "CA-D-460"]}
---
# Represent One Governed Object with Each Directory Carrier

**every** represented Directory Carrier **must** carry **`=1`** governed object Revision: either one Structural Entity Revision **or**, where an applicable Delivery rule permits it, one Atom Revision; it **must not** establish a second object merely because it contains subordinate Carriers.
