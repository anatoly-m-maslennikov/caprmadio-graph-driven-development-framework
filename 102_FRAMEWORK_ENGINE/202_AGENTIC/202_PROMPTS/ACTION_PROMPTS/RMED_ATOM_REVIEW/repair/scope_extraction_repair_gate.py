"""Admit one staged Scope-extraction plus DEPENDS_ON candidate, never a write."""
from __future__ import annotations

from collections import Counter
from copy import deepcopy
import re
from typing import Any

from context_builder import body_sections, markdown, metadata
from evaluation_contract import summarize_evaluations
from layout_preview import _frontmatter
from layout_repair_gate import (_assessed_preflight, _digest, _permission, authority_digest)
from layout_subject_repair_gate import _confirmed_subjects_finding, _final_passes, _original_layout_gaps
from repair_gate import _identity, _output_binding, _outputs, _resolutions, _summary
from review_evidence import ReviewContext, probability, text
from scope_extraction_preview import admit_scope_extraction_preview
from subject_repair_gate import _dependency_change


DISPOSITION = 'scope_extraction_subject_recoding'
CANONICAL_HEADING_IDS = {
    '# Summary': {'CA-D-479:Summary', 'CA-D-479:# Summary'},
    '## Scope': {'CA-D-479:Scope', 'CA-D-479:## Scope'},
    '## Claim': {'CA-D-479:Claim', 'CA-D-479:## Claim'},
    '## Details': {'CA-D-479:Details', 'CA-D-479:## Details'},
}


def _final_freshness(preflight: dict[str, Any], binding: dict[str, Any], final_packet: dict[str, Any]) -> None:
    evidence = preflight.get('final_freshness')
    if (not isinstance(evidence, dict)
            or set(evidence) != {'source', 'authority_sha256', 'provenance'}
            or evidence.get('source') != binding
            or evidence.get('authority_sha256') != authority_digest(final_packet)
            or not text(evidence.get('provenance'))):
        raise ValueError('missing exact final source and authority freshness evidence')


def _exact_scope_evidence(preflight: dict[str, Any], mapping: dict[str, Any], original: str,
                          virtual: str) -> None:
    """Bind independent Scope evidence to the literal moved source and result spans."""
    assessment = preflight['identity_assessment']
    scope = assessment.get('scope_equivalence')
    source_body, proposed_body = markdown(original), markdown(virtual)
    source_span = mapping['sections'][1]['source_span']
    proposed_span = mapping['sections'][1]['proposed_span']
    if (not isinstance(scope, dict)
            or scope.get('independent') is not True
            or scope.get('source_excerpt') != source_body[source_span[0]:source_span[1]]
            or scope.get('final_scope') != proposed_body[proposed_span[0]:proposed_span[1]]
            or scope['source_excerpt'] != mapping['sections'][1]['source_text']
            or scope['final_scope'] != mapping['sections'][1]['proposed_text']):
        raise ValueError('Scope assessment must bind the exact moved source and final Scope spans')


def _declared_subjects(raw: str) -> set[str]:
    subjects = metadata(raw).get('subjects')
    if not isinstance(subjects, dict):
        return set()
    result = {subjects['governs']} if text(subjects.get('governs')) else set()
    dependencies = subjects.get('depends_on', [])
    if isinstance(dependencies, list):
        result.update(value for value in dependencies if text(value))
    return result


def _ordinary_role_echo_line(raw: str, role: str) -> str | None:
    """Return the one literal plain/quoted ordinary role-echo line, if present."""
    parts = _frontmatter(raw)
    if parts is None:
        return None
    pattern = re.compile(rf'type:[ \t]*(?:{re.escape(role)}|"{re.escape(role)}"|\'{re.escape(role)}\')[ \t]*')
    lines = [line.rstrip('\r') for line in parts[0].splitlines() if pattern.fullmatch(line.rstrip('\r'))]
    return lines[0] if len(lines) == 1 else None


def _admitted_original_findings(evaluation: dict[str, Any], original: str, final: str) -> None:
    """Allow only defects the exact staged delta demonstrably repairs.

    A complete final pass never withdraws unrelated original findings.  This is
    a mechanical scope check; it does not establish the semantic review.
    """
    before_subjects, after_subjects = _declared_subjects(original), _declared_subjects(final)
    original_headings = Counter(address.split(':', 2)[2] for address in body_sections(original)
                                if address != 'body:preamble')
    final_headings = Counter(address.split(':', 2)[2] for address in body_sections(final)
                             if address != 'body:preamble')
    old_props, new_props = metadata(original), metadata(final)
    role = old_props.get('content_role')
    ordinary_role_echo_removed = (role in ('Requirement', 'Method', 'Delivery')
                                  and old_props.get('type') == role
                                  and new_props.get('content_role') == role
                                  and 'type' not in new_props)
    registered = set(CANONICAL_HEADING_IDS)
    role_echo_line = _ordinary_role_echo_line(original, role) if isinstance(role, str) else None
    for row in evaluation['checks']:
        for finding in row['findings']:
            if row['id'] == 'subjects':
                entity = finding.get('entity')
                if (finding.get('kind') == 'omission' and text(entity)
                        and entity not in before_subjects and entity in after_subjects):
                    continue
                if (finding.get('kind') == 'violation' and finding.get('subject_issue') == 'extra'
                        and text(entity) and entity in before_subjects and entity not in after_subjects):
                    continue
                raise ValueError('unadmitted Subjects finding')
            if row['id'] == 'properties':
                heading = finding.get('obligation_id')
                if finding.get('kind') == 'omission':
                    matching = [name for name, ids in CANONICAL_HEADING_IDS.items() if heading in ids]
                    if (len(matching) == 1 and original_headings[matching[0]] == 0
                            and final_headings[matching[0]] == 1):
                        continue
                if (finding.get('kind') == 'violation' and ordinary_role_echo_removed
                        and finding.get('location') == 'frontmatter'
                        and role_echo_line is not None and finding.get('excerpt') == role_echo_line):
                    continue
                raise ValueError('unadmitted Properties finding')
            if row['findings']:
                raise ValueError('unadmitted original finding: ' + row['id'])


def admit_scope_extraction_subject_recoding(
        evaluation: dict[str, Any], proposal: dict[str, Any], *, context: dict[str, Any],
        final_evaluation: dict[str, Any], final_context: dict[str, Any],
        section_mapping: dict[str, Any], permission: dict[str, Any],
        preflight: dict[str, Any]) -> dict[str, Any]:
    """Return one fully assessed staged candidate, never write a source.

    The virtual original-to-layout candidate is evidence only.  The real final
    output may additionally make the one constrained ``subjects.depends_on``
    correction accepted by ``subject_repair_gate._dependency_change``.
    """
    original_context, output_context = ReviewContext(context), ReviewContext(final_context)
    if original_context.report_contract != 5 or output_context.report_contract != 5:
        raise ValueError('Scope extraction admission requires report contract 5')
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
            or not probability(proposal.get('confidence')) or proposal['confidence'] < threshold):
        raise ValueError('Scope extraction confidence or final review threshold is insufficient')
    allowed = _permission(proposal, permission, DISPOSITION)
    if 'deferred_findings' in proposal:
        raise ValueError('Scope extraction cannot defer original findings')
    _resolutions(evaluation, proposal)
    outputs = _outputs(proposal, allowed)
    if len(outputs) != 1:
        raise ValueError('Scope extraction requires exactly one final output')
    output = outputs[0]
    binding = _output_binding(output)
    if (final_evaluation['source'] != binding
            or output_context.candidate_text(binding) != output['text']):
        raise ValueError('final evaluation does not bind the exact proposed output')
    parts = _frontmatter(original)
    if parts is None or metadata(original).get('content_role') not in ('Requirement', 'Method', 'Delivery'):
        raise ValueError('Scope extraction requires an R/M/D Carrier with complete frontmatter')
    virtual = parts[0] + markdown(output['text'])
    preview = admit_scope_extraction_preview(proposal['source'], original, virtual,
                                             section_mapping=section_mapping)
    if preview['result'] != 'preview':
        raise ValueError('exact Scope extraction proof rejected: ' + preview['reason'])
    if (proposal.get('before_summary') != _summary(virtual)
            or proposal.get('after_summary') != _summary(output['text'])):
        raise ValueError('declared Summary must preserve the exact legacy title value')
    stripped_virtual, stripped_final = _dependency_change(virtual, output['text'])
    stripped_output = dict(output, text=stripped_final)
    removes_type = 'type' in metadata(virtual) and 'type' not in metadata(output['text'])
    _identity(stripped_output, proposal['source'], stripped_virtual,
              'recoding' if removes_type else 'formatting', 'carrier_only')
    _admitted_original_findings(evaluation, original, output['text'])
    _assessed_preflight(preflight, proposal, binding, original_context, output_context,
                        context, final_context, section_mapping, original, threshold, final_evaluation)
    _exact_scope_evidence(preflight, section_mapping, original, virtual)
    _final_freshness(preflight, binding, final_context)
    return {'result': 'candidate', 'source_mutation_permitted': False,
            'source': deepcopy(proposal['source']), 'outputs': [binding],
            'context_sha256': original_context.sha256,
            'final_context_sha256': output_context.sha256,
            'original_evaluation_sha256': _digest(evaluation),
            'final_evaluation_sha256': _digest(final_evaluation),
            'resolved_layout_gaps': [dict(original_gap=deepcopy(gap), final_check_id=gap['check_id'])
                                     for gap in evaluation['coverage_gaps']],
            'next': ('Fresh saved-source, authority, history and affected-reference checks are still required '
                     'before an authorized write and verification.')}
