---
cce_version: cce_1
cce_form: obligation
subjects:
  declared:
    continuant:
      - principles
tier: core
version: 11
updated_at: 2026-08-29 01:16:37 +0400
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CA-M-001-PRINCIPLE-METHOD--mece_mutually-exclusive-collectively-exhaustive
    - CA-D-001-PRINCIPLE-DELIVERY--provide-replaceable-technical-realizations
---
# Keep SEMANTICS and GOVERNANCE implementation neutral

CAPRMEDIO SEMANTICS **and** GOVERNANCE authority defines universal semantics, governance invariants, **and** extension boundaries **without** depending on a programming language, LLM provider **or** model, agent host, operating system, repository host, package manager, database, deployment platform, **or** other replaceable implementation mechanism.

Mechanism-specific obligations live **in** the earliest downstream scope that owns the mechanism, such as a Method, Evaluation, Delivery, Extension, Project Adaptation, tool, skill, **or** repository configuration. A downstream Extension **or** Project Adaptation **may** specialize SEMANTICS **and** GOVERNANCE for its bounded use but cannot redefine their meaning **or** create a backward dependency.

SEMANTICS **or** GOVERNANCE **may** name a mechanism **only** **when** the mechanism itself is the explicit Entity of Concern, such as a portability boundary **or** external constraint. The reference **must not** make that mechanism a hidden prerequisite of the universal kernel.
