# AI Skills and Agents Samples

A **skill** is a Markdown file that teaches an AI coding assistant how to approach a specific kind of task — the same way a checklist or a runbook teaches a new hire — instead of you re-typing the same detailed instructions into a prompt every time. This repository is a learning collection of such skills, written once and reused across Codex, Claude Code, and GitHub Copilot CLI without changes.

## Quick start

```bash
git clone https://github.com/khadir-syed/ai-agent-skills.git && cd ai-agent-skills
./install.sh root-cause-investigator
```

Then, in Codex, Claude Code, or Copilot CLI, try the first prompt from [Try the samples](skills/README.md#try-the-samples) in the Skills doc.

## Contents

- [About this collection](#about-this-collection)
- [Skills (Stage 1)](skills/README.md) — how a skill works, the full skill table, sample runs, try-it-yourself prompts, negative tests
- [Agents (Stage 2)](agents/README.md) — the four agents, controlled vs. autonomous, sample runs, negative tests
- [Use a skill or agent in an AI coding tool](#use-a-skill-in-an-ai-coding-tool)
- [Troubleshooting](#troubleshooting)
- [What these samples do not provide](#what-these-samples-do-not-provide)
- [Customise them](#customise-them)
- [Official documentation](#official-documentation)

## About this collection

The collection is being developed progressively:

1. Skills
2. Agents
3. Orchestrators and multiple agents

**Stage 1 (Skills)** is organised as a grid: the same three shapes — read-only, write-capable, and multi-step chain — applied across a growing set of domains, so the pattern is proven by repetition rather than a single example. See [skills/README.md](skills/README.md) for the full breakdown.

| Domain | Status |
|---|---|
| Tech / Software | Done — 3 skills |
| Product | Done — 3 skills |
| Content | Done — 3 skills |
| Social Media | Done — 3 skills |

**Stage 2 (Agents)** ships the same real-world job twice per domain — once with a human approving every step ("controlled"), once with fewer checkpoints ("autonomous") — so you can compare what changes when a human leaves the loop. See [agents/README.md](agents/README.md) for all four agents, how they're tested, and what a real negative (bypass-attempt) test found.

| Domain | Status |
|---|---|
| Tech / Software | Done — 2 agents (1 controlled, 1 autonomous) |
| Product | Done — 2 agents (1 controlled, 1 autonomous) |

More skills, agents, and domains are welcome through contributions (see [CONTRIBUTING.md](CONTRIBUTING.md)). Stage 3 (orchestration) has not started.

## Use a skill in an AI coding tool

Copy the complete skill directory, including its supporting files, into a skill location recognised by your tool — either by hand, or with `install.sh` (see below).

| Tool | Project location | Personal location | Example invocation |
|---|---|---|---|
| Codex | `.agents/skills/<skill-name>/` | `~/.agents/skills/<skill-name>/` | `$<skill-name> investigate why the customer list is empty` |
| Claude Code | `.claude/skills/<skill-name>/` | `~/.claude/skills/<skill-name>/` | `/<skill-name> investigate why the customer list is empty` |
| GitHub Copilot CLI | `.github/skills/<skill-name>/`, `.agents/skills/<skill-name>/`, or `.claude/skills/<skill-name>/` | `~/.copilot/skills/<skill-name>/` or `~/.agents/skills/<skill-name>/` | `/<skill-name> investigate why the customer list is empty` |

Restart or reload the relevant tool if it does not detect a newly copied skill. Invocation syntax and discovery behaviour can change between product versions, so consult the current product documentation when adopting the sample.

### CLI apps vs. desktop apps

The table above covers the **CLI tools** (Codex CLI, Claude Code CLI/IDE, Copilot CLI) and the standalone **Codex desktop app** — all of them read a skill directly from a project folder, so copying the folder (by hand or with `install.sh`) is enough.

The **Claude desktop/web app is different**: it does not read a project folder at all. It keeps a separate, global skill list that you populate by uploading a ZIP:

1. **Settings → Capabilities** → enable "Code execution and file creation" (a skill will not run without this).
2. **Customize → Skills** → **+** → **Create skill** → **Upload a skill**.
3. Select a ZIP of the skill folder with `SKILL.md` at the ZIP's root — not nested inside another folder, which is the most common upload failure.
4. Toggle the skill **on** after uploading — uploaded is not the same as enabled.

This upload flow works for any Markdown-only skill or agent in this repo.
It does **not** work for [test-fix-loop-agent](agents/software/test-fix-loop-agent/) —
that one is a Python script, not a Markdown instruction file, and neither
Claude Desktop nor Claude web can execute it. That agent is CLI-only; see its
own [README](agents/software/test-fix-loop-agent/README.md).

### Using the install script

`install.sh` is repo tooling, not part of any skill — the skills themselves stay Markdown-only; this script just automates the copy step above. It copies a skill into whichever tool directories already exist on disk. It does not detect which tools are installed beyond that, make network calls, or delete anything.

```bash
./install.sh root-cause-investigator
```

Copies into project-level directories only (`.agents/skills/`, `.claude/skills/`, `.github/skills/`) — whichever already exist in the current project. Pass `--global` to also copy into the personal (home) directories:

```bash
./install.sh --global changelog-entry-drafter
```

## Troubleshooting

Real friction encountered while building and testing this repo — not hypothetical.

**A skill doesn't show up in the slash-command / `@`-mention menu.**
Skills are discovered at session start, not live. Restart or reload the tool after copying a new skill in. Also confirm you copied the *whole* folder (`SKILL.md` plus `examples/` and `references/`), not just the `SKILL.md` file on its own.

**A skill doesn't trigger from a plain-language prompt, only when named explicitly.**
That's the tool's own matching against the skill's frontmatter `description` falling short, not a broken skill. Try invoking it explicitly first (`/skill-name` or `@skill-name`) to confirm discovery works at all, then tighten the `description` to name the situations it should catch.

**`install.sh` printed "Nothing copied."**
It only copies into tool directories that already exist (`.agents/`, `.claude/`, `.github/`) in your current project — it won't create them from scratch. Create one yourself first (e.g. `mkdir .claude`) or pass `--global` to target your home directory instead.

**Claude Desktop doesn't see a skill that works fine in Claude Code.**
Expected — they use two different mechanisms. Claude Code reads a project folder's `.claude/skills/` directly; Claude Desktop needs the skill uploaded as a ZIP through Settings, with Code execution enabled (see [CLI apps vs. desktop apps](#cli-apps-vs-desktop-apps) above).

**A write-capable skill wrote a file without asking again on a later run.**
Check whether an earlier prompt granted session-scoped approval without you noticing (e.g. "yes, and don't ask me again"). If you never granted that, treat it as a bug in the skill's approval wording — it should default to asking every single time, not assume standing permission from one "yes."

**GitHub shows a different commit author name/email than what's in your local git config.**
If the commit's email matches a verified email on a GitHub account (this includes `@users.noreply.github.com` addresses), GitHub displays that account's username and avatar instead of the raw name string stored in the commit. This is standard GitHub behaviour, not a caching bug or a sign the push failed — `git log` on the actual commit will still show whatever name you configured.

## What these samples do not provide

- They do not guarantee that an AI tool will select a skill automatically.
- They do not provide access to files, terminals, logs, databases, or external services.
- They do not override the tool's permission model or the user's instructions.
- They do not make a diagnosis, draft, or check correct merely because the response follows the expected format.
- They are learning samples, not a production incident-response, release, or security-control system.

## Customise them

Fork or copy a sample and change one concern at a time:

1. Refine the frontmatter description for the problems that should trigger it.
2. Add domain-specific paths to trace, such as browser to API to database.
3. Add evidence sources available in your environment.
4. Adjust the report template without weakening evidence and uncertainty requirements.
5. Test it with a known defect and at least one prompt that should not activate it.

Keep permissions separate from instructions. Declaring that a skill is read-only describes intended behaviour; the host tool's sandbox and approval controls remain the actual enforcement boundary.

## Official documentation

- [OpenAI: Build skills for ChatGPT and Codex](https://learn.chatgpt.com/docs/build-skills)
- [Anthropic: Extend Claude with skills](https://code.claude.com/docs/en/slash-commands)
- [GitHub: Add agent skills for GitHub Copilot CLI](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-skills)
