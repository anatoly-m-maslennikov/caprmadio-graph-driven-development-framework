---
cce_version: cce_1
cce_form: concern_question
subjects:
  governs: "Project Structure Maintenance"
  depends_on:
    - "Project Structure"
    - "Action"
    - "Artifact/Carrier"
    - "Operator"
priority: medium
version: 2
updated_at: "2026-09-20 23:49:39 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {}
---
# Which Action retires a Project Structure candidate?

which existing **or** justified new Action owns retirement of a staged Project Structure candidate **after** successful activation **or** rejection, **and** what happens **after** partial cutover failure?

## Evidence

CA-D-444 combines filename, placement **and** discovery eligibility with cutover prerequisites, retained old bytes, **and** candidate retirement. CA-O-012 prepares a proposal; CA-O-013 authorizes its exact effects; CA-O-014 applies an authorized recoverable cutover; CA-O-015 routes failed **or** rejected checks **to** a stop. these Actions do **not** explicitly place candidate retirement on **both** acceptance **and** rejection paths. treating retirement as deletion would add an unauthorized destructive meaning.

## Principle check

CA-M-002 favors those existing Actions over a duplicate migration Process. CA-M-005 requires a justified new Action boundary; CA-M-006 requires Carrier eligibility **and** operational effects **to** agree; CA-R-1490 requires old source bytes **and** failure evidence **to** remain recoverable. CA-R-1342 gives Carrier representation **to** D; CA-R-1530 gives reusable behavior **to** O. these rules establish ownership categories but **not** the missing rejection **and** partial-failure transition.

## Disposition

defer replacement of CA-D-444 **until** candidate retirement has an explicit operational owner **and** outcomes that preserve its authorization **and** recovery constraints. retain **all** original requirements. the split **must** preserve the candidate filename **and** separate path, explicit candidate validation, a single discoverable active source, freshness **and** consumer-readiness checks, recoverable old bytes, **and** rejection/failure behavior. this Concern does **not** authorize deletion, a Tool implementation change, a new registry, **or** an extra Process whose Actions are undefined.
