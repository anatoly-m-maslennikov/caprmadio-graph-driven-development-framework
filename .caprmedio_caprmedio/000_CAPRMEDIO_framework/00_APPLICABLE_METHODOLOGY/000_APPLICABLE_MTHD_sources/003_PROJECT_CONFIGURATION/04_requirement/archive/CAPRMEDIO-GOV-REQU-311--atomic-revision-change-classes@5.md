---
subject_scopes:
  - lifecycle
version: 5
updated_at: 2026-08-22 04:39:08
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-GOV-REQU-345--represent-accepted-meaning-faithfully
  relates_to:
    - CAPRMEDIO-META-REQU-154--semantic-irreducibility
    - CAPRMEDIO-META-REQU-090--propagate-atomic-revision-impact-through-lineage
    - CAPRMEDIO-GOV-REQU-310--lineage-impact-dispositions
---
# Classify every Atomic Artifact change

Before changing an admitted Atomic Artifact, CAPRMEDIO assigns exactly one change
class:

| Change class | Boundary | Identity result | Required review |
|---|---|---|---|
| `carrier_only` | Representation, summary, filename, path, or encoding changes without changing governed meaning | Keep the artifact ID | Verify lossless recoding |
| `refinement` | Wording or criteria become clearer or stricter while primary claim, applicability, and acceptance meaning remain equivalent | Keep the artifact ID and commit a new revision | Demonstrate equivalence and assess lineage |
| `semantic_revision` | Meaning or applicability changes while the same primary claim remains recognizable | Keep the artifact ID and commit a new revision | Declare the delta and complete lineage-impact review |
| `replacement` | The primary claim changes identity, or an independently replaceable claim is added or removed | Create a new artifact ID; declare predecessor `replaced_by` in its archival Journal event | Review the replacement boundary and affected lineage |

Scope narrowing or expansion is a `semantic_revision`, not a carrier-only
change. Splitting or combining independently replaceable claims is a
`replacement`.

The semantic change class is independent of the Git change set. Every persisted
carrier change follows the canonical direct typed-relation commit-message rule. A
same-ID content change creates a new Revision, while a carrier-only move or
rename may preserve the current version. A replacement first commits the
successor as active, then archives the predecessor in a `MOVE` whose
authoritative Work Journal event declares direct `replaced_by`. Neither Atom's
frontmatter authors a replacement edge; the graph derives `replacement_of` for
inverse navigation. The archival move preserves the predecessor's content,
filename, frontmatter, and version. Each successor and predecessor carrier
change remains a separate one-file commit.

Tools may propose a class but must fail closed when the distinction between
refinement, semantic revision, and replacement is uncertain.

## Rationale

The four classes preserve stable identities for genuine claim evolution while
preventing formatting changes, refinements, semantic changes, and replacements
from being treated as interchangeable.
