---
subject_scopes:
  - provenance
version: 15
updated_at: 2026-08-22 04:39:08
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-GOV-REQU-345--represent-accepted-meaning-faithfully
    - CAPRMEDIO-META-REQU-110--bind-governed-transactions-to-stable-artifact-revisions
---
# Use direct typed-relation change-set commit messages

Every governed Git commit represents exactly one governed subject file identity through one change set and uses exactly one line as its complete commit message:

```text
<direct-relations> | <CHANGES> | <affected-file>
```

The canonical source of this line is the structured `governed_file_change` event in the Project Work Journal. The renderer derives the three fields from that event's `sources`, `action_type`, and singular `result`, consulting the event named by `previous_result_event` only when the syntax needs the immediately previous carrier address. The rendered line must not be stored again in the Journal as an `action_message` or other duplicate payload.

## Direct typed relations

The left field renders the ordered `sources` entries that preserve every direct typed relation reference from the affected file to the Atom Revisions selected by the registry. Relations may be authored or programmatically derived from the current graph. The relation registry declares the authored direction, derived inverse name, and endpoint position for each kind; the generator must not infer direction from a relation's spelling. Each entry uses the canonical relation kind, target carrier filename, and target version:

```text
<relation-kind>=<filename>@<version>
```

Targets of the same relation kind are separated by a comma followed by one space. Relation groups are separated by a semicolon followed by one space and sorted first by relation kind and then by filename. `0` represents no direct typed relation reference. Transitive ancestors and association-only relations are excluded. A derived inverse relation is included only when the registry selects its endpoint for the affected file.

`ADD`, `UPDATE`, and `MOVE+UPDATE` resolve relations from the resulting staged graph, `MOVE` resolves them from the unchanged Artifact graph, and `REMOVE` resolves them from the last committed graph. Target versions must be current immediately before the change. `updated_at` is omitted because the Git commit already records the change time.

## Changes

The change set renders `action_type` and is exactly one of `ADD`, `MOVE`, `UPDATE`, `MOVE+UPDATE`, or `REMOVE`. `ADD` and `REMOVE` are exclusive lifecycle changes. `MOVE` means that the directory or Structural location changes. `UPDATE` means that content, filename, or other governed carrier state changes. `MOVE+UPDATE` means that both changes occur for the same file identity.

An add has no `previous_result_event` and names its present `result` Revision:

```text
child_of=parent.md@2 | ADD | new-file.md@1
```

A move renders the previous path from `previous_result_event` and the new path from the present `result`; it changes Structural location without changing content or filename and preserves the version:

```text
child_of=parent.md@2 | MOVE | old/path/file.md@3 -> new/path/file.md@3
```

An update names the present `result` Revision when the carrier filename is unchanged:

```text
child_of=parent.md@2; derived_from=analysis.md@1 | UPDATE | file.md@4
```

A rename is an update of the same file identity and renders the previous filename from `previous_result_event` and the current filename from `result`. A rename-only update preserves the version:

```text
child_of=parent.md@2 | UPDATE | old-file.md@3 -> new-file.md@3
```

A move and update may occur together for one file identity and render the previous and current carrier addresses from those same result events:

```text
child_of=parent.md@2 | MOVE+UPDATE | old/path/old-file.md@3 -> new/path/new-file.md@4
```

A remove names its singular removed-state `result`; `previous_result_event` identifies the immediate last present result without copying its path or digest into the removal event:

```text
child_of=parent.md@2 | REMOVE | file.md@4
```

Replacement uses the same typed-relation syntax as every other governed relation. First add the successor as an active Atom without authoring an inverse replacement edge:

```text
child_of=parent.md@2 | ADD | replacement-file.md@1
```

Then archive the predecessor in a `MOVE` whose authoritative Work
Journal event declares the direct `replaced_by` edge from that predecessor:

```text
replaced_by=replacement-file.md@1 | MOVE | active/old-file.md@4 -> archive/old-file.md@4
```

The successor must already be active before the predecessor change. The
authoritative archival Journal event is the only persisted replacement
declaration: neither the active successor nor the archived predecessor Atom
frontmatter stores `replaced_by` or `replacement_of`. The graph derives
`replacement_of` for inverse navigation. The archival move changes no
predecessor content, filename, relation frontmatter, or version. Adding each
successor and archiving each predecessor remain separate one-file commits.

An affected governed file uses `<filename>@<version>` and includes repository-relative path when the change set changes structural location. A governed native file without embedded Revision properties uses the version from its external revision binding. `UPDATE` may change content, filename, or both while preserving one file identity; content changes advance the version, while a rename-only update preserves it. `MOVE` changes structural location only. `MOVE+UPDATE` changes structural location and also performs an update. No governed commit may contain more than one governed subject file identity.

The same commit must also contain every and only receipt-bound Work Journal line related to the subject action by the same `action_id`. Related records may span multiple Journal carriers because of partition rollover. These lines and carriers are provenance sidecars of the one governed subject change and do not count as additional governed subjects; no unrelated Journal record may share the commit.

The message contains no parentheses, free-form labels, summary, description, body, or trailers. Canonical relation kinds and change tokens are structural syntax rather than prose labels. Once another commit references an Atom Revision through a direct typed relation, the referenced Git history must remain reachable and unchanged.

## Rationale

One governed subject change plus its complete related Journal sidecar set gives Hook and retry logic one deterministic recovery boundary, preserves the exact direct typed-relation frontier consumed by the change, and prevents unrelated work from sharing that boundary.
