---
subject_scopes:
  - extension-lifecycle
version: 5
updated_at: 2026-09-06 01:45:12 +0400
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  child_of:
    - CAPRMEDIO-META-REQU-160-CORE_META_MODEL-CORE-REQUIREMENT--govern-extension-semantics
    - CAPRMEDIO-REQU-702--define-framework-engine-layer-scope
---
# Guide Extension lifecycle operations

the framework **must** provide one Skill that resolves an operator's Extension install, uninstall, update, **or** downgrade intent, presents the exact source **and** target version, **and** invokes the governed Tool **only** **after** explicit approval.
