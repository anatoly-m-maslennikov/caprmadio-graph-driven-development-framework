---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "Journal"
  depends_on:
    - "Core Meta-Model"
    - "Extension"
    - "Projection/Type: Artifact Change Log"
    - "Projection/Type: Process Log"
version: 2
updated_at: "2026-09-14 06:21:07 +0400"
relations:
  evaluation_for:
    - CA-R-1466
    - CAPRMEDIO-META-REQU-158
    - CA-R-1463
    - CA-R-1467
    - CA-R-1468
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Validate Journal independence from Git

the Evaluation **must** reject a Core Meta-Model rule that makes Journal recording, replacement evidence, **or** either canonical log Projection depend on Git installation, commit topology, hooks, **or** commit messages.

with no Git Extension selected, admitted Journal records **and** their Artifact Change Log **and** Process Log Projections **must** remain valid under their applicable authority. with the Git Extension selected, its commit references **may** add provenance but **must not** create a second authoritative event history. changing **or** removing secondary Git history **must not** destroy the recorded identity **and** evidence needed **to** rebuild the two logs. a missing **or** invalid authoritative Journal remains a failure **in** either case.
