#!/usr/bin/env node
/** Explicit source extraction + checked rendering. Never uploads or publishes. */
import { readFileSync, mkdirSync } from 'node:fs';
import { join } from 'node:path';
import { compileLeadmagnet } from './leadmagnet-data.mjs';
import { renderLeadmagnet } from './build-leadmagnet.mjs';
import { isMain, options, readJSON, atomicWrite, distinctOutput, sha256 } from './runtime.mjs';
const HELP = `Usage: node scripts/build-leadmagnet-all.mjs EXPORT.json CONFIG.json OUTDIR [--chrome=/path] [--html-only]
Writes leadmagnet.json only after successful rendering. Normal mode produces leadmagnet.pdf,
leadmagnet.html and leadmagnet.pdf.checks.json. --html-only produces an HTML proof and no PDF.
No source guessing, browser installation, network content, upload or publication. Review every page.`;
export async function main(argv) {
  if (argv.includes('--help')) { console.log(HELP); return 0; }
  const args = options(argv, ['--chrome'], ['--html-only']);
  if (args.positional.length !== 3) throw new Error(HELP);
  const [exportPath, configPath, outDir] = args.positional;
  const manifest = join(outDir, 'leadmagnet.json'), pdf = join(outDir, 'leadmagnet.pdf');
  for (const output of [manifest, pdf, join(outDir, 'leadmagnet.html'), pdf + '.checks.json']) distinctOutput(output, [exportPath, configPath]);
  const d = compileLeadmagnet(readJSON(exportPath), readJSON(configPath), { exportSha256: sha256(readFileSync(exportPath)), configSha256: sha256(readFileSync(configPath)) });
  mkdirSync(outDir, { recursive: true });
  const result = await renderLeadmagnet(d, pdf, { chrome: args['--chrome'], htmlOnly: args['--html-only'] });
  atomicWrite(manifest, JSON.stringify(d, null, 2) + '\n');
  console.log(JSON.stringify({ manifest, ...result }, null, 2));
  return 0;
}
if (isMain(import.meta.url)) main(process.argv.slice(2)).then(code => { process.exitCode = code; }).catch(e => { console.error(`Lead-magnet pipeline failed: ${e.message}`); process.exitCode = 1; });
