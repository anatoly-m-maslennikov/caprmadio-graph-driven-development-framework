---
subject_scopes:
  - requirement-topology
version: 16
updated_at: "2026-09-17 16:16:04 +0000"
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {"child_of":["CAPRMEDIO-REQU-029-CORE-REQUIREMENT--govern-each-scope-by-authority-mode"]}
cce_version: cce_1
cce_form: obligation
---
# Require parent coverage without claiming topology completeness

**in** strict authority mode, **every** active tier-classified PRMEDO Atom **must** have **`>=1`** permitted active parent **unless** the applicable Type authority registers its Type as orphan-permitted.

a permitted parent is:

- the active Project Goal Atom for a Project Principle;
- an applicable lower-global-tier Atom **in** the same structural scope; **or**
- an Atom permitted by the global tier topology **in** an ancestor structural scope.

this parent-coverage condition is necessary but insufficient for authority-topology completeness **and** cannot establish Principle-set completeness.
