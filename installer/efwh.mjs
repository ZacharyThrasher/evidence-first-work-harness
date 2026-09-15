#!/usr/bin/env node
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import crypto from 'node:crypto';
import { fileURLToPath } from 'node:url';

const here = path.dirname(fileURLToPath(import.meta.url));
const root = path.resolve(here, '..');
const source = path.join(root, '.claude', 'skills', 'efwh');
const version = fs.readFileSync(path.join(root, 'VERSION'), 'utf8').trim();

function ansi(code, text) {
  return process.stdout.isTTY && !process.env.NO_COLOR ? `\x1b[${code}m${text}\x1b[0m` : text;
}
const bold = (s) => ansi('1', s);
const dim = (s) => ansi('2', s);
const green = (s) => ansi('32', s);
const cyan = (s) => ansi('36', s);

function expandHome(p) {
  if (!p) return p;
  if (p === '~') return os.homedir();
  if (p.startsWith('~/') || p.startsWith('~\\')) return path.join(os.homedir(), p.slice(2));
  return p;
}

function configRoot() {
  const configured = process.env.CLAUDE_CONFIG_DIR?.trim();
  return path.resolve(expandHome(configured || path.join(os.homedir(), '.claude')));
}

function destination() {
  return path.join(configRoot(), 'skills', 'efwh');
}

function listFiles(dir, base = dir) {
  const out = [];
  for (const entry of fs.readdirSync(dir, { withFileTypes: true }).sort((a, b) => a.name.localeCompare(b.name))) {
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) out.push(...listFiles(full, base));
    else if (entry.isFile()) out.push(path.relative(base, full).replaceAll('\\', '/'));
  }
  return out;
}

function hashTree(dir) {
  const h = crypto.createHash('sha256');
  for (const rel of listFiles(dir)) {
    h.update(rel); h.update('\0');
    h.update(fs.readFileSync(path.join(dir, ...rel.split('/')))); h.update('\0');
  }
  return h.digest('hex');
}

function copyTree(src, dst) {
  fs.mkdirSync(dst, { recursive: true });
  for (const entry of fs.readdirSync(src, { withFileTypes: true })) {
    const s = path.join(src, entry.name);
    const d = path.join(dst, entry.name);
    if (entry.isDirectory()) copyTree(s, d);
    else if (entry.isFile()) fs.copyFileSync(s, d);
  }
}

function stamp() {
  const d = new Date();
  const p = (n) => String(n).padStart(2, '0');
  return `${d.getFullYear()}${p(d.getMonth()+1)}${p(d.getDate())}-${p(d.getHours())}${p(d.getMinutes())}${p(d.getSeconds())}`;
}

function installedVersion(dest) {
  try {
    const text = fs.readFileSync(path.join(dest, 'SKILL.md'), 'utf8');
    return text.match(/^\s*version:\s*["']?([^"'\r\n]+)["']?/m)?.[1]?.trim() || 'unknown';
  } catch { return 'unknown'; }
}

function verifySource() {
  if (!fs.existsSync(path.join(source, 'SKILL.md'))) throw new Error(`Bundled EFWH payload is incomplete: ${source}`);
}

function header() {
  console.log();
  console.log(bold('EFWH'));
  console.log(dim('Evidence-First Work Harness'));
  console.log();
}

function install() {
  verifySource();
  const dest = destination();
  const skillsRoot = path.dirname(dest);
  const sourceHash = hashTree(source);

  header();
  console.log(`${dim('Target')}  ${dest}`);
  console.log(`${dim('Version')} ${version}`);

  if (fs.existsSync(dest)) {
    const currentHash = hashTree(dest);
    if (currentHash === sourceHash) {
      console.log();
      console.log(green('✓ EFWH is already installed and verified.'));
      console.log(dim(`  /efwh <what you're trying to solve>`));
      console.log();
      return;
    }
    const backup = `${dest}.backup-${stamp()}`;
    fs.renameSync(dest, backup);
    console.log(`${green('✓')} Backed up existing EFWH ${dim(`(${installedVersion(backup)})`)}`);
    console.log(`  ${dim(backup)}`);
  }

  fs.mkdirSync(skillsRoot, { recursive: true });
  copyTree(source, dest);

  const installedHash = hashTree(dest);
  if (installedHash !== sourceHash) throw new Error('Installation verification failed: copied Skill does not match bundled payload.');

  console.log(`${green('✓')} Installed EFWH ${version}`);
  console.log(`${green('✓')} Verified ${listFiles(dest).length} files`);
  console.log();
  console.log(bold('Ready.'));
  console.log(`Start Claude Code anywhere and type:`);
  console.log(cyan(`  /efwh <what you're trying to solve>`));
  console.log();
  console.log(dim('If this was the first personal Skill ever added during an already-running Claude session, restart that session once.'));
  console.log();
}

function status() {
  verifySource();
  const dest = destination();
  header();
  console.log(`${dim('Target')}  ${dest}`);
  if (!fs.existsSync(dest)) {
    console.log(`${dim('Status')}  not installed`);
    console.log();
    process.exitCode = 1;
    return;
  }
  const iv = installedVersion(dest);
  const match = hashTree(dest) === hashTree(source);
  console.log(`${dim('Status')}  ${match ? green('installed · verified') : ansi('33', 'installed · differs from this package')}`);
  console.log(`${dim('Version')} ${iv}`);
  console.log(`${dim('Package')} ${version}`);
  console.log();
}

function uninstall(args) {
  const dest = destination();
  header();
  if (!fs.existsSync(dest)) {
    console.log('EFWH is not installed at personal scope.');
    console.log();
    return;
  }
  if (args.includes('--purge')) {
    fs.rmSync(dest, { recursive: true, force: true });
    console.log(`${green('✓')} Removed EFWH`);
  } else {
    const backup = `${dest}.uninstalled-${stamp()}`;
    fs.renameSync(dest, backup);
    console.log(`${green('✓')} EFWH is no longer active.`);
    console.log(`  Recovery copy: ${backup}`);
    console.log(dim('  Use --purge if you explicitly want deletion instead.'));
  }
  console.log();
}

function help() {
  header();
  console.log('Usage:');
  console.log('  npx --yes @zacharythrasher/efwh install      Install or safely update the personal Claude Code Skill');
  console.log('  npx --yes @zacharythrasher/efwh update       Alias for install');
  console.log('  npx --yes @zacharythrasher/efwh status       Verify the current personal installation');
  console.log('  npx --yes @zacharythrasher/efwh uninstall    Disable EFWH and keep a recovery copy');
  console.log('  npx --yes @zacharythrasher/efwh uninstall --purge');
  console.log();
  console.log(dim('No Git checkout is used. The npm package contains the complete Skill payload.'));
  console.log();
}

try {
  const [cmd = 'help', ...args] = process.argv.slice(2);
  if (cmd === 'install' || cmd === 'update') install();
  else if (cmd === 'status') status();
  else if (cmd === 'uninstall') uninstall(args);
  else if (cmd === 'help' || cmd === '--help' || cmd === '-h') help();
  else throw new Error(`Unknown command: ${cmd}`);
} catch (err) {
  console.error();
  console.error(ansi('31', `EFWH installer failed: ${err?.message || err}`));
  console.error();
  process.exitCode = 1;
}
