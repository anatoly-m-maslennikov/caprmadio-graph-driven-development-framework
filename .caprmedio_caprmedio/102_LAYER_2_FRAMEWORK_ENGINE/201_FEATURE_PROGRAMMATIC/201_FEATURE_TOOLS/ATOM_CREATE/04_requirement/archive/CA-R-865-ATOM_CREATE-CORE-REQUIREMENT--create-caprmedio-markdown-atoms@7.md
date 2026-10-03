---
atom_id: CA-R-865
cce_version: cce_1
cce_form: obligation
subjects:
  governs:
    continuant:
      - artifact-operations
version: 7
updated_at: 2026-09-04 03:10:59 +0400
---
# Create CAPRMEDIO Markdown Atoms

The `ATOM_CREATE` Tool is the canonical Doer for creating CAPRMEDIO Markdown Atom carriers only under content-role locations in the configured Project control root. It must accept a complete path or a directory and filename with frontmatter and content, enforce the current filename grammar, reject carrier and stable Atom-ID collisions, establish revision metadata, and preflight the complete operation. An atomic action creates exactly one carrier; a bulk action creates a frozen set of two or more carriers and is all-or-nothing. It may use generic carrier-construction mechanics but owns Atom admission, identity, revision, and effect semantics. It must default to a mutation-free dry run and accept `--apply` only through an authorized project-local MCP delegation with a sealed Initiative action envelope.

## Check

Automated tests must prove singular and bulk creation, current filename validation, Atom-ID and path collision rejection, automatic initial revision metadata, mutation-free dry run, MCP-gated apply, and no partial creation after a failed bulk preflight or apply.
