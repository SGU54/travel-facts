#!/usr/bin/env node
/** Synthetic offline regressions for provenance and candidate reconciliation. */
import test from 'node:test';
import assert from 'node:assert/strict';
import {mkdtempSync,mkdirSync,writeFileSync,readFileSync,existsSync,rmSync} from 'node:fs';
import {tmpdir} from 'node:os';
import {join,dirname} from 'node:path';
import {fileURLToPath} from 'node:url';
import {spawnSync} from 'node:child_process';
import {validateFacts,collectFacts} from './validate-facts.mjs';
import {reconcile} from './reconcile.mjs';
const here=dirname(fileURLToPath(import.meta.url)),asOf='2026-10-08';
const leaf=(overrides={})=>({value:12,status:'verified',source_url:'https://authority.example/fixture',source_kind:'primary',checked_at:'2026-10-07',review_after:'2026-11-01',scope:'Synthetic fixture for testing only; adult standard ticket.',support:'Synthetic source section A states the sample value.',risk:'standard',fact_key:'transport.sample',...overrides});
const data=(node=leaf())=>({_meta:{schema_version:4,project:'synthetic-test',country:'Example',country_iso:'XX',audience:{nationality:'Example'},locale:{site_language:'en'}},transport:{sample:node}});
const check=(d,options={})=>validateFacts(d,{asOf,...options});
const source=(name,node)=>({name,data:data(node)});
const withTemp=fn=>{const dir=mkdtempSync(join(tmpdir(),'travel-facts-'));try{return fn(dir);}finally{rmSync(dir,{recursive:true,force:true});}};
const run=(script,args)=>spawnSync(process.execPath,[join(here,script),...args],{encoding:'utf8'});

test('declared complete metadata passes with exact coverage and an explicit scope limitation',()=>{
  const r=check(data());assert.equal(r.ok,true);assert.deepEqual(r.coverage,{records:1,selected:1,verified:1,highRisk:0});assert(r.warnings.some(w=>w.code==='scope-of-check'));
});
test('zero and false values remain valid factual values',()=>{assert(check(data(leaf({value:0}))).ok);assert(check(data(leaf({value:false}))).ok);});
test('partially unresolved compound values cannot publish as a verified whole',()=>{assert(!check(data(leaf({value:{adult:12,child:null}}))).ok);assert(!check(data(leaf({value:{}}))).ok);});
test('a partially populated unverified record is not silently skipped by the default selection',()=>{const d=data();d.other={sample:leaf({fact_key:'other.sample',status:'unverified',value:{adult:12,child:null}})};const r=check(d);assert.equal(r.coverage.selected,2);assert(!r.ok);});
for(const [name,overrides,code] of [
  ['model consensus',{status:'agreed_stable'},'unverified'],
  ['missing primary source URL',{source_url:null},'source-url'],
  ['missing actual check date',{checked_at:null},'checked_at'],
  ['invented calendar date',{checked_at:'2026-02-30'},'checked_at'],
  ['future source check',{checked_at:'2026-10-09'},'future-check'],
  ['stale source review',{review_after:'2026-10-01'},'stale'],
  ['review before verification',{review_after:'2026-10-06'},'review-order'],
  ['missing scope',{scope:''},'scope'],
  ['missing source support',{support:''},'support'],
  ['high-risk secondary source',{risk:'high',source_kind:'secondary'},'primary-required'],
  ['source with credentials',{source_url:'https://user:secret@example.test/rule'},'source-url'],
  ['source not effective yet',{valid_from:'2026-11-01'},'not-effective'],
  ['source effective period ended',{valid_until:'2026-10-01'},'expired'],
  ['static live value',{status:'serve_live'},'unverified'],
])test(`blocks ${name}`,()=>{const r=check(data(leaf(overrides)));assert.equal(r.ok,false);assert(r.errors.some(e=>e.code===code));});
test('unknown used keys and empty selections cannot pass',()=>{
  assert(check(data(),{usedKeys:['unknown.key']}).errors.some(e=>e.code==='unknown-key'));
  assert(check(data(),{usedKeys:[]}).errors.some(e=>e.code==='empty-selection'));
  assert.equal(check({_meta:{schema_version:4,project:'empty'}}).ok,false);
});
test('duplicate span aliases cannot select an arbitrary fact',()=>{const d=data();d.other={sample:leaf()};assert(check(d).errors.some(e=>e.code==='duplicate-key'));});
test('unused unresolved field does not block a selected verified fact',()=>{const d=data();d.other={sample:leaf({fact_key:'other.sample',status:'unverified',value:null})};assert.equal(check(d,{usedKeys:['transport.sample']}).ok,true);});
test('legacy shape parses but old confidence statuses cannot publish',()=>{const d=data(leaf({status:'verify_recommended'}));d._meta.schema_version=3;const r=check(d);assert(!r.ok);assert(r.warnings.some(w=>w.code==='legacy'));});
test('recommendations and private candidate records are not miscounted as verified facts',()=>{const d=data();d.recommendations={value:[{name:'A'}],rank:'candidate'};d.transport.sample._candidates=[{value:999,status:'verified'}];assert.equal(collectFacts(d).length,1);});
test('matching model values remain unverified with preserved provenance',()=>{const {data:d,report}=reconcile([source('a',leaf()),source('b',leaf())]);assert.equal(d.transport.sample.status,'unverified');assert.equal(d.transport.sample.source_url,null);assert.equal(d.transport.sample._candidates.length,2);assert.equal(report.counts.agreements,1);});
test('one supplied value plus a missing answer is not an agreement',()=>{const {data:d,report}=reconcile([source('a',leaf()),source('b',leaf({value:null}))]);assert.equal(d.transport.sample.status,'unverified');assert.equal(report.counts.agreements,0);assert.equal(report.counts.missing,1);});
test('disagreement does not average or choose a fact value',()=>{const {data:d,report}=reconcile([source('a',leaf({value:10})),source('b',leaf({value:20}))]);assert.equal(d.transport.sample.value,null);assert.equal(d.transport.sample.status,'disputed');assert.equal(report.counts.disputes,1);});
test('string case is not erased when it may carry meaning',()=>{const {data:d}=reconcile([source('a',leaf({value:'mW'})),source('b',leaf({value:'MW'}))]);assert.equal(d.transport.sample.status,'disputed');});
test('fields supplied only by a later researcher survive as unverified candidates',()=>{const a=source('a',leaf()),b=source('b',leaf());b.data.extra={new:leaf({fact_key:'extra.new',value:99})};const {data:d}=reconcile([a,b]);assert.equal(d.extra.new.value,99);assert.equal(d.extra.new.status,'unverified');assert.equal(d.extra.new._candidates[0].record,null);});
test('any live designation prevents freezing a value',()=>{const {data:d}=reconcile([source('a',leaf()),source('b',leaf({status:'serve_live'}))]);assert.equal(d.transport.sample.value,null);assert.equal(d.transport.sample.status,'serve_live');});
test('mismatched audience and duplicate named entities are rejected',()=>{
  const a=source('a',leaf()),b=source('b',leaf());b.data._meta.audience.nationality='Different';assert.throws(()=>reconcile([a,b]),/scope|audience/);
  a.data.cities=[{name:'A',facts:{x:leaf()}},{name:'A',facts:{x:leaf()}}];assert.throws(()=>reconcile([a]),/Duplicate entity/);
});
test('recommendation votes remain candidate provenance and differing reasons are preserved',()=>{
  const a=source('a',leaf()),b=source('b',leaf());a.data.recos={kind:'recommendation',rank:'core',value:[{name:'Hotel A',why:'reason one'}]};b.data.recos={kind:'recommendation',rank:'core',value:[{name:'Hotel A',why:'reason two'}]};
  const {data:d}=reconcile([a,b]);assert.equal(d.recos.rank,'candidate');assert.equal(d.recos.value[0]._variants.length,2);assert.equal(d.recos.value[0]._named_by.length,2);
});
test('CLI candidates do not overwrite canonical facts, including on malformed inputs',()=>withTemp(dir=>{
  mkdirSync(join(dir,'raw'));writeFileSync(join(dir,'facts.json'),'CANONICAL DO NOT CHANGE');writeFileSync(join(dir,'raw','a.json'),JSON.stringify(data()));
  let r=run('reconcile.mjs',[dir]);assert.equal(r.status,0,r.stderr);assert(existsSync(join(dir,'facts.candidates.json')));assert.equal(readFileSync(join(dir,'facts.json'),'utf8'),'CANONICAL DO NOT CHANGE');
  const candidate=readFileSync(join(dir,'facts.candidates.json'),'utf8');writeFileSync(join(dir,'raw','broken.json'),'{');r=run('reconcile.mjs',[dir]);assert.notEqual(r.status,0);assert.equal(readFileSync(join(dir,'facts.candidates.json'),'utf8'),candidate);
}));
test('facts CLI propagates invalid input and cannot overwrite its input with the report',()=>withTemp(dir=>{
  const path=join(dir,'facts.json');writeFileSync(path,JSON.stringify(data(leaf({support:''}))));let r=run('validate-facts.mjs',[path,'--as-of',asOf]);assert.notEqual(r.status,0);
  const before=readFileSync(path,'utf8');r=run('validate-facts.mjs',[path,'--output',path]);assert.notEqual(r.status,0);assert.equal(readFileSync(path,'utf8'),before);
}));
test('optional research prompt is source-first and rejects unsafe reviewer paths',()=>withTemp(dir=>{
  writeFileSync(join(dir,'project-meta.json'),JSON.stringify({project:'example',country:'Example',audience:{nationality:'Example',home_hubs:[],home_currency:'USD'},locale:{site_language:'en'}}));
  writeFileSync(join(dir,'article-list.json'),JSON.stringify([{title:'One clear question',slug:'one-question'}]));
  let r=run('make-prompts.mjs',[dir,'reviewer']);assert.equal(r.status,0,r.stderr);const prompt=readFileSync(join(dir,'prompts','prompt-reviewer.txt'),'utf8');assert(prompt.includes('Open suitable primary sources'));assert(prompt.includes('remains a candidate'));
  r=run('make-prompts.mjs',[dir,'../../escape']);assert.notEqual(r.status,0);
}));
