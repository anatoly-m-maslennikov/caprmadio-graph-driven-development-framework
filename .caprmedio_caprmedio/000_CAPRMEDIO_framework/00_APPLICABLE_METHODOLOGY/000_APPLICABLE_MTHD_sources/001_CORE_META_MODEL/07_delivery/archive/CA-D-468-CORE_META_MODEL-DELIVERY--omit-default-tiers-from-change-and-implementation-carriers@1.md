---
cce_version: cce_1
cce_form: serialization
subjects:
  governs: "Carrier/Local Tier Representation"
  depends_on:
    - "Change Content Roles"
    - "Implementation"
    - "Atom Collection"
    - "Artifact/Carrier"
    - "Atom/Local Tier: Standard"
    - "Projection"
version: 1
updated_at: "2026-09-21 00:57:42 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {"delivery_for": ["CA-R-1566", "CA-R-1567", "CA-R-1571"], "relates_to": ["CA-D-285"]}
---
# Omit default tiers from Change and Implementation carriers

a Carrier for CAPO **or** I content **or** its collection grouping **must** omit an explicit Local Tier token **or** field **when** representing its default Standard classification.

this omission does **not** add Atom metadata **to** a non-Atom Artifact **or** alter fields **in** represented source content; a Projection's source representation continues **to** follow its own Delivery authority.
