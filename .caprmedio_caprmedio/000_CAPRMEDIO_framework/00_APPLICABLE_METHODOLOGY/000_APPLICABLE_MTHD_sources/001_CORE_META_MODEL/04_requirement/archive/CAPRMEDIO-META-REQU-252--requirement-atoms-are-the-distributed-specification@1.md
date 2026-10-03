---
subject_scope: framework-boundary
priority: high
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: replacement_of
    targets:
      - CAPRMEDIO-META-REQU-247--thin-maintained-specifications
  - type: child_of
    targets:
      - CAPRMEDIO-META-REQU-248--three-artifact-forms
      - CAPRMEDIO-META-REQU-249--seven-content-roles-and-three-governance-loci
  - type: relates_to
    targets:
      - CAPRMEDIO-META-REQU-243--single-claim-atomic-artifacts
      - CAPRMEDIO-META-REQU-090--propagate-atomic-revision-impact-through-lineage
      - CAPRMEDIO-META-REQU-246--provenance-does-not-establish-evidence
---

# Requirement — Treat Requirement Atoms as the distributed specification

The applicable active internal Requirement Atoms are the project’s normative specification. Each Atom owns one independently replaceable desired result, obligation, boundary, invariant, entity rule, lifecycle rule, status criterion, transition rule, event rule, or other requirement claim.

A second maintained document must not become another specification authority by rephrasing those claims. Full written Specifications are retired as an independent maintained semantic surface.

Projects may expose thin Projections over the Atom set. A conforming Projection:

- names its declared source Atoms directly;
- organizes them through selection, grouping, ordering, navigation, or already-governed relations;
- remains rebuildable from its declared sources;
- introduces no independently normative paraphrase of a source claim;
- never becomes evidence merely by citing an Atom; and
- never overrides an Atom or hides which Atom owns a represented claim.

Catalog, map, and hub are permitted GOV-level Projection vocabularies. A requirement catalog may provide sections and lists of Requirement Atom IDs; a requirement map may render their governed relations; a requirement hub may provide navigation to scoped catalogs, maps, and Atoms. Correct interpretation of an Atom must never depend on wording present only in a Projection.

Concern, Analysis, Method, Evaluation, Implementation, and Observation Atoms remain distinct supporting roles. They may be included in role-appropriate Projections but do not become Requirements merely because a Projection groups them with the normative specification.

## Primary claim

Applicable Requirement Atoms are the distributed normative specification, while catalogs, maps, and hubs are thin non-authoritative Projections rather than rewritten Specifications.

## Rationale

When each desired rule is already an updatable, independently governed Atom, a second prose specification duplicates authority and creates drift. Thin Projections preserve overview and navigation while every normative change remains localized to its owning Requirement Atom.
