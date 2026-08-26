# CLAUDE.md

Each subfolder in this repository contain a different set of code standards/rule, used in my various websites and user-interfaces.

To run Obsidian with remote debugging: `Start-Process -FilePath "C:\Program Files\Obsidian\Obsidian.exe" -ArgumentList "--remote-debugging-port=9222"`

## Obsidian Retro folder

Any edit to files in `retro/Obsidian Retro/` must be copied to `C:\Users\Sander\Documents\Github\Notes\.obsidian\themes\Obsidian Retro`. A hook handles most edits automatically, but not all of them; after editing, verify the copy landed and copy it manually if the hook did not catch it.

Do NOT use symlinks (or junctions/hardlinks) to keep these in sync. It breaks Obsidian.