---
subject_scopes:
  - relation-model
tier: core
version: 12
updated_at: 2026-08-22 04:39:08
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  method_for:
    - CA-R-806-REQUIREMENT-BSEED_GOVERNANCE--register-complete-relation-kind-metadata
    - CA-R-807-REQUIREMENT-BSEED_GOVERNANCE--store-replacement-as-direct-replaced-by
    - CA-R-808-REQUIREMENT-BSEED_GOVERNANCE--limit-active-direct-relations-to-upstream-or-same-tier
    - CA-R-809-REQUIREMENT-BSEED_GOVERNANCE--validate-direct-relation-global-tier-direction
  child_of:
    - CA-R-871-REQUIREMENT-BSEED_METAMODEL--distinguish-shared-authority-edges-and-relational-atoms
---

# Compile the canonical relation-kind registry

Compile the active GOVERNANCE Requirement Atoms that register semantic relations into exactly one machine-readable dictionary at `.caprmedio/FRAMEWORK_ENGINE/TOOLS/caprmedio_relation_types.toml`. Install a content-identical copy with every self-contained Tool runtime release that reads the dictionary. Each registration Atom owns one declared relation's exclusive meaning and supplies every field required by the complete relation-kind metadata Requirement. The compilation must not invent aliases, merge near-synonyms, or infer inverse names, ordering domains, target positions, authority, lifecycle, or endpoint rules from spelling.

For each admitted direct relation, emit exactly one row with these columns in canonical order:

| Column | Meaning |
|---|---|
| `declared_name` | The only name authored by the persisted owner |
| `inverse_name` | The unique name derived for reverse navigation |
| `declaration_carrier` | `atom_carrier` or `work_journal_event`, the sole persisted carrier for the direct edge |
| `ordering_domain` | The domain in which upstream and downstream positions are interpreted |
| `declared_target_position` | The registered target position in that ordering domain |
| `source_lifecycles` | Lifecycle states permitted to author the direct edge |
| `target_lifecycles` | Lifecycle states permitted at direct-edge creation |
| `owner` | The endpoint that persists the direct edge |
| `source_classes` | Allowed source project-graph node classes |
| `target_classes` | Allowed target project-graph node classes |
| `cardinality` | Allowed endpoint cardinality |
| `authority_effect` | Authority, coverage, precedence, or no-authority effect |
| `transitive` | Whether transitive closure is semantically valid |
| `symmetric` | Whether reversing endpoints preserves meaning |
| `authority_modes` | Modes in which the relation may be authored |
| `status` | Active, deprecated, or sealed lifecycle state |
| `exclusive_meaning` | The bounded fact expressed by the relation |

Sort rows by `declared_name`. Persist a direct edge only in its registered `declaration_carrier`: an `atom_carrier` persists it on its registered owner, while a `work_journal_event` persists it in the authoritative Journal event naming that owner. Derive the inverse view at query time. Validate target position only within the row's registered ordering domain; compare global tiers only for normative-authority relations whose metadata requires that comparison. Compile replacement only as `replaced_by` in a `work_journal_event` with inverse-derived `replacement_of`. Reject compilation when a declared or inverse name is duplicated, an inverse is also admitted as declared, a required field is absent, a declaration carrier is unknown, endpoint rules conflict, or more than one active registration claims the same meaning. Relation kinds used only by rule registries or Structural configuration remain outside this Atom relation-type dictionary unless a GOVERNANCE Requirement explicitly admits them.
