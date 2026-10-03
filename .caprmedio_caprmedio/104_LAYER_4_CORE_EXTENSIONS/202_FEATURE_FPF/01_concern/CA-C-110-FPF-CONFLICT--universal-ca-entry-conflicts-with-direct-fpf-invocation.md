---
atom_id: CA-C-110
cce_version: cce_1
cce_form: concern_conflict
priority: high
subjects:
  governs: "FPF"
  depends_on:
    - "Skill"
    - "Extension"
version: 1
updated_at: "2026-09-15 02:22:01 +0400"
relations: {}
---
# Universal `ca` entry conflicts with direct FPF invocation

Active Skills Requirement `CAPRMEDIO-FRAMEWORK-ENGINE-REQU-558` requires `ca` as the universal primary Skill entry, while the latest Operator decision and CA-R-1474 require the CAPRMEDIO-aligned FPF Extension to be invoked directly as `$fpf` without a `ca` wrapper; both claims cannot govern the same FPF Extension invocation boundary, so the obsolete universal-entry authority must be replaced or retired before this Extension is activated.
