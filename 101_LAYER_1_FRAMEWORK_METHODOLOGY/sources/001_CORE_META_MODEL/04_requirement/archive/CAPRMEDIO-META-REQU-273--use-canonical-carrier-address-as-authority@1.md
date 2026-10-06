---
subject_scopes:
  - artifact-model
tier: core
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  replacement_of:
    - CAPRMEDIO-META-REQU-258--derive-artifact-coordinates-from-registered-types
    - CAPRMEDIO-META-REQU-259--nonduplicative-current-artifact-properties
  child_of:
    - CAPRMEDIO-REQU-065--natural-operator-surface
    - CAPRMEDIO-REQU-003--apply-dry-across-caprmedio
---
# Use canonical carrier address as authority

Whenever a governed fact can be derived completely and unambiguously from an artifact's canonical project-relative directory, filename, or file extension, that carrier address is the single source of truth for the fact. The artifact must not repeat the derived value in frontmatter or body metadata.

The canonical resolver derives, when encoded by the active GOV grammar:

- ambient project identity from the repository;
- structural scope from the ordered structural-scope directories;
- Content role from the numbered Content-role directory;
- an Atom's draft, active, completed-Plan, or archived lifecycle position from
  direct, `drafts/`, `done/`, or `archive/` placement;
- Artifact type, optional subtype, sequence, and filename summary from the filename; and
- carrier format from the file extension.

The decoded registered type and optional subtype continue to determine their registered semantic coordinates. An explicit property remains mandatory only when its meaning cannot be derived safely from the canonical carrier address. Priority, provenance, Subject scope, relations, applicability, and other non-address facts therefore remain explicit unless another canonical owner is separately established.

A resolver must fail closed when an address is unknown, ambiguous, malformed, or inconsistent with its registered grammar. A rename or move that changes a derived fact is a governed semantic operation, not a cosmetic edit, and Git preserves its history.

CAPRMEDIO uses canonical directory placement, filenames, and extensions as the sole authority for every fact they encode deterministically and forbids duplicate embedded representations of those facts.
