---
subject_scopes:
  - settings
priority: high
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: child_of
    targets:
      - CAPRMEDIO-META-REQU-209--progressive-governance-surface-activation
  - type: relates_to
    targets:
      - CAPRMEDIO-GOV-REQU-407--single-settings-catalog
---

# Requirement — Store governance-surface activation

`.caprmedio/caprmedio_settings.toml` owns one documented `governance_surfaces` table.
Every registered surface has one explicit boolean:

- `evergreen_specification`;
- `test_plan`;
- `evaluation_plan`;
- `implementation_plan`;
- `project_overview`; and
- `architecture_view`.

All values default to `false`. Missing configuration reads as the same
atomic-first default. Unknown surface names fail closed.

Activation makes the selected surface applicable to currentness and downstream
gates. Deactivation removes those obligations without deleting or archiving an
existing carrier. Retained files become inactive references until a later
reactivation reconciles them against current atomic authority.

## Primary claim

caprmedio_settings.toml owns an explicit boolean activation state for every registered optional governance surface, with every surface inactive by default and deactivation preserving carriers and history.

## Rationale

One documented settings owner makes progressive activation deterministic while preserving the distinction between semantic revision mode and optional governance participation.


## Historical frontmatter metadata

```yaml
promotion:
  affected_children:
    - "tool"
    - "skill"
    - "implementation"
    - "operations"
  applies_unchanged: true
  local_context_required: false
```
