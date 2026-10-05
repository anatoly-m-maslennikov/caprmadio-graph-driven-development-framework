---
atom_id: CA-C-480
content_role: Concern
type: Problem
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-05 22:11:52 +0000"
subjects:
  governs: "Tool/RELEASE_VERSION/Candidate E2E Driver"
  depends_on: [Tool, Release Version, Candidate Manifest, Docker Image, Test Suite, JUnit Report]
relations:
  concern_about: [CA-P-1751, CA-P-1745]
---
# Summary

Reject duplicate E2E testcase identities

## Concern

The actual Driver emits two passing JUnit rows with the same testcase identity and returns zero, violating the exact-once declared-case requirement.

## Evidences

The initial characterization was replaced by an enforcing regression. The focused real Driver suite now has seven passing cases and one expected RED: duplicate (classname, name) identities return zero rather than non-passing. No Docker or fabricated Driver XML was used.

## Blast radius

P1751 behavioral acceptance and the separately admitted Candidate E2E/Full Gate boundary. Real Docker and runtime installation remain separately unproved.

## Disposition

Reject duplicate observed testcase identities before a passing Driver outcome. Keep all actual unittest.TestResult observations and terminal outcomes; do not exclude or silently deduplicate cases.
