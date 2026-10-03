"""Admit one assessed no-write composition of layout and DEPENDS_ON repair.

This staged gate is intentionally narrower than either standalone admission:
the virtual layout carrier is evidence only, while the one final output must
also make exactly one unambiguous ``subjects.depends_on`` correction.  It does
not make a generic revision, a physical preview, or a source mutation legal.
"""
from __future__ import annotations

from copy import deepcopy
from typing import Any

from context_builder import markdown, metadata
from evaluation_contract import summarize_evaluations
from layout_preview import _frontmatter, admit_layout_preview
from layout_repair_gate import _assessed_preflight, _digest, _permission
from review_evidence import ReviewContext, probability
from semantic_boundaries import unavailable_sections
from subject_repair_gate import _dependency_change
from repair_gate import _identity, _output_binding, _outputs, _resolutions, _summary


def _final_passes(evaluation: dict[str, Any]) -> bool:
    return (evaluation['result'] == 'passed' and not evaluation['coverage_gaps']
            and all(row['status'] == 'passed' and not row['findings']
                    for row in evaluation['checks']))


def _original_layout_gaps(evaluation: dict[str, Any], original: str) -> None:
    """Accept only actual absent-section layout gaps from the original review."""
    absent = unavailable_sections(original)
    gaps = evaluation['coverage_gaps']
    if (not gaps or any(gap.get('kind') != 'layout_dependency'
                        or gap.get('check_id') not in absent for gap in gaps)):
        raise ValueError('only evidenced original layout_dependency gaps are admitted')


def _confirmed_subjects_finding(evaluation: dict[str, Any]) -> None:
    if not any(row['id'] == 'subjects' and row['findings'] for row in evaluation['checks']):
        raise ValueError('layout_subject recoding requires a confirmed Subjects finding')


def admit_layout_subject_recoding(
        evaluation: dict[str, Any], proposal: dict[str, Any], *, context: dict[str, Any],
        final_evaluation: dict[str, Any], final_context: dict[str, Any],
        section_mapping: dict[str, Any], permission: dict[str, Any],
        preflight: dict[str, Any]) -> dict[str, Any]:
    """Return the one fully assessed composed candidate, never write a source.

    Proof is deliberately staged: first ``admit_layout_preview`` establishes
    that the original Claim/Summary prose reaches the virtual canonical layout;
    then ``_dependency_change`` plus the strict existing identity helpers prove
    that virtual-layout-to-final changes only DEPENDS_ON, optional ordinary
    R/M/D Type elision, matching filename recoding, and ``updated_at``.
    Independent identity/provenance evidence still binds the real original and
    final carriers, never that virtual intermediate.
    """
    original_context, output_context = ReviewContext(context), ReviewContext(final_context)
    if original_context.report_contract != 5 or output_context.report_contract != 5:
        raise ValueError('layout_subject repair admission requires report contract 5')
    summarize_evaluations([evaluation], context=original_context)
    summarize_evaluations([final_evaluation], context=output_context)
    if (proposal.get('source') != evaluation['source']
            or proposal.get('context_sha256') != original_context.sha256):
        raise ValueError('proposal does not bind original source and evaluation')

    original = original_context.candidate_text(proposal['source'])
    _original_layout_gaps(evaluation, original)
    _confirmed_subjects_finding(evaluation)
    if not _final_passes(final_evaluation):
        raise ValueError('exact final evaluation must pass every check without findings or gaps')

    threshold = max(.99, original_context.confidence_threshold, output_context.confidence_threshold)
    if (output_context.confidence_threshold < original_context.confidence_threshold
            or output_context.confidence_threshold < .99
            or not probability(proposal.get('confidence'))
            or proposal['confidence'] < threshold):
        raise ValueError('layout_subject confidence or final review threshold is insufficient')
    allowed = _permission(proposal, permission, 'layout_subject_recoding')
    if 'deferred_findings' in proposal:
        raise ValueError('layout_subject repair cannot defer original findings')
    _resolutions(evaluation, proposal)
    outputs = _outputs(proposal, allowed)
    if len(outputs) != 1:
        raise ValueError('layout_subject recoding requires exactly one final output')
    output = outputs[0]
    binding = _output_binding(output)
    if (final_evaluation['source'] != binding
            or output_context.candidate_text(binding) != output['text']):
        raise ValueError('final evaluation does not bind the exact proposed output')

    parts = _frontmatter(original)
    if parts is None or metadata(original).get('content_role') not in ('Requirement', 'Method', 'Delivery'):
        raise ValueError('layout_subject recoding requires an R/M/D Carrier with complete frontmatter')
    # The candidate Markdown, paired with untouched original frontmatter, is a
    # virtual proof object.  It is never emitted as an output or admitted for a
    # write, so the only candidate is the real final carrier above.
    layout_text = parts[0] + markdown(output['text'])
    layout = admit_layout_preview(proposal['source'], original, layout_text,
                                  section_mapping=section_mapping)
    if layout['result'] != 'preview':
        raise ValueError('lossless layout proof rejected: ' + layout['reason'])
    if (proposal.get('before_summary') != _summary(layout_text)
            or proposal.get('after_summary') != _summary(output['text'])):
        raise ValueError('declared Summary must preserve the exact legacy title value')

    # The dependency comparator strips just DEPENDS_ON on each side.  The
    # established identity gate then byte-checks the remaining frontmatter and
    # body, including ID, Version, GOVERNS, every other relation/property, and
    # optional ordinary role-echo Type/path recoding.
    stripped_old, stripped_new = _dependency_change(layout_text, output['text'])
    stripped_output = dict(output, text=stripped_new)
    removes_type = 'type' in metadata(layout_text) and 'type' not in metadata(output['text'])
    _identity(stripped_output, proposal['source'], stripped_old,
              'recoding' if removes_type else 'formatting', 'carrier_only')
    _assessed_preflight(preflight, proposal, binding, original_context, output_context,
                        context, final_context, section_mapping, original, threshold,
                        final_evaluation)
    return {'result': 'candidate', 'source_mutation_permitted': False,
            'source': deepcopy(proposal['source']), 'outputs': [binding],
            'context_sha256': original_context.sha256,
            'final_context_sha256': output_context.sha256,
            'original_evaluation_sha256': _digest(evaluation),
            'final_evaluation_sha256': _digest(final_evaluation),
            'resolved_layout_gaps': [dict(original_gap=deepcopy(gap), final_check_id=gap['check_id'])
                                     for gap in evaluation['coverage_gaps']],
            'next': 'Fresh source/authority, history and affected-reference checks before an authorized write; '
                    'independently evaluate the actual saved source and affected references before verified.'}
