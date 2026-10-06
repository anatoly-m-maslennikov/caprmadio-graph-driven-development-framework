---
cce_version: cce_1
cce_form: definition
subjects:
  governs: "Publish Reconciled Projection"
  depends_on:
    - "Action"
    - "Projection/Type: Reconciled Projection"
    - "Artifact/Revision"
    - "Atom/Claim"
    - "Carrier"
    - "Atom/Content Role: Delivery"
version: 2
updated_at: "2026-09-14 01:36:43 +0400"
relations: {}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Publish reconciled projections

Publish Reconciled Projection **means** the reusable Action that publishes a Reconciled Projection from the exact final selected source Revisions **only** **when** the applicable required checks are complete, no conflict remains unresolved under those checks, **and** required resolution approvals remain valid for that frontier. **before** changing live output, it **must** recheck that the exact current selected sources match the assessed frontier **and** required approval bindings; unresolved **or** indeterminate checks **or** a changed frontier block publication **without** changing that output. it **must** preserve the selected source content, identities, **and** Revisions **without** Claim synthesis **or** merge **and** use the applicable Delivery authority for representation, source traceability, **and** publication. failure **must** be reported **without** claiming a completed publication; prior published state **and** recovery remain governed by applicable authority. the Action does **not** fix source conflicts by editing the result **or** gain source authority through publication.
