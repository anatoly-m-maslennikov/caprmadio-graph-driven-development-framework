---
atom_id: CA-M-223
cce_version: cce_1
cce_form: method
subjects:
  governs:
    continuant:
      - tool-effect-result
  depends_on:
    continuant:
      - TOOLS
version: 4
updated_at: 2026-08-27 14:52:39 +0400
relations:
  method_for:
    - CA-R-1186
  derived_from:
    - CA-A-057
---
# Bind Tool effect results to the canonical operation

Bind every Tool effect request and result to the canonical operation that
authorized it.

## Applicable when

Apply after the shared PROGRAMMATIC file-and-subprocess Method (`CA-M-161`)
admits an effect for one Tool operation.

## Procedure

1. Resolve the canonical operation identity and its sealed target or explicit
   argument contract before applying an effect.
2. Bind every admitted effect request and returned receipt to that operation.
3. Preserve the operation identity through failure, recovery, and retry.
4. Return the Tool's declared structured outcome without selecting a separate
   file, subprocess, platform, or MCP policy.

## Outcome

Every Tool effect and receipt remains attributable to one canonical operation
and recoverable without reconstructing authority from incidental runtime state.

## Failure or stop

Stop when the operation identity, sealed target, argument contract, or effect
receipt is missing, ambiguous, stale, or inconsistent with the Tool outcome.

## Sources

- [Python documentation: subprocess security considerations](https://docs.python.org/3.14/library/subprocess.html#security-considerations)
- [Python documentation: tempfile](https://docs.python.org/3.14/library/tempfile.html)
- [Python documentation: os.replace](https://docs.python.org/3.14/library/os.html#os.replace)
