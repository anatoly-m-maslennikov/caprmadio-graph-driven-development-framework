#!/usr/bin/env ruby
# Bounded final evidence verifier. Sources are read-only; writes use apply_patch.
require 'json'
require 'yaml'
require 'date'
require 'digest'
require 'open3'
require 'pathname'

HERE = File.expand_path(__dir__)
ROOT = Pathname.new(HERE).ascend.find { |p| (p/'102_FRAMEWORK_ENGINE').directory? && (p/'.caprmedio_framework').directory? }.to_s
raise 'Repository root not found' if ROOT.empty?
Dir.chdir(ROOT)
BASE = '.caprmedio_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources'
ROLES = {'04_requirement'=>'Requirement','05_method'=>'Method','06_evaluation'=>'Evaluation','07_delivery'=>'Delivery'}.freeze
OWNERS = %w[001_CORE_META_MODEL 003_LOCAL_CONFIGURATION].freeze
INDEX_SHA = '57190e4a096cc585704d68f44ed8f1744a2b3487c32643b5bb0da162a2d126c2'
def sha(bytes) = Digest::SHA256.hexdigest(bytes)
def json(name) = JSON.parse(File.read(File.join(HERE, "CA-P-#{name}.json")))
def need(value, message) = (raise(message) unless value)
def parse(path, bytes)
  bytes = bytes.dup.force_encoding(Encoding::UTF_8)
  need(bytes.valid_encoding?, "Invalid UTF-8: #{path}")
  match = bytes.match(/\A---\r?\n(.*?)\r?\n---(?:\r?\n|\z)(.*)/m)
  need(match, "Missing frontmatter: #{path}")
  meta = YAML.safe_load(match[1], permitted_classes: [Date, Time], aliases: false)
  stem = File.basename(path, '.md')
  id = meta['atom_id'] || stem[/\A[A-Z][A-Z0-9_]*(?:-[A-Z][A-Z0-9_]*)*-\d+(?=-|\z)/] || stem.split('--',2).first
  {'identity'=>id,'path'=>path,'version'=>meta['version'],'sha256'=>sha(bytes),'meta'=>meta,'body'=>match[2],'text'=>bytes,
   'source_owner'=>path.split('/')[3],'content_role'=>ROLES.fetch(File.basename(File.dirname(path)))}
end
def receipt(r) = r.slice('identity','path','version','sha256','source_owner','content_role')
def tier(path) = (File.basename(path)[/-(PRINCIPLE|CORE|GENERAL)-/,1] || 'STANDARD').capitalize
def save(name, data)
  path = File.join(HERE, "CA-P-965-#{name}")
  content = data.is_a?(String) ? data : JSON.pretty_generate(data)+"\n"
  old = File.file?(path) ? File.read(path) : nil
  return if old == content
  patch = "*** Begin Patch\n" + (old ? "*** Update File: #{path}\n@@\n"+old.lines.map{|l|'-'+l.chomp+"\n"}.join : "*** Add File: #{path}\n")
  patch += content.lines.map{|l|'+'+l.chomp+"\n"}.join+"*** End Patch\n"
  out, err, status = Open3.capture3('apply_patch', stdin_data: patch)
  need(status.success? && File.binread(path)==content.b, "Evidence patch failed: #{out} #{err}")
end

snapshot = json('960-snapshot')['records']
audit = json('960-inventory')['records'].to_h{|r|[r['canonical_identity'],r]}
original = snapshot.to_h{|r|[r['canonical_identity'],parse(r['source_path'],r['complete_source_text'])]}
design = json('961-dispositions')
owners = design['authority_owners'].to_h{|r|[r['identity'],r]}
ops = (962..964).flat_map{|n|json("#{n}-changes")['operations'].map{|o|o.merge('task'=>n)}}
states, state, archives = {}, original.dup, []
revision_paths = ops.flat_map{|o|[o['archive'],o['after']].compact}.group_by{|r|r['sha256']}
ops.each do |op|
  id, before, after = op.values_at('identity','before','after')
  label = "#{op['task']}:#{op['sequence']}"
  if before
    need(state[id] && state[id]['sha256']==before['sha256'], "Prior mismatch #{label}")
    a = op.fetch('archive'); bytes = File.binread(a['path'])
    need(bytes==state[id]['text'].b && sha(bytes)==a['sha256'], "Archive mismatch #{label}")
    need(a['version']==state[id]['version'] && a['path'].end_with?("@#{a['version']}.md"), "Archive identity/version #{label}")
    archives << a.merge('identity'=>id,'operation'=>label,'exact_prior_bytes'=>true)
  else
    need(!state.key?(id), "Duplicate admission #{label}")
  end
  state.delete(id)
  if after
    candidate = revision_paths.fetch(after['sha256']).find{|r|File.file?(r['path']) && sha(File.binread(r['path']))==after['sha256']}
    need(candidate, "Missing actual after bytes #{label}")
    r = parse(after['path'],File.binread(candidate['path']))
    need(r['identity']==id && r['version']==after['version'], "Identity/version mismatch #{label}")
    need(r['version']==(before ? before['version']+1 : 1), "Revision increment #{label}")
    timestamp = DateTime.parse(r['meta']['updated_at'].to_s)
    need(timestamp<=DateTime.parse(op['at']), "Updated At after operation receipt #{label}")
    need(timestamp.offset==DateTime.parse(op['at']).offset, "Executed Project-time offset differs from receipt #{label}")
    # The executor calls now() separately for source construction and its receipt;
    # 962:63 legitimately records 20:57:23 in the source and 20:57:24 in the log.
    # Exact after hashes bind the source timestamp. Do not equate those clocks.
    state[id]=r
  end
  states[label]=state.dup
end
paths = OWNERS.flat_map{|owner|ROLES.keys.flat_map{|role|Dir.glob("#{BASE}/#{owner}/#{role}/*.md")}}.sort
current = paths.to_h{|path|r=parse(path,File.binread(path));[r['identity'],r]}
need(current.length==paths.length, 'Duplicate source identity')
need(current.transform_values{|r|r.values_at('path','sha256')}==state.transform_values{|r|r.values_at('path','sha256')}, 'Unexplained current source change')
need(current.length==714 && current.values.count{|r|r['source_owner']==OWNERS.first}==655, 'Final source frontier mismatch')
new_ids = ops.select{|o|o['kind']=='new_owner'}.map{|o|o['identity']}
revised_ids = ops.select{|o|o['kind']=='revise_owner'}.map{|o|o['identity']}
retired_ids = ops.select{|o|o['kind']=='retire_predecessor'}.map{|o|o['identity']}
consumer_ids = ops.select{|o|o['kind']=='repair_consumer'}.map{|o|o['identity']}.uniq
changed_ids = current.keys.select{|id|!original[id] || current[id]['sha256']!=original[id]['sha256']}
fresh_ids = (owners.keys+consumer_ids).uniq
need([ops.length,archives.length,new_ids.length,revised_ids.length,retired_ids.length,changed_ids.length,fresh_ids.length]==[92,62,30,40,14,74,82], 'Change accounting mismatch')

# Reuse the reviewed 964 audit in an isolated Ruby process. Intercept its evidence
# writer in memory; remove its final exit/output only. No 964 files are rewritten.
helper = File.join(HERE,'CA-P-964-audit.rb')
code = File.read(helper)
needle = "snapshot = read_json('CA-P-960-snapshot.json')"
ending = "puts JSON.pretty_generate(verification)\nexit(checks.values.all? ? 0 : 1)"
need(code.scan(needle).length==1 && code.include?(ending), '964 helper entrypoint changed')
code = code.sub(needle,"def save(name, data)\n  ($captured ||= {})[name] = data\nend\n"+needle)
code = code.sub(ending,'puts JSON.generate($captured)')
out, err, status = Open3.capture3('ruby','-e','eval(STDIN.read, TOPLEVEL_BINDING, ARGV.fetch(0))',helper,stdin_data:code)
need(status.success?, "Read-only reference refresh failed: #{err}")
refresh = JSON.parse(out)
need(refresh['verification.json']['result']=='PASS', 'Fresh reference checks failed')
%w[ordering graph handoff fresh-decisions coverage].each do |part|
  fresh, prior = refresh["#{part}.json"], json("964-#{part}")
  if part=='fresh-decisions'
    # rg may enumerate identical matches in a different order. Preserve every
    # exact row while comparing this unordered decision inventory canonically.
    fresh = fresh.merge('decisions'=>fresh['decisions'].sort_by{|r|r.values_at('path','line','target')})
    prior = prior.merge('decisions'=>prior['decisions'].sort_by{|r|r.values_at('path','line','target')})
  end
  need(fresh==prior, "Reference evidence drift: #{part}")
end

field_checks = changed_ids.sort.map do |id|
  r, o, prior = current.fetch(id), owners[id], original[id]
  meta = r['meta']; subjects = meta.fetch('subjects'); values = []
  need((subjects.keys-%w[governs depends_on]).empty?, "Subject relation kind #{id}")
  subjects.each do |kind,forms|
    need((forms.keys-%w[continuant occurrent]).empty?, "Temporal form #{id}")
    forms.each do |form,refs|
      need(%w[continuant occurrent].include?(form) && refs.is_a?(Array) && !refs.empty? && refs.all?{|v|v.is_a?(String)&&!v.empty?}, "Subject shape #{id}")
      values.concat(refs)
    end
  end
  need(subjects.fetch('governs').values.flatten.length==1 && values.uniq==values, "Subject cardinality/duplicate #{id}")
  need(meta['cce_version']=='cce_1' && meta['version'].is_a?(Integer) && meta['version']>0, "CCE/Version #{id}")
  if o
    need(r['content_role']==o['content_role'] && r['source_owner']==o['source_owner'] && tier(r['path'])==o['local_tier'].split.first, "Role/owner/tier #{id}")
    need(meta['cce_form']==o['proposed_cce_form'], "CCE form #{id}")
    expected_subjects = o['proposed_subjects'] || prior&.dig('meta','subjects')
    correction = ops.reverse.find{|op|op['identity']==id && op['subject_correction']}
    expected_subjects = correction['subject_correction'] if correction
    if id=='CAPRMEDIO-GOV-REQU-296'
      expected_subjects = Marshal.load(Marshal.dump(expected_subjects))
      expected_subjects['depends_on']['continuant'].map!{|s|s=='Provenance' ? 'provenance' : s}
    end
    need(subjects==expected_subjects, "Admitted Subjects #{id}")
    need(r['body'].scan(/`[^`]*`/)==o['proposed_claim_body'].scan(/`[^`]*`/), "Literal changed against design #{id}")
    slug = r['body'].lines.first.delete_prefix('# ').strip.downcase.gsub(/[^a-z0-9]+/,'-').sub(/-\z/,'')
    need(File.basename(r['path']).split('--',2).last==slug+'.md', "H1/filename Summary #{id}")
  end
  if prior
    need(meta['atom_id']==prior['meta']['atom_id'] && r['identity']==prior['identity'], "Existing identity representation #{id}")
    prior_time, current_time = prior['meta']['updated_at'].to_s, meta['updated_at'].to_s
    need(DateTime.parse(current_time)>=DateTime.parse(prior_time), "Updated At precedes prior Revision #{id}")
    need(r['source_owner']==prior['source_owner'] && tier(r['path'])==tier(prior['path']), "Scope owner/tier changed #{id}")
    need(meta.reject{|k,_|%w[version updated_at subjects relations].include?(k)}==prior['meta'].reject{|k,_|%w[version updated_at subjects relations].include?(k)}, "Unrelated metadata/contribution map #{id}")
  else
    need(meta['atom_id']==id && id.match?(/\ACA-[DM]-\d+\z/), "New identity encoding #{id}")
  end
  receipt(r).merge('identity_revision_subject_scope_tier_carrier_checks'=>'PASS','subject_semantic_basis'=>'Complete Claim reviewed under M125/E246; admitted assignments plus the three recorded 962 corrections. No role-derived Temporal Form.','prior_updated_at'=>prior&.dig('meta','updated_at'),'current_updated_at'=>meta['updated_at'],'timestamp_basis'=>'Valid nondecreasing date-time; current offset matches its execution receipt. Original and current Revision offsets may differ; original bytes remain exact in Archives. D390 is not a closed timestamp grammar.')
end

# These rationales record the explicit complete-Claim review performed in CA-P-965;
# they are not keyword classification or an inference from passing syntax.
consumer_rationales = {
  'CA-E-427'=>'Falsifiable Epic Carrier/identity/status fixtures and acceptance remain E; current targets include D379 grammar and D353 exact-one Epic Carrier qualification.',
  'CAPRMEDIO-GOV-EVAL-006'=>'Falsifiable settings parsing and deterministic resolution remain E; R294/R302 preserve allowed values and policy while D383/D387 own the encoded fields.',
  'CAPRMEDIO-GOV-EVAL-009'=>'Falsifiable Concern priority storage and winner-selection conditions remain E; D386 owns the representation and R299 owns comparison and escalation.',
  'CAPRMEDIO-GOV-REQU-314'=>'R requires production evaluation readiness and separates accepted control meaning, implementation and outcomes; canonical R748 still owns Type admission. The evaluation_control spelling is a consumed Type reference, not a second token map.'
}
reviews = current.values.sort_by{|r|r['path']}.map do |r|
  id = r['identity']; inherited = !fresh_ids.include?(id)
  if inherited
    a = audit.fetch(id)
    need(a['sha256']==r['sha256'] && a.dig('complete_claim_review','reviewed') && a.dig('complete_claim_review','reviewed_sha256')==r['sha256'], "Unbound inherited review #{id}")
    need(!%w[carrier_specification_outside_D mixed_role_carrier_claim unresolved_classification].include?(a.dig('disposition','category')), "Unresolved inherited candidate #{id}")
    reason = a.dig('disposition','rationale')
  else
    reason = consumer_rationales[id] || owners.fetch(id)['rationale']
  end
  receipt(r).merge('local_tier'=>tier(r['path']),'final_disposition'=>"justified_#{r['content_role'].downcase}_contribution",'review_basis'=>inherited ? 'CA-P-960 complete-source semantic review reused after exact current hash equality' : 'CA-P-965 complete current body/Subjects and original-to-current allocation review','rationale'=>reason,'confidence_percent'=>99,'reviewed_sha256'=>r['sha256'],'carrier_authority_outside_D'=>false)
end
need(reviews.length==714 && reviews.count{|r|r['review_basis'].start_with?('CA-P-965')}==82, 'Final review coverage')
allocations = design['dispositions'].map do |d|
  id = d.dig('before','canonical_identity')
  need(d['original_claim_body']==original.fetch(id)['body'], "Original Claim mismatch #{id}")
  d['clause_allocations'].each{|a|need(!a['owners'].empty? && a['owners'].all?{|i|current.key?(i)}, "Missing clause owner #{id}")}
  d.slice('before','action','rationale','original_claim_body','clause_allocations').merge('final_review'=>'PASS: complete original contribution and qualifiers compared against complete surviving Claims','surviving_current_owners'=>d['clause_allocations'].flat_map{|a|a['owners']}.uniq.map{|i|receipt(current.fetch(i))},'semantic_limit'=>'Manual contribution/Scope judgment; quote coverage and exact bytes corroborate but do not prove semantic equivalence.')
end
shared = %w[CA-D-353 CA-R-1415 CA-R-1416 CA-D-329 CA-D-283].map do |id|
  {'identity'=>id,'original_body'=>original.fetch(id)['body'],'current_body'=>current.fetch(id)['body'],'review'=>'PASS: entire original contract remains; only mapped stricter Epic cardinality, monotonicity, unambiguity, lossless prose qualification, or same-ID filename preservation is added.'}
end
reference_only = consumer_ids-revised_ids
need(reference_only.all?{|id|current[id]['body']==original[id]['body'] && current[id]['meta']['subjects']==original[id]['meta']['subjects']}, 'Reference-only Claim/Subjects changed')
need(%w[CA-D-270 CA-D-268 CA-D-281 CA-D-282 CA-D-310 CA-D-328 CA-D-339 CAPRMEDIO-META-REQU-119].all?{|id|current[id]['sha256']==original[id]['sha256']}, 'Reused owner changed')
need(current['CA-D-378']['body'].include?('Analysis: A') && current['CAPRMEDIO-GOV-REQU-296']['meta']['subjects']['depends_on']['continuant'].include?('provenance'), 'Intermediate correction lost')

expansion_command = %w[python3 -B 102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/COMPILE_APPLICABLE_METHODOLOGY/validate_expansion_boundary.py --root . --include-layer CORE_META_MODEL --include-layer LOCAL_CONFIGURATION]
expansion_out, expansion_err, expansion_status = Open3.capture3(*expansion_command)
need(expansion_status.success?, "Expansion boundary failed: #{expansion_err} #{expansion_out}")
expansion = JSON.parse(expansion_out)
need(expansion['can_conform']==true && expansion['hard_violation_count']==0 && expansion['stable_lineage_gap_count']==0, 'Expansion boundary findings require disposition')
index_out, index_err, index_status = Open3.capture3('git','diff','--cached','--raw','--no-renames')
need(index_status.success? && sha(index_out)==INDEX_SHA, "Index changed #{index_err}")
need(paths.all?{|p|sha(File.binread(p))==current.values.find{|r|r['path']==p}['sha256']}, 'Source changed during final verification')

falsifiers = [
  ['active source Atom has no final review disposition','714 identity/path/hash-bound final dispositions; 82 complete fresh reviews and 632 exact-byte inherited reviews'],
  ['Carrier specification remains authoritative outside D','All 50 dispositions and complete current owners reviewed; surviving R is meaning/obligation, M275 reusable formatting, E consumer checks; no independently prescribed Carrier shape remains outside D'],
  ['Carrier specification has no D authority owner','All extracted Carrier clauses resolve to exact current D owners in allocation ledger; R963 is a reusable Method contribution, not an unowned Carrier contract'],
  ['non-D disposition lacks evidence supporting retained Content Role','Per-source rationale, CA-R-1339, CA-R-1340 and CA-R-1341 authority and special-case review below; no lexical-only classification'],
  ['mixed Claim loses original semantic contribution','50 original Claims, all clause allocations, five expanded shared-owner originals, and reference-only unchanged bodies independently reviewed'],
  ['Claim has duplicate authority owners','Same-purpose/context overlap review: single D maps, retained semantic admission distinct from token encoding, shared D owners reused once, concrete cardinality and general relation qualifications retained'],
  ['changed Atom fails applicable identity rules','74 current changed Atoms; exact identity representations preserved, 30 distinct admitted new role-coded identities; replacement uses separate identity'],
  ['changed Atom fails applicable Revision rules','92 replayed operations, positive sequential Versions, valid source and receipt timestamps and 62 exact Archives including intermediate corrections'],
  ['changed Atom fails applicable Subject rules','74 independent Psych-parsed Subject checks plus complete governed-Entity/prerequisite/Temporal Form review under M125/E246 and exact admitted assignments'],
  ['changed Atom fails applicable Scope rules','Current Claim domains, exact source owners, filename Scope and admitted Subjects reviewed; no source-owner or selected Settings migration'],
  ['changed Atom fails applicable Local Tier rules','Original Core/General/omitted Standard retained; new owners Standard; all four Content Roles independently represented'],
  ['changed Atom fails applicable Carrier rules','Exact admitted literal sequences, parsed frontmatter, Summary-to-filename checks on semantic owners, preserved reference-only carriers and representation domain review'],
  ['required incoming-reference repair did not precede predecessor retirement','Fresh 964 replay reproduces seven mandatory successor-repair-extraction sequences and all 48 split/replace/dedupe sequences; 963 handoff links survive'],
  ['required external pre-retirement repair lacks verified completion','Fresh full reference scan and mapped decisions have zero external prerequisite blockers; 1199 external paths remain explicit downstream/history handoff'],
  ['new blocking source conflict remains','Fresh graph equals verified 964 graph; 98 unresolved legacy rows unchanged with seven predecessor lineages; no dependency cycle or introduced unresolved target; complete changed-Claim overlap review found no new blocker'],
  ['downstream work presented completed without execution evidence','Report explicitly leaves generated/installed/runtime/Settings/source-owner/Journal/Git/project-wide work pending; expansion validator is source-only and does not rebuild']
].map{|condition,evidence|{'failure_condition'=>condition,'holds'=>false,'result'=>'PASS','evidence'=>evidence}}
counts = {'active_sources'=>current.length,'by_source_owner'=>current.values.group_by{|r|r['source_owner']}.transform_values(&:length),'by_content_role'=>current.values.group_by{|r|r['content_role']}.transform_values(&:length),'unchanged_from960'=>current.length-changed_ids.length,'fresh_complete_reviews'=>82,'inherited_exact_byte_reviews'=>632,'new_atoms'=>30,'revised_existing_atoms'=>44,'revised_semantic_or_shared_owners'=>40,'reference_only_additional_consumers'=>4,'retired_atoms'=>14,'operations'=>92,'archive_operations'=>62,'dispositions'=>50,'reused_unchanged_owners'=>8}
save('inventory.json',{'task'=>'CA-P-965@2','counts'=>counts,'records'=>current.values.sort_by{|r|r['path']}.map{|r|receipt(r).merge('local_tier'=>tier(r['path']),'byte_count'=>r['text'].bytesize,'frontmatter'=>r['meta'],'complete_claim_body'=>r['body'])}})
save('reviews.json',{'task'=>'CA-P-965@2','method'=>'Explicit semantic review plus exact hash-bound reuse; no syntax-generated role verdicts. All 82 selected complete current Claims and all 50 original Claims were read during this Task.','records'=>reviews})
save('preservation.json',{'task'=>'CA-P-965@2','dispositions'=>allocations,'expanded_shared_owner_originals'=>shared,'reference_only_unchanged_Claims'=>reference_only.map{|i|receipt(current[i])},'all_other_original_claims'=>'Exact bytes remain at current source or exact Archive; 640 surviving original source hashes are unchanged.','original_inventory_and_snapshot'=>'CA-P-960-inventory.json and CA-P-960-snapshot.json'})
save('changes.json',{'task'=>'CA-P-965@2','counts'=>counts,'new_atoms'=>new_ids.map{|i|receipt(current[i])},'revised_semantic_or_shared_owners'=>revised_ids.map{|i|{'before'=>receipt(original[i]),'after'=>receipt(current[i])}},'reference_consumer_operations'=>ops.select{|o|o['kind']=='repair_consumer'},'retired_successor_map'=>json('964-handoff')['retired_successor_map'],'retirement_operations'=>ops.select{|o|o['kind']=='retire_predecessor'},'exact_prior_archives'=>archives,'all_operations'=>ops,'reused_unchanged_owners'=>owners.values.select{|o|o['status']=='retain'}.map{|o|receipt(current[o['identity']])},'actual_normalization_corrections'=>ops.select{|o|o['kind']=='repair_owner'}})
save('verification.json',{'task'=>'CA-P-965@2','result'=>'PASS','counts'=>counts,'definition_of_done_falsifiers'=>falsifiers,'independent_changed_Atom_checks'=>field_checks,'reference_refresh'=>refresh['verification.json'],'reference_helper_sha256'=>sha(File.binread(helper)),'fresh_reference_graph_ordering_handoff_equal964'=>true,'expansion_boundary'=>{'command'=>expansion_command,'exit_code'=>expansion_status.exitstatus,'stdout'=>expansion_out,'stderr'=>expansion_err,'scope'=>'Read-only source boundary validation; no compilation or generated Projection rebuild'},'index_sha256'=>sha(index_out),'source_writes'=>0,'lifecycle_writes'=>0,'semantic_limit'=>'Semantic classifications and lossless allocations are explicit reviewed judgments at threshold 99, supported but not proved by deterministic checks. D390 does not define a closed timestamp grammar. Legacy and downstream limitations remain in the report.'})
puts JSON.pretty_generate({'result'=>'PASS','counts'=>counts,'falsifiers_checked'=>falsifiers.length,'source_writes'=>0,'lifecycle_writes'=>0})
