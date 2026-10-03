+++
artifact_subtype = "run_record"
child_of = ["CAPRMEDIO-GOV-REQU-392--artifact-lineage"]
version = 1
updated_at = "2026-08-17 19:36:01"
llm_session_ids = ["codex:019f591f-04f6-70f2-8de7-828b7cccc69d"]
+++

# Artifact-lineage self-application — 2026-07-20

## Proof identity

- **Claim:** DSET accepts one or more immediate `child_of` IDs on a governed
  child, derives `parent_to` and transitive ancestry, and fails closed on
  malformed or invalid artifact lineage without editing parents.
- **Intended use:** Support `CAPRMEDIO-GOV-REQU-392--artifact-lineage`,
  `CAPRMEDIO-INVARIANT-GOV-024`, `CAPRMEDIO-TEST-CASE-GOV-034`, and
  `CAPRMEDIO-TASK-GOV-056`.
- **Producer/performed work:** Main-session implementation, repository-local
  self-application, generated traceability refresh, and deterministic
  validation.
- **LLM session IDs:**
  - `codex:019f591f-04f6-70f2-8de7-828b7cccc69d`
- **Evaluated revisions:** `86a582e61bd2cff9645fafab3e5feb3047d9c608`
  and `1ce0d1b548d55f25fc5b272d2e4a7591b3d5dbe9`.
- **Observed:** 2026-07-20.
- **Currentness:** current for the cited revisions and this evidence-only
  reconciliation commit.
- **Reopen when:** the lineage metadata contract, artifact identity resolver,
  traceability schema/generator, commit-provenance mapping, or lineage
  validator changes.
- **Unsupported uses:** this proof does not claim that every historical DSET
  artifact already has complete lineage, that `Implements:` trailers are yet
  rendered as graph nodes, or that qualitative `CAPRMEDIO-EVALUATION-CASE-GOV-024` has run.

## Deterministic results

| Boundary | Observation | Result |
|---|---|---|
| Cardinality | One child with two parents and one parent with multiple children validate | Pass |
| Direction | Children author `child_of`; generated traceability derives `parent_to` | Pass |
| Transitive view | Ancestors derive from immediate edges without dense authored links | Pass |
| Immutability | `CAPRMEDIO-GOV-REQU-391--artifact-inheritance` was not edited to register its new child | Pass |
| Failure matrix | Scalar, empty, duplicate, unresolved, self, cyclic, and authored-reverse relations fail | Pass |
| Recursive application | `CAPRMEDIO-GOV-REQU-392--artifact-lineage` is a child of `CAPRMEDIO-GOV-REQU-391--artifact-inheritance`; the generated reverse edge is current | Pass |
| Canonical test gate | `TMPDIR=/tmp .venv/bin/python -m unittest discover -v` ran 162 tests in 61.319 seconds | Pass |
| Static and structural gates | Ruff, strict mypy, DSET validation, trace freshness, and diff hygiene | Pass |

The implementation uses an atomic record's semantic ID as its lineage node and
retains the carrier `artifact_id` in the derived index. Non-atomic classified
artifacts use their artifact ID directly. Distributed templates are excluded
from the live graph because placeholders are not project artifacts.
