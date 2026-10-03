"""Prove one exact exclusion-to-Scope relocation without admitting a write.

This staged component is intentionally narrower than the production lossless
layout preview.  It recognizes one legacy assertion, moves only its selector
to Scope, preserves the rest byte-for-byte, and retains exact spans for both
source and proposed bodies.  It does not establish semantic equivalence.

The admitted selector grammar is deliberately ASCII-only (``[A-Za-z ]`` and
``[A-Za-z -]``). Non-ASCII names must fail closed until separately assessed.
"""
from __future__ import annotations

from copy import deepcopy
import hashlib
import re
from typing import Any

from layout_preview import _binding_reason, _frontmatter, _reject, _source_layout, _span, _text


def _mapping(mapping: Any, source_body: str, proposed_body: str, *, title_end: int,
             selector_start: int, selector_end: int, selector: str,
             reduced_claim: str, expected_body: str) -> bool:
    if (not isinstance(mapping, dict)
            or set(mapping) != {'source_body_sha256', 'proposed_body_sha256', 'sections'}
            or mapping.get('source_body_sha256') != hashlib.sha256(source_body.encode()).hexdigest()
            or mapping.get('proposed_body_sha256') != hashlib.sha256(proposed_body.encode()).hexdigest()):
        return False
    sections = mapping.get('sections')
    if not isinstance(sections, list) or len(sections) != 4 or any(not isinstance(x, dict) for x in sections):
        return False
    scope = selector + '.'
    summary_end = expected_body.index('\n\n## Scope') + 1
    scope_start = expected_body.index(scope, expected_body.index('## Scope'))
    claim_start = expected_body.index(reduced_claim, expected_body.index('## Claim'))
    expected = (
        ('# Summary', [0, title_end], [0, summary_end], 'legacy_h1_to_summary_value', None, None),
        ('## Scope', [selector_start, selector_end], [scope_start, scope_start + len(scope)],
         'extracted_applicability', selector, scope),
        ('## Claim', [title_end, len(source_body)], [claim_start, claim_start + len(reduced_claim)],
         'selector_reduced_to_bearer', None, None),
        ('## Details', None, None, 'unassessed_absent', None, None),
    )
    for index, (heading, source_span, proposed_span, state, source_text, proposed_text) in enumerate(expected):
        record = sections[index]
        keys = {'heading', 'source_span', 'proposed_span', 'state', 'provenance'}
        if index == 1:
            keys |= {'source_text', 'proposed_text'}
        if set(record) != keys or record.get('heading') != heading or record.get('state') != state:
            return False
        if not _text(record.get('provenance')):
            return False
        if source_span is None:
            if record.get('source_span') is not None:
                return False
        elif _span(record.get('source_span'), source_body) != tuple(source_span):
            return False
        if proposed_span is None:
            if record.get('proposed_span') is not None:
                return False
        elif _span(record.get('proposed_span'), proposed_body) != tuple(proposed_span):
            return False
        if index == 1 and (record.get('source_text') != source_text
                           or record.get('proposed_text') != proposed_text):
            return False
    return proposed_body == expected_body


def admit_scope_extraction_preview(source_binding: dict[str, Any], source_text: str,
                                  candidate_text: str, *, section_mapping: dict[str, Any]) -> dict[str, Any]:
    """Return a no-write proof for exactly one simple selector relocation."""
    if not isinstance(source_text, str) or not isinstance(candidate_text, str):
        return _reject('source binding and texts must be supplied')
    reason = _binding_reason(source_binding, source_text)
    if reason is not None:
        return _reject(reason)
    layout = _source_layout(source_binding, source_text, candidate_text)
    if isinstance(layout, str):
        return _reject(layout)
    header, body, title, title_end = layout
    match = re.fullmatch(
        r'(?P<leading>\n*)\*\*every\*\* '
        r'(?P<selector>(?P<bearer>[A-Z][A-Za-z ]*?) other than (?P<exclusion>[A-Za-z][A-Za-z -]*))'
        r' \*\*must\*\* (?P<predicate>[^\n.]+\.)(?P<trailing>\n*)',
        body[title_end:])
    if match is None:
        return _reject('unsupported source: expected one universally quantified exclusion assertion')
    selector = match['selector']
    if (selector.count(' other than ') != 1
            or any(token in selector for token in (' and ', ' or ', ' unless ', ' if '))):
        return _reject('compound or conditional selectors require separate assessment')
    selector_start = title_end + match.start('selector')
    selector_end = title_end + match.end('selector')
    reduced_claim = body[title_end:selector_start] + match['bearer'] + body[selector_end:]
    expected_body = ('# Summary\n' + title + '\n\n## Scope\n' + selector + '.\n\n## Claim\n'
                     + reduced_claim + '\n## Details\n')
    proposed = _frontmatter(candidate_text)
    if proposed is None or candidate_text != header + expected_body:
        return _reject('candidate is not the exact selector-to-Scope relocation')
    if not _mapping(section_mapping, body, proposed[1], title_end=title_end,
                    selector_start=selector_start, selector_end=selector_end,
                    selector=selector, reduced_claim=reduced_claim, expected_body=expected_body):
        return _reject('section mapping must bind exact original and proposed spans')
    return {
        'result': 'preview', 'source_mutation_permitted': False,
        'source': dict(source_binding),
        'candidate': dict(source_binding, sha256=hashlib.sha256(candidate_text.encode()).hexdigest()),
        'section_mapping': deepcopy(section_mapping), 'classification': 'unclassified',
        'equivalence_claimed': False,
        'next': ('Obtain independently bound original/final Scope and identity assessments plus complete '
                 'evaluations; this preview never authorizes a source write.'),
    }
