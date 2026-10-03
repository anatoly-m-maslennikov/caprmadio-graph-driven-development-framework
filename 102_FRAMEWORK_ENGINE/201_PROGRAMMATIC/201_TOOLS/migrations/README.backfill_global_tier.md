# Backfill Global Tier

`backfill_global_tier.py` derives a missing `global_tier` from an Atom's carried
`current_scope_unit` and `local_tier`, using an explicit, frozen logical parent
map. It never uses a filename, physical directory depth, navigational number,
or relational Claim target as the owning unit.

Authority: CA-R-1388, CA-R-1389, CA-R-1390, CA-R-1391, CA-R-680, CA-R-1442.

- Project: Principle = 0, Core = 1, Standard = 2.
- Non-Project: Core = direct parent's Standard + 1; General = Core + 1;
  Standard = Core + 2. Equivalently, `3 * structural_level + (0, 1, 2)`.
- An explicitly identified external Project Goal is -1 and has no Local Tier.

The caller supplies current carrier hashes and a reviewed parent map from the
authoritative Project Structure, or an explicit Operator-directed migration
context. This script neither creates nor replaces `project_structure.toml`.

```json
{
  "source_root": "/absolute/methodology_sources",
  "scope_context": {
    "project": "example",
    "parents": {"example": null, "METHODS": "example"},
    "operators": [],
    "evidence": "Reviewed Project Structure binding"
  },
  "carriers": [{"path": "/absolute/methodology_sources/atom.md", "sha256": "actual SHA-256"}]
}
```

```sh
python backfill_global_tier.py --input request.json --output plan.json
python backfill_global_tier.py --apply plan.json --output receipt.json
```

Review the preview before applying. Apply checks the frozen request, re-derives
every proposed value, and uses the existing safe property-backfill writer:
whole-batch baseline checks, exact prior-Revision archives, Version increment,
unchanged Claims and `updated_at`, atomic carrier replacement, and idempotent
repeat. Unknown owners, invalid tiers, hierarchy cycles, inactive/projected
carriers, changed inputs, and mismatching existing Global Tiers block the batch.
An already correct Global Tier is preserved. No value is silently overwritten.

Missing Local Tier is an error, not a filename-derived Standard default. The
single explicit exception is the external Project Goal described above.
Scope Units can have more than ten structural levels.

The caller remains responsible for the applicable Journal integration and
refreshing exact-byte checker pins/fixtures after preservation verification.
No full-methodology conformance is claimed by this property-only migration.
