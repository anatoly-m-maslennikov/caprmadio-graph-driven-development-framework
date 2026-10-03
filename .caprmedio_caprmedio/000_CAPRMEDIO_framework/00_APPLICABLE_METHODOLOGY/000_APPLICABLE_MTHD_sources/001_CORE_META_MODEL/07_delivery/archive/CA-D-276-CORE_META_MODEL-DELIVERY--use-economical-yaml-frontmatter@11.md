---
subjects:
  governs: "Markdown Atom Carrier/YAML Frontmatter"
  depends_on: []
version: 11
updated_at: "2026-09-24 14:16:19 +0000"
relations: {}
---
# Use Economical YAML Frontmatter

the YAML Frontmatter of a Markdown Atom Carrier **must** use the least syntax **and** nesting that preserves unambiguous deterministic parsing, validation, extensibility, **and** human readability.

### Common field encoding

use the following field encodings for the applicable Atom Properties. presence follows the cited Property authority, **not** observed filename tokens. a String is a nonempty YAML string; an Integer excludes Booleans. a null value does **not** satisfy a required Property.

| Property | Top-level field | Encoding **and** applicable presence |
|---|---|---|
| Atom Identity | `atom_id` | String under CA-D-446; forbidden for Draft, required for non-Draft; carry Version separately |
| Content Role | `content_role` | **=1** String selecting its canonical Content Role; resolve the admitted domain from applicable authority |
| Type | `type` | **=1** String selecting the admitted Type under the carried Content Role; filename Type tokens are **not** a second value |
| current Scope Unit **or** Operator owner | `current_scope_unit` | **=1** String: the registered Scope Unit Name, **or**, for an admitted Atom with no Scope Unit owner, the registered name of **=1** human Operator under CA-R-930 |
| Claim Target Scope Unit | `claim_target_scope_unit` | use CA-D-482 |
| Local Tier | `local_tier` | String under CA-R-155; omit for a Project Goal under CA-R-1393; otherwise carry the selected canonical tier explicitly, including Standard |
| Global Tier | `global_tier` | **=1** Integer under CA-R-1413, including an admitted negative value; verify against applicable tier authority **without** substituting a filename-derived value |
| Version **and** Updated At | `version`, `updated_at` | use CA-D-270 |
| Author | `author` | use CA-D-274 |
| Status | `status` | use CA-D-483 |
| Subjects | `subjects` | use CA-D-269; **only** the governed Subject keys **and** their admitted encodings |
| authored Atom Relations | `relations` | use CA-D-268; omission **or** an empty mapping represents no authored Relations; each present Relation Kind carries its nonempty target collection |

- `current_scope_unit` **must not** be null, a list, a joined set of names, **or** replaced by an `operators` field. an Operator owner is **not** thereby a Scope Unit; resolve the permitted reference kind from the applicable Atom model **and** registered identities. never infer the owner from its filename.
- the Revision Identifier is composed from `atom_id` **and** `version` under CA-D-446; do **not** duplicate it **in** an `identifier` field. a Draft has Version **and** Updated At but no assigned Atom ID.
- Summary **and** Claim use their body sections under CA-D-479, **not** `summary` **or** `claim` frontmatter copies. other body Properties use their own registered section authority.

### Conditional fields and expansion

- a Plan's explicit `assignee` uses **<=1** String identifying an admitted Actor under CA-D-473. `autonomous_confidence_threshold` **and** `implementation_retry_limit` use their integer encodings under CA-D-472 **and** CA-D-447. inherited values remain omitted unless explicitly selected; self-sufficiency does **not** copy them.
- `priority` follows CA-D-386 for Concern Atoms **only**. additional Plan, Operations, proof, **or** other Type-specific fields require their applicable Delivery declarations; their occurrence **in** old Carriers does **not** admit them.
- the generated `projection` block is admitted **only** **in** a projected representation under CA-D-305, with **only** its defined `source_carrier_path` String. it is **not** an authored source Atom Property.
- a new field **or** nested key requires applicable authority that settles its canonical location, value type, cardinality, admission condition, **and** permitted values **or** reference resolution. unadmitted fields are invalid; an admitted Property with an unsettled encoding is a schema gap, **not** permission **to** guess **or** report full conformance.
- apply explicitly governed migration exceptions **only** within their declared boundary. legacy presence alone is **not** an exception; retired fields under CA-D-478 remain rejected.
