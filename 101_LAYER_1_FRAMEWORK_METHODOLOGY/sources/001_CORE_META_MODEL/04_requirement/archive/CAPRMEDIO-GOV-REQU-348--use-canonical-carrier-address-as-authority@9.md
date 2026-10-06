---
cce_version: cce_1
cce_form: classification
subjects:
  - carrier-format
version: 9
updated_at: 2026-08-23 12:02:00
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CA-R-1054
  replacement_of:
    - CAPRMEDIO-META-REQU-273--use-canonical-carrier-address-as-authority
---
# Use canonical carrier address as authority

When the active GOVERNANCE grammar derives a governed fact completely and unambiguously from a Carrier's canonical project-relative directory, filename, or extension, that address is the fact's sole authority and the Carrier MUST NOT repeat it as embedded metadata. For a role-classified Atom, the filename's immutable Atom-ID segment is the sole authority for Atom ID and `atom_id` frontmatter is forbidden as derived duplication. An expressly registered native Atom whose executable filename cannot carry the role-classified grammar uses its governed external identity binding.

The resolver derives only registered address facts, including Atom ID, Structural scope, Content role, lifecycle placement, Tier, Type, Summary, and format, and fails closed for an unknown, ambiguous, malformed, missing, duplicated, or inconsistent fact. A move or rename that changes a derived address fact is a governed operation but MUST preserve the Atom-ID segment of the same identified Atom.
