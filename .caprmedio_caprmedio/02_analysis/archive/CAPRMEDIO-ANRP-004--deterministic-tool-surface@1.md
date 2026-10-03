---
subject_scopes:
  - artifact-model
version: 1
updated_at: 2026-08-18 01:39:16
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
---
# Session analysis — deterministic Tool surface

## Evidence and boundary

This analysis uses CAPRMEDIO main-session activity from 2026-08-14 through 2026-08-18 as its evidence source. It does not infer the Tool surface from Git history or repository-file changes.

The session repeatedly exposed a costly pattern: the agent had to load or rewrite complete artifacts to perform small mechanical operations on metadata, carrier identity, lifecycle location, graph structure, catalogs, settings, Projections, provenance, Plans, and release records. Those operations are specifiable, testable, and reusable, so they belong behind deterministic Tool interfaces. Semantic judgment remains with the operator or a Skill; a Tool applies an explicit choice, validates it, and reports exact effects.

## Cases already covered

The active Tool Requirements already cover deterministic routing (`TOOL-025` and `TOOL-026`), bounded session state (`TOOL-027`), Tool-owned scripts (`TOOL-028`), generated-stage validation (`TOOL-029`), Work Journal append and reconciliation (`TOOL-030` and `TOOL-031`), Work Journal projection (`TOOL-033`), semantic Projection generation (`TOOL-034`), and aggregate metrics (`TOOL-035`). `TOOL-034` and `TOOL-035` now each specify one Tool rather than an unspecified plurality.

## Missing atomic Tool cases

The session-derived gaps are encoded as `TOOL-036` through `TOOL-057`: metadata read and patch; typed relation patch; carrier creation and rename; lifecycle transition; filtered artifact query; carrier and graph validation; migration plan, apply, and verification; catalog generation and validation; settings patch; Projection rebuild and currentness validation; external-source capture and external-Analysis ingestion; provenance reconciliation; release-outcome recording; and accepted deferred-Plan persistence.

Each Standard Requirement specifies one Tool. Multi-step migration is intentionally a set of three Tools so planning is read-only, application is transactional, and post-migration verification is independently replayable.

## Unresolved session conflicts

The session did not settle whether a generated catalog remains part of project settings or is removed. `TOOL-048` and `TOOL-049` therefore define behavior only when a catalog is registered: they do not declare catalog authority or require a catalog to exist.

The session also used `handled` both as a lifecycle status and as derived information. `TOOL-041` does not choose between those models; it requires a registered lifecycle transition and fails closed when the active schema is ambiguous.

## Adoption order

The highest-leverage first slice is `TOOL-036`, `TOOL-037`, `TOOL-038`, `TOOL-040`, `TOOL-042`, and `TOOL-044`: together they remove most full-artifact reads and unsafe ad hoc graph edits. The migration set (`TOOL-045` through `TOOL-047`) should follow because it composes those primitives into rollbackable repository-wide change. The remaining Tools can then reuse the same identity, validation, frontier, and Journal contracts.
