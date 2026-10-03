---
subjects:
  declared:
    continuant:
      - decision-closure
      - project-backlog
      - realized-project-state
    occurrent:
      - conversation-audit
version: 5
updated_at: 2026-08-25 14:25:00 +0400
relations:
  analysis_of:
    - CA-C-107
---
# Audit seven-day conversation closure

## Audit boundary

This Analysis compares 436 user entries in the current Codex task from
2026-08-18 through 2026-08-25 with the current CAPRMEDIO Atoms and realized
repository state. The latest user statement on a subject supersedes earlier
variants. Existing authority remains the owner when it already captures the
surviving decision; this Analysis does not duplicate that backlog.

The audit distinguishes four states: captured and applied; captured but not
fully applied; uncaptured and requiring a CAP Task; and superseded input that
must not be preserved as current intent.

## Captured and applied

| Surviving decision | Current closure |
| --- | --- |
| Use the CAPRMEDIO identity and current graph-driven-framework repository name | Current repository, active Atoms, and README use CAPRMEDIO. |
| Use the Project structure with FRAMEWORK_METHODOLOGY, FRAMEWORK_ENGINE, OPERATOR_DOCUMENTATION, CORE_EXTENSIONS, RELEASES, COMMUNITY_EXTENSIONS, and FIELD | Current root and `.caprmedio` topology represent the accepted structure; remaining legacy-carrier migration is separately owned. |
| Structure FRAMEWORK_ENGINE as PROGRAMMATIC containing TOOLS, APPS, and MCP, plus AGENTIC containing SKILLS | Current authority and realized root folders use this split. |
| Keep current operation local-only and provide Codex as the only natively supported LLM application | README states the local-only boundary and `CA-R-826` owns the Codex-only Boundary. |
| Use CAP for tasks, RMED for the distributed specification, Implementation for actual code, and Operations for evidence and feedback | Current README and active role authority capture the model. |
| Distribute equal-authority Principles across RMEDO and remove `principle_order` | The current active Principle set uses RMEDO roles and no ordering field. |
| Support the stable CPython `3.14.*` series | `CA-P-080` is Done and current checked-in selectors use Python 3.14. |
| Keep only the owner-authored `dev` to `main` PR-policy check as a PR check and auto-enable merge | The active PR workflow has the two accepted policy jobs; other workflows do not run as PR checks. |
| Store structured LLM session provenance only in Journal events and partition governed change records by author, local date, and 100-event parts | Active APPEND_CHANGE_RECORDS authority and implementation contain the structured event and partition rules. |

## Captured but not fully applied

| Surviving decision | Existing owner | Remaining state |
| --- | --- | --- |
| Finish the current BSEED-to-Project topology and carrier migration | `CA-P-040` and Tasks `CA-P-041` through `CA-P-048` | The shared worktree still contains old and new topology carriers; do not create a duplicate migration Plan. |
| Implement the common Tool interface, router, Finders, Doers, Markdown projections, business projections, Skills, and Graph App | `CAPRMEDIO-P-017` | Authority is present, but the Graph App contains only a placeholder and many slices remain unrealized. |
| Give operator documentation a simpler human style and consider strict plus A2+/B1 variants | `CAPRMEDIO-P-022` and `CAPRMEDIO-P-023` | The Plans exist; no duplicate CAP item is needed. |
| Improve the framework from observed project outcomes | `CAPRMEDIO-PLAN-009` and active Operations Principles | The loop is governed; later implementation remains under its existing Plan. |
| Use asynchronous durable intake, one pure decision manager, a mechanical recoverable Scheduler, atomic non-deciding workers, one serialized Git pipeline, repository reconciliation, and controlled background services | Active TOOLS authority `CA-R-802`, `CA-R-803`, `CA-R-857`, `CA-M-087`, `CA-M-104`, `CA-M-182`, their Deliveries and Evaluations, and PROGRAMMATIC Task `CA-P-083` | The latest Hook architecture is governed and its implementation Task exists, but native and installed-path realization is not closed. Current evidence includes blocking legacy Hook code and a frontier-seal mismatch: context creation hashes relation-registry metadata while both downstream validators omit it. `CA-P-083` owns implementation, lifecycle controls, recovery, and fresh end-to-end proof, so no duplicate Plan is created here. |
| Use `uv` for every admitted Python workflow capability it provides while keeping installed Tools self-contained | Current PROGRAMMATIC draft Method | The Method is not active, no lockfile establishes a reproducible development environment, and the workflow is not applied consistently. |

## Missing CAP Tasks

1. Materialize the current CAPRMEDIO Definition as a projection of active
   Principles, identify CAPRMEDIO compactly as an Intelligent Work Environment
   framework, and keep the Goal and README synchronized without duplicating
   authority.
2. Run the executable parity spike already specified by `CA-A-042` and select
   the rebuildable derived database architecture without pretending the current
   options report selected an engine.
3. Implement one current Graph App vertical slice over authoritative Atoms and
   full Journals, a rebuildable database, a local backend, and an HTML/JavaScript
   frontend; keep self-contained static publication optional.
4. Promote and apply the accepted `uv` workflow boundary.
5. Bring current PROGRAMMATIC source into a measured conformance baseline under
   the accepted Methods and remove generated Python cache directories from
   governed source locations.
6. Add the accepted playful logo: a carp, `CAPR` on the fish, `MEDIO` above the
   instrument, and a harp. Do not restore the rejected balalaika and ushanka
   variant or duplicate the wordmark.

These six gaps are represented by `CA-P-095` through `CA-P-100`.

## Superseded input

- CAPRMADIO, CARPMEDIO, and earlier repository-name variants are not current.
- Assurance is not restored; Evaluation is the current Content role.
- The balalaika and ushanka logo is rejected; the harp is the final instrument.
- Separate backup copies are not required; Git history is the recovery
  mechanism. Runtime recovery state still belongs under `.caprmedio_runtime`.
- A self-contained HTML plus `data.js` package is optional, not the only or
  primary frontend architecture.
- GitHub-hosted review is outside the requested FPF-style local review flow.
- The suspended test suite is not an execution route for this closure pass;
  current Evaluation authority remains distinct from running those tests.

## Result

The six new Tasks close only missing ownership. Existing Plans retain their
scope. This Analysis and the new CAP Tasks do not claim that any underlying
implementation has been completed.

The later `CA #5: hooks fixing` closure promoted the commit-automation design
from draft discussion into active RMED authority, added numbered concurrency,
recovery, lifecycle, and installed-path Evaluations, and created `CA-P-083`.
That closure changes the classification from uncaptured design to governed but
not fully realized work; it does not add another Project-level Task.
