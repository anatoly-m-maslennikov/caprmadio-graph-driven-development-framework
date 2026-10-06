---
artifact_subtype: technical_decision
subject_scopes:
  - methodology
tier: core
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: replacement_of
    targets:
      - CAPRMEDIO-GOV-METH-012--governance-constitution-and-rule-evaluation
  - type: child_of
    targets:
      - CAPRMEDIO-META-REQU-088--meta-eligibility-rule
      - CAPRMEDIO-META-REQU-096--propagate-caprmedio-change-forward
---

# Use one governance constitution

META owns the layer constitution and governance invariants. GOV is its only
direct governance implementation owner and defines the project-local carrier,
catalog, settings, admission, precedence, maintenance, and evaluation rules.
No sibling registry, rule family, or proof source may become an independent
constitutional root.

Accepted authority and its evaluation remain distinct. Evidence and
Verification can establish confidence in an applicable rule, but cannot create
or erase the rule. Conflicting authority is resolved through the governed
conflict policy and successor artifacts; registry order and file order never
create precedence.

## Rationale

The successor retains the useful single-root and authority-versus-evaluation
boundaries while removing the retired rule graph, compile-down, and lifecycle
event mechanisms from the former Decision.
