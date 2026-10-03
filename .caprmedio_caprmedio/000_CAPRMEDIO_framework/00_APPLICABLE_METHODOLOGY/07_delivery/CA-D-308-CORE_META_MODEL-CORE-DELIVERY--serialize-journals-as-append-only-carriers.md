---
atom_id: CA-D-308
cce_version: cce_1
cce_form: serialization
subjects:
  governs:
    continuant:
      - Journal/Carrier
  depends_on:
    continuant:
      - Journal/Record
version: 4
updated_at: 2026-09-06 01:45:12 +0400
relations: {}
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/07_delivery/CA-D-308-CORE_META_MODEL-CORE-DELIVERY--serialize-journals-as-append-only-carriers.md
---
# Serialize Journals as Append-Only Carriers

**every** Journal Carrier **must** serialize its ordered Records append-only **in** its registered format **and** **must not** rewrite an admitted Record.
