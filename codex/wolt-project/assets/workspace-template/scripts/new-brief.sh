#!/usr/bin/env bash
set -euo pipefail

if [[ $# -ne 1 ]]; then
  printf 'Usage: %s "brief-name"\n' "$0" >&2
  exit 64
fi

raw_name=$1
slug=$(printf '%s' "$raw_name" \
  | tr '[:upper:]' '[:lower:]' \
  | sed -E 's/[[:space:]]+/-/g; s/[^[:alnum:]_-]+/-/g; s/-+/-/g; s/^[-_]+//; s/[-_]+$//')

if [[ -z "$slug" ]]; then
  printf 'Brief name must contain at least one letter or number.\n' >&2
  exit 64
fi

script_dir=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
project_dir=$(cd "$script_dir/.." && pwd)
template_dir="$project_dir/templates/brief"
brief_root="$project_dir/briefs"
date_prefix=$(date +%F)
base_name="$date_prefix-$slug"
target_dir="$brief_root/$base_name"
counter=2

while [[ -e "$target_dir" ]]; do
  suffix=$(printf '%02d' "$counter")
  target_dir="$brief_root/$base_name-$suffix"
  counter=$((counter + 1))
done

mkdir -p "$brief_root"
cp -R "$template_dir" "$target_dir"

printf 'Created: %s\n' "$target_dir"
printf 'Next: place immutable client originals in source/ and fill 00-brief-intake.md.\n'
