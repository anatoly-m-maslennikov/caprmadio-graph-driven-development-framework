---
cce_version: cce_1
cce_form: permission
subjects:
  governs: "AI Agent/authorization"
  depends_on:
    - "AI Agent"
    - "Atom/Content Role: Concern"
    - "Atom"
    - "Operator"
    - "Atom/Content Role"
    - "AI Agent Delegation"
    - "AI Agent/Confidence"
    - "Autonomous Confidence Threshold"
version: 1
updated_at: "2026-09-17 16:04:33 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {"child_of":["CA-R-846","CA-P-034"],"relates_to":["CA-R-1058","CA-R-815","CA-R-846","CA-O-049"]}
---
# Let AI Agents resolve Concerns under bounded authority

an identified AI Agent **may** resolve a Concern from active Atoms **when** its active Operator delegation permits **every** required action **and** resolution confidence meets the configured semantic-resolution threshold; the resolution **may** create **or** change Atoms **in** other Content Roles **only** within that same delegated authority.
