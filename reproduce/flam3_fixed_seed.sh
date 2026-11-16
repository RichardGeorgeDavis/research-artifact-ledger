#!/bin/sh
set -eu

artifact_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
upstream_revision=1cdfc77275821182ad3c057e629c75a240dd52d3
scratch=$(mktemp -d)
trap 'rm -rf "$scratch"' EXIT
trap 'exit 1' HUP INT TERM

git init -q "$scratch/source"
git -C "$scratch/source" fetch -q --depth=1 https://github.com/scottdraves/flam3.git "$upstream_revision"
git -C "$scratch/source" checkout -q --detach FETCH_HEAD
test "$(git -C "$scratch/source" rev-parse HEAD)" = "$upstream_revision"
source_hash=$(shasum -a 256 "$scratch/source/flam3.c" | cut -d ' ' -f 1)
test "$source_hash" = 60e62e32344f35b4fc8a3d71fc5c342c86325e02bc7b5cdd368b144c8ce11b33

{
    printf '#include "variations.h"\n'
    sed -n '70,71p;164,224p;232,300p;2519,2525p;2541,2544p' "$scratch/source/flam3.c"
} > "$scratch/functions.c"

sdk=$(xcrun --show-sdk-path)
cc -I "$scratch/source" -I "$sdk/usr/include/libxml2" -std=gnu11 -O0 \
    -ffunction-sections -Wl,-dead_strip "$scratch/functions.c" \
    "$artifact_dir/flam3_fixed_seed_witness.c" "$scratch/source/variations.c" \
    "$scratch/source/isaac.c" -o "$scratch/witness"

actual=$("$scratch/witness")
expected='seed=1 bins=10893,662,16292 output_x=2,1 vs 2,2 counters=14,12'
printf '%s\n' "$actual"
test "$actual" = "$expected"
