---
subject_scopes:
  - feature-boundary
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
version: 5
updated_at: 2026-08-23 15:33:04 +0400
---
# Own deterministic scripts in Tools

Every independently executable deterministic script must realize exactly one Tool, and every Tool must have exactly one canonical independently executable script, including a Tool invoked exclusively by a Skill. Shared non-executable libraries may serve multiple Tools but do not constitute Tools themselves.
