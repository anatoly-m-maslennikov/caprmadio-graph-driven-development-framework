---
cce_version: cce_1
cce_form: definition
subjects:
  governs: "Read Atom Carriers"
  depends_on:
    - "Action"
    - "Tool/ATOM_READ"
    - "Atom"
    - "Artifact/Carrier"
    - "Scope Unit"
version: 1
updated_at: "2026-09-17 04:11:29 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {}
---
# Read selected CAPRMEDIO Atom carriers

Read Atom Carriers **means** the reusable read-only Action that returns the requested faithful Carrier view for **every** exact Atom selector under CA-R-864. its boundary is the complete attributable response; a missing **or** ambiguous selection is an explicit result, **not** permission **to** substitute another Carrier.

## Applicable conditions

a caller requests current content, metadata, **or** the combined view for **>=1** explicitly selected Atom Carriers.

## Action

1. resolve the configured control root. normalize **every** selector as **=1** exact repository-relative path, full filename, filename stem, **or** stable Atom ID, together with its requested output view.
2. resolve **every** selector independently. permit **<=1** current Atom Carrier per selector; retain missing **and** ambiguous outcomes as explicit attributable results.
3. read **every** resolved Carrier once **without** rewriting it. preserve its raw frontmatter **and** body as read.
4. derive identity, Content Role, Scope Unit, placement, **and** lifecycle facts from the current filename **and** location rather than inventing them from the request.
5. return content **only**, metadata **only**, **or** the combined view exactly as requested. preserve selector-to-result attribution for singular **and** bulk requests.
6. perform no mutation, normalization, repair, **or** selector widening.

## Outcome and stops

**every** selector has **=1** attributable result containing the requested view **or** an explicit resolution error. do **not** guess **when** a selector is missing, ambiguous, unreadable, **or** outside the control root; return the exact condition **without** exposing another Carrier.
