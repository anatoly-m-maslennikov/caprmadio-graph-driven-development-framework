"""Admit one assessed lossless legacy-layout candidate, never a source write.

Both contexts are frozen packet dictionaries, not just ReviewContext objects:
their complete authority manifests, resources and applicable Principles must
remain consistent. Caller freshness/independence claims are checked for exact
binding, not established as facts. Semantic Scope equivalence remains an
independent CA-O-067 judgment; a passing final evaluation alone cannot supply it.
"""
from __future__ import annotations

from copy import deepcopy
import hashlib
import json
from typing import Any

from context_builder import authority_reference, markdown, metadata
from evaluation_contract import summarize_evaluations
from layout_preview import _frontmatter, admit_layout_preview
from repair_gate import (_identity, _local_repair_boundary, _output_binding,
                         _outputs, _path, _resolutions, _summary)
from review_evidence import ReviewContext, probability, text, validate_quotes
from semantic_boundaries import unavailable_sections


def _digest(value: Any) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':'),
                                    ensure_ascii=False, allow_nan=False).encode()).hexdigest()


def _resources(packet: dict[str, Any]) -> dict[str, dict[str, Any]]:
    local = packet.get('review_constraints', {}).get('report_contract') == 6
    resources = packet.get('resources', {} if local else None)
    if (not isinstance(resources, dict) or any(not text(role) or not isinstance(row, dict)
                                             for role, row in resources.items())):
        raise ValueError('explicit keyed authority resources required')
    paths = []
    for row in resources.values():
        if (not text(row.get('path')) or not isinstance(row.get('text'), str)
                or hashlib.sha256(row['text'].encode()).hexdigest() != row.get('sha256')):
            raise ValueError('authority resource binding contradicts its text')
        paths.append(row['path'])
    if len(paths) != len(set(paths)):
        raise ValueError('duplicate authority resources')
    return resources


def authority_digest(packet: dict[str, Any]) -> str:
    """Digest the exact caller re-read authority manifest and control resources."""
    bindings = packet.get('authority_bindings')
    if not isinstance(bindings, list) or not bindings or any(not isinstance(b, dict) for b in bindings):
        raise ValueError('explicit nonempty authority manifest required')
    return _digest({'authority_bindings': sorted(bindings, key=_digest), 'resources': _resources(packet)})


def _authority_consistency(context: ReviewContext, final_context: ReviewContext,
                           packet: dict[str, Any], final_packet: dict[str, Any],
                           before: dict[str, Any], output: dict[str, Any], aliases: Any) -> None:
    authority_digest(packet)
    authority_digest(final_packet)
    old, new = context.authority_bindings, final_context.authority_bindings
    if len(old) != len({_digest(b) for b in old}) or len(new) != len({_digest(b) for b in new}):
        raise ValueError('duplicate authority bindings')
    for ctx, bindings in ((context, old), (final_context, new)):
        for binding in bindings:
            ctx.source_text(binding)
    if not isinstance(aliases, list):
        raise ValueError('explicit authority alias list required')
    replacements = {}
    destinations = set()
    for alias in aliases:
        if not isinstance(alias, dict) or set(alias) != {'original', 'final'}:
            raise ValueError('invalid authority alias')
        a, b = alias['original'], alias['final']
        if (a not in old or b not in new or a == b
                or {k: v for k, v in a.items() if k != 'path'} != {k: v for k, v in b.items() if k != 'path'}
                or context.source_text(a) != final_context.source_text(b)
                or _digest(a) in replacements or _digest(b) in destinations):
            raise ValueError('authority alias must preserve an exact independently bound source')
        replacements[_digest(a)] = b
        destinations.add(_digest(b))
    normalized = [replacements.get(_digest(binding), binding) for binding in old]
    if {_digest(b) for b in normalized} != {_digest(b) for b in new}:
        raise ValueError('changed or unknown authority requires a fresh review')
    if _resources(packet) != _resources(final_packet):
        raise ValueError('authority resources changed between reviews')
    for ctx in (context, final_context):
        if ((not ctx.preflight and ctx.report_contract != 6) or any(not isinstance(row, dict) or row.get('state') != 'available'
                                     for row in ctx.preflight.values())):
            raise ValueError('unavailable authority or context')
    if set(context.preflight) != set(final_context.preflight):
        raise ValueError('authority context coverage changed')
    old_principles = [replacements.get(_digest(row['binding']), row['binding'])
                      for row in packet.get('principle_admissions', [])
                      if before['path'] in row['applicable_to']]
    new_principles = [row['binding'] for row in final_packet.get('principle_admissions', [])
                      if output['path'] in row['applicable_to']]
    if {_digest(b) for b in old_principles} != {_digest(b) for b in new_principles}:
        raise ValueError('applicable Principle authority changed')


def _permission(proposal: dict[str, Any], permission: dict[str, Any],
                disposition: str = 'layout_recoding') -> set[str]:
    if proposal.get('disposition') != disposition:
        raise ValueError(f'explicit {disposition} disposition required')
    if (not isinstance(permission, dict) or not isinstance(permission.get('paths'), list)
            or not isinstance(permission.get('dispositions'), list)
            or any(not isinstance(value, str) for value in permission['dispositions'])
            or disposition not in permission['dispositions'] or not text(permission.get('provenance'))):
        raise ValueError(f'{disposition} lacks exact caller permission')
    allowed = {_path(path) for path in permission['paths']}
    if _path(proposal['source']['path']) not in allowed:
        raise ValueError('source path lacks exact permission')
    return allowed


def _assessed_original_to_final(preflight: Any, proposal: dict[str, Any], binding: dict[str, Any],
                        context: ReviewContext, final_context: ReviewContext,
                        packet: dict[str, Any], final_packet: dict[str, Any],
                        threshold: float, final_evaluation: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(preflight, dict) or not text(preflight.get('provenance')):
        raise ValueError('caller preflight required')
    if 'identity_assessment' in proposal:
        raise ValueError('proposal cannot self-attest identity assessment')
    expected = dict(source=proposal['source'], context_sha256=context.sha256,
                    final_context_sha256=final_context.sha256, outputs=[binding])
    if any(preflight.get(key) != value for key, value in expected.items()):
        raise ValueError('preflight does not bind the complete original-to-final proposal')
    review = preflight.get('final_review')
    if (not isinstance(review, dict) or review.get('independent') is not True
            or review.get('source') != binding or review.get('context_sha256') != final_context.sha256
            or review.get('evaluation_sha256') != _digest(final_evaluation)
            or not text(review.get('provenance'))):
        raise ValueError('independent final review must bind the exact complete evaluation')
    attempt, budget = preflight.get('attempt'), preflight.get('retry_budget')
    if type(attempt) is not int or type(budget) is not int or not 0 <= attempt <= budget:
        raise ValueError('invalid repair attempt or retry budget')
    freshness = preflight.get('freshness')
    if (not isinstance(freshness, dict) or freshness.get('source') != proposal['source']
            or freshness.get('authority_sha256') != authority_digest(packet)
            or not text(freshness.get('provenance'))):
        raise ValueError('missing exact source and authority freshness evidence')
    _authority_consistency(context, final_context, packet, final_packet, proposal['source'],
                           binding, preflight.get('authority_aliases'))
    assessment = preflight.get('identity_assessment')
    if (not isinstance(assessment, dict) or any(assessment.get(k) != v for k, v in expected.items())
            or assessment.get('classification') != 'carrier_only'
            or assessment.get('independent') is not True or not text(assessment.get('provenance'))
            or not probability(assessment.get('confidence')) or assessment['confidence'] < threshold):
        raise ValueError('independent carrier_only assessment must bind the full delta at the threshold')
    return assessment


def _assessed_preflight(preflight: Any, proposal: dict[str, Any], binding: dict[str, Any],
                        context: ReviewContext, final_context: ReviewContext,
                        packet: dict[str, Any], final_packet: dict[str, Any],
                        mapping: dict[str, Any], original: str, threshold: float,
                        final_evaluation: dict[str, Any]) -> None:
    assessment = _assessed_original_to_final(preflight, proposal, binding, context, final_context,
                                             packet, final_packet, threshold, final_evaluation)
    scope = assessment.get('scope_equivalence')
    claim_start, claim_end = mapping['sections'][2]['source_span']
    if (not isinstance(scope, dict) or scope.get('result') != 'equivalent'
            or scope.get('final_scope') != mapping['sections'][1]['proposed_text']
            or not text(scope.get('source_excerpt'))
            or scope['source_excerpt'] not in markdown(original)[claim_start:claim_end]
            or not text(scope.get('reason'))):
        raise ValueError('independent exact Scope equivalence evidence required')
    support = scope.get('support')
    if not isinstance(support, list) or any(not isinstance(quote, dict) for quote in support):
        raise ValueError('Scope equivalence needs bound authority support')
    support_refs = {quote.get('authority') for quote in support if text(quote.get('authority'))}
    support_bindings = [b for b in final_context.authority_bindings if authority_reference(b) in support_refs]
    authorities = final_context.authorities(support_bindings, candidate=binding)
    validate_quotes(scope.get('support'), authorities)


def admit_layout_recoding(evaluation: dict[str, Any], proposal: dict[str, Any], *,
                          context: dict[str, Any], final_evaluation: dict[str, Any],
                          final_context: dict[str, Any], section_mapping: dict[str, Any],
                          permission: dict[str, Any], preflight: dict[str, Any]) -> dict[str, Any]:
    """Admit an exact legacy H1/layout recoding after complete final evaluation.

    The original report remains failed/blocked evidence. Only physical layout
    gaps can be discharged against passed checks on the exact final candidate.
    All other gates, findings, semantic judgments and writer obligations remain.
    """
    original_context, output_context = ReviewContext(context), ReviewContext(final_context)
    if (original_context.report_contract not in (5, 6)
            or output_context.report_contract != original_context.report_contract):
        raise ValueError('layout repair admission requires matching report contracts 5 or 6')
    summarize_evaluations([evaluation], context=original_context)
    summarize_evaluations([final_evaluation], context=output_context)
    if (proposal.get('source') != evaluation['source']
            or proposal.get('context_sha256') != original_context.sha256):
        raise ValueError('proposal does not bind original source and evaluation')
    original = original_context.candidate_text(proposal['source'])
    missing = unavailable_sections(original)
    if (not evaluation['coverage_gaps'] or any(gap.get('kind') != 'layout_dependency'
            or gap.get('check_id') not in missing for gap in evaluation['coverage_gaps'])):
        raise ValueError('only evidenced original layout_dependency gaps are admitted')
    if (final_evaluation['result'] != 'passed' or final_evaluation['coverage_gaps']
            or any(row['status'] != 'passed' or row['findings'] for row in final_evaluation['checks'])):
        raise ValueError('exact final evaluation must pass every check without findings or gaps')
    threshold = max(.99, original_context.confidence_threshold, output_context.confidence_threshold)
    if (output_context.confidence_threshold < original_context.confidence_threshold
            or output_context.confidence_threshold < .99
            or not probability(proposal.get('confidence')) or proposal['confidence'] < threshold):
        raise ValueError('layout repair confidence or final review threshold is insufficient')
    allowed = _permission(proposal, permission)
    if 'deferred_findings' in proposal:
        raise ValueError('layout repair cannot defer original findings')
    _resolutions(evaluation, proposal)
    output = _outputs(proposal, allowed)[0]
    if original_context.report_contract == 6:
        _local_repair_boundary(proposal, output, original)
    binding = _output_binding(output)
    if final_evaluation['source'] != binding or output_context.candidate_text(binding) != output['text']:
        raise ValueError('final evaluation is not bound to the exact proposed output')
    parts = _frontmatter(original)
    if parts is None or metadata(original).get('content_role') not in ('Requirement', 'Method', 'Delivery'):
        raise ValueError('layout recoding requires an R/M/D Carrier with complete frontmatter')
    # This virtual intermediate is never admitted or written. Recompute the
    # original-to-layout proof; do not trust a caller-supplied preview status.
    layout_text = parts[0] + markdown(output['text'])
    layout = admit_layout_preview(proposal['source'], original, layout_text, section_mapping=section_mapping)
    if layout['result'] != 'preview':
        raise ValueError('lossless layout proof rejected: ' + layout['reason'])
    if proposal.get('before_summary') != _summary(layout_text) or proposal.get('after_summary') != _summary(output['text']):
        raise ValueError('declared Summary must preserve the exact legacy title value')
    removes_type = 'type' in metadata(original) and 'type' not in metadata(output['text'])
    _identity(output, proposal['source'], layout_text,
              'recoding' if removes_type else 'formatting', 'carrier_only')
    _assessed_preflight(preflight, proposal, binding, original_context, output_context,
                        context, final_context, section_mapping, original, threshold, final_evaluation)
    return {'result': 'candidate', 'source_mutation_permitted': False,
            'source': deepcopy(proposal['source']), 'outputs': [binding],
            'context_sha256': original_context.sha256, 'final_context_sha256': output_context.sha256,
            'original_evaluation_sha256': _digest(evaluation), 'final_evaluation_sha256': _digest(final_evaluation),
            'resolved_layout_gaps': [dict(original_gap=deepcopy(gap), final_check_id=gap['check_id'])
                                     for gap in evaluation['coverage_gaps']],
            'next': 'Fresh source/authority, history and affected-reference checks before an authorized write; '
                    'independently evaluate the actual saved source and affected references before verified.'}
