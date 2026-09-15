#!/usr/bin/env sh
set -eu
SCRIPT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
REPO_ROOT=$(dirname "$SCRIPT_DIR")
SOURCE="$REPO_ROOT/.claude/skills/efwh"
CONFIG_ROOT=${CLAUDE_CONFIG_DIR:-"$HOME/.claude"}
case "$CONFIG_ROOT" in '~/'*) CONFIG_ROOT="$HOME/${CONFIG_ROOT#~/}" ;; esac
SKILLS_ROOT="$CONFIG_ROOT/skills"
DEST="$SKILLS_ROOT/efwh"
[ -f "$SOURCE/SKILL.md" ] || { echo "EFWH source not found at $SOURCE" >&2; exit 1; }
if [ -e "$DEST" ]; then
  if diff -qr "$SOURCE" "$DEST" >/dev/null 2>&1; then
    echo "EFWH 2.3.0 is already installed and verified at $DEST"
    exit 0
  fi
  stamp=$(date +%Y%m%d-%H%M%S)
  backup="$DEST.backup-$stamp"
  mv "$DEST" "$backup"
  echo "Backed up existing EFWH -> $backup"
fi
mkdir -p "$SKILLS_ROOT"
cp -R "$SOURCE" "$DEST"
diff -qr "$SOURCE" "$DEST" >/dev/null 2>&1 || { echo "EFWH verification failed after copy." >&2; exit 1; }
echo "Installed and verified EFWH 2.3.0 -> $DEST"
echo "Start Claude Code anywhere and run: /efwh <your problem>"
