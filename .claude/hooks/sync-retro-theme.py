"""PostToolUse hook: mirror the Obsidian Retro theme into the Notes vault.

Reads the hook JSON on stdin. If the edited/written file lives under the
source theme folder, copies the whole theme folder over to the vault's
themes directory (plain file copy, no symlink; Obsidian dislikes symlinks).
Exits 0 no matter what so it never blocks a tool call.
"""
import sys, json, os, shutil

SRC = r"C:\Users\Sander\Documents\Github\sander-standards\retro\Obsidian Retro"
DST = r"C:\Users\Sander\Documents\Github\Notes\.obsidian\themes\Obsidian Retro"


def norm(p):
    return os.path.normcase(os.path.abspath(str(p).replace("\\", "/")))


def main():
    try:
        data = json.load(sys.stdin)
    except Exception:
        return
    ti = data.get("tool_input") or {}
    tr = data.get("tool_response") or {}
    fp = ti.get("file_path") or tr.get("filePath")
    if not fp:
        return

    src = norm(SRC)
    target = norm(fp)
    if not (target == src or target.startswith(src + os.sep)):
        return  # change was not inside the theme folder

    os.makedirs(DST, exist_ok=True)
    shutil.copytree(SRC, DST, dirs_exist_ok=True)


if __name__ == "__main__":
    main()
