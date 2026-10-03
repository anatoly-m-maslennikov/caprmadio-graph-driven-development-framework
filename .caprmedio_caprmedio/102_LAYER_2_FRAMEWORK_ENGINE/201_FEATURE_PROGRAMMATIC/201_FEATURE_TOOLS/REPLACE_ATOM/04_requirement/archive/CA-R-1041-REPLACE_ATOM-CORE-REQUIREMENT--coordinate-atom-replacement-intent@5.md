---
subjects:
  governs: "artifact-operations"
version: 5
updated_at: "2026-09-15 21:31:49 +0000"
---
# Coordinate Atom replacement intent

REPLACE_ATOM **must** coordinate explicit Atom replacement intent **without** owning generic Carrier creation, relation editing, **or** archival semantics.

- an atomic replacement accepts **=1** exact active predecessor Atom ID, **>=1** distinct exact already-active successor Atom IDs, **and** action context.
- reject missing, duplicate, inactive, **or** self-referential IDs; return a sealed replacement action containing the supplied predecessor, successor set, **and** predecessor archive intent.
- a bulk replacement accepts a frozen set of explicit predecessor-to-successor-set mappings **and** preserves the approved all-or-nothing change-set boundary.
- use the canonical Atom lifecycle capability for the archive effect **and** pass the explicit IDs **to** the provenance pipeline. do **not** infer, create, **or** write replacement relations **in** Atom Carriers.
- default **to** a mutation-free dry run. permit apply **only** through authorized project-local MCP delegation with a sealed Initiative action envelope.
- a successful effect requires durable COMMIT_TRIGGER intake acknowledgment **before** MCP reports success. REPLACE_ATOM does **not** append the Journal, stage files, **or** create a Git Commit.
