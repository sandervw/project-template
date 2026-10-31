---
name: handoff
description: Current project state, next work, parked questions, and gotchas. Use at the start of every session, and update it when the state or next work changes.
---

# Handoff

Current state and next work. Rewrite this file (`.claude/skills/handoff/SKILL.md`) when stale; never log history.

## State

- Created from the project template. Nothing decided yet.

## Next

1. Run `/kickoff`.

## Parked

Questions that can wait until after the MVP.

## Gotchas

- `gh pr merge` is blocked by `.claude/hooks/require_reviews.py` until the review PASS comments name the head commit. Re-review after every push.
- An unquoted `: ` in an agent `description` breaks loading. Agent, skill, and hook changes need a session restart.
- The blackbox-tester can run only what `.claude/project.json` allows; until kickoff fills it, it can only read and write specs. Escape backslashes in its `safeFlags` regexes as `\\`.
