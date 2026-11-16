# A zero-opacity FLAM3 setting changes a fixed-seed trajectory

**Evidence** — Reproduced implementation counterexample at one upstream commit. Independent AI source challenge and arithmetic cross-check. Version 0.1.0, 16 November 2026.

## What changed

An enabled final transform at zero opacity can change which recurrent transform FLAM3 selects next, even though the final transform is never applied. In a two-sample test from identical ISAAC contexts, the recorded x-coordinates were **2, 1** with the final transform disabled and **2, 2** with it enabled at zero opacity. Both runs returned zero bad points.

This matters for seeded comparisons in fractal rendering. A change intended to affect only display can make a test compare different underlying trajectories.

## How it happens

Two equally weighted linear transforms produce x=1 and x=2 respectively. The pinned table builder assigns bins 0–8191 to the first and 8192–16383 to the second. Each recurrent selection uses the low 14 bits of one ISAAC word. The first three selection masks from the starting context are 10893, 662 and 16292.

| Configuration | First selection | What happens to the second word | Second selection |
| --- | --- | --- | --- |
| Final disabled | Bin 10893, x=2 | Used for recurrent selection | Bin 662, x=1 |
| Final enabled, opacity 0 | Bin 10893, x=2 | Consumed by the opacity comparison, which rejects the final transform | Bin 16292, x=2 |

The opacity gate compares a non-negative random value with opacity using strict less-than. Zero opacity therefore rejects every final application, while advancing the same random context used for selection. The final transform reads the current recurrent vector and writes to a separate output vector on paths where it runs. That separation of vectors leaves the shared generator state as a route to later recurrence. [Wrapper and table](https://github.com/scottdraves/flam3/blob/1cdfc77275821182ad3c057e629c75a240dd52d3/flam3.c#L164-L299), [Opacity helper](https://github.com/scottdraves/flam3/blob/1cdfc77275821182ad3c057e629c75a240dd52d3/flam3.c#L2519-L2525), [Transform implementation](https://github.com/scottdraves/flam3/blob/1cdfc77275821182ad3c057e629c75a240dd52d3/variations.c#L2129-L2184)

## Reproduce

Run this from the ledger root on arm64 macOS with Git and the Xcode command-line toolchain and SDK available. The verified compiler was Apple Clang 21. The script fetches the exact upstream revision into a temporary directory, checks the wrapper hash, compiles the selected upstream functions and executes the two-sample fixture. No renderer image is generated.

```sh
sh reproduce/flam3_fixed_seed.sh
```

```text
seed=1 bins=10893,662,16292 output_x=2,1 vs 2,2 counters=14,12
```

[Runner](../../reproduce/flam3_fixed_seed.sh) · [C fixture](../../reproduce/flam3_fixed_seed_witness.c) · [Source manifest](../../sources/flam3-fixed-seed-final-opacity.md)

## Attribution and limits

Artifact by Richard George Davis with AI assistance. FLAM3 and its method are the work of Scott Draves, Erik Reckase and contributors. Bob Jenkins developed ISAAC. Section 3.2 of *The Fractal Flame Algorithm* already separates the displayed final coordinates from the recurrent coordinates. This artifact isolates a specific shared-random-state effect in the pinned C implementation. It establishes path dependence at a fixed seed. Equality in law across a specified seed ensemble, image-level effects, other builds and field-level novelty remain unassessed. [Draves and Reckase, §3.2](https://flam3.com/flame_draves.pdf)

The independent AI source challenge used a separately transcribed ISAAC trace and different settings. With zero seed words and an identity final transform, opacity 1 skips the gate draw while opacity 0.25 consumes it and rejects the transform. Under the equal-weight lookup the next selection differs. This was a separate source and arithmetic check. The published C run was repeated in the same macOS environment. Human specialist and peer review have not occurred.

Version 0.1.0 records the initial example. Report reproducibility issues or corrections via the [ledger issue tracker](https://github.com/RichardGeorgeDavis/research-artifact-ledger/issues).
