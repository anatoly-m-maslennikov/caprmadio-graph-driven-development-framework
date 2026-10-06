---
subject_scopes:
  - scope-topology
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-META-REQU-153--preserve-bounded-meaning-across-structural-scales
---
# Govern Layer extensions

A candidate layer must declare:

- one responsibility not already owned by another layer;
- its predecessor and successor;
- accepted inputs and produced outputs;
- entry, exit, and failure behavior;
- its dependency direction; and
- why a Feature or ordinary scope cannot own the concern.

The candidate is admissible only when the resulting graph remains acyclic and
existing responsibilities remain non-overlapping. Otherwise, model it as a Feature or another governed scope rather than adding a Layer.
