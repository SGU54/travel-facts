#!/usr/bin/env node
/** Validate declared provenance for facts actually used. Does not fetch or certify sources. */
import { readFileSync, writeFileSync, renameSync, mkdirSync } from 'node:fs';
import { resolve, dirname } from 'node:path';
import { pathToFileURL } from 'node:url';
export const validDate = v => typeof v === 'string' && /^\d{4}-\d{2}-\d{2}$/.test(v) && Number.isFinite(Date.parse(`${v}T00:00:00Z`)) && new Date(`${v}T00:00:00Z`).toISOString().slice(0,10) === v;
const object = v => v !== null && typeof v === 'object' && !Array.isArray(v);
const filled = v => {
  if (v === null || v === undefined || v === '') return false;
  if (typeof v === 'number') return Number.isFinite(v);
  if (Array.isArray(v)) return v.length > 0 && v.every(filled);
  if (object(v)) return Object.keys(v).length > 0 && Object.values(v).every(filled);
  return true;
};
const text = v => typeof v === 'string' && v.trim().length > 0;
const supplied = v => v !== null && v !== undefined && v !== '' && (!Array.isArray(v) || v.length > 0) && (!object(v) || Object.keys(v).length > 0);
export function collectFacts(data) {
  const result = [];
  function walk(node, parts) {
    if (Array.isArray(node)) { node.forEach((v,i)=>walk(v,[...parts,String(i)])); return; }
    if (!object(node) || node.kind === 'recommendation' || 'rank' in node) return;
    if ('value' in node) { const path=parts.join('.'); result.push({path,key:text(node.fact_key)?node.fact_key:path,node}); return; }
    for (const [key,value] of Object.entries(node)) {
      if (key.startsWith('_') || ['itineraries','recommendations','national_recommendations'].includes(key)) continue;
      walk(value,[...parts,key]);
    }
  }
  walk(data,[]); return result;
}
export function validateFacts(data, {asOf=new Date().toISOString().slice(0,10),usedKeys=null}={}) {
  const errors=[],warnings=[],issue=(code,path,message)=>errors.push({code,path,message});
  if (!validDate(asOf)) issue('date','--as-of','Use a real YYYY-MM-DD date.');
  if (!object(data) || !object(data._meta)) issue('metadata','_meta','Expected facts with _meta.');
  if (![3,4].includes(data?._meta?.schema_version)) issue('schema','_meta.schema_version','Supported facts schemas are 3 and 4; migrate explicitly.');
  if (!text(data?._meta?.project)) issue('project','_meta.project','A project identity is required.');
  if (usedKeys!==null && (!Array.isArray(usedKeys) || usedKeys.some(key=>!text(key)))) { issue('selection','usedKeys','Expected an array of nonempty fact keys.'); usedKeys=[]; }
  const records=collectFacts(data),byKey=new Map();
  for (const r of records) { if(byKey.has(r.key))issue('duplicate-key',r.path,`Duplicate fact key: ${r.key}`); else byKey.set(r.key,r); }
  if (!records.length) issue('empty','','No factual records were found.');
  const keys=usedKeys===null?records.filter(({node})=>supplied(node.value)||node.status==='verified').map(({key})=>key):[...new Set(usedKeys)];
  if (!keys.length) issue('empty-selection','','No facts selected. This cannot certify an article as fact-free.');
  let verified=0,highRisk=0;
  for (const key of keys) {
    const r=byKey.get(key); if(!r){issue('unknown-key',key,'Used fact key is missing.');continue;}
    const {node,path}=r;
    if (!filled(node.value)) issue('missing-value',path,'A used fact needs a complete value; split unresolved subcases into separate scoped records.');
    if (node.status!=='verified') issue('unverified',path,`Status ${JSON.stringify(node.status)} is not source verification; live values need their runtime mechanism.`); else verified++;
    if (!['primary','secondary'].includes(node.source_kind)) issue('source-kind',path,'Declare primary or secondary evidence.');
    if (node.risk != null && !['high','standard'].includes(node.risk)) issue('risk',path,'Use high or standard risk.');
    try { const u=new URL(node.source_url); if(!['http:','https:'].includes(u.protocol)||!u.hostname||u.username||u.password)throw Error(); }
    catch { issue('source-url',path,'Use an absolute HTTP(S) source URL without credentials.'); }
    for (const field of ['scope','support']) if(!text(node[field]))issue(field,path,`Record the ${field} that supports this exact claim.`);
    for (const field of ['checked_at','review_after']) if(!validDate(node[field]))issue(field,path,`Record a real ${field} date.`);
    if(validDate(node.checked_at)&&validDate(asOf)&&node.checked_at>asOf)issue('future-check',path,'A check cannot be in the future.');
    if(validDate(node.review_after)&&validDate(node.checked_at)&&node.review_after<node.checked_at)issue('review-order',path,'The review date precedes the check.');
    if(validDate(node.review_after)&&validDate(asOf)&&node.review_after<asOf)issue('stale',path,'The review date has passed; re-open the source.');
    for(const f of ['valid_from','valid_until'])if(node[f]!=null&&!validDate(node[f]))issue(f,path,`Use a source-stated ${f} date or omit it.`);
    if(validDate(node.valid_from)&&validDate(node.valid_until)&&node.valid_from>node.valid_until)issue('validity-order',path,'Effective dates are reversed.');
    if(validDate(node.valid_from)&&validDate(asOf)&&node.valid_from>asOf)issue('not-effective',path,'This fact is not yet effective. Model future rules separately.');
    if(validDate(node.valid_until)&&validDate(asOf)&&node.valid_until<asOf)issue('expired',path,'Source-stated validity has ended.');
    const high=node.risk==='high'||/(^|\.)(visa|entry|documents|safety_health|vaccines|passport|emergency_numbers|currency_import_export_limit|car_rental_and_driving)(\.|$)/.test(`${path}.${key}`);
    if(high){highRisk++;if(node.source_kind!=='primary')issue('primary-required',path,'Entry, safety, health, legal and consequential money rules need competent primary evidence.');}
  }
  if(data?._meta?.schema_version===3)warnings.push({code:'legacy',path:'_meta.schema_version',message:'Legacy shape is readable; used facts still need evidence.'});
  warnings.push({code:'scope-of-check',path:'',message:'Checks declared metadata, dates and references only. Independently review source support, scope, calculations, recommendations and unmarked prose claims.'});
  return {ok:errors.length===0,errors,warnings,coverage:{records:records.length,selected:keys.length,verified,highRisk}};
}
function main(){
  const args=process.argv.slice(2);
  if(args.includes('--help')||args.includes('-h')){console.log('Usage: node validate-facts.mjs FACTS.json [--used KEYS.json] [--as-of YYYY-MM-DD] [--output REPORT.json]\nKEYS.json is an array of exact fact keys. Without it, checks all populated facts. No network or database access.');return;}
  const file=args.shift();if(!file||file.startsWith('-'))throw Error('A facts JSON path is required; see --help.');
  const options={},paths={};
  while(args.length){const o=args.shift(),v=args.shift();if(!['--used','--as-of','--output'].includes(o)||!v||v.startsWith('--'))throw Error(`Invalid option ${o}; see --help.`);if(o==='--as-of')options.asOf=v;else paths[o]=v;}
  if(paths['--used'])options.usedKeys=JSON.parse(readFileSync(paths['--used'],'utf8'));
  const report=validateFacts(JSON.parse(readFileSync(file,'utf8')),options);
  if(paths['--output']){const out=resolve(paths['--output']);if([file,paths['--used']].filter(Boolean).some(p=>resolve(p)===out))throw Error('Report must differ from every input.');mkdirSync(dirname(out),{recursive:true});const tmp=`${out}.${process.pid}.tmp`;writeFileSync(tmp,JSON.stringify(report,null,2)+'\n');renameSync(tmp,out);}
  console.log(JSON.stringify(report,null,2));if(!report.ok)process.exitCode=1;
}
if(process.argv[1]&&import.meta.url===pathToFileURL(resolve(process.argv[1])).href){try{main();}catch(e){console.error(`FACTS CHECK FAILED: ${e.message}`);process.exitCode=1;}}
