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
version: 1
updated_at: "2026-10-05 00:00:00 +0400"
subjects:
  governs: "Artifact query and selected fetch"
  depends_on: [Artifact, Markdown, Action, Tool, Journal]
relations: {}
---
# Summary

Query and fetch Artifacts

## Action

Query and fetch Artifacts **must** evaluate a caller filter only against one
sealed, allowlisted Markdown-carrier snapshot and return matching canonical
Artifact IDs by default, or only the caller-selected frontmatter properties
and sections when fetch is requested.

## Scope

This Action is called only by CA-O-160 for CA-O-158. `atom_id` carried in a
valid frontmatter block is the canonical Artifact identity; a filename, path,
or heading never supplies or repairs it. The Action reads neither credentials
nor secrets and evaluates neither SQL, code, templates, nor arbitrary
expressions.

## Details

1. Seal an ordered snapshot of the caller-selected, allowlisted source root
   before evaluating a filter. Each member records safe relative path and
   content digest; unreadable Markdown, malformed frontmatter, a missing
   `atom_id`, duplicate frontmatter key, duplicate heading path, or an
   incomplete enumeration returns an incomplete diagnostic, not an accepted
   partial result.
2. Address frontmatter as `fm:<exact-key>` and a section as
   `section:<slash-separated level-and-text path>`. The namespaces are
   distinct: a same-spelled frontmatter key and heading do not collide. A
   repeated key or heading path is ambiguous and is rejected rather than
   resolved by position. An explicitly carried YAML `null` is a value; an
   absent selected field is returned as `missing`, not as `null`.
3. Apply CA-R-1850's closed literal comparison grammar. For this Action, YAML
   scalar types must match exactly, section values are strings, no coercion
   occurs, and an absent selector makes its comparison false. Invalid syntax,
   selector, type, or literal is rejected.
4. Apply every caller-selected property and status exactly as expressed; no
   implicit `Active` filter, status narrowing, or property exclusion exists.
   With no fetch selection return only Artifact IDs. With a selection return
   only IDs plus those named values/sections and their explicit `missing` or
   `null` states.
5. Sort matches by canonical Artifact ID in ascending bytewise order. A page
   uses a positive limit no greater than the configured bound and an opaque
   cursor bound to the snapshot digest and last returned ID. An absent cursor
   starts the first page; a changed, malformed, foreign-snapshot, or exhausted
   cursor is an error. Every response reports snapshot reference/digest,
   examined count, matched count, returned count, and `has_more`, so coverage
   is truthful and pagination cannot silently cross snapshots.
