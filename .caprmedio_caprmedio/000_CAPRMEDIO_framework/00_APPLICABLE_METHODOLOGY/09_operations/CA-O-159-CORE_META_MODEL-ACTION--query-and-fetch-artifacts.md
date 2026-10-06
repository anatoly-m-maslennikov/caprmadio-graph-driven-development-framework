---
atom_id: "CA-O-159"
content_role: "Operations"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
global_tier: 11
status: "Active"
author: "Anatoly Maslennikov"
type: "Action"
version: 2
updated_at: "2026-10-05 01:20:00 +0400"
subjects:
  governs: "Artifact query and selected fetch"
  depends_on: [Artifact, Markdown, Action, Tool, Journal]
relations: {}
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/09_operations/CA-O-159-CORE_META_MODEL-ACTION--query-and-fetch-artifacts.md
  source_atom_id: CA-O-159
  source_atom_revision: 2
  source_sha256: 3fd33badbff039e58c1c0b31dfbf3608c37a58d779a1b3ebc14d7bb5ee27dc08
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Query and fetch Artifacts

## Action

Query and fetch Artifacts **must** evaluate a caller filter only against one
sealed, allowlisted Markdown-carrier snapshot and return matching canonical
Artifact IDs by default, or only the caller-selected frontmatter properties
and sections when fetch is requested.

## Scope

This Action may be invoked standalone or by CA-O-160 for CA-O-158. An Atom
Artifact carries `atom_id`; every other admitted Markdown Artifact carries
`artifact_id`. Exactly one applicable identity is required; missing,
conflicting, or snapshot-duplicate identity is diagnostic. A filename, path,
or heading never supplies or repairs identity. The Action reads neither credentials
nor secrets and evaluates neither SQL, code, templates, nor arbitrary
expressions.

## Details

1. This Action alone enumerates and retains one ordered, allowlisted snapshot
   within CA-R-1850 budgets before evaluation. Members record safe relative
   path, identity, and digest. Unreadable Markdown, malformed frontmatter,
   identity failure, duplicate frontmatter key/heading path, or incomplete
   enumeration is diagnostic, not an accepted partial result. A continuation
   enumerates nothing: it validates its exact retained member paths, identities,
   and digests or rejects.
2. A frontmatter selector is JSON string `"fm:/<pointer>"`; a section selector
   is `"section:/<level>:<heading>/<level>:<heading>"`. Pointer tokens and each
   complete heading segment use RFC 6901 escaping (`~` -> `~0`, `/` -> `~1`).
   JSON Pointer addresses nested maps and arrays. Namespaces are distinct.
   Explicit null is a value; absent selected field returns `missing`, never null.
3. Apply CA-R-1850's closed JSON grammar. YAML temporal values normalize to
   explicit strings; strings are never dates. Deep typed equality distinguishes
   booleans from numbers, supports arrays/maps, and never coerces values.
4. Apply every caller-selected property and status exactly as expressed; no
   implicit `Active` filter, status narrowing, or property exclusion exists.
   With no fetch selection return only Artifact IDs. With a selection return
   only IDs plus those named values/sections and their explicit `missing` or
   `null` states.
5. Sort matches by canonical Artifact ID in ascending bytewise order. A page
   uses a positive limit no greater than configured `query.max_page_size` and an opaque
   cursor bound to retained snapshot digest and last returned ID. An absent cursor
   starts the first page; a changed, malformed, foreign-snapshot, exhausted, or exact-member-mismatched cursor
   cursor is an error. Every response reports snapshot reference/digest,
   examined count, matched count, returned count, and `has_more`, so coverage
   is truthful and pagination cannot silently cross snapshots.
