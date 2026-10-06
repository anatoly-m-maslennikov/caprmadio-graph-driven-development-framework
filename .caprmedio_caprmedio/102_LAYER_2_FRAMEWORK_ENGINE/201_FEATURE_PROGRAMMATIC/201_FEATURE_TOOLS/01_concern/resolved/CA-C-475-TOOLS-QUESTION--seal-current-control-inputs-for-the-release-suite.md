---
atom_id: CA-C-475
content_role: Concern
type: Question
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: resolved
author: Anatoly Maslennikov
version: 2
updated_at: "2026-10-05 19:52:27 +0000"
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

## Resolution

The source contract was independently accepted in b7d44ccfa and the repaired implementation in 689dd212f. Independent review accepts exact closed references, descriptor-safe capture without shared-reader mutation, fresh trusted checks immediately before and after execution, canonical retained context and digest-bound report admission. Root passed 34 focused context/timing/checkpoint/handoff/executor/image-reader cases; the driver owner passed 12 golden cases. This resolves the reference-context design and implementation question only. Actual Docker/full-suite, first N and Release promotion remain separate open gates; C476 records the E2E environment prerequisite.
