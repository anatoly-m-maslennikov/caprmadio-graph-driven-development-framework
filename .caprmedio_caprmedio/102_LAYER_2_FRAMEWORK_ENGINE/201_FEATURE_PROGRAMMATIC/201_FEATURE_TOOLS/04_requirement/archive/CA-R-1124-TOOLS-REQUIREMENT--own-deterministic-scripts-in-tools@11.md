---
subjects:
  governs: "feature-boundary"
  depends_on: []
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
version: 11
updated_at: 2026-08-30 16:44:07 +0400
---
# Own deterministic scripts in Tools

**every** independently executable deterministic script **must** realize exactly one Tool, **and** **every** Tool **must** have exactly one canonical independently executable script, including a Tool invoked exclusively by a Skill. Shared non-executable libraries **may** serve multiple Tools but do **not** constitute Tools themselves.
