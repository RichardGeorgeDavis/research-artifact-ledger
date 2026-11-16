# Sources for the FLAM3 fixed-seed final-opacity example

| Source | Version and role |
| --- | --- |
| [Scott Draves and Erik Reckase, *The Fractal Flame Algorithm*](https://flam3.com/flame_draves.pdf) | §3.2 describes the final transform and keeps final display coordinates outside recurrence. Author-hosted PDF, inspected 16 November 2026. |
| [FLAM3 upstream](https://github.com/scottdraves/flam3/tree/1cdfc77275821182ad3c057e629c75a240dd52d3) | Pinned implementation. `flam3.c` SHA-256 `60e62e32344f35b4fc8a3d71fc5c342c86325e02bc7b5cdd368b144c8ce11b33`. |
| [FLAM3 iteration and table](https://github.com/scottdraves/flam3/blob/1cdfc77275821182ad3c057e629c75a240dd52d3/flam3.c#L164-L299) | Table construction, transform selection, retry, final gate and sample emission. |
| [ISAAC context](https://github.com/scottdraves/flam3/blob/1cdfc77275821182ad3c057e629c75a240dd52d3/isaac.h#L19-L52) and [implementation](https://github.com/scottdraves/flam3/blob/1cdfc77275821182ad3c057e629c75a240dd52d3/isaac.c) | Bob Jenkins’s generator, in the pinned FLAM3 version. The context holds a 16-word buffer plus generator state. |
| [C witness](../reproduce/flam3_fixed_seed_witness.c) | Original test fixture with AI assistance. SHA-256 `634679a131cadd9612b95d4124cb7e953464fc7859708465fec8afda64463aa0`. |

Upstream FLAM3 terms and notices remain in the [pinned source tree](https://github.com/scottdraves/flam3/blob/1cdfc77275821182ad3c057e629c75a240dd52d3/COPYING). The ledger contains the original runner, test fixture and explanatory text. The runner fetches the dependency for local use. Upstream code, compiled binaries and paper copies are absent from the release payload. No separate reuse licence is assigned to this ledger entry.
