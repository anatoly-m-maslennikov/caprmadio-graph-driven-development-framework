---
artifact_subtype: implementation_decision
subject_scopes:
  - carrier-format
priority: high
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: child_of
    targets:
      - CAPRMEDIO-GOV-REQU-394--canonical-toml-artifacts
---

# Decision — Keep JSON Schema at its standard boundary

Files whose primary contract is JSON Schema remain canonical JSON. They are an
externally prescribed interoperability boundary, like GitHub Actions or host
skill metadata, rather than ordinary CAPRMEDIO-owned structured artifacts.

The generic TOML migration must classify and retain these files, must not emit
an editable TOML duplicate, and must continue validating them as JSON Schema.
Any future DSET schema DSL and generated JSON adapter require separate accepted
authority, a lossless mapping, and a freshness gate before replacing this
boundary.

## Rationale

A private TOML encoding for mixed JSON values and JSON-Schema keywords would
be harder to read, less interoperable, and another schema language to maintain.
Keeping the standard carrier avoids dual authority while applying TOML to the
project artifacts where it materially improves authoring.

This emitted Decision atom is immutable. Later correction requires a successor
Decision and append-only lifecycle evidence.

## Primary claim

Standards-compliant JSON Schema files are externally prescribed contract carriers and remain canonical JSON exceptions rather than generated copies of a private TOML schema dialect.
