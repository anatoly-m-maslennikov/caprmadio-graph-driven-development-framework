---
atom_id: CA-C-491
content_role: Concern
type: Problem
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: resolved
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-06 04:41:21 +0000"
subjects:
  governs: "Retained Release source-copy ownership"
  depends_on: [Implementation, Evaluation, Workflow Run, Journal, Manifest]
relations:
  concern_about: [CA-P-1774]
---
# Summary

Prove retained Release source-copy ownership

## Concern

Fresh Release Run `release-epic-resume-20261006-N6` stopped during source delivery because complete retained executing-N ownership could not be proved.

## Evidences

The Run checkpoint is terminal at phase 2 with `release-copy-ownership-unproven`, no delivery evidence and no pending Journal events. Its interruption is recorded. Installed N remains selected; no test gate or promotion ran.

## Blast radius

The Release Version vertical cut and the final CA-P-1117 acceptance gate.

## Disposition

CA-P-1774 diagnoses the exact ownership failure, repairs confirmed defects with regression evidence and independent review, and preserves the installed package and existing delivery. A corrected candidate requires a fresh Run, not replay of N6 or bypass of the ownership guard.

The exact exception chain was retained-package inventory mismatch: four Finder metadata files were counted despite the existing persistent inventory exclusion. Canonical and delivered source trees otherwise have identical bytes, modes, directory topology and persistent digest `7ff204b0618234550599ce41b617a03d9c6b785469e122fb5746adf948a8a605`.

The bounded repair aligns package verification and delivery no-op selection with that existing ephemeral-file rule, after rejecting unsafe and secret-shaped carriers. Thirty-four delivery/package/bootstrap tests pass; independent review accepts the boundary. Secret-shaped bytecode cannot use the metadata exclusion to bypass refusal. No installed package, metadata payload, predecessor tree or selector was changed. N6 remains terminal-interrupted; actual Release acceptance remains pending.
