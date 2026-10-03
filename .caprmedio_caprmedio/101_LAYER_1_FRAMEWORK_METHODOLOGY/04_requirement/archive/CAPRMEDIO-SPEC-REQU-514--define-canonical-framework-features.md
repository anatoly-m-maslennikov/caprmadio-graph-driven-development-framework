---
subject_scopes:
  - scope-topology
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-REQU-060--define-spec-layer-scope-and-contracts
    - CAPRMEDIO-CNTR-001--map-spec-features-to-implementation-realizations
---
# Define canonical framework Features

SPEC defines this ordered canonical Feature partition:

1. METHODOLOGY — operational cases and playbooks consumed by Skills and Evaluation.
2. TOOLS — deterministic operations, command-line behavior, migrations, and generated controls.
3. SKILLS — thin agent-facing wrappers and gated Skill chaining.
4. PROFILES — reusable practices selected for a project or component.
5. ADAPTERS — provider, platform, host-runtime, and external-system integrations.
6. EVALUATION — Test Cases, Evaluation Cases, checks, evaluators, and evaluation execution.
7. DOCUMENTATION — README and framework documentation, navigation, examples, portability, and freshness.

Templates, schemas, shared libraries, Tests, Evaluations, installation logic, and generated dashboards belong to their applicable canonical Feature rather than defining additional Features.
