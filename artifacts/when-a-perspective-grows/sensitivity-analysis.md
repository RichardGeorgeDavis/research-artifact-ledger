# When a Perspective Grows: Supporting Sensitivity Analysis

Supporting analysis for Richard George Davis’s final author release v2.6, *When a Perspective Grows: Experience, learning and the warrant for comparison*. 5 November 2026. Public supporting material; not an empirical validation.

## Question and model

This note asks how strongly the conditional example in §6.1 depends on its stipulated numerical assumptions. It states the model and derivations independently so it can be read without the manuscript or the review log. Its subject is separation between predicted response probabilities, not a completed experiment or evidence that learning actually changes experience.

Imagine a reference colour patch r and alternatives x and y. Before learning, x appears more similar to r than y does. Two accounts compete after learning: continuity preserves that appearance ordering; reversal makes y appear closer to r. The observer chooses either x or y. On a proportion w of trials a category route supplies the response; on the other trials an appearance route chooses the appearance-consistent option with probability a. The two routes are exhaustive in this model. The further task is assumed not to reverse the target ordering, and its accuracy and route bounds require justification independently of simply fitting the target choices to the preferred account.

In the manuscript’s baseline, the category route always chooses x, a=0.9 and 0≤w≤0.1. Continuity therefore predicts an x-choice probability of w+(1−w)×0.9, between 0.90 and 0.91; reversal predicts w+(1−w)×0.1, between 0.10 and 0.19. With w=1 both predict x every time. These are stipulated model predictions. They do not themselves establish the appearance ordering, the accuracy or the category-route probability.

| Symbol | Meaning |
|---|---|
| p_C, p_R | Probability of selecting x under continuity and reversal respectively |
| a | Appearance-route accuracy, a probability no greater than 1 |
| w | Probability that the category route supplies the response |
| u | Justified upper bound on w, between 0 and 1 |
| l, h | Lower and upper bounds on a |
| c | Category route’s probability of selecting x when always-x categorisation is relaxed |

The bounds below are composite prediction ranges: each competing account may use any admissible values of its nuisance parameters. Non-overlap is a robust separation of these model classes. Overlap leaves at least some response probabilities compatible with both; it does not show that every possible observation is uninformative.

## Sensitivity derivations

This is an algebraic generalisation of the existing two-route example, developed with AI assistance and checked in a separate model review. It is not claimed as novel mathematics, an empirical finding or a validated measurement method. The analysis retains the two competing orderings, binary x/y response, appearance route and category route specified above. Appearance accuracy is the probability of selecting the appearance-consistent answer; category weight is the probability of using the category route. These are model probabilities, not measured values in this task.

First retain always-x category responding. If appearance accuracy is `a>1/2` and category weight `w∈[0,u]`, where `0≤u≤1`, then continuity predicts `p_C=a+w(1−a)` and reversal predicts `p_R=1−a+wa`. The composite prediction intervals are `[a,a+u(1−a)]` and `[1−a,1−a+ua]`. They are strictly separated exactly when `a>1−a+ua`, equivalently `a>1/(2−u)`. Equality means touching, not separation. At `u=0.1`, the threshold is `10/19≈0.5263`. This demonstrates that the illustrative accuracy need not be exactly 0.9; it does not show that any actual task reaches the necessary accuracy.

If accuracy is itself only bounded by `1/2≤l≤a≤h≤1`, permitting each competing account to use any admissible value, the composite intervals become `[l,h+u(1−h)]` and `[1−h,1−l+ul]`. Separation is equivalent to `l>1/(2−u)`. With `l=.80,h=.95,u=.10`, the intervals are `[.80,.955]` and `[.05,.28]`. They are ranges of model predictions, not confidence intervals for observed data.

Next relax always-x categorisation entirely. Let its x-choice probability be `c∈[0,1]`, with `w∈[0,u]` and `a∈[l,1]`, `l>1/2`. Then `p_C=(1−w)a+wc` and `p_R=(1−w)(1−a)+wc`. Across all admissible nuisance parameters, continuity has minimum `(1−u)l` and reversal has maximum `1−l+ul`. For `u<1`, their composite intervals are strictly separated exactly when `l>1/[2(1−u)]`. No permitted `l≤1` can give strict separation when `u≥1/2`. At `l=.9,u=.1`, continuity predicts at least `.81` and reversal at most `.19`. Thus even an entirely unspecified category response can leave the accounts separable under sufficiently strong route/accuracy bounds.

Derivation check: each expression is affine in each parameter separately, so extrema over the parameter boxes occur at endpoints; subtracting the competing bounds yields the conditions above. Exact-fraction computation reproduced the uncertain-accuracy example and checked the relaxed-category extrema and strict-separation equivalence at 200 `(l,u)` pairs. These finite checks complement the algebra; they do not validate the behavioural interpretation, independence of calibration evidence, transfer across tasks, exhaustiveness of the two routes, or finite-sample identification. Observed response proportions still require an appropriate uncertainty analysis before deciding between accounts.

The substantive gain is diagnostic: the criticism is not that the numerical conclusion exists only at one hand-picked parameter pair. The open problem is earning sufficiently informative bounds and defending the model/target interpretation. The stricter threshold under unknown category responding also shows the price of relaxing an assumption. The calculation supplements the manuscript’s conditional example without replacing its empirical obligations.
