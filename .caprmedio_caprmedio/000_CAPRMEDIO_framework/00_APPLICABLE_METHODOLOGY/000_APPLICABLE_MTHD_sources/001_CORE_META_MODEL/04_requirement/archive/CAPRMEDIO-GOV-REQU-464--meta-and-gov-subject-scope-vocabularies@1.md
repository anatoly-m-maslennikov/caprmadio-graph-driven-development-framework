---
subject_scopes:
  - subject-scope
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-GOV-REQU-345--represent-accepted-meaning-faithfully
  relates_to:
    - CAPRMEDIO-META-REQU-240--atomic-structural-and-subject-scopes
    - CAPRMEDIO-GOV-REQU-308--plain-scalar-frontmatter-values
---
# Register META and GOV subject scopes

Atomic Artifacts owned by `layer:meta` use only these subject scopes:

| Subject scope | Governed subject |
|---|---|
| `artifact-model` | Atomic structure, semantic routes, properties, and artifact distinctions |
| `evaluation` | Test, Evaluation, evidence, verification, and evaluation boundaries |
| `authority` | Constitutional ownership, precedence, and rule placement |
| `candidate-promotion` | Promotion of non-authoritative planning candidates into governed Atoms |
| `delivery-planning` | Development Backlog and target-version allocation semantics |
| `external-boundary` | Obligations imposed by systems or authorities outside the project |
| `framework-identity` | Canonical framework name, expansion, and public logline |
| `governance-surface` | Activation and composition of the governed control surface |
| `interaction` | Operator input, Exploration Mode, and interaction behavior |
| `lifecycle` | Admission, archive, replacement, and temporal claim rules |
| `product-framing` | Optional User Story and Outcome framing around governed claims |
| `profile` | Optional applicability and product or implementation profiles |
| `release-finalization` | Version freeze and immutable release-boundary semantics |
| `release-reconciliation` | Reconciliation of released work with future-work planning |
| `scope` | Structural ownership, Work Areas, features, and subject scoping |
| `self-hosting` | Recursive application of CAPRMEDIO to its own repository |
| `topology` | Layer order, handoffs, and forward-only propagation |

Atomic Artifacts owned by `layer:gov` use only these subject scopes:

| Subject scope | Governed subject |
|---|---|
| `applicability` | Tier vocabulary, assignment, inheritance, and validation |
| `artifact-catalog` | Type, subtype, route, whitelist, and naming catalogs |
| `evaluation` | QA Cases, production Evaluation Controls, logging and observability policies, evaluation standards, review protocols, evidence, and verification |
| `carrier-format` | Markdown properties and other governed storage carriers |
| `external-boundary` | External constraints, references, reviews, and legal boundaries |
| `interaction` | Operator-facing settings and artifact admission behavior |
| `layout` | Control-plane folders, placement, discovery, and architecture views |
| `lifecycle` | Atomic admission, archive, recurrence, replacement, and release readiness |
| `methodology` | Methodology installation, synchronization, and governing constitution |
| `priority` | Priority vocabulary and conflict selection |
| `provenance` | Git, session, commit, and evidence provenance |
| `public-interface` | Public command, skill, and other operator-facing interface identities |
| `relation-model` | Artifact relations, endpoints, conflicts, and lineage |
| `runtime` | Runtime state, journals, scratch storage, and execution boundaries |
| `settings` | Project settings, configuration selection, and enabled governance surfaces |
| `subject-scope` | Subject-scope vocabulary, cardinality, and validation |

The vocabularies are closed for their respective structural owners. Adding,
renaming, or removing a subject is a semantic revision of this vocabulary
authority while its primary claim remains the same. It keeps this artifact ID,
creates a new committed revision, and triggers lineage-impact review. A new
artifact ID is required only when the primary vocabulary-governance claim
changes identity.

## Rationale

A small governed vocabulary makes subject scopes useful for bounded searches
and obsolete-atom reviews. Free-form or per-file labels would satisfy syntax
while recreating an unbounded tag system with no stable retrieval meaning.
