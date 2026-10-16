#!/bin/sh
set -eu
repo_root=$(git rev-parse --show-toplevel)
script_dir="$repo_root/reproduce/bft-first-event-census"
data_dir=$(mktemp -d)
trap 'rm -rf "$data_dir"' EXIT HUP INT TERM
cp "$repo_root/artifacts/bft-first-event-census/evidence/freeze.json" "$data_dir/freeze.json"
python3 - "$repo_root" "$data_dir" <<'PY'
from pathlib import Path
import bz2, sys
root=Path(sys.argv[1]); dest=Path(sys.argv[2])
for name in ('forecasts.jsonl','labels.jsonl','scores.jsonl'):
    source=root/'artifacts/bft-first-event-census/evidence'/(name+'.bz2')
    (dest/name).write_bytes(bz2.decompress(source.read_bytes()))
PY
python3 "$script_dir/bft_census_verifier.py" --data-dir "$data_dir" --manifest "$script_dir/manifest.json"
python3 "$script_dir/check_first_survivor_equivalence.py" "$data_dir/forecasts.jsonl"
