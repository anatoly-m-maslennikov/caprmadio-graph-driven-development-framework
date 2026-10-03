---
subject_scopes:
  - lifecycle
priority: high
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: child_of
    targets:
      - CAPRMEDIO-META-REQU-248--three-artifact-forms
  - type: relates_to
    targets:
      - CAPRMEDIO-GOV-REQU-300--semantic-immutability-and-lossless-recoding
      - CAPRMEDIO-GOV-REQU-302--atomic-admission-and-promotion-gate
      - CAPRMEDIO-GOV-REQU-474--register-current-type-prefixes
      - CAPRMEDIO-GOV-REQU-311--atomic-revision-change-classes
---

# Requirement — Derive atomic lifecycle from Type-local placement

Every enabled Atomic Artifact Type uses one Type-local directory with this
layout:

```text
<type>/
├── <active atomic artifacts>
├── drafts/
│   └── <mutable pre-admission candidates>
└── archive/
    └── <inactive atomic artifacts>
```

Repository placement determines the carrier kind:

| Placement | Derived carrier kind | Meaning |
|---|---|---|
| Directly under `<type>/` | `active` | Admitted atom participating in current project authority |
| Under `<type>/drafts/` | `draft` | Mutable candidate with no atomic identity or authority |
| Under `<type>/archive/` | `archived` | Admitted atom retained unchanged outside current authority |

The resolver derives `carrier_kind` from location. Carriers never persist a
duplicating status or `carrier_kind` property.

A Draft filename uses the intended project, scope-path, and Type-prefix
segments followed by `DRAFT`, for example:

```text
CAPRMEDIO-GOV-ANRP-DRAFT--artifact-carrier-analysis.md
```

A Draft has no `artifact_id`, cannot be a canonical relation target, does not
consume a Type sequence number, and is excluded from authority, coverage,
conflict, and completeness calculations. It may cite admitted artifacts as
authoring sources without creating canonical relations.

Promotion requires explicit acceptance and the applicable admission gate. It
allocates the next Type number, creates the stable artifact ID, replaces
`DRAFT` in the filename with that number, completes the required atomic
frontmatter, moves the carrier to the Type root, and commits the initial
immutable revision. The candidate may be edited while promotion is being
prepared because it has not yet become an admitted Atomic Artifact.

An active Atomic Artifact may gain later committed revisions under the same ID
through the governed change-class and lineage-impact procedures. Earlier
revisions remain immutable and reachable in Git.

Archiving moves an admitted carrier unchanged from the Type root into its
Type-local `archive/` directory. It preserves the filename, artifact ID,
frontmatter, narrative content, and relations, and records the transition
through the governed parent-to-child Git transaction. An archived atom never
returns to Draft or active placement; renewed work creates another candidate or
successor atom.

## Primary claim

Each Atomic Artifact Type derives Draft, active, and archived carrier kinds
from Type-local directory placement, with identity allocated only during
promotion and accepted contents preserved during archival.

## Rationale

Type-local placement makes lifecycle visible in ordinary file navigation while
avoiding a second writable status representation. Git preserves immutable
committed revisions while placement identifies which artifact IDs currently
participate in project authority.
