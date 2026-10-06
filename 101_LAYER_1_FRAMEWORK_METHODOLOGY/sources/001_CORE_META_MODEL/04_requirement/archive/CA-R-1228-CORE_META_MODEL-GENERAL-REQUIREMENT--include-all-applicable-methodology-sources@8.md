---
atom_id: CA-R-1228
cce_version: cce_1
cce_form: obligation
subjects:
  governs:
    continuant:
      - Applicable Methodology/Sources
  depends_on:
    continuant:
      - Methodology Source
      - Core Meta-Model
      - Local Configuration
      - Extension
      - Framework Instance Settings
version: 8
updated_at: "2026-09-11 02:49:55 +0400"
relations: {}
---
# Include all applicable Methodology Sources

the Applicable Methodology source set **must** include CORE_META_MODEL, LOCAL_CONFIGURATION, **and** **every** installed Extension Source applicable under the current Framework Instance Settings. **when** **none** is applicable, the Extension contribution is empty **without** a rule requiring zero installed Extensions **or** a Carrier for an empty INSTALLED_EXTENSIONS collection.
