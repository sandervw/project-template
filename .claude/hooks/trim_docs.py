"""Block the first commit of changed docs until they are trimmed."""

# The retry with the same document set passes, so trimming never loops.

import json
import os
import re
import subprocess
import sys
from pathlib import Path

COMMIT_COMMAND = re.compile(r"(?:^|[;&|(\n])\s*git\s+(?:-C\s+\S+\s+)?commit\b")
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

**Cut them, except security warnings.** Cut whole clauses and entire sections. Cut both your own and pre-existing examples. Documentation should record exactly the way a project runs/should-run, and nothing else. Then commit again."""


def git(root: Path, *command: str) -> str:
    """Run a git command in the project and return its output."""
    return subprocess.run(["git", *command], cwd=root, capture_output=True, text=True, check=True).stdout


def changed_documents(root: Path) -> list[str]:
    """List changed or new Markdown files, staged or not."""
    entries = git(root, "status", "--porcelain=v1", "-z", "--no-renames", "--untracked-files=all").split("\0")
    documents = []
    for entry in entries:
        status, path = entry[:2], entry[3:]
        is_markdown = path.endswith(".md")
        is_deleted = "D" in status
        if is_markdown and not is_deleted:
            documents.append(path)
    return sorted(documents)


def main() -> None:
    """Block a commit once per set of changed documents."""
    command = json.load(sys.stdin)["tool_input"]["command"]
    if not COMMIT_COMMAND.search(command):
        return
    root = Path(os.environ.get("CLAUDE_PROJECT_DIR", "."))
    documents = changed_documents(root)
    if not documents:
        return
    marker = root / git(root, "rev-parse", "--git-path", "trim-docs-reminded").strip()
    document_set = "\n".join(documents)
    reminded_set = marker.read_text(encoding="utf-8") if marker.exists() else None
    if reminded_set == document_set:
        marker.unlink()
        return
    marker.write_text(document_set, encoding="utf-8")
    print(REMINDER.format(paths="\n".join(f"- {path}" for path in documents)), file=sys.stderr)
    sys.exit(2)


if __name__ == "__main__":
    main()
