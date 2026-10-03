---
atom_id: CA-D-492
content_role: Delivery
type: Delivery
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
author: Anatoly Maslennikov
status: Active
cce_version: cce_1
cce_form: serialization
subjects:
  governs: "Tool/VALIDATE_ATOMS/Request"
  depends_on:
    - "Tool/VALIDATE_ATOMS"
    - "Action"
    - "Project Structure"
    - "Global Tier"
    - "Local Tier"
    - "Scope Unit"
    - "Artifact/Revision"
version: 3
updated_at: "2026-09-24 14:07:30 +0000"
relations:
  delivery_for:
    - CA-R-1622
    - CA-R-1623
  relates_to:
    - CA-O-087
---
# Summary

Serialize Atom validator requests

## Claim

a `VALIDATE_ATOMS` request **must** use the following closed JSON representation of the Check Atoms inputs.

### Scalar and object conventions

- a String below is a nonempty JSON string; a Path is an absolute local filesystem path. an Integer excludes Booleans. a Digest is **=64** lowercase hexadecimal SHA-256 characters.
- a File Binding is an object with required `path: Path` **and** optional `sha256: Digest`. an Atom Binding has required `atom_id: String`, `version: Integer >=1`, `sha256: Digest`, **and** `path: Path`.
- **every** object rejects unknown keys, duplicate JSON keys, non-finite numbers, **and** wrong types. null is forbidden **unless** expressly admitted. an optional absent field follows its stated default; an invalid supplied value **must not** silently fall back.
- lists of paths, identifiers, Statuses, tiers, **and** references are sets: reject duplicates **and** resolve them deterministically. data **must not** contain executable selectors **or** code.

### Top-level object

| Key | Shape | Presence **and** default |
|---|---|---|
| `schema_version` | Integer **=1** | required |
| `source_roots` | nonempty list of Path | required; candidate-discovery boundary |
| `allowed_read_roots` | nonempty list of Path | required; grants no permission |
| `methodology` | Methodology object below | required |
| `selection` | Selection object below | required |
| `action_binding` | Atom Binding | optional; otherwise resolve the admitted CA-O-087 Revision from methodology |
| `project_structure` | File Binding | optional; required context **when** unit identity **or** descendants need it |
| `reference_roots` | list of Path | optional; default empty; resolution context **only** |
| `exclude_paths` | list of Path | optional; default empty; exact files **or** directory subtrees excluded from discovery |
| `limits` | Limits object below | optional partial per-invocation overrides |
| `framework_settings` | File Binding | optional selected Framework Instance Settings Carrier |
| `default_settings` | File Binding | optional locator for the Default Settings selected by applicable Delivery authority |
| `run_context` | object with optional `workflow_run_id: String` **and** `step_run_id: String` | optional; default empty |
| `rule_bundle` | Rule Bundle below | optional derived input; never authority **or** executable code |

read supplied paths **only** after boundary checks. an unavailable required file **or** stale supplied digest is an assessment gap **when** the request is otherwise well formed. a missing permission is **not** resolved by a locator. no unsupported schema version is executed.

### Methodology

- required `kind`: `sources` **or** `projection`; required `roots`: a nonempty list of Path.
- optional `frontier`: a nonempty list of Atom Binding. **when** supplied, it pins the complete applicable authority frontier, **not** an arbitrary subset capable of suppressing checks; otherwise resolve **and** record that frontier from the selected methodology.
- source selection must preserve the applicable Core, selected Extensions, **and** Project Configuration contributions **and** their conflict disposition. unresolved composition, missing authority, **or** unverifiable completeness yields `incomplete`; this Tool does **not** compile, repair, **or** approve a methodology.

### Selection

- admit optional `scope_unit: String`, `include_descendants: Boolean`, `global_tiers: nonempty list of Integer`, `local_tiers: nonempty list of String`, `atoms: nonempty list of Atom Selector`, **and** `statuses` below. require **>=1** of `scope_unit`, `global_tiers`, `local_tiers`, **or** `atoms`.
- `include_descendants` defaults **to** `false` **and** is admitted **only** with `scope_unit`. criteria intersect; values within a list are alternatives.
- `statuses` is the keyword `active`, the keyword `all`, **or** a nonempty list of exact Status values admitted by applicable Status models. `active` means the model's Active classification, **not** a hard-coded spelling. `all` includes historical **and** current Revision candidates of **every** Status **and** does **not** excuse an invalid Status value.
- without `atoms`, omitted `statuses` defaults **to** `active`. with `atoms`, omission adds no Status filter: explicit Atom/Revision selection remains exact. an explicitly supplied Status filter still intersects that list.
- an Atom Selector is an object with optional `atom_id: String`, `version: Integer >=1`, **and** `carrier_path: Path`. require `atom_id` **or** `carrier_path`; `version` requires `atom_id`. all supplied selectors **must** agree with internally carried values. a locator **may** identify an unassigned Draft **or** malformed candidate.
- an ID lacking Version selects **only** **when** the applicable filters leave **=1** authoritative Revision. multiple Revisions remain ambiguous; do **not** guess by highest Version, newest timestamp, filename, **or** traversal order. a projected representation of that same Revision does **not** create another authoritative identity.
- distinguish invalid selector syntax from valid but unresolved membership. unavailable Status/Scope authority is an incomplete assessment; an explicit Status value absent from complete applicable models is an invalid request.

### Rule Bundle

- the optional object has required `schema_version: Integer =1`, `authority: nonempty list of Atom Binding`, **and** `checks: list of Check Binding`.
- a Check Binding has required `code: String`, `adapter_id: String`, `authority: nonempty list of Atom Binding`, **and** `parameters: object`. codes are unique; `adapter_id` resolves **only** **to** an installed, source-bound adapter. its parameter schema **must** be admitted by the exact authority binding; otherwise the check is unsupported, **not** executed.
- the bundle is a data-only Projection. compare its authority frontier **and** rule coverage against independently resolved applicable obligations under CA-M-316. omitted checks, stale bindings, undeclared parameters, **or** contradictory constraints cannot establish complete coverage. no bundle value admits an additional Atom Property.

### Limits and settings

- Limits admits **only** `max_candidates`, `max_file_bytes`, `max_total_read_bytes`, `timeout_seconds`, **and** `max_findings`, **every** supplied value an Integer **>=1**.
- the same parameter names live under `[atom_validation]` **in** Framework Instance Settings **and** Default Settings. resolve **every** parameter independently: explicit request value, otherwise explicit instance value, otherwise selected Default Settings value. missing required defaults, invalid values, **or** unresolved settings bindings produce `error` **before** candidate validation; do **not** embed competing numeric defaults **in** code **or** Atom Claims.
- host permissions **and** hard execution ceilings remain upper bounds, **not** overrideable settings; an impossible requested bound is rejected **before** execution.
- count distinct candidate paths toward `max_candidates`; count raw file size toward `max_file_bytes`; count **all** bytes read, including authority, references, **and** currentness rereads, toward `max_total_read_bytes`. start the monotonic deadline **before** methodology resolution. count emitted findings toward `max_findings`.
- check bounds **before** the next bounded operation. reaching a bound that prevents outstanding work yields `incomplete`; preserve completed findings **and** report the affected limit **and** unassessed work. unavailable measurement **or** execution failure yields `error`, **not** a pass.
