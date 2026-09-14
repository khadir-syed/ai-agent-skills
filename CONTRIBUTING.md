# Contributing

Thanks for your interest in contributing. This repository collects learning
samples for AI skills that work generically across tools such as Codex,
Claude Code, and GitHub Copilot CLI. Contributions should keep that goal in
mind: instruction-only, tool-agnostic, and safe to run without special setup.

## Before you open a pull request

- Read [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) — participation in this
  project means agreeing to it.
- Search existing issues and pull requests to avoid duplicating work.
- For a change larger than a typo or wording fix, open an issue first to
  discuss the approach before writing it up.

## Adding a new skill

Skills are grouped by domain under `skills/<domain>/<skill-name>/`, but each skill is still installed and invoked by its own name alone — `install.sh` and every host tool look it up without needing the domain in the command. Current domains: `software`, `product`, plus `content` and `socialmedia` (planned — see their placeholder `README.md` files under `skills/`). A new domain is welcome; open an issue first to agree on the name and its three planned skills before submitting one skill in isolation.

```text
skills/<domain>/<skill-name>/
├── SKILL.md
├── examples/
│   └── <synthetic-example>.md
└── references/
    └── <output-format-or-template>.md
```

Within each domain, aim for the same three shapes the existing domains use — one read-only investigator, one write-capable drafter (approval-gated), and one multi-step readiness checklist — rather than three skills of the same shape. That variety is what proves the pattern generalises, not just the domain.

A new skill should:

1. **Have a clear, scoped `description` in the frontmatter.** State when the
   skill should trigger and, ideally, one thing it should *not* be used for
   — this is what lets a host tool select the right skill among several.
2. **Declare its operating boundary explicitly.** Say plainly what the skill
   will and will not do (read-only vs. write-capable, what it may touch,
   what needs explicit user approval). Do not rely on the host tool's
   permissions to cover for an underspecified skill.
3. **Distinguish evidence from assumption.** Skills in this repo label
   claims as observed, reported, inferred, or unknown (or an equivalent
   scheme suited to the skill, e.g. stated/reported/inferred/unknown for
   product and content skills) rather than presenting guesses as fact.
4. **Include at least one synthetic example** under `examples/` that a
   reader can follow without a real application, product, or piece of
   content — show a sample input, the expected reasoning or output shape,
   and at least one *deliberately weak* response that should fail the
   learning objective.
5. **Contain no scripts, dependencies, credentials, or secrets.** Skills in
   this repo are Markdown instructions only. Repo-level tooling (like
   `install.sh`) is kept separate from the skills themselves.
6. **Add the skill to the README** — the skills table, the repository
   structure tree, and the "Try the samples" section.

## Improving an existing skill

- Keep changes scoped to one concern per pull request (wording, a new
  check, a tightened boundary) rather than mixing several unrelated
  changes.
- Do not weaken the evidence-labelling or approval-gating language in a
  skill to make it "more convenient" — the safety posture is a deliberate
  part of the sample, not an oversight.
- Update the matching `examples/` and `references/` files if the workflow
  changes shape.

## Testing your change

There is no build step. "Testing" a skill means:

1. Installing it into a real tool (see the README's install table, or run
   `./install.sh <skill-name>`).
2. Running the prompts in its `examples/` file and confirming the response
   matches the expected shape.
3. Running at least one prompt that should **not** trigger the skill, and
   confirming it doesn't.

## Pull request checklist

- [ ] Frontmatter `description` is scoped and states what the skill is not
      for, if relevant.
- [ ] Operating boundary and any approval requirements are explicit.
- [ ] At least one synthetic example is included, with a deliberately weak
      response documented.
- [ ] No secrets, credentials, or real proprietary data anywhere in the
      change.
- [ ] README updated if a skill was added, renamed, or removed.

## Reporting a security issue

If you find a security concern (not a general bug), please open an issue
and describe it — this repository is a learning sample with no runtime
service or user data, so most reports can be handled in the open, but flag
anything sensitive so it can be triaged appropriately.
