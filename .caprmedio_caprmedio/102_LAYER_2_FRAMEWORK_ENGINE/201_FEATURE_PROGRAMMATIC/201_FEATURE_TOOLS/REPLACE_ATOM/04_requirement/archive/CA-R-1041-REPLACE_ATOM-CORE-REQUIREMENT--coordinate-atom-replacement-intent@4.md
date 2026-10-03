---
subjects:
  governs:
    continuant:
      - artifact-operations
version: 4
updated_at: 2026-08-30 16:44:07 +0400
---
# Coordinate Atom replacement intent

`REPLACE_ATOM` is the canonical CAPRMEDIO Markdown Atom Doer that coordinates replacement without owning generic carrier creation, relation patching, or archival semantics. An atomic replacement accepts one exact active predecessor Atom ID, one exact already-active successor Atom ID, and action context. It rejects missing, duplicate, inactive, or identical IDs and returns one sealed replacement action that names the successor and the predecessor archive intent. A bulk replacement accepts a frozen set of two or more distinct exact predecessor-successor pairs and is all-or-nothing.

The Tool must not infer, create, or write Atom relations. It must use the canonical Atom lifecycle Tool for each resulting archive and hand the supplied IDs and sealed action to the provenance pipeline. It must default to a mutation-free dry run and accept `--apply` only through an authorized project-local MCP delegation with a sealed Initiative action envelope. A successful effect must receive durable `COMMIT_TRIGGER` intake acknowledgement before MCP reports success; `REPLACE_ATOM` itself does not append the Journal, stage files, or create a Git commit.
