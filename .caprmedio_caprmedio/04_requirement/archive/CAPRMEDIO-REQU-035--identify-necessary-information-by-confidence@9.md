---
tier: core
version: 9
updated_at: "2026-09-05 23:00:00 +0400"
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CA-M-003
subjects:
  governs:
    occurrent:
      - "Project/information necessity assessment"
  depends_on:
    continuant:
      - "Project"
      - "Atom/Local Tier: Principle"
      - "Atom"
cce_version: cce_1
cce_form: obligation
atom_id: CAPRMEDIO-REQU-035
---
# Identify necessary information by confidence

**to** determine whether Project information is necessary, an LLM **must** inspect **every** active Project Principle, **every** active Atom **in** the information's full ancestor **and** descendant lineage, **and** **every** other active Atom **in** the same structural scope. the information is necessary **when** its omission would leave the LLM below the effective framework-owned confidence threshold configured for the active `FRAMEWORK_ENGINE`. the confidence **and** threshold are operational heuristics, **not** comparable probabilities across configurations.
