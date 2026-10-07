---
atom_id: CA-P-1828
content_role: Plan
type: Plan
label: Task
work_sequence_number: 8
current_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
status: Active
author: Anatoly Maslennikov
assignee: AI Agent
autonomous_confidence_threshold: 90
version: 1
updated_at: "2026-10-07 23:52:40 +0000"
subjects:
  governs: "Bind isolated Release fixtures to current control sources"
  depends_on: [Tool, Evaluation, Carrier, Manifest, Framework Package]
relations:
  is_decomposition_of: [CA-P-1620]
  blocks: [CA-P-1823]
---
# Summary

Bind isolated Release fixtures to current control sources

## Objective

Complete the existing isolated fixture snapshot with its exact source-admitted control closure and keep fixture writes inside container tmpfs.

## Details

- Input: the retained N23 diagnostic ran 109 cases, with 30 delivery passes and 79 image/initialization setup errors. Their engine-only snapshot lacked the selected binding manifest and attempted fixture writes under the read-only workspace.
- Reuse the existing reference-context reader to derive only current admitted control paths. Add no independent path registry, fixture-only selector rewrite, new admission semantics, writable host source mount or permission workaround. Preserve regular-file, symlink, secret-path, byte/mode and source-currentness checks.
- Use separate exclusive workers for the closure accessor, fixture runner and its tests; root owns source-pin refresh, Git and actual Docker execution. Estimated active work: <=15 minutes; preserve existing worker edits and old failed diagnostic evidence.
- Keep the actual Release Unit, E2E, Full Gate, source publication and promotion contracts unchanged. This work supplies focused regression evidence only; it does not replay N22 or queue N23.

## Definition of Done

The saved fixture snapshot contains the exact derived control closure. Tests prove completeness, preserved bytes/modes, missing/unsafe/secret refusal before Docker and a single read-only source mount with container-only writable workdir. Independent acceptance passes and the same delivery/image/initialization fixture selection runs with truthful results. Exact affected private-carrier source pins are refreshed through the existing authorized publisher; no focused result is claimed as a full Release gate.
