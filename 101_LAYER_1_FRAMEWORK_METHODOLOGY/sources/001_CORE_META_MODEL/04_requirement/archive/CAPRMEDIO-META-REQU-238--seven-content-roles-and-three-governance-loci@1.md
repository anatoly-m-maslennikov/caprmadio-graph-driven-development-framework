---
subject_scope: artifact-model
priority: high
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: replacement_of
    targets:
      - CAPRMEDIO-META-REQU-233--seven-role-artifact-model-and-qa-layer
  - type: relates_to
    targets:
      - CAPRMEDIO-META-REQU-211--type-derived-artifact-routes
      - CAPRMEDIO-META-REQU-217--three-revision-modes-without-evergreen
      - CAPRMEDIO-META-REQU-224--analysis-and-observation-boundary
      - CAPRMEDIO-META-REQU-225--distinct-test-and-evaluation-chains
      - CAPRMEDIO-META-REQU-084--relational-artifacts-declare-endpoints
      - CAPRMEDIO-META-REQU-227--scope-path-is-structural
---

# Requirement — Use seven Content roles and three Governance loci

CAPRMEDIO classifies governed artifact meaning through exactly seven Content roles:

1. Problem;
2. Analysis;
3. Definition;
4. Method;
5. Evaluation;
6. Implementation; and
7. Observation.

Governance locus is an independent semantic axis with exactly three values:

- `internal` for project-owned meaning;
- `external` for meaning imposed or owned outside the project; and
- `relation` for meaning that exists between explicit endpoints.

Revision mode remains the independent change-semantics axis owned by its own
META requirement. `scope_path` remains a structural coordinate rather than a
semantic axis.

Concrete artifact Type names, subtype vocabulary, identity prefixes, and
carrier rules are downstream GOV responsibilities. META defines only the
stable semantic dimensions and their meanings.

## Primary claim

CAPRMEDIO uses seven Content roles and three Governance loci as independent
technology-neutral semantic dimensions, without assigning concrete artifact
Type names in META.

## Rationale

The predecessor correctly introduced Evaluation and the seven-role model but
coupled them to a later-retired QA layer and duplicated GOV-owned Type names.
The successor preserves only the universal semantic invariant.
