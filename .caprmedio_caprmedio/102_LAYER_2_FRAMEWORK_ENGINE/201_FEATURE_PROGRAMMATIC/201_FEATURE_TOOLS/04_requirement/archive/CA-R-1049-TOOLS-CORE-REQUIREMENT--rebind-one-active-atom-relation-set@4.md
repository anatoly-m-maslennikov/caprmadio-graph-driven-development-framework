---
subject_scopes:
  - artifact-operations
version: 4
updated_at: 2026-08-23 15:59:05 +0400
---
# Rebind one active Atom relation set

`REBIND_ATOM_RELATIONS` is the canonical CAPRMEDIO Markdown Atom Doer for updating exactly one selected active Atom carrier after another active Atom has received a canonical filename-derived ID. It must default to dry run and accept one exact JSON request containing the explicit source path, expected source SHA-256 and version, explicit `updated_at`, and exact relation rewrite and removal maps. A set of two or more relation rebindings belongs to an explicitly governed bulk coordinator that freezes all single-rebinding requests and is all-or-nothing; this Tool must not silently widen its one-Atom operation.

The Tool must preserve the source filename, Markdown body, and every undeclared frontmatter field and relation target. It may change only the declared relation targets, `version`, and `updated_at`; `version` must advance by exactly one. A rewrite must name a registered, active, direct relation admitted to an Atom carrier and a noncanonical, inactive, missing, or ambiguous new target ID must be rejected. A removal may delete any syntactically valid relation key and exact target that occurs once in the source, including an unregistered, deferred, inverse-derived, or wrong-carrier entry; removal neither adds nor translates semantic meaning. Every action must reject an inactive or non-Atom source, digest or version mismatch, missing or repeated named old target, and every undeclared mutation.

An apply is accepted only through an authorized project-local MCP delegation with a sealed Initiative action envelope. It must atomically replace the selected source carrier only, then cause durable `COMMIT_TRIGGER` intake before MCP reports success. Every successful receipt must truthfully report `journal: not_performed`, `git: not_performed`, and `trigger: acknowledged`; this Tool must not create backups, mutate a target carrier, append a Journal event, stage files, or create a Git commit.
