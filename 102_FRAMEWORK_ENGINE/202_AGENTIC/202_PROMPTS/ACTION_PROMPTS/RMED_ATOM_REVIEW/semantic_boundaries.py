"""Keep legacy layout guards separate from current local content review.

Local reviewers assess readable text even with broken headings. Evidence
addresses and quotes are checked by report_quality, not invented sections.
"""
from __future__ import annotations

from collections import Counter
from typing import Any

from context_builder import body_sections


REQUIRED_SECTIONS = {
    'scope': ('## Scope', '## Claim'),
    'claim': ('## Claim',),
    'details': ('## Scope', '## Claim', '## Details'),
    'governed_entity': ('## Scope', '## Claim', '## Details'),
    'alignment': ('## Scope', '## Claim', '## Details'),
    'summary': ('# Summary', '## Scope', '## Claim'),
}


def unavailable_sections(source: str) -> dict[str, list[str]]:
    headings = Counter(address.split(':', 2)[2] for address in body_sections(source)
                       if address != 'body:preamble')
    return {check: [name for name in names if headings[name] != 1]
            for check, names in REQUIRED_SECTIONS.items()
            if any(headings[name] != 1 for name in names)}


def validate_boundaries(part: dict[str, Any], source: str) -> None:
    """No semantic success/failure without its unambiguous local input slots."""
    if part['evaluator'] != 'coherence':
        return
    if part.get('contract_version') == 6 and part.get('review_profile') == 'atom_local':
        if any(gap.get('kind') == 'layout_dependency' for gap in part['coverage_gaps']):
            raise ValueError('layout alone cannot block local content review; describe the actual ambiguity or missing evidence')
        return
    missing = unavailable_sections(source)
    for row in part['checks']:
        if row['id'] not in missing:
            continue
        if row['status'] != 'blocked':
            names = ', '.join(missing[row['id']])
            raise ValueError(f"{row['id']} needs unavailable or ambiguous sections: {names}")
        gaps = [gap for gap in part['coverage_gaps']
                if isinstance(gap, dict) and gap.get('check_id') == row['id']]
        if not any(gap.get('kind') == 'layout_dependency' for gap in gaps):
            raise ValueError(f"{row['id']} needs its layout dependency gap")
