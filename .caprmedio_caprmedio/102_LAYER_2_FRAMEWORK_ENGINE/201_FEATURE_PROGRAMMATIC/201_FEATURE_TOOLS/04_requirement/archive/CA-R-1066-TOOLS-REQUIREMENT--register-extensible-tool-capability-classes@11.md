---
subjects:
  governs: "feature-boundary"
  depends_on: []
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
version: 11
updated_at: "2026-09-16 23:48:40 +0000"
---
# Register extensible Tool capability classes

Every Tool must register exactly one primary Tool kind: `finder` for strictly read-only retrieval or evaluation, or `doer` for governed mutation or materialization. `checker` is a registered Finder specialization that applies explicit Evaluation criteria and returns issues, evidence, or a verdict; additional specializations may extend a primary kind only through explicit registration of their semantics and interface obligations.

Capability class is not an operation-semantics owner. The registered canonical Tool owns the behavior of its public operation; generic Artifact Tools own only form-agnostic mechanics, while CAPRMEDIO Markdown Atom Tools own Atom-specific identity, admission, lifecycle, and mutation behavior. A Doer must default to dry run and require explicit `--apply`; a Finder must never mutate.
