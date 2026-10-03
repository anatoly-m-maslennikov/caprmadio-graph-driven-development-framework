---
cce_version: cce_1
cce_form: method
subjects:
  - carrier-format
version: 11
updated_at: 2026-08-23 12:02:00
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  method_for:
    - CA-R-1053
  child_of:
    - CA-R-1054
---
# Atomize carrier transitions

Moving a Carrier between directories while preserving its bytes and assigned Atom-ID filename segment is not a semantic transition and creates no semantic location authority. The identity resolver finds the current Carrier by deriving Atom ID from that immutable filename segment inside the selected `.caprmedio`; its governed Journal and Git provenance MAY record the old and new carrier addresses.

A carrier-name or representation migration is one immutable governed transition, not a separate semantic location record. Its Journal and Git evidence record the Atom ID, old and new Carrier names, old and new digests, semantic-equivalence proof, Git return identity, implementation commit, session provenance, and declared loss. It never stores the old or new physical path as current authority.

Before changing an admitted Atomic Artifact, classify the intended change under the four GOV REQU-311 classes. The classifier MUST return exactly one class:

- `carrier_only` for a lossless representation, summary, filename, path, or encoding change; preserve the Atom ID and verify lossless recoding;
- `refinement` when wording or criteria become clearer or stricter while the primary claim, applicability, and acceptance meaning remain equivalent;
- `semantic_revision` when meaning or applicability changes but the same primary claim remains recognizable; and
- `replacement` only when the primary claim changes identity or independently replaceable claims are added, removed, split, or combined.

`refinement` and `semantic_revision` preserve the Atom ID and create a new Revision with their required equivalence or lineage review. Only `replacement` creates a successor Atom ID and follows the archive lifecycle.

Tools MAY propose a class but MUST fail closed: when they cannot distinguish `refinement`, `semantic_revision`, and `replacement` with the required evidence, they return the ambiguity without changing the admitted Artifact.
