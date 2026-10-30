# Project template

A starting point for any project built with code: a web app, embedded firmware, a machine-learning pipeline, a CLI, anything. It fixes how the work is done, not what it is built with. Languages, frameworks, services, and folder layout are decided per project in a planning session.

## Start a project

```bash
gh repo create <name> --template sandervw/project-template --private --clone
```

Then open the new folder in Claude Code and run `/kickoff`. The CTO agent walks you through the idea and every decision, one question at a time, with researched options and tradeoffs, then fills in the docs, tooling, and backlog. After kickoff, `/implement-issue <number>` takes an issue to a merged PR.

Needs Python 3.10 or newer (hooks and checks), the GitHub CLI, and Claude Code. `python -m pip install ruff` for Python projects.

## What every project gets

- **Always a repo, always agent-built.** You are the CEO; a CTO agent plans, builds, reviews, and merges through PRs. `CLAUDE.md` is its manual; `/handoff` its running notes.
- **Domain-driven design.** A pure functional core split into bounded contexts, adapter shells with no business rules, a glossary, and a machine-checked boundary rule.
- **Simple code.** Seven practices and hard house rules (comments of 12 words or fewer, full-word names, files under 300 lines, docs under 700 words), checked on every edit and in CI.
- **Black-box testing first.** A tester agent that cannot see the code writes specs from user-side use cases. Integration tests come second; unit tests only where nothing else can observe.
- **Three reviewers.** Simplicity, architecture, and security, with a hook that blocks merging until they pass on the latest commit.
- **Current docs, no history.** Docs describe the design as it is now; tradeoffs live in research briefs; git holds the past.

## What kickoff decides

The stack, the parts, the black-box surface and its harness, storage, services, environments, deploys, CI steps, engineer agents, MCP servers, and language packs for the checker.

## Layout

```
CLAUDE.md                     CTO manual (placeholders filled at kickoff)
.claude/
  project.json                black-box and merge-gate settings for the hooks
  settings.json               permissions and hooks
  agents/                     product-manager, architect, researcher, blackbox-tester, three reviewers
  hooks/                      merge gate, black-box tester isolation
  skills/kickoff/             planning session, question agenda, engineer agent template
  skills/implement-issue/     issue to merged PR
  skills/handoff/             current state and next work, loaded with /handoff
  skills/simple-code/         rules, examples, checker, Python and TypeScript packs
docs/
  vision.md  glossary.md  architecture.md  ceo-todo.md
  use-cases/                  black-box test script
  research/                   tradeoff briefs
.github/                      CI, issue and PR templates, dependabot
```
