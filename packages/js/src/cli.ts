#!/usr/bin/env node
/**
 * glitch-badges CLI
 *
 * Usage:
 *   npx glitch-badges custom "POST QUANTUM" --accent "#a78bfa" --tag "Security" --width 260
 *   npx glitch-badges list
 *   npx glitch-badges url repo security-pq --wide
 */
import { writeFileSync, mkdirSync } from "node:fs";
import { resolve, dirname } from "node:path";
import { makeBadge, badgeUrl } from "./core.js";
import { ALL_PRESETS, getPreset } from "./presets.js";

const args = process.argv.slice(2);

function printHelp(): void {
  console.log(`
glitch-badges — VRIL LABS animated glitch badge generator

USAGE
  npx glitch-badges <command> [options]

COMMANDS
  custom <VALUE>          Generate a one-off custom badge
    --tag     <TAG>       Left-side label           (default: none)
    --accent  <HEX>       Accent colour             (default: #1fe8a8)
    --width   <PX>        Badge width               (default: 220)
    --height  <PX>        Badge height              (default: 36)
    --out     <PATH>      Output .svg path          (default: <VALUE>.svg)

  url <collection> <slug> [--wide]
                          Print the raw CDN URL for a pre-built badge

  list [collection]       List all available badge slugs

  help                    Show this message

EXAMPLES
  npx glitch-badges custom "POST QUANTUM" --accent "#a78bfa" --tag "Security"
  npx glitch-badges url repo security-pq --wide
  npx glitch-badges list repo
`.trim());
}

function parseFlags(argv: string[]): Record<string, string | boolean> {
  const flags: Record<string, string | boolean> = {};
  for (let i = 0; i < argv.length; i++) {
    const a = argv[i];
    if (a.startsWith("--")) {
      const key = a.slice(2);
      const next = argv[i + 1];
      if (next && !next.startsWith("--")) {
        flags[key] = next;
        i++;
      } else {
        flags[key] = true;
      }
    }
  }
  return flags;
}

const cmd = args[0];

if (!cmd || cmd === "help" || cmd === "--help" || cmd === "-h") {
  printHelp();
  process.exit(0);
}

if (cmd === "list") {
  const col = args[1];
  const presets = col
    ? ALL_PRESETS.filter(p => p.collection === col)
    : ALL_PRESETS;
  if (presets.length === 0) {
    console.error(`Unknown collection: ${col}`);
    process.exit(1);
  }
  for (const p of presets) {
    const tag = p.tag ? `[${p.tag}]` : "        ";
    console.log(`  ${p.collection.padEnd(8)}  ${p.slug.padEnd(28)} ${tag} ${p.text}`);
  }
  process.exit(0);
}

if (cmd === "url") {
  const collection = args[1] as "social" | "comms" | "repo" | "status";
  const slug = args[2];
  const flags = parseFlags(args.slice(3));
  if (!collection || !slug) {
    console.error("Usage: glitch-badges url <collection> <slug> [--wide]");
    process.exit(1);
  }
  const preset = getPreset(slug);
  const col = preset?.collection ?? collection;
  console.log(badgeUrl(col, slug, !!flags["wide"]));
  process.exit(0);
}

if (cmd === "custom") {
  const value = args[1];
  if (!value) {
    console.error("Usage: glitch-badges custom <VALUE> [options]");
    process.exit(1);
  }
  const flags  = parseFlags(args.slice(2));
  const tag    = typeof flags["tag"]    === "string" ? flags["tag"]    : undefined;
  const accent = typeof flags["accent"] === "string" ? flags["accent"] : "#1fe8a8";
  const width  = typeof flags["width"]  === "string" ? parseInt(flags["width"], 10)  : 220;
  const height = typeof flags["height"] === "string" ? parseInt(flags["height"], 10) : 36;
  const outArg = typeof flags["out"]    === "string" ? flags["out"]    : undefined;
  const out    = outArg ?? `${value.toLowerCase().replace(/\s+/g, "-")}.svg`;

  const svg = makeBadge({ text: value, tag, accent, width, height });
  const dest = resolve(out);
  mkdirSync(dirname(dest), { recursive: true });
  writeFileSync(dest, svg, "utf8");
  console.log(`✓  ${dest}`);
  process.exit(0);
}

console.error(`Unknown command: ${cmd}\nRun 'glitch-badges help' for usage.`);
process.exit(1);
