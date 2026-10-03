"""Validate a no-write layout preview; this is not repair admission.

The caller constructs the temporary candidate.  This module only proves a
very narrow byte-preserving layout transform and deliberately makes no claim
about meaning, evaluation status, or authorization to mutate a source.
"""
from __future__ import annotations

from copy import deepcopy
import hashlib
import re
from typing import Any

from context_builder import metadata


def _reject(reason: str) -> dict[str, Any]:
    return {'result': 'rejected', 'source_mutation_permitted': False,
            'reason': reason}


def _text(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _frontmatter(raw: str) -> tuple[str, str] | None:
    if not isinstance(raw, str) or not raw.startswith('---'):
        return None
    match = re.match(r'\A---[^\n]*\n.*?^---[^\n]*(?:\n|\Z)', raw, re.MULTILINE | re.DOTALL)
    if match is None:
        return None
    return match.group(), raw[match.end():]


def _span(value: Any, body: str) -> tuple[int, int] | None:
    if (not isinstance(value, list) or len(value) != 2 or type(value[0]) is not int
            or type(value[1]) is not int or value[0] < 0 or value[0] > value[1]
            or value[1] > len(body)):
        return None
    return value[0], value[1]


def _mapped_sections(mapping: Any, body: str) -> list[dict[str, Any]] | None:
    if (not isinstance(mapping, dict) or set(mapping) != {'source_body_sha256', 'sections'}
            or mapping.get('source_body_sha256') != hashlib.sha256(body.encode()).hexdigest()):
        return None
    sections = mapping.get('sections')
    if (not isinstance(sections, list) or len(sections) != 4
            or any(not isinstance(section, dict) for section in sections)):
        return None
    return sections


def _section(record: dict[str, Any], heading: str, span: list[int] | None,
             state: str, body: str) -> bool:
    if record.get('heading') != heading or record.get('state') != state:
        return False
    if not _text(record.get('provenance')):
        return False
    if span is None:
        return record.get('source_span') is None
    return _span(record.get('source_span'), body) == tuple(span)


def _mapping(mapping: Any, body: str, title_end: int) -> str | None:
    """Validate the explicit two-source-span, four-section preview map."""
    sections = _mapped_sections(mapping, body)
    if sections is None:
        return None
    expected = (
        ('# Summary', [0, title_end], 'legacy_h1_to_summary_value'),
        ('## Scope', None, 'unassessed_author_proposal'),
        ('## Claim', [title_end, len(body)], 'verbatim_carried'),
        ('## Details', None, 'unassessed_absent'),
    )
    if not all(_section(record, heading, span, state, body)
               for record, (heading, span, state) in zip(sections, expected)):
        return None
    scope = sections[1].get('proposed_text')
    if (set(sections[1]) != {'heading', 'source_span', 'state', 'provenance', 'proposed_text'}
            or not _text(scope) or re.search(r'(?m)^#{1,6}\s', scope)):
        return None
    if any(set(record) != {'heading', 'source_span', 'state', 'provenance'}
           for record in (sections[0], sections[2], sections[3])):
        return None
    return scope


def _binding_reason(binding: Any, source_text: str) -> str | None:
    required = {'path', 'atom_id', 'version', 'sha256'}
    if not isinstance(binding, dict) or set(binding) != required:
        return 'source binding is incomplete'
    if not _text(binding.get('path')) or not _text(binding.get('atom_id')):
        return 'source binding is incomplete'
    if type(binding.get('version')) is not int or binding['version'] < 1:
        return 'source binding has an invalid version'
    if binding['sha256'] != hashlib.sha256(source_text.encode()).hexdigest():
        return 'source text does not match its binding hash'
    return None


def _source_layout(binding: dict[str, Any], source_text: str, candidate_text: str
                   ) -> tuple[str, str, str, int] | str:
    source_parts, candidate_parts = _frontmatter(source_text), _frontmatter(candidate_text)
    if source_parts is None or candidate_parts is None:
        return 'both texts need complete frontmatter'
    source_header, body = source_parts
    if source_header != candidate_parts[0]:
        return 'candidate frontmatter must be byte-for-byte unchanged'
    props = metadata(source_text)
    if (props.get('atom_id') != binding['atom_id'] or type(props.get('version')) is not int
            or props.get('version') != binding['version']):
        return 'carried identity or version disagrees with source frontmatter'
    first = re.match(r'\A# ([^\n\r]+)(\r?\n|\Z)', body)
    if first is None or first.group(1).strip() == 'Summary':
        return 'source needs a legacy first H1 for this narrow preview'
    if re.search(r'(?m)^#{1,6}\s', body[first.end():]):
        return 'source has deeper headings; this layout is unsupported'
    return source_header, body, first.group(1), first.end()


def admit_layout_preview(source_binding: dict[str, Any], source_text: str,
                         candidate_text: str, *, section_mapping: dict[str, Any]) -> dict[str, Any]:
    """Return immutable temporary-preview evidence or a diagnostic.

    A preview is intentionally restricted to a source body whose first line is
    a legacy H1. Scope is an explicit, unassessed caller proposal; the legacy
    prose is carried verbatim into Claim. Candidate generation and later full
    evaluation remain outside this validator.
    """
    if not isinstance(source_text, str) or not isinstance(candidate_text, str):
        return _reject('source binding and texts must be supplied')
    reason = _binding_reason(source_binding, source_text)
    if reason is not None:
        return _reject(reason)
    layout = _source_layout(source_binding, source_text, candidate_text)
    if isinstance(layout, str):
        return _reject(layout)
    source_header, body, title, title_end = layout
    scope = _mapping(section_mapping, body, title_end)
    if scope is None:
        return _reject('section mapping must explicitly bind the lossless four-section transform')
    expected_body = ('# Summary\n' + title + '\n\n## Scope\n' + scope
                     + '\n\n## Claim\n' + body[title_end:] + '\n## Details\n')
    if candidate_text != source_header + expected_body:
        return _reject('candidate adds, removes, reorders, or rewrites source body prose')
    candidate_binding = dict(source_binding, sha256=hashlib.sha256(candidate_text.encode()).hexdigest())
    return {
        'result': 'preview', 'source_mutation_permitted': False,
        'source': dict(source_binding), 'candidate': candidate_binding,
        'section_mapping': deepcopy(section_mapping),
        'classification': 'unclassified',
        'equivalence_claimed': False,
        'next': ('Run a full independent evaluation of this exact temporary candidate, then obtain an '
                 'independent change assessment; normal repair admission still controls any mutation.'),
    }
