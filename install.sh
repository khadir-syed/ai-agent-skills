#!/usr/bin/env bash
# Copy a skill from this repo's skills/ folder into whichever tool
# directories already exist. Project-level dirs by default; pass --global
# to also copy into the personal (home) directories. Pure copy: no tool
# detection beyond "does this directory already exist", no network calls,
# no deletions. Repo tooling only — the skills themselves stay Markdown-only.
set -euo pipefail

usage() {
  echo "Usage: $0 [--global] <skill-name>" >&2
  echo "  <skill-name> must be a directory under skills/" >&2
  exit 1
}

global=false
skill=""
for arg in "$@"; do
  case "$arg" in
    --global) global=true ;;
    -h|--help) usage ;;
    *) skill="$arg" ;;
  esac
done

[ -n "$skill" ] || usage
case "$skill" in
  */*|*..*) echo "Invalid skill name: $skill" >&2; exit 1 ;;
esac

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
src="$script_dir/skills/$skill"

[ -d "$src" ] || { echo "No such skill: skills/$skill" >&2; exit 1; }

project_targets=(".agents/skills" ".claude/skills" ".github/skills")
global_targets=("$HOME/.agents/skills" "$HOME/.claude/skills" "$HOME/.copilot/skills")

targets=("${project_targets[@]}")
$global && targets+=("${global_targets[@]}")

copied=false
for dir in "${targets[@]}"; do
  parent="$(dirname "$dir")"
  [ -d "$parent" ] || continue
  mkdir -p "$dir"
  cp -R "$src" "$dir/"
  echo "Copied $skill -> $dir/$skill"
  copied=true
done

$copied || echo "No matching tool directories found. Nothing copied."
