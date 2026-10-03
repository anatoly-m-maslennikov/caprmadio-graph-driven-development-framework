"""Admit an independently assessed carrier-only DEPENDS_ON correction.

This explicit operation does not widen generic revision or isolated recoding.
It requires an unchanged complete Markdown body, GOVERNS and Version, and a
full passing final evaluation under unchanged authority. The only editable
property is subjects.depends_on, plus ordinary role-echo omission and timestamp.
"""
from __future__ import annotations

from copy import deepcopy
import re
from typing import Any

from context_builder import markdown, metadata
from evaluation_contract import summarize_evaluations
from layout_preview import _frontmatter
from layout_repair_gate import _assessed_original_to_final, _digest, _permission
from repair_gate import _candidate_bindings, _identity, _outputs, _resolutions
from review_evidence import ReviewContext, probability, text


def _without_dependencies(raw: str) -> str:
    """Remove just one simple block-Subjects DEPENDS_ON field for comparison.

    Inline Subjects maps, aliases and ambiguous indentation are deliberately
    unsupported; a final independent pass is not permission to rewrite them.
    The dependency value itself may be a flow list or a four-space block list.
    """
    parts = _frontmatter(raw)
    if parts is None:
        raise ValueError('complete frontmatter required')
    header, body = parts
    starts = list(re.finditer(r'(?m)^subjects:[ \t]*\r?\n', header))
    if len(starts) != 1:
        raise ValueError('Subjects must have one unambiguous block mapping')
    start = starts[0].end()
    next_field = re.search(r'(?m)^[^ \t\r\n]', header[start:])
    end = start + next_field.start() if next_field else len(header)
    block = header[start:end]
    pattern = r'(?m)^  depends_on:[^\r\n]*(?:\r?\n|\Z)(?:[ \t]{4,}[^\r\n]*(?:\r?\n|\Z))*'
    for field in re.finditer(pattern, block):
        value = field.group().splitlines()[0].split(':', 1)[1].strip()
        if value and not value.startswith('['):
            raise ValueError('DEPENDS_ON must use a block or flow list, not aliases or tags')
    stripped, count = re.subn(pattern, '', block)
    if count != int('depends_on' in metadata(raw)['subjects']):
        raise ValueError('DEPENDS_ON field has unsupported or duplicate encoding')
    # Reject alternate indentation/duplicate spellings that YAML equality could
    # otherwise hide. Everything outside the admitted property stays exact.
    if re.search(r'(?m)^\s*depends_on\s*:', stripped):
        raise ValueError('ambiguous DEPENDS_ON field encoding')
    return header[:start] + stripped + header[end:] + body


def _dependency_change(original: str, candidate: str) -> tuple[str, str]:
    old, new = metadata(original), metadata(candidate)
    if old.get('content_role') not in ('Requirement', 'Method', 'Delivery'):
        raise ValueError('subject recoding requires an R/M/D Carrier')
    old_subjects, new_subjects = old.get('subjects'), new.get('subjects')
    if not isinstance(old_subjects, dict) or not isinstance(new_subjects, dict):
        raise ValueError('Subjects mapping required')
    if not text(old_subjects.get('governs')) or new_subjects.get('governs') != old_subjects['governs']:
        raise ValueError('subject recoding must preserve GOVERNS')
    values = []
    for subjects in (old_subjects, new_subjects):
        dependencies = subjects.get('depends_on', [])
        if (not isinstance(dependencies, list) or any(not text(value) for value in dependencies)
                or len(dependencies) != len(set(dependencies))):
            raise ValueError('DEPENDS_ON must be an unambiguous list of distinct strings')
        values.append(dependencies)
    if values[0] == values[1]:
        raise ValueError('subject recoding needs an actual DEPENDS_ON correction')
    if markdown(original) != markdown(candidate):
        raise ValueError('subject recoding must preserve the complete Markdown body')
    return _without_dependencies(original), _without_dependencies(candidate)


def admit_subject_recoding(evaluation: dict[str, Any], proposal: dict[str, Any], *,
                           context: dict[str, Any], final_evaluation: dict[str, Any],
                           final_context: dict[str, Any], permission: dict[str, Any],
                           preflight: dict[str, Any]) -> dict[str, Any]:
    """Return a no-write candidate after exact full-delta evidence admission."""
    original_context, output_context = ReviewContext(context), ReviewContext(final_context)
    if original_context.report_contract != 5 or output_context.report_contract != 5:
        raise ValueError('subject repair admission requires report contract 5')
    summarize_evaluations([evaluation], context=original_context)
    summarize_evaluations([final_evaluation], context=output_context)
    if (proposal.get('source') != evaluation['source']
            or proposal.get('context_sha256') != original_context.sha256):
        raise ValueError('proposal does not bind original source and evaluation')
    if evaluation['coverage_gaps']:
        raise ValueError('original coverage gaps block subject recoding')
    if not any(row['id'] == 'subjects' and row['findings'] for row in evaluation['checks']):
        raise ValueError('subject recoding requires a confirmed Subjects finding')
    if (final_evaluation['result'] != 'passed' or final_evaluation['coverage_gaps']
            or any(row['status'] != 'passed' or row['findings'] for row in final_evaluation['checks'])):
        raise ValueError('exact final evaluation must pass every check without findings or gaps')
    threshold = max(.99, original_context.confidence_threshold, output_context.confidence_threshold)
    if (output_context.confidence_threshold < original_context.confidence_threshold
            or output_context.confidence_threshold < .99
            or not probability(proposal.get('confidence')) or proposal['confidence'] < threshold):
        raise ValueError('subject repair confidence or final review threshold is insufficient')
    allowed = _permission(proposal, permission, 'subject_recoding')
    if 'deferred_findings' in proposal:
        raise ValueError('subject repair cannot defer original findings')
    _resolutions(evaluation, proposal)
    outputs = _outputs(proposal, allowed)
    binding = _candidate_bindings(proposal, outputs, original_context)[0]
    output = outputs[0]
    if final_evaluation['source'] != binding or output_context.candidate_text(binding) != output['text']:
        raise ValueError('final evaluation does not bind the exact proposed output')
    original = original_context.candidate_text(proposal['source'])
    stripped_old, stripped_new = _dependency_change(original, output['text'])
    # Mechanically compare all other bytes using the existing strict helpers;
    # the independent assessment still binds the unmodified original and final.
    stripped_output = dict(output, text=stripped_new)
    removes_type = 'type' in metadata(original) and 'type' not in metadata(output['text'])
    _identity(stripped_output, proposal['source'], stripped_old,
              'recoding' if removes_type else 'formatting', 'carrier_only')
    _assessed_original_to_final(preflight, proposal, binding, original_context, output_context,
                                context, final_context, threshold, final_evaluation)
    return {'result': 'candidate', 'source_mutation_permitted': False,
            'source': deepcopy(proposal['source']), 'outputs': [binding],
            'context_sha256': original_context.sha256, 'final_context_sha256': output_context.sha256,
            'original_evaluation_sha256': _digest(evaluation), 'final_evaluation_sha256': _digest(final_evaluation),
            'next': 'Fresh source/authority, history and affected-reference checks before an authorized write; '
                    'independently evaluate the actual saved source and affected references before verified.'}
