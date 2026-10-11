# Gaussian-moat dependency patch audit

Date: 2026-10-12. This is a read-only comparison of the tracked changes in the eleven dependency worktrees that emitted local-change warnings during the bounded Lean endpoint run. The audit did not run Lean or alter the retained worktrees.

The source configuration was `openai/math` at `fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb`. Its Lake manifest SHA-256 was `cf6105a25d9dca2f166b241d9191bd12c7e13305890dc9c4d0952351cccc0794`. The comparison covered the configured `lean/patches/*-lean4341.patch` files for these eleven warning packages:

| Package | Tracked changed paths | Configured patch | Patch SHA-256 |
|---|---:|---|---|
| `belyi` | 15 | `belyi-lean4341.patch` | `f54c2e211464c0f8194ce63a80a6562489f23f688b1c233efe3c2debfc1b9f66` |
| `elliptic-curves` | 22 | `elliptic-curves-lean4341.patch` | `69e6575dae5797d43242694dc737b400b3e1e8fcb854094fead2a204a1f58632` |
| `formal-schemes` | 5 | `formal-schemes-lean4341.patch` | `5376716aa94fe0c6907570d650dd6604f170687c218cea7028d09b9f95877cea` |
| `genl` | 3 | `genl-lean4341.patch` | `3a9edd7dd539e98f81145a3b6cc980c9d62a821b7d41e2591f9aa5c557a7b6fa` |
| `heights` | 17 | `heights-lean4341.patch` | `bd3b58a301df273a199d9a0fe486b25d194df176afe32583289d42b64ab583a3` |
| `iut` | 29 | `iut-lean4341.patch` | `610ef069f7de5a5d500ead287287b60f193269ea4ddc0011101a9c7c98356dd4` |
| `oka` | 87 | `oka-lean4341.patch` | `02995b860e7d566a10adc3488439d38abc06dcb317ae4576d504c71c921816e7` |
| `orbicurve-cores` | 26 | `orbicurve-cores-lean4341.patch` | `4376110b9b7c823057cda21479a45de688c5138c81e5d4f1c050b632f168b93d` |
| `pi1` | 19 | `pi1-lean4341.patch` | `816e0d8123d5622c5b3415675638053ae31126a829e4f21d96f7af28db292f5f` |
| `tate-curves-theta` | 3 | `tate-curves-theta-lean4341.patch` | `885a19a0dc2d004aaece1987e2b7d2ff4745aef8881cbc53971a852cc5644c3f` |
| `tempered-fundamental-groups` | 6 | `tempered-fundamental-groups-lean4341.patch` | `f2e51b5f38459f11515c21801c92c39de85a8feb5f2b490ebbe07a93511a8860` |

For every package, `git apply --reverse --check <configured-patch>` succeeded. The full `git diff --binary` content also matched the configured patch after ignoring only Git's `index` metadata lines, whose blob hashes are abbreviated in the generated diff but written in full in the pinned patch. The changed tracked-path sets matched exactly. No standard untracked files were reported in these worktrees; ignored files and cache contents were outside this comparison.

**Meaning:** the eleven tracked source diffs responsible for the warnings are accounted for by the Lake-configured compatibility patches. This corrects the earlier statement that the tracked patch inventory was incomplete.

**Limit:** patch correspondence does not prove that cached `.olean` files were built from those exact sources, authenticate cache bytes, or establish a complete dependency proof audit. No numeric wrapper exit-status receipts or original wrapper stderr were recovered. Comparator-harness execution and independent clean reproduction remain open.
