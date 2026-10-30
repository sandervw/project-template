---
name: kickoff
description: Run the idea and planning session with the CEO, question by question, turning an idea into a vision, decided stack, architecture, use cases, project tooling, and a backlog. Use when the CEO runs /kickoff on a project made from this template.
disable-model-invocation: true
---

# Kickoff: idea and planning session

Goal: leave this session with every MVP-blocking question decided and written into the current docs, so `/implement-issue` can start with no further questions. Write no application code.

Two kinds of writing, kept apart:

- **Tradeoffs** go in `docs/research/<topic>.md`, one brief per decision, from the `researcher` agent.
- **Decisions** go straight into the current docs (`CLAUDE.md`, `docs/vision.md`, `docs/architecture.md`, `docs/glossary.md`, `docs/use-cases/`). No decision log, no ADRs, no dates, no "was X before".

## 1. The idea

1. Ask the CEO to describe the idea in their own words. Restate it in three sentences and ask what you got wrong.
2. Draft `docs/vision.md` with them: what it is, who it is for, MVP success, principles, non-goals.

## 2. Map the parts

Break the idea into parts the product needs, with no technology yet: for example the interface a user touches, the core domain logic, storage, an API, firmware, a model, a pipeline, deploy. Show the list and ask the CEO to add, cut, or merge.

## 3. Decide, one question at a time

Work through [agenda.md](agenda.md), part by part. For each question:

1. If it needs fresh facts, send `researcher` agents first, in parallel across independent questions, each with one topic and a 15 to 30 minute time box.
2. Give a three-sentence summary of the options and your recommendation, with an analogy if the tradeoff is abstract. Point to the brief.
3. Ask one question with `AskUserQuestion`: two to four options, recommended first and marked "(Recommended)", each option's description naming its main tradeoff.
4. When the CEO answers, restate the decision in one line and write it into the doc that owns it. If the answer raises a new question, ask it next.
5. Never decide a CEO item yourself: scope, pricing, brand, legal, anything that costs money or needs their identity.

Keep momentum. A question that can wait until after the MVP goes to "Parked" in `docs/handoff.md` with the reason.

## 4. Produce the plan

1. `architect` writes `docs/architecture.md` and `docs/glossary.md` from the decisions: contexts, context map, shells, interfaces, layout, security.
2. `product-manager` writes `docs/use-cases/` from the vision. Use cases describe only what the actor does and observes through the black-box surface decided in the agenda.
3. Review both against the decisions yourself; fix contradictions before showing the CEO.
4. Show the CEO a short summary of each, and the full use cases. Get a yes or the changes they want.

## 5. Fit the tooling to the decisions

1. **`CLAUDE.md`**: fill every `[bracketed]` placeholder: project name, one-line description, stack, commands, agents, and the paths the security review covers.
2. **Engineer agents**: one per major part, from [engineer-template.md](engineer-template.md), in `.claude/agents/`.
3. **`.claude/project.json`**: the black-box test and start commands, safe flags, allowed tools and hosts; the code suffixes and security paths for the merge gate.
4. **`blackbox-tester`**: add the tester's browser, device, or API tools to its `tools` line.
5. **simple-code**: a language pack for any language the checker lacks (see the skill's "Language packs").
6. **Boundary check**: the import-boundary tool the architect chose, with its config and a command.
7. **`.claude/settings.json`**: allow the project's routine commands, deny reading its secret files, ask before deploys and remote deletes. Add MCP servers to `.mcp.json` and plugins as decided.
8. **CI and dependabot**: add the build, test, and boundary steps to `.github/workflows/ci.yml`, pinning every action to a commit SHA; add the package ecosystems to `.github/dependabot.yml`.
9. **Housekeeping**: the build output and tool folders in `.gitignore`; `README.md` rewritten for this project; issue templates worded for its users.
10. **CEO to-do**: every account, login, key, or payment only the CEO can set up goes in `docs/ceo-todo.md`.

## 6. Build the backlog

Only after the CEO approves the plan:

1. `product-manager` drafts issues. The first is "Scaffold the project": the chosen stack, an empty app that builds, the black-box harness running one trivial spec, the boundary check, and CI green. The rest are vertical slices in build order, each naming the use cases it makes pass. Prefer fewer, larger issues.
2. Show the CEO the titles. On a yes, create labels (`mvp`, `bug`, `enhancement`, `question`) with `gh label create --force`, then the issues with `gh issue create`, labeled `mvp`.

## 7. Close

1. Rewrite `docs/handoff.md`: state, next work, parked questions.
2. Report: what was decided (by doc), what's parked, the backlog, and the CEO's to-do list.
3. Commit on a branch named `kickoff`, open a PR, and suggest the next step: `/implement-issue <scaffold issue number>`.
