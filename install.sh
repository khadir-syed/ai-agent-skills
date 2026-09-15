#!/usr/bin/env bash
# Copy a skill from this repo's skills/ folder into whichever tool
# directories already exist. Project-level dirs by default; pass --global
# to also copy into the personal (home) directories. Pure copy: no tool
# detection beyond "does this directory already exist", no network calls,
# no deletions. Repo tooling only — the skills themselves stay Markdown-only.
set -euo pipefail

usage() {
  echo "Usage: $0 [--global] <skill-name>" >&2
  echo "  <skill-name> must be a skill folder under skills/<domain>/ or agents/<domain>/" >&2
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

matches=()
for f in "$script_dir"/skills/*/"$skill" "$script_dir"/agents/*/"$skill"; do
  [ -f "$f/SKILL.md" ] && matches+=("$f")
done

case "${#matches[@]}" in
  0) echo "No such skill: $skill (looked under skills/*/$skill and agents/*/$skill)" >&2; exit 1 ;;
  1) src="${matches[0]}" ;;
  *) echo "Ambiguous skill name '$skill' found in multiple domains:" >&2
     printf '  %s\n' "${matches[@]}" >&2
     exit 1 ;;
esac

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
