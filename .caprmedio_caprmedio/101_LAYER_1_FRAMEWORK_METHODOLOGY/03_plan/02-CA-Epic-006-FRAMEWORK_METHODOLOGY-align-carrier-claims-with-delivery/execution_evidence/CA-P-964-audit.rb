#!/usr/bin/env ruby
# Read-only source audit. Only CA-P-964 evidence is written, through apply_patch.
require 'json'
require 'yaml'
require 'date'
require 'digest'
require 'open3'
require 'set'

ROOT = Dir.pwd
HERE = File.dirname(__FILE__)
BASE = '.caprmedio_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources'
OWNERS = %w[001_CORE_META_MODEL 003_LOCAL_CONFIGURATION].freeze
ROLES = %w[04_requirement 05_method 06_evaluation 07_delivery].freeze
INACTIVE = %w[archive draft drafts done solved onhold cancelled canceled goals_archive jobs_archive].freeze
EXCLUDES = %w[!**/.git/** !**/.env !**/.env.* !**/*.env !**/.DS_Store !**/execution_evidence/**].freeze
def sha(s) = Digest::SHA256.hexdigest(s)
def read_json(name) = JSON.parse(File.read(File.join(HERE, name)))
def save(name, data)
  path = File.join(HERE, 'CA-P-964-' + name)
  content = data.is_a?(String) ? data : JSON.pretty_generate(data) + "\n"
  old = File.file?(path) ? File.read(path) : nil
  return if old == content
  patch = "*** Begin Patch\n"
  patch += old ? "*** Update File: #{path}\n@@\n" + old.lines.map { |l| '-' + l.chomp + "\n" }.join : "*** Add File: #{path}\n"
  patch += content.lines.map { |l| '+' + l.chomp + "\n" }.join + "*** End Patch\n"
  out, err, status = Open3.capture3('apply_patch', stdin_data: patch)
  raise "apply_patch failed: #{out} #{err}" unless status.success? && File.binread(path) == content.b
end
def parse(path, text)
  m = text.match(/\A---\r?\n(.*?)\r?\n---(?:\r?\n|\z)(.*)/m)
  raise "Missing frontmatter: #{path}" unless m
  meta = YAML.safe_load(m[1], permitted_classes: [Date, Time], aliases: false)
  stem = File.basename(path, '.md')
  id = meta['atom_id'] || stem[/\A[A-Z][A-Z0-9_]*(?:-[A-Z][A-Z0-9_]*)*-\d+(?=-|\z)/] || stem.split('--', 2).first
  { 'identity' => id, 'path' => path, 'version' => meta['version'], 'sha256' => sha(text), 'meta' => meta, 'body' => m[2], 'text' => text }
end
def receipt(record) = record.slice('identity', 'path', 'version', 'sha256')
def relation_values(record, kind) = (record['meta']['relations'] || {}).fetch(kind, [])
def resolve(value, records)
  return value if records.key?(value)
  exact = records.values.select { |r| File.basename(r['path'], '.md') == value }
  return exact.first['identity'] if exact.length == 1
  ids = records.keys.select { |id| value.start_with?(id + '-') || value.start_with?(id + '@') }.sort_by { |id| -id.length }
  ids.first
end
def edges_for(records, universe)
  edges, unresolved = [], []
  records.each_value do |r|
    (r['meta']['relations'] || {}).each do |kind, values|
      Array(values).each do |raw|
        raise "Non-string relation #{r['identity']} #{kind}" unless raw.is_a?(String)
        target = resolve(raw, universe)
        row = { 'source' => r['identity'], 'relation' => kind, 'target' => target || raw, 'raw' => raw, 'path' => r['path'] }
        target ? edges << row : unresolved << row
      end
    end
  end
  [edges, unresolved]
end
def cyclic_components(edges)
  graph = Hash.new { |h,k| h[k] = [] }
  edges.each { |e| graph[e['source']] << e['target']; graph[e['target']] ||= [] }
  index, stack, indices, low, on_stack, components = 0, [], {}, {}, Set.new, []
  visit = lambda do |v|
    indices[v] = low[v] = index; index += 1; stack << v; on_stack << v
    graph[v].uniq.sort.each do |w|
      if !indices.key?(w)
        visit.call(w); low[v] = [low[v],low[w]].min
      elsif on_stack.include?(w)
        low[v] = [low[v],indices[w]].min
      end
    end
    if low[v] == indices[v]
      component = []
      loop do
        w = stack.pop; on_stack.delete(w); component << w; break if w == v
      end
      components << component.sort if component.length > 1 || graph[v].include?(v)
    end
  end
  graph.keys.sort.each { |v| visit.call(v) unless indices.key?(v) }
  components.sort
end

snapshot = read_json('CA-P-960-snapshot.json')
incoming = read_json('CA-P-961-incoming-references.json')
maps = %w[962 963].to_h { |n| [n, read_json("CA-P-#{n}-mapping.json")] }
logs = %w[962 963].to_h { |n| [n, read_json("CA-P-#{n}-changes.json")] }
%w[962-verification 962-local-handoff 963-verification 963-handoff].each { |n| read_json("CA-P-#{n}.json") }
state = snapshot['records'].to_h { |r| [r['canonical_identity'], parse(r['source_path'], r['complete_source_text'])] }
initial_state = state.dup
all_ops = logs.flat_map { |task,l| l['operations'].map { |o| o.merge('task' => task) } }
revision_paths = all_ops.flat_map { |o| [o['archive'], o['after']].compact }.group_by { |r| r['sha256'] }
checks, order, disposition_order, archive_receipts = {}, [], [], []
last_operation = {}
all_ops.each do |op|
  id, before, after = op.values_at('identity', 'before', 'after')
  label = "#{op['task']}:#{op['sequence']}"
  if before
    raise "Before-state mismatch #{label} #{id}" unless state[id] && state[id]['sha256'] == before['sha256']
    archive = op.fetch('archive')
    bytes = File.binread(archive['path'])
    raise "Archive mismatch #{label}" unless bytes.b == state[id]['text'].b && sha(bytes) == archive['sha256']
    archive_receipts << archive.merge('operation' => label, 'byte_exact_against_replayed_before' => true)
  else
    raise "Duplicate admission #{id}" if state.key?(id)
  end
  d = maps[op['task']]['dispositions'].find { |x| (x['before'] || x['execution_before']).values_at('canonical_identity','identity').compact.first == id }
  if d && %w[split replace dedupe].include?(d['action']) && %w[revise_owner retire_predecessor].include?(op['kind'])
    successors = d['after_owners'].map { |x| x['identity'] }.reject { |x| x == id }
    raise "Missing successor at #{label}" unless successors.all? { |x| state.key?(x) }
    required = incoming['references'].select { |r| r['target_before'] == id && (r['required_before_extraction'] || r['classification'] == 'required_pre_retirement_repair') }
    required.each do |ref|
      repair = logs['962']['reference_repairs'].find { |r| r['reference_id'] == ref['reference_id'] }
      raise "Missing repair #{ref['reference_id']}" unless repair
      consumer = state.fetch(repair['consumer'])
      values = relation_values(consumer, repair['relation'])
      raise "Required repair absent before #{label}" unless repair['targets_after'].all? { |target| values.include?(target) && state.key?(target) }
      raise "Retired target still consumed #{label}" if op['kind'] == 'retire_predecessor' && values.any? { |v| resolve(v,state) == id }
      repair_op = all_ops.find { |o| o['task'] == '962' && o['sequence'] == repair['operation_sequence'] }
      raise "Repair order violation #{label}" unless all_ops.index(repair_op) < all_ops.index(op)
      target_ops = repair['targets_after'].reject { |t| t == id }.map do |target|
        target_op = all_ops.select { |o| o['identity'] == target && o['after'] && all_ops.index(o) < all_ops.index(repair_op) }.last
        raise "Successor was not established before repair #{label}" unless target_op
        { 'identity' => target, 'operation' => "#{target_op['task']}:#{target_op['sequence']}", 'sha256_at_admission' => target_op['after']['sha256'] }
      end
      order << repair.merge('successor_operations' => target_ops, 'consumer_repair_operation' => "962:#{repair['operation_sequence']}", 'extraction_or_retirement_operation' => label, 'consumer_bytes_at_extraction' => receipt(consumer), 'verified_from_replayed_bytes' => true)
    end
    disposition_order << { 'predecessor' => id, 'action' => d['action'], 'operation' => label, 'successors' => successors.map { |x| receipt(state[x]).merge('established_by' => last_operation[x] || 'CA-P-960 baseline') }, 'required_reference_ids' => required.map { |r| r['reference_id'] }, 'verified' => true }
  end
  state.delete(id)
  if after
    candidate = revision_paths.fetch(after['sha256']).find { |r| File.file?(r['path']) && sha(File.binread(r['path'])) == after['sha256'] }
    raise "After bytes unavailable #{label}" unless candidate
    state[id] = parse(after['path'], File.binread(candidate['path']))
    raise "After identity/version mismatch #{label}" unless state[id]['identity'] == id && state[id]['version'] == after['version']
    last_operation[id] = label
  end
end
raise 'Expected seven mandatory mappings' unless order.length == 7
checks['all_91_operations_replayed_against_exact_bytes'] = all_ops.length == 91
checks['all_61_prior_archives_exact'] = archive_receipts.length == 61
checks['all_7_required_repairs_preceded_extraction_or_retirement'] = true
checks['all_48_split_replace_dedupe_successor_sequences_valid'] = disposition_order.length == 48
before964 = state.dup
source_paths = OWNERS.flat_map { |owner| ROLES.flat_map { |role| Dir.glob("#{BASE}/#{owner}/#{role}/*.md") } }.sort
current = source_paths.to_h { |p| r = parse(p, File.binread(p)); [r['identity'],r] }
raise 'Source identity collision' unless current.length == source_paths.length
source_changes = (current.keys | state.keys).select { |id| current[id]&.values_at('path','sha256') != state[id]&.values_at('path','sha256') }
checks['source_frontier_exactly_714_Core655_Local59'] = current.length == 714 && current.values.count { |r| r['path'].include?('/001_CORE_META_MODEL/') } == 655
checks['only_GOV314_reference_only_change_since963'] = (source_changes - ['CAPRMEDIO-GOV-REQU-314']).empty?
change964 = read_json('CA-P-964-changes.json')['operations'].fetch(0)
prior314, current314 = before964.fetch('CAPRMEDIO-GOV-REQU-314'), current.fetch('CAPRMEDIO-GOV-REQU-314')
checks['GOV314_exact_prior_archive_and_current_receipts'] = sha(File.binread(change964['archive']['path'])) == prior314['sha256'] && current314['sha256'] == change964['after']['sha256']
checks['GOV314_Claim_Subjects_unrelated_metadata_preserved'] = prior314['body'].b == current314['body'].b && prior314['meta'].reject { |k,_| %w[version updated_at relations].include?(k) } == current314['meta'].reject { |k,_| %w[version updated_at relations].include?(k) }
checks['GOV314_only_mapped_reference_changed_and_collection_canonically_ordered'] = relation_values(prior314,'child_of') == relation_values(current314,'child_of') && relation_values(current314,'relates_to') == relation_values(prior314,'relates_to').map { |v| v == change964['target_before'] ? change964['target_after'] : v }.uniq.sort
checks['GOV314_revision_metadata_and_General_tier_preserved'] = current314['version'] == prior314['version']+1 && current314['path'] == prior314['path'] && current314['path'].include?('-GENERAL-') && current314['meta']['updated_at'] == change964['at']

file_stdout, file_stderr, file_status = Open3.capture3('rg', '--files', '--hidden', '--no-ignore', *EXCLUDES.flat_map { |g| ['-g',g] }, '.')
raise file_stderr unless file_status.success?
files = file_stdout.lines.map { |p| p.strip.sub(%r{\A\./},'') }.sort
active_authority_paths = files.select do |p|
  parts = p.split('/')
  p.end_with?('.md') && (p.start_with?(BASE + '/') || p.start_with?('.caprmedio_caprmedio/')) && (parts & INACTIVE).empty? && File.basename(File.dirname(p)).match?(/\A0[1-9]_/) && !File.symlink?(p)
end
authority, authority_by_path, parse_diagnostics = {}, {}, []
active_authority_paths.each do |path|
  begin
    r = parse(path, File.binread(path))
    authority[r['identity']] = r
    authority_by_path[path] = r
  rescue Psych::Exception, RuntimeError => e
    parse_diagnostics << { 'path' => path, 'diagnostic' => e.message.lines.first.strip }
  end
end
authority.merge!(current)
external_rmed = authority.select { |_,r| ROLES.include?(File.basename(File.dirname(r['path']))) && !current.key?(r['identity']) }
external_rmed_paths = authority_by_path.values.select { |r| ROLES.include?(File.basename(File.dirname(r['path']))) && !source_paths.include?(r['path']) }
duplicate_authority_ids = authority_by_path.values.group_by { |r| r['identity'] }.select { |_,rows| rows.length > 1 }.transform_values { |rows| rows.map { |r| receipt(r) } }
graph_stages = { 'before962' => initial_state, 'before964' => before964, 'after964' => current }.transform_values do |sources|
  universe = authority.reject { |_,r| source_paths.include?(r['path']) || before964.key?(r['identity']) || initial_state.key?(r['identity']) }.merge(sources)
  graph_records = external_rmed.merge(sources)
  edges, unresolved = edges_for(graph_records, universe)
  cycles = { 'all_directed_relation_kinds' => cyclic_components(edges) }
  edges.map { |r| r['relation'] }.uniq.sort.each { |kind| cycles[kind] = cyclic_components(edges.select { |r| r['relation'] == kind }) }
  { 'edges' => edges, 'unresolved' => unresolved, 'cyclic_components' => cycles, 'graph_records' => graph_records.length }
end
edge_key = ->(e) { e.values_at('source','relation','target') }
base_graph, before_graph, after_graph = graph_stages.values_at('before962','before964','after964')
unresolved_new_owner_rows = after_graph['unresolved'].reject { |e| base_graph['unresolved'].any? { |b| edge_key.call(e) == edge_key.call(b) } }
inherited_unresolved = unresolved_new_owner_rows.filter_map do |edge|
  predecessors = maps.values.flat_map { |m| m['dispositions'] }.select { |d| d['after_owners'].any? { |o| o['identity'] == edge['source'] } }.map { |d| (d['before']||d['execution_before']).values_at('canonical_identity','identity').compact.first }
  prior = base_graph['unresolved'].find { |b| predecessors.include?(b['source']) && b.values_at('relation','target') == edge.values_at('relation','target') }
  { 'before' => prior, 'after' => edge, 'classification' => 'Exact unresolved target/relation inherited from mapped predecessor; not a newly unresolved authority identity.' } if prior
end
introduced_unresolved = unresolved_new_owner_rows.reject { |e| inherited_unresolved.any? { |r| r['after'] == e } }
introduced_cycles = after_graph['cyclic_components'].to_h { |kind,items| [kind, items - base_graph['cyclic_components'].fetch(kind,[])] }.reject { |_,v| v.empty? }
checks['no_new_unresolved_typed_target_since_before962_after_explicit_predecessor_lineage'] = introduced_unresolved.empty?
checks['no_new_per_relation_cycles_since_before962'] = introduced_cycles.reject { |kind,_| kind == 'all_directed_relation_kinds' }.empty?
checks['CA_P_964_preserves_exact_semantic_edges_and_diagnostics'] = before_graph['edges'].map(&edge_key).sort == after_graph['edges'].map(&edge_key).sort && before_graph['unresolved'].map(&edge_key).sort == after_graph['unresolved'].map(&edge_key).sort && before_graph['cyclic_components'] == after_graph['cyclic_components']

reference_decisions = incoming['references'].select { |r| r['consumer_active_RMED'] }.map do |ref|
  original = initial_state.values.find { |r| r['path'] == ref['consumer_path'] } || authority.values.find { |r| r['path'] == ref['consumer_path'] }
  consumer = current[original&.fetch('identity',nil)] || authority[original&.fetch('identity',nil)]
  raise "Consumer missing #{ref['consumer_path']}" unless consumer
  values = ref['typed_relation'] ? relation_values(consumer,ref['typed_relation']) : []
  resolved = values.map { |v| resolve(v,authority) }
  verified = ref['typed_relation'] ? ref['proposed_targets'].all? { |t| resolved.include?(t) } : ref['proposed_targets'].all? { |t| consumer['body'].include?(t) && authority.key?(t) }
  raise "Lost mapped target #{ref['reference_id']}" unless verified
  ref.slice('reference_id','target_before','proposed_targets','typed_relation','mapping_rationale','required_before_extraction','blocking_external_prerequisite').merge('current_consumer' => receipt(consumer), 'actual_relation_values' => values, 'resolved_relation_targets' => resolved, 'semantic_target_set_verified' => verified, 'changed_in964' => source_changes.include?(consumer['identity']))
end

identities = (maps.values.flat_map { |m| m['dispositions'].flat_map { |d| [(d['before']||d['execution_before']).values_at('canonical_identity','identity').compact.first] + d['after_owners'].map { |o| o['identity'] } } }).uniq.sort_by { |id| -id.length }
retired = all_ops.select { |o| o['kind'] == 'retire_predecessor' }.map { |o| o['identity'] }
pattern = '(?<![A-Za-z0-9])(?:' + identities.map { |id| Regexp.escape(id) }.join('|') + ')(?![0-9])'
stdout, stderr, status = Open3.capture3('rg','--json','--hidden','--no-ignore','--pcre2',*EXCLUDES.flat_map { |g| ['-g',g] },pattern,'.')
raise stderr unless [0,1].include?(status.exitstatus)
by_path = authority_by_path
scan, handoff = [], {}
stdout.each_line do |line|
  event = JSON.parse(line); next unless event['type'] == 'match'
  data = event['data']; path = data['path']['text']&.sub(%r{\A\./},''); next unless path
  text = data['lines'].fetch('text','').chomp; next if text.match?(/\Aatom_id\s*:/)
  parts = path.split('/'); consumer = by_path[path]
  generated = path.match?(%r{00_APPLICABLE_METHODOLOGY/0[45679]_}) || path.include?('.projection.') || parts.include?('.caprmedio_install') || parts.include?('.caprmedio_runtime')
  context = !(parts & INACTIVE).empty? || path.include?('/work_journal/') ? 'historical_or_journal' : generated ? 'generated_or_installed' : consumer && ROLES.include?(File.basename(File.dirname(path))) ? (current.key?(consumer['identity']) ? 'active_source_RMED' : 'external_active_RMED') : parts.include?('03_plan') ? 'other_plan' : path.match?(%r{(?:/201_TOOLS/|\.py\z|\.rb\z|\.js\z|\.ts\z)}) ? 'tool_or_implementation' : 'other_non_RMED'
  data['submatches'].each do |m|
    target = m['match']['text']; next if consumer && consumer['identity'] == target
    row = { 'path' => path, 'line' => data['line_number'], 'target' => target, 'context' => context, 'retired_target' => retired.include?(target) }
    row['text'] = text.length <= 800 ? text : text[[m['start']-100,0].max,250]
    scan << row
    next if context == 'active_source_RMED'
    h = handoff[path] ||= { 'path' => path, 'sha256' => sha(File.binread(path)), 'context' => context, 'targets' => {}, 'required_before_retirement' => false }
    (h['targets'][target] ||= []) << data['line_number']
  end
end
active_mentions = scan.select { |r| %w[active_source_RMED external_active_RMED].include?(r['context']) }
fresh_rationales = {
  ['CAPRMEDIO-GOV-REQU-353','CA-D-329'] => 'Retained proof-binding semantics explicitly delegate frontier representation to the revised D329 owner; correct contribution.',
  ['CAPRMEDIO-GOV-REQU-337','CA-D-388'] => 'Retained stage vocabulary explicitly delegates physical prefixes/formats to D388; correct contribution.',
  ['CAPRMEDIO-GOV-REQU-315','CA-D-396'] => 'Retained production logging policy delegates record content to D396; correct contribution.',
  ['CA-D-383','CAPRMEDIO-GOV-REQU-294'] => 'Reporting field serialization consumes retained allowed values/default behavior in R294; correct semantic target.',
  ['CA-D-387','CAPRMEDIO-GOV-REQU-302'] => 'Admission field serialization consumes retained allowed strictness/default in R302; correct semantic target.',
  ['CA-D-406','CA-D-328'] => 'Residual workflow/local-control Journal contract explicitly excludes and points to the unchanged Work Journal placement owner.',
  ['CA-D-406','CA-D-339'] => 'Residual workflow/local-control Journal contract explicitly excludes and points to the unchanged Implementation Journal owner.'
}
fresh_decisions = active_mentions.map do |mention|
  consumer = by_path.fetch(mention['path'])
  baseline_decision = reference_decisions.find { |d| d['current_consumer']['identity'] == consumer['identity'] && d['proposed_targets'].include?(mention['target']) }
  reason = baseline_decision&.fetch('mapping_rationale',nil) || fresh_rationales[[consumer['identity'],mention['target']]]
  reason ||= 'Existing consumer retains unchanged D268 direct-relation serialization authority; reused D268 was not reclassified and requires no link change.' if mention['target'] == 'CA-D-268' && %w[CAPRMEDIO-META-REQU-100 CAPRMEDIO-META-REQU-127 CA-E-404 CAPRMEDIO-GOV-EVAL-005].include?(consumer['identity'])
  raise "Unreviewed fresh reference #{consumer['identity']} -> #{mention['target']}" unless reason
  mention.merge('consumer' => consumer['identity'], 'target_current' => receipt(authority.fetch(mention['target'])), 'decision' => 'Retain verified surviving contribution', 'rationale' => reason, 'confidence_percent' => 99)
end
checks['no_active_RMED_mention_of_14_retired_identities'] = active_mentions.none? { |r| r['retired_target'] }
checks['all_27_fresh_active_mentions_have_contribution_specific_decisions'] = fresh_decisions.length == 27
checks['all_11_baseline_active_reference_decisions_preserved'] = reference_decisions.length == 11
index_out, index_err, index_status = Open3.capture3('git','diff','--cached','--raw','--no-renames')
raise index_err unless index_status.success?
checks['git_index_unchanged'] = sha(index_out) == '57190e4a096cc585704d68f44ed8f1744a2b3487c32643b5bb0da162a2d126c2'
handoff.each_value do |h|
  h['targets'].transform_values! { |v| v.uniq.sort }
  h['follow_up'] = case h['context']
  when 'historical_or_journal' then 'Preserve exact original identity/revision provenance; no history rewrite or follow-up required for these mentions.'
  when 'generated_or_installed' then 'Separately authorized source-driven rebuild/reinstall must consume surviving owner mapping; do not hand-edit generated/installed bytes.'
  when 'external_active_RMED' then 'Retained semantic contribution remains valid; preserve current Claim. Canonicalize a decorated relation only in separately authorized consumer revision; no pre-retirement blocker.'
  when 'other_plan' then 'Preserve planning/design references as scoped instructions and evidence; refresh only when separately executing or revising that Plan.'
  when 'tool_or_implementation' then 'Separately inspect whether identifier is executable lookup or a migration/history fixture; apply exact successor contribution mapping only in its owned Tool/implementation change.'
  else 'Non-RMED mention remains outside this Task; use the exact path and target map during separately scoped reconciliation.'
  end
end
save('ordering.json', { 'task' => 'CA-P-964@2', 'basis' => 'Replay exact CA-P-960 bytes through all 91 CA-P-962/963 operations; read each successor and intermediate consumer Revision from current or exact Archive bytes.', 'mandatory_reference_order' => order, 'all_extraction_retirement_order' => disposition_order, 'archive_receipts' => archive_receipts, 'known_corrected_intermediate_claim' => 'CA-D-378@1 contained lowercase Analysis a; CA-P-962:57 restored A in @2 and preserved @1. This is recorded, not concealed; no required incoming consumer repair depended on D378. All current owner semantic correctness remains subject to CA-P-965 final review.' })
save('references.json', { 'task' => 'CA-P-964@2', 'decisions' => reference_decisions, 'fresh_active_RMED_mentions' => active_mentions, 'scan' => { 'pattern' => pattern, 'candidate_identities' => identities, 'retired_identities' => retired, 'repository_files_enumerated' => files.length, 'occurrences' => scan.length, 'consumer_paths' => scan.map { |r| r['path'] }.uniq.length, 'contexts' => scan.group_by { |r| r['context'] }.transform_values(&:length), 'source_frontier' => current.values.map { |r| receipt(r) }.sort_by { |r| r['path'] }, 'active_external_RMED_count' => external_rmed.length, 'external_parse_diagnostics' => parse_diagnostics, 'limits' => 'Repository-local read-only rg includes hidden/ignored files. .git, secret files, .DS_Store and execution_evidence excluded; symlinks not followed. Prose matching covers changed predecessor/successor identities, not every natural-language conceptual mention.' } })
save('graph.json', { 'task' => 'CA-P-964@2', 'graph_scope' => 'Directed authored Atom relations from both source RMED owners plus current external active RMED consumers; resolution universe includes other active source/Project authority. Decorated legacy targets resolve by exact current stem or longest canonical identity prefix. Every relation kind is checked independently. Mixed-kind components are diagnostics only, never classified as dependency cycles.', 'stages' => graph_stages, 'inherited_unresolved_at_successor_owners' => inherited_unresolved, 'introduced_unresolved_since_before962' => introduced_unresolved, 'introduced_cycles_since_before962' => introduced_cycles })
save('handoff.json', { 'task' => 'CA-P-964@2', 'next_task' => 'CA-P-965', 'external_prerequisite_blockers' => [], 'exact_out_of_scope_paths' => handoff.values.sort_by { |h| h['path'] }, 'retired_successor_map' => maps.values.flat_map { |m| m['dispositions'] }.select { |d| retired.include?((d['before']||d['execution_before']).values_at('canonical_identity','identity').compact.first) }.to_h { |d| [(d['before']||d['execution_before']).values_at('canonical_identity','identity').compact.first,d['after_owners'].map { |o| o['identity'] }] }, 'boundaries' => 'Root owns lifecycle. No source-owner migration, Settings selections or pending Epic005 decisions, external source mutation, Tool/compiler/install/runtime or Projection build, Journal or Git index/commit/push change.' })
verification = { 'task' => 'CA-P-964@2', 'result' => checks.values.all? ? 'PASS' : 'FAIL', 'checks' => checks, 'source_changes_since963' => source_changes, 'counts' => { 'sources' => current.length, 'operations_replayed' => all_ops.length, 'exact_archives' => archive_receipts.length, 'ordered_dispositions' => disposition_order.length, 'mandatory_reference_mappings' => order.length, 'fresh_active_mentions' => active_mentions.length, 'external_handoff_paths' => handoff.length, 'unresolved_before962' => base_graph['unresolved'].length, 'unresolved_before964' => before_graph['unresolved'].length, 'unresolved_after964' => after_graph['unresolved'].length, 'cycle_components_before962' => base_graph['cyclic_components']['all_directed_relation_kinds'].length, 'cycle_components_after964' => after_graph['cyclic_components']['all_directed_relation_kinds'].length }, 'index_sha256' => sha(index_out), 'new_cycles' => introduced_cycles, 'new_unresolved_targets' => introduced_unresolved }
save('verification.json',verification)
save('fresh-decisions.json', { 'task' => 'CA-P-964@2', 'decisions' => fresh_decisions })
save('coverage.json', { 'task' => 'CA-P-964@2', 'all_source_RMED_paths' => source_paths.length, 'all_parsed_external_RMED_paths' => external_rmed_paths.length, 'external_RMED_unique_ids_in_graph' => external_rmed.length, 'active_authority_duplicate_identity_paths' => duplicate_authority_ids, 'graph_limit' => 'The identity graph uses one current record per duplicate external identity. These legacy duplicates are outside964 scope; the fresh text scan classifies every parsed path independently. CA-P-964 changes no resolved edge, so its zero edge/cycle delta is unaffected. This is not a repository-wide graph-health verdict.' })
puts JSON.pretty_generate(verification)
exit(checks.values.all? ? 0 : 1)
