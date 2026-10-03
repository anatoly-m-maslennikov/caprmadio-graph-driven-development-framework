---
subjects:
  governs: "project-settings"
  depends_on:
    - "Project Structure"
    - "Project Settings"
    - "Framework Instance Settings"
    - "Projection"
version: 14
updated_at: "2026-09-17 21:32:20 +0000"
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  evaluation_for:
    - CA-M-149
    - CA-R-1070
---
# Bind admitted Scope Unit Graph sources in canonical order

## Test case

provide a fixed valid Project Structure Artifact with multiple accepted Scope Unit declarations **and** a fixed set of admitted Settings, Atom, directory-observation **and** Journal inputs. discover the input Carriers **in** different filesystem orders **without** changing their identities, content **or** declared structural **and** navigational order.

## Acceptance criteria

- **every** run emits the same Project Scope Unit Graph **and** Sources bindings **in** canonical source-identity order.
- Project Structure remains the sole authority for accepted declarations **and** bindings under CA-R-1070; an Atom-owned contribution map cannot redefine them.
- Project Settings **and** Framework Instance Settings retain their own selected-value authority; observations **and** generated views do **not** select Settings.
- filesystem enumeration order does **not** rewrite declared structural order **or** navigational order. **all** source Carriers remain unchanged.
