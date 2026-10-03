---
subject_scopes:
  - lifecycle
tier: core
version: 7
updated_at: 2026-08-22 04:30:00
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  method_for:
    - CAPRMEDIO-GOV-REQU-309--revision-bound-parent-child-commit-messages
    - CAPRMEDIO-GOV-REQU-311--atomic-revision-change-classes
    - CA-R-807-REQUIREMENT-BSEED_GOVERNANCE--store-replacement-as-direct-replaced-by
    - CAPRMEDIO-GOV-REQU-767--keep-active-rmed-relations-out-of-archives
  child_of:
    - CAPRMEDIO-GOV-REQU-345--represent-accepted-meaning-faithfully
---

# Use an archive-based Atomic Artifact lifecycle

CAPRMEDIO has no `lifecycle_event` Artifact Type. Lifecycle placement is a
Carrier fact and does not itself change an assigned Atom ID.

- **draft:** its Carrier is in the role-local `drafts/` folder, has no assigned Atom ID, remains mutable, and is not current authority;
- **active:** its identified carrier is directly in its Content-role folder and
  participates in current authority, planning, evaluation, or work views as
  applicable;
- **solved:** a Concern carrier is in the role-local `solved/` folder and keeps
  its assigned Atom ID as preserved post-acceptance evidence;
- **done:** an Analysis or Plan carrier is in the role-local `done/` folder and
  keeps its assigned Atom ID as preserved post-acceptance evidence;
- **archived:** its carrier is in the role-local `archive/` folder, keeps its
  assigned Atom ID, and remains discoverable as immutable history.

Moving an unchanged identified Carrier among registered post-acceptance lifecycle folders is a committed storage transition, not a mutation of the Atomic Artifact or its Atom ID. Accepting a draft is different: acceptance assigns an Atom ID in the canonical Carrier filename and creates the first identified Revision.

## Closing active artifacts

- A replacement first commits its successor as an active Atom without any
  authored inverse replacement edge. A second, one-file archival action moves
  the predecessor to `archive/` and records the direct `replaced_by` edge from
  that predecessor in the authoritative Work Journal event. The graph derives
  `replacement_of` only for inverse navigation. No active Atom relation may
  target an archived predecessor or successor.
- A resolver carrying `resolution_of` closes a Concern Atom with the `question`
  or `problem` Type. A resolver carrying `solution_for` closes a relational
  Conflict. After the resolver is committed, the resolved atom moves to
  `archive/`.
- An atom removed from current work without current implementation is moved to
  `archive/`, and any intended future work is represented by a draft in the
  Development Backlog. That draft may reference the archived Atom ID for provenance while still having no Atom ID of its own.
- An atom that no longer applies and has no future intent moves to `archive/`
  in a commit whose rationale identifies why no successor is required.

Terms such as `absorbed`, `resolved`, `retired`, and `withdrawn` may describe
the reason for archival in human-facing history, but they are not stored
lifecycle states or artifact types.

## Returning matters

Reopening an archived Atom is forbidden. A recurring Concern with the
`question` or `problem` Type begins as a new draft without an Atom ID and, if
accepted, becomes a new Atom with its own Atom ID, current claim, provenance,
and priority. The admitting Work Journal event records the archived
predecessor's exact Atom ID as recurrence provenance. The active recurrence
Atom must not author a direct relation to the archived predecessor; derived
history views may expose the recurrence from the Journal and archive record.

## History and derivation

The authoritative Journal archival event retains the predecessor-owned direct
`replaced_by` relation, rationale, and session provenance. Git records the
committed successor introduction and predecessor archival transition. Derived
views infer the current set from active folders and infer replacement history
and inverse `replacement_of` navigation from Journal and archive history; they
do not author historical replacement links in the active graph.

## Historical frontmatter metadata

```yaml
promotion:
  affected_children:
    - "governance"
    - "tool"
    - "skill"
    - "implementation"
    - "ops"
  applies_unchanged: false
  local_context_required: true
```
