#!/usr/bin/env bash
set -euo pipefail

if [[ $# -ne 1 ]]; then
  printf 'Usage: %s "project-name"\n' "$0" >&2
  exit 64
fi

raw_name=$1
slug=$(printf '%s' "$raw_name" \
  | tr '[:upper:]' '[:lower:]' \
  | sed -E 's/[[:space:]]+/-/g; s/[^[:alnum:]_-]+/-/g; s/-+/-/g; s/^[-_]+//; s/[-_]+$//')

if [[ -z "$slug" ]]; then
  printf 'Project name must contain at least one letter or number.\n' >&2
  exit 64
fi

script_dir=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
project_dir=$(cd "$script_dir/.." && pwd)
template_dir="$project_dir/templates/project"
project_root="$project_dir/projects"
date_prefix=$(date +%F)
base_name="$date_prefix-$slug"
target_dir="$project_root/$base_name"
counter=2

while [[ -e "$target_dir" ]]; do
  suffix=$(printf '%02d' "$counter")
  target_dir="$project_root/$base_name-$suffix"
  counter=$((counter + 1))
done

mkdir -p "$project_root"
cp -R "$template_dir" "$target_dir"

printf 'Created: %s\n' "$target_dir"
printf 'Next: link the matching ideas/*.md record, fill 00-idea.md and place idea-specific references in assets/.\n'
