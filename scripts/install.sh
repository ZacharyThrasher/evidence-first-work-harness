#!/usr/bin/env sh
set -eu
force=0
[ "${1:-}" = "--force" ] && force=1
SCRIPT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
REPO_ROOT=$(dirname "$SCRIPT_DIR")
SOURCE="$REPO_ROOT/.claude/skills/efwh"
CONFIG_ROOT=${CLAUDE_CONFIG_DIR:-"$HOME/.claude"}
case "$CONFIG_ROOT" in
  '~/'*) CONFIG_ROOT="$HOME/${CONFIG_ROOT#~/}" ;;
esac
SKILLS_ROOT="$CONFIG_ROOT/skills"
DEST="$SKILLS_ROOT/efwh"
[ -f "$SOURCE/SKILL.md" ] || { echo "EFWH source not found at $SOURCE" >&2; exit 1; }
if [ -e "$DEST" ]; then
  if [ "$force" -ne 1 ]; then
    echo "EFWH is already installed at $DEST. Re-run with --force to replace it." >&2
    exit 1
  fi
  stamp=$(date +%Y%m%d-%H%M%S)
  backup="$DEST.backup-$stamp"
  mv "$DEST" "$backup"
  echo "Backed up existing EFWH -> $backup"
fi
mkdir -p "$SKILLS_ROOT"
cp -R "$SOURCE" "$DEST"
echo "Installed EFWH 2.2.0 -> $DEST"
echo "Start Claude Code in any workspace and run: /efwh <your problem>"
