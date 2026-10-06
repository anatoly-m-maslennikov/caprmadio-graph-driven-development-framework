---
atom_id: CA-C-490
content_role: Concern
type: Problem
current_scope_unit: PROMPTS
local_tier: Standard
global_tier: 11
status: active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-06 03:53:17 +0000"
subjects:
  governs: "Implementation Workflow/workspace admission"
  depends_on: [Implementation, Workflow, Action, Carrier]
relations:
  concern_about: [CA-P-1764]
---
# Summary

Accept safe workspace ancestor aliases

## Concern

A valid absolute workspace whose ancestor canonicalizes through a system alias is rejected before the Implementation Action can execute.

## Evidences

At commit c011b68fa, IMPLEMENTATION_WORKFLOW/implementation_actions.py:207 compares resolved and lexical paths. On macOS, /var resolves to /private/var. The focused tests test_selected_project_root_is_used_instead_of_immutable_code_root and test_fixed_test_first_path_performs_real_baseline_candidate_and_assertion reproduce blocked results instead of implemented/evaluation_ready.

## Blast radius

W09 implementation admission and the full release suite.

## Disposition

CA-P-1764 canonicalizes legitimate ancestors while retaining leaf-symlink and protected-authority overlap refusal. Validate with a platform-independent regression before resolving.
