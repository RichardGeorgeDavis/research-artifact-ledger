# Source map — equal extension counts and subquery consistency

This map supports the bounded synthetic example in [`artifacts/sampler-subquery-consistency-toy/README.md`](../artifacts/sampler-subquery-consistency-toy/README.md). The construction and arithmetic are author-created; the cited papers supply the testing definitions and theorem context, not the toy sampler's stipulated behaviour.

## Primary sources

| Source | Pinned version | Relevant location | Claim supported | Limit |
|---|---|---|---|---|
| Kuldeep S. Meel, Yash Pote and Sourav Chakraborty, [“On Testing of Samplers”](https://proceedings.neurips.cc/paper/2020/file/3f1656d9668dffcf8119e3ecff873558-Paper.pdf) | NeurIPS 2020 proceedings PDF | Definition 5, p. 3; Definitions 8–9, p. 4; Algorithms 1–2, p. 6; Theorem 1, p. 7 | Multiplicative `ε`-closeness, formula-specific `ℓ₁` `η`-farness, subquery consistency and the distinct close-case ACCEPT and far-case REJECT hypotheses | Does not specify the synthetic `G` used in this artifact; this artifact does not audit the paper's full proof or implementation. |
| Meel, Pote and Chakraborty, [“On Testing of Samplers,” supplemental material](https://proceedings.neurips.cc/paper_files/paper/2020/file/3f1656d9668dffcf8119e3ecff873558-Supplemental.pdf) | NeurIPS 2020 supplemental PDF | Lemma 7, equation (9), printed p. 17 | Locates the conditional-law equality used in the bounded far-case proof mapping | No full independent proof audit is claimed. |
| Yash Pote and Kuldeep S. Meel, [“On Scalable Testing of Samplers”](https://proceedings.neurips.cc/paper_files/paper/2022/file/b3875605f2e35714fc8a807cadf8a5e8-Paper-Conference.pdf) | NeurIPS 2022 proceedings PDF | Distance definitions, §2, p. 2; oracle model, §2.1, p. 3; Theorem 1, p. 4 | Total-variation farness and the DUAL / PCOND+SAMP oracle model | No query complexity, runtime or empirical claim is tested here. |

## Author-created finite input

The toy formula, sampler probabilities and auxiliary disjunction are fully specified in the artifact README. The count `2^12−1=4,095`, the projected probability `1/2`, the original conditional probability `5/6`, the `ℓ₁` distance `3/4` and the total-variation distance `3/8` are exact consequences of that construction. They are not quoted experimental results.

## Review

An independent AI reviewer checked the construction arithmetic and source-to-claim boundaries on 2026-11-19 using the primary sources above. No human review, external implementation run, proof-assistant check or priority search is claimed.
