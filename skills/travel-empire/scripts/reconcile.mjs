#!/usr/bin/env node
/** Reconcile research candidates. Never promote agreement or write facts.json. */
import {readFileSync,writeFileSync,readdirSync,renameSync} from 'node:fs';
import {join,resolve} from 'node:path';
import {pathToFileURL} from 'node:url';
const object=v=>v!==null&&typeof v==='object'&&!Array.isArray(v);
const stable=v=>object(v)?Object.fromEntries(Object.keys(v).sort().map(k=>[k,stable(v[k])])):Array.isArray(v)?v.map(stable):v??null;
const canonical=v=>JSON.stringify(stable(v));
const fact=v=>object(v)&&'value' in v&&!('rank' in v)&&v.kind!=='recommendation';
const identity=v=>object(v)?['id','name','title','passport','place','area','name_or_type'].map(k=>v[k]).find(x=>typeof x==='string'&&x.trim())??null:null;
export function reconcile(sources){
  if(!Array.isArray(sources)||!sources.length)throw Error('At least one valid research file is required.');
  const names=sources.map(s=>s.name);if(new Set(names).size!==names.length)throw Error('Source names must be unique.');
  for(const s of sources)if(!object(s.data)||![3,4].includes(s.data._meta?.schema_version)||!s.data._meta?.project)throw Error(`Missing project or unsupported facts schema in ${s.name}.`);
  for(const select of [m=>m.project,m=>m.country,m=>m.country_iso,m=>m.audience,m=>m.locale])if(new Set(sources.map(s=>canonical(select(s.data._meta)))).size!==1)throw Error('Research files disagree on project, country, audience or locale. Resolve scope first.');
  const report={sources:names,counts:{facts:0,agreements:0,disputes:0,missing:0,recommendations:0},disputes:[],notes:[]};
  function walk(path,versions){
    const present=versions.filter(v=>v!==undefined&&v!==null),first=present[0];if(!present.length)return null;
    if(present.some(fact)){
      if(present.some(v=>!fact(v)))throw Error(`Incompatible fact shapes at ${path}.`);
      report.counts.facts++;
      const values=versions.map(v=>v?.value),supplied=values.filter(v=>v!==null&&v!==undefined),unique=[...new Set(supplied.map(canonical))];
      const live=present.some(v=>v.status==='serve_live'),conflict=unique.length>1;
      if(supplied.length<sources.length)report.counts.missing++;
      if(conflict){report.counts.disputes++;report.disputes.push({path,values:versions.map((record,i)=>({source:names[i],record:record??null}))});}
      else if(supplied.length===sources.length&&supplied.length)report.counts.agreements++;
      const out={...first,value:live||conflict?null:supplied[0]??null,status:live?'serve_live':conflict?'disputed':'unverified',source_url:null,source_kind:null,checked_at:null,review_after:null,scope:'',support:'',_candidates:versions.map((record,i)=>({source:names[i],record:record??null}))};
      delete out.valid_from;delete out.valid_until;return out;
    }
    if(present.some(v=>object(v)&&('rank' in v||v.kind==='recommendation'))){
      if(present.some(v=>!object(v)||!('value' in v)))throw Error(`Incompatible recommendations at ${path}.`);
      const pool=new Map();versions.forEach((v,i)=>{
        const values=Array.isArray(v?.value)?v.value:v?.value==null?[]:[v.value];
        for(const value of values){const key=identity(value)?.toLocaleLowerCase()??canonical(value);if(!pool.has(key))pool.set(key,{value,named:[],variants:[]});const row=pool.get(key);if(!row.named.includes(names[i]))row.named.push(names[i]);row.variants.push({source:names[i],value});}
      });
      report.counts.recommendations+=pool.size;
      return {...first,kind:'recommendation',rank:'candidate',value:[...pool.values()].map(({value,named,variants})=>({...object(value)?value:{name:value},_named_by:named,_variants:variants}))};
    }
    if(Array.isArray(first)){
      if(present.some(v=>!Array.isArray(v)))throw Error(`Incompatible array at ${path}.`);
      const named=present.flat().length>0&&present.flat().every(v=>identity(v)!==null);
      if(named){for(const arr of present){const ids=arr.map(identity);if(new Set(ids).size!==ids.length)throw Error(`Duplicate entity at ${path}.`);}const ids=[...new Set(present.flat().map(identity))];return ids.map(id=>walk(`${path}[${id}]`,versions.map(arr=>arr?.find(v=>identity(v)===id))));}
      if(present.flat().every(v=>!object(v)&&!Array.isArray(v)))return [...new Map(present.flat().map(v=>[canonical(v),v])).values()];
      const max=Math.max(...present.map(v=>v.length));if(new Set(present.map(v=>v.length)).size>1)report.notes.push({path,note:'Unnamed arrays differed in length; index alignment requires review.'});
      return Array.from({length:max},(_,i)=>walk(`${path}[${i}]`,versions.map(v=>v?.[i])));
    }
    if(object(first)){
      if(present.some(v=>!object(v)))throw Error(`Incompatible object at ${path}.`);const out={};
      for(const key of new Set(present.flatMap(Object.keys))){
        if(key==='_meta'){out[key]={...first._meta,schema_version:4,ai_source:`candidates:${names.join('+')}`,produced_at:new Date().toISOString().slice(0,10)};continue;}
        if(key.startsWith('_')){out[key]=present.find(v=>key in v)?.[key];continue;}
        out[key]=walk(path?`${path}.${key}`:key,versions.map(v=>v?.[key]));
      }return out;
    }
    if(new Set(present.map(canonical)).size>1){report.notes.push({path,note:'Scalar disagreement, left unresolved.',values:versions.map((value,i)=>({source:names[i],value:value??null}))});return null;}
    return first;
  }
  const data=walk('',sources.map(s=>s.data));if(!report.counts.facts)throw Error('No fact records found; no output will be written.');data._meta.verification='candidate_only';return {data,report};
}
function main(){
  const args=process.argv.slice(2);if(args.includes('--help')||args.includes('-h')){console.log('Usage: node reconcile.mjs PROJECT_DIR\nReads all raw/*.json (schemas 3/4). Writes facts.candidates.json, reconciliation-report.json, disputes.md. Agreement remains unverified. Never writes facts.json or calls external services.');return;}
  if(args.length!==1||args[0].startsWith('-'))throw Error('Supply one project directory; see --help.');
  const dir=resolve(args[0]),raw=join(dir,'raw');
  const sources=readdirSync(raw).filter(n=>n.endsWith('.json')).sort().map(name=>({name:name.slice(0,-5),data:JSON.parse(readFileSync(join(raw,name),'utf8'))}));
  const ids=sources.map(s=>s.data?._meta?.ai_source).filter(Boolean);if(new Set(ids).size!==ids.length)throw Error('Duplicate ai_source identities; copies are not independent research.');
  const {data,report}=reconcile(sources);
  const md=['# Research disagreements','','Candidates only. Consensus is not source verification. facts.json was not changed.','',`Facts: ${report.counts.facts}; equal supplied values: ${report.counts.agreements}; disagreements: ${report.counts.disputes}; incomplete responses: ${report.counts.missing}.`,'',...report.disputes.flatMap(d=>[`## ${d.path}`,...d.values.map(v=>`- ${v.source}: ${JSON.stringify(v.record?.value??null)}`),'']),'Open appropriate sources, check scope and effective dates, then write verified facts separately. Review all unresolved items; never cap their count.',''].join('\n');
  for(const [name,body] of [['facts.candidates.json',JSON.stringify(data,null,2)+'\n'],['reconciliation-report.json',JSON.stringify(report,null,2)+'\n'],['disputes.md',md]]){const out=join(dir,name),tmp=`${out}.${process.pid}.tmp`;writeFileSync(tmp,body);renameSync(tmp,out);}
  console.log(JSON.stringify({result:'CANDIDATES_ONLY',...report.counts,output:join(dir,'facts.candidates.json'),canonical_facts_untouched:true}));
}
if(process.argv[1]&&import.meta.url===pathToFileURL(resolve(process.argv[1])).href){try{main();}catch(e){console.error(`RECONCILIATION FAILED: ${e.message}`);process.exitCode=1;}}
