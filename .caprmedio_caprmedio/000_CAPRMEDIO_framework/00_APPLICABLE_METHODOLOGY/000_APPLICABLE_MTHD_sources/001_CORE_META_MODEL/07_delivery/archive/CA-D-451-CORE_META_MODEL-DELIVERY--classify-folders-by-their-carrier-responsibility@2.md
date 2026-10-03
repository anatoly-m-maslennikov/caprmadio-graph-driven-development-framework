---
subjects:
  governs: "Directory Carrier"
  depends_on:
    - "Structural Entity"
    - "Artifact/Carrier Placement"
    - "Atom/Content Role"
version: 2
updated_at: "2026-09-17 12:25:20 +0000"
relations: {}
---
# Classify folders by their Carrier responsibility

a filesystem folder **must** be classified as a Directory Carrier **only** **when** it carries a Structural Entity under CA-D-263.

- a folder's visibility **in** a graph **or** its containment of files does **not** itself establish that binding.
- administrative Content Role directories **and** Status subdirectories provide Carrier placement, **not** separate Structural Entities **or** Directory Carriers. Status placement remains governed by CA-D-295 **and** CA-D-352.
