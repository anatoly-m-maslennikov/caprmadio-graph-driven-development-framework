---
subjects:
  declared:
    continuant:
      - feature-boundary
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
version: 7
updated_at: 2026-08-23 16:16:20 +0400
---
# Accept common Atom target selectors

Every Atom-targeting Tool must accept the same target-selector input that addresses Atoms through composable filters for Structural unit, Content role, and Type or through one or more explicit canonical Atom filenames, and must return the fully resolved target set before performing its capability.

The selector contract supplies no Atom operation semantics. For an Atom Doer, one resolved target is an atomic action and two or more frozen resolved targets are a bulk action; the canonical Atom Tool alone owns the operation's preflight, effect, and all-or-nothing result. Generic Artifact Tools may use the selector only as a helper and must not become a public substitute for a CAPRMEDIO Markdown Atom Tool.
