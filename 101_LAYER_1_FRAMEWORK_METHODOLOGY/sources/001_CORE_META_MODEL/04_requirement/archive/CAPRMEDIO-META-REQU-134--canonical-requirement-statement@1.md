---
subject_scopes:
  - semantics
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-META-REQU-135--write-context-complete-minimal-atom-prose
---
# Canonical Requirement statement

Every Requirement Atom states its one claim through this semantic form:

```text
<obligation bearer> <must | must not | may> <observable predicate>
[for/on <target>] [within/when <Applicability>]
```

The obligation bearer is the system, project, Artifact, actor, or other entity
bound by the Requirement. The observable predicate states the required outcome,
state, action, permission, or prohibition without prescribing its realization.
A target identifies what receives or is affected by the predicate;
Applicability identifies where, when, for whom, or under which conditions the
claim governs.

`must` establishes an obligation, `must not` establishes a prohibition, and
`may` establishes a permission boundary. `should`, `ought`, `recommended`, and
other ambiguous normative substitutes are forbidden as Requirement modality.
The sentence may omit an optional segment only when its meaning is absent or
already unambiguous from canonical terms in the claim.
