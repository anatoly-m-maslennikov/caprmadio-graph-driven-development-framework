---
subject_scopes:
  - scope-topology
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-REQU-061--define-implementation-layer-scope-and-contracts
    - CAPRMEDIO-CNTR-001--map-spec-features-to-implementation-realizations
  replacement_of:
    - CAPRMEDIO-REALIZATION-REQU-600--realize-canonical-spec-features
---
# Define IMPLEMENTATION Feature scopes

IMPLEMENTATION defines this ordered Feature partition for realized framework artifacts:

1. METHODOLOGY — operational methodology files and cases.
2. TOOLS — deterministic executables, libraries, migrations, and generated controls.
3. SKILLS — agent-facing Skill packages and routing wrappers.
4. PROFILES — reusable realization practices and their supporting assets.
5. ADAPTERS — provider, platform, host-runtime, and external-system integrations.
6. EVALUATION — executable Tests, Evaluations, checks, evaluators, and fixtures.
7. DOCUMENTATION — README, navigation, examples, and maintained framework documentation.

Other realized artifacts belong to their applicable IMPLEMENTATION Feature rather than defining additional Feature scopes.
