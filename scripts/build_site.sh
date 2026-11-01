#!/usr/bin/env bash
set -euo pipefail

repo_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
source_dir="$(realpath "${2:-$repo_dir}")"
output_dir="${1:-$repo_dir/_site}"
mkdir -p "$output_dir"
output_dir="$(realpath "$output_dir")"
if [[ "$source_dir" == "$output_dir" ]]; then
  echo 'Source and output directories must differ.' >&2
  exit 1
fi

# Official GitHub Pages build image; its digest fixes Ruby/Jekyll/plugin versions.
# No network access is needed while rendering the site.
env -u DOCKER_HOST -u DOCKER_CONTEXT -u DOCKER_TLS \
  -u DOCKER_TLS_VERIFY -u DOCKER_CERT_PATH \
  docker --host=unix:///var/run/docker.sock run --rm --network none \
  --user "$(id -u):$(id -g)" \
  --mount "type=bind,src=$source_dir,dst=/work/source,readonly" \
  --mount "type=bind,src=$output_dir,dst=/work/site" \
  -e GITHUB_WORKSPACE=/work -e INPUT_SOURCE=source -e INPUT_DESTINATION=site \
  -e GITHUB_REPOSITORY=carbonsoul/iLang-Gospel -e GITHUB_API_URL=https://api.github.com \
  -e INPUT_VERBOSE=false \
  ghcr.io/actions/jekyll-build-pages@sha256:6791ebfd912185ed59bfb5fb102664fa872496b79f87ff8b9cfba292a7345041
