---
content_role: Delivery
type: Delivery
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
author: Anatoly Maslennikov
status: Draft
cce_version: cce_1
cce_form: serialization
subjects:
  governs: "PROGRAMMATIC/software-source distribution"
  depends_on:
    - "Artifact/Carrier"
    - "Atom/Content Role: Implementation"
    - "PROGRAMMATIC/software carriers"
    - "Project Temporary State"
version: 1
updated_at: "2026-09-23 19:08:49 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {"delivery_for": ["CA-M-162"], "relates_to": ["CA-D-250", "CA-D-437"]}
---
# Summary

Separate generated outputs from hand-authored software sources

## Claim

the hand-authored software-source portion of a PROGRAMMATIC source distribution **must** exclude generated Runtime **and** Delivery outputs.

- generated outputs use their separately declared output locations under CA-D-250; temporary build, staging, **and** cache Carriers use CA-D-437. those locations **must not** overlap the hand-authored source portion.
- this source boundary does **not** prohibit packaging an admitted generated output **in** its separately declared installable-output portion.
