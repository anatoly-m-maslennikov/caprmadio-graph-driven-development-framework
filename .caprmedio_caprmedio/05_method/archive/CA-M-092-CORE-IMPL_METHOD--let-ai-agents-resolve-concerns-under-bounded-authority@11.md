---
version: 11
updated_at: "2026-09-05 23:00:00 +0400"
relations:
  child_of:
    - CA-R-846
    - CA-P-034
  method_for:
    - CA-R-1058
    - CA-R-815
    - CA-R-846
subjects:
  governs: "Atom/Content Role: Concern/resolution"
  depends_on:
    - "AI Agent"
    - "Atom/Content Role: Concern"
    - "Atom"
    - "Operator"
    - "Atom/Content Role"
cce_version: cce_1
cce_form: permission
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Let AI Agents resolve Concerns under bounded authority

an identified AI Agent **may** resolve a Concern from active Atoms **when** its active Operator delegation permits **every** required action **and** resolution confidence meets the configured semantic-resolution threshold; the resolution **may** create **or** change Atoms **in** other Content Roles **only** within that same delegated authority.
