"""Block the first commit of changed docs until they are trimmed."""

# The retry with the same doc set passes, so trimming never loops.
# Research briefs hold tradeoffs by design, so they are exempt.

import json
import os
import re
import subprocess
import sys
from pathlib import Path

COMMIT_COMMAND = re.compile(r"(?:^|[;&|(\n])\s*git\s+(?:-C\s+\S+\s+)?commit\b")
EXEMPT_PATHS = ("docs/research/",)
REMINDER = """**STOP.** Before this commit, reread these docs:
{paths}

Did you see or write any instances of the following?
- 'X, not Y'
- Justification
- Exhaustive examples or metaphors
- Other consideration
- Bonus effects
- Tradeoffs/alternatives
- 'Did X because Y'
- Stating the way a thing worked in the past
- 'Key findings'
- Edit date logging

**Cut them.** Cut whole clauses and entire sections. Cut both your own and pre-existing examples. Documentation should record exactly the way a project runs/should-run, and nothing else. Then commit again."""


def git(root: Path, *command: str) -> str:
    """Run a git command in the project and return its output."""
    return subprocess.run(["git", *command], cwd=root, capture_output=True, text=True, check=True).stdout


def changed_docs(root: Path) -> list[str]:
    """List changed or new Markdown files, staged or not."""
    entries = git(root, "status", "--porcelain=v1", "-z", "--no-renames", "--untracked-files=all").split("\0")
    docs = []
    for entry in entries:
        status, path = entry[:2], entry[3:]
        is_deleted = "D" in status
        if path.endswith(".md") and not is_deleted and not path.startswith(EXEMPT_PATHS):
            docs.append(path)
    return sorted(docs)


def main() -> None:
    """Block a commit once per set of changed docs."""
    command = json.load(sys.stdin)["tool_input"]["command"]
    if not COMMIT_COMMAND.search(command):
        return
    root = Path(os.environ.get("CLAUDE_PROJECT_DIR", "."))
    docs = changed_docs(root)
    if not docs:
        return
    marker = root / git(root, "rev-parse", "--git-path", "trim-docs-reminded").strip()
    document_set = "\n".join(docs)
    if marker.exists() and marker.read_text(encoding="utf-8") == document_set:
        marker.unlink()
        return
    marker.write_text(document_set, encoding="utf-8")
    print(REMINDER.format(paths="\n".join(f"- {path}" for path in docs)), file=sys.stderr)
    sys.exit(2)


if __name__ == "__main__":
    main()
