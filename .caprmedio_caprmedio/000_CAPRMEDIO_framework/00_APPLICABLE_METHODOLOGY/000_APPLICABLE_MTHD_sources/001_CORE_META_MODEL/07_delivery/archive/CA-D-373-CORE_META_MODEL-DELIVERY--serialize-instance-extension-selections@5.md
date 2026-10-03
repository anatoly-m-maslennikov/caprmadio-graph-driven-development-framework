---
subjects:
  governs: "Framework Instance Settings/Extension selections"
  depends_on:
    - "Framework Instance Settings"
    - "Extension"
version: 5
updated_at: "2026-09-09 23:04:14 +0400"
relations:
  child_of:
    - "CA-D-361"
---
# Serialize instance Extension selections

the Framework Instance Settings TOML Carrier **must** encode enabled **or** disabled Extensions with selected revisions **when** applicable **and** retained per-Extension settings; retained settings **must not** activate a disabled Extension.
