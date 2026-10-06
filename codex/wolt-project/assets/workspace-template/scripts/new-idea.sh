#!/usr/bin/env bash
set -euo pipefail

if [[ $# -lt 1 || $# -gt 2 || ( $# -eq 2 && "$2" != "--skip-search" ) ]]; then
  printf 'Usage: %s "idea-name" [--skip-search]\n' "$0" >&2
  exit 64
fi

raw_name=$1
slug=$(printf '%s' "$raw_name" \
  | tr '[:upper:]' '[:lower:]' \
  | sed -E 's/[[:space:]]+/-/g; s/[^[:alnum:]_-]+/-/g; s/-+/-/g; s/^[-_]+//; s/[-_]+$//')

if [[ -z "$slug" ]]; then
  printf 'Idea name must contain at least one letter or number.\n' >&2
  exit 64
fi

script_dir=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
project_dir=$(cd "$script_dir/.." && pwd)
template_file="$project_dir/templates/idea.md"
idea_root="$project_dir/ideas"
idea_inbox="$idea_root/inbox"
index_template="$project_dir/templates/idea-index.md"
date_prefix=$(date +%F)
base_name="$date_prefix-$slug"
target_file="$idea_inbox/$base_name.md"
counter=2

while [[ -e "$target_file" ]]; do
  suffix=$(printf '%02d' "$counter")
  target_file="$idea_inbox/$base_name-$suffix.md"
  counter=$((counter + 1))
done

mkdir -p "$idea_root/inbox" "$idea_root/active" "$idea_root/archive"

if [[ ! -e "$idea_root/INDEX.md" ]]; then
  cp "$index_template" "$idea_root/INDEX.md"
fi

if [[ "${2:-}" != "--skip-search" && -x "$project_dir/scripts/find-similar-ideas.py" ]]; then
  "$project_dir/scripts/find-similar-ideas.py" "$raw_name" --limit 5 || true
fi

cp "$template_file" "$target_file"

python3 - "$target_file" "$raw_name" "$date_prefix" "$slug" <<'PY'
from pathlib import Path
import sys

path = Path(sys.argv[1])
title, created, slug = sys.argv[2:]
text = path.read_text(encoding="utf-8")
replacements = {
    "- Idea ID: IDEA-YYYYMMDD-slug": f"- Idea ID: IDEA-{created.replace('-', '')}-{slug}",
    "- Title: TBD": f"- Title: {title}",
    "- Created: TBD": f"- Created: {created}",
    "- Updated: TBD": f"- Updated: {created}",
}
for old, new in replacements.items():
    text = text.replace(old, new, 1)
path.write_text(text, encoding="utf-8")
PY

if [[ -x "$project_dir/scripts/rebuild-idea-index.py" ]]; then
  "$project_dir/scripts/rebuild-idea-index.py" --write >/dev/null
fi

printf 'Created: %s\n' "$target_file"
printf 'Next: preserve the raw idea, fill its fingerprint, then rebuild the local index.\n'
