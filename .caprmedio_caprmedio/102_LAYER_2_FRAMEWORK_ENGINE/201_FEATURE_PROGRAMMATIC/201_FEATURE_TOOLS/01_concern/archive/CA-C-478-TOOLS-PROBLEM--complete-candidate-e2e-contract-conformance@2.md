---
atom_id: CA-C-478
content_role: Concern
type: Problem
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: active
author: Anatoly Maslennikov
version: 2
updated_at: "2026-10-05 22:18:24 +0000"
subjects:
  governs: "Tool/RELEASE_VERSION/Candidate E2E contract conformance"
  depends_on: [Tool, Release Version, Candidate Manifest, Docker Image, Test Suite, JUnit Report, Journal]
relations:
  concern_about: [CA-P-1744, CA-P-1745, CA-P-1750, CA-P-1751, CA-P-1752, CA-P-1753, CA-P-1754]
---
# Summary

Complete Candidate E2E contract conformance

## Concern

The private Candidate E2E implementation is not yet fully accepted against D582; smoke tests do not prove its required bounded execution and durable receipt contract.

## Evidences

1. initial review found predecessor receipts were trusted by fields, the grammar digest substituted for the phase-map digest, and host executable identity was not sealed. Subsequent source review accepts their repaired reopening/map boundary.
2. a later review found host capability evidence was an unbound sidecar and the attested controller was not executed. The latest bounded static review accepts the repaired receipt-bound capability and actually executed frozen-N Driver; behavioral proof remains required.
3. the implementation still uses hard-coded caps and an invented total timeout rather than the six per-key Framework Instance parameters and canonical defaults required by D582.
4. the old behavioral fixture invokes production publication and is denied before the gate. A synthetic presealed golden fixture is being constructed; it must exercise unchanged predecessor readers without bypassing the real publication failure.

## Blast radius

P1744 and P1745 acceptance, Full Gate aggregation, current source admission and Release promotion. Actual Docker and publication permission blockers remain separate.

## Disposition

Finish the bounded P1750-P1754 decomposition, prove configured limits and receipt tamper/refusal cases using golden inputs, and obtain independent local acceptance. Keep real Docker, complete-suite and installed-runtime evidence unfinished until actually executed. No test-double or static-only result is Release acceptance.

## Current verification

The synthetic presealed fixture now passes the established suite/image byte readers and rejects receipt/source mutation. The incorrect comparison of the image reader's retained attempt path with the Project root is repaired. Six settings-backed caps and the capability/settings receipt bindings pass bounded static review; expanded gate behavior remains under test. Context and Driver repairs C479/C480 are resolved with real tests and saved in 5e0dfee93. Root confirmed 24 combined context/Driver/phase-map cases, five Runtime binding cases and two actual MCP stdio transport cases passing. D582#10 still requires explicit Harness source hashes, wall-clock timestamps and retained output/JUnit path bindings; that metadata repair is in progress. C478 remains Active pending the complete private-gate behavioral result and final acceptance.
