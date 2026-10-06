---
atom_id: CA-C-475
content_role: Concern
type: Question
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-05 18:51:25 +0000"
subjects:
  governs: "Release suite current control references"
  depends_on: [Evaluation, Manifest, Project Settings, Operator, Source Carrier, Test Suite]
relations:
  concern_about: [CA-P-1717, CA-P-1727]
---
# Summary

Seal current control inputs for the Release suite

## Concern

How should the read-only full-suite environment include current selected-source control inputs without making them candidate Implementation inputs or a competing source of truth?

## Evidences

Seven declared test modules read current selected bindings, registry/settings, the selected source registry, D572 and their exact source-pin closure. Those evaluator references are absent from the candidate package inventory. Captured-frontier golden data would be hermetic but would stop these tests from detecting current source-pin drift. An unsealed live checkout mount would violate the isolated suite boundary.

## Blast radius

Current-source admission assurance in the actual complete Framework suite. Candidate package/image identity, canonical authority, installed N and the published sixteen-route projection remain unchanged.

## Decision

Use a Suite Owner-derived, separately sealed read-only reference context for the exact current control closure. Bind its normalized digest in the private envelope and actual suite evidence; verify capture before execution and freshness afterward. Supply no caller-selected paths and copy no Journal, secrets or runtime state. Independent design review finds this compatible with the existing candidate inventory because it is evaluator-owned reference input, not candidate Implementation input. R1887/M344/E587/D580 and D579 schema 2 must be accepted before implementation. This choice records uncertainty under the Epic's autonomous policy; it is not execution or release evidence.
