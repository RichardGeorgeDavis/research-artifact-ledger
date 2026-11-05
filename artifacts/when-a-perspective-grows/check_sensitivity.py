#!/usr/bin/env python3
"""Exact checks of stipulated sensitivity bounds; no empirical calibration."""
from fractions import Fraction as F
from itertools import product

# Separately affine formulas attain extrema at vertices of each parameter box.
def ranges(lo, hi, u, category=None):
    cs = (F(0), F(1)) if category is None else (category,)
    cases = list(product((lo, hi), (F(0), u), cs))
    continuity = [(1-w)*a+w*c for a,w,c in cases]
    reversal = [(1-w)*(1-a)+w*c for a,w,c in cases]
    return (min(continuity), max(continuity)), (min(reversal), max(reversal))

fixed_checks = 0
for ai in range(11, 21):
    a = F(ai,20)
    for ui in range(21):
        u = F(ui,20)
        C,R = ranges(a,a,u,F(1))
        assert C == (a,a+u*(1-a))
        assert R == (1-a,1-a+u*a)
        assert (C[0]>R[1]) == (a>1/(2-u))
        fixed_checks += 1

uncertain_checks = 0
for li in range(10,21):
    for hi in range(li,21):
        l,h = F(li,20),F(hi,20)
        for ui in range(21):
            u = F(ui,20)
            C,R = ranges(l,h,u,F(1))
            assert C == (l,h+u*(1-h))
            assert R == (1-h,1-l+u*l)
            assert (C[0]>R[1]) == (l>1/(2-u))
            uncertain_checks += 1
assert ranges(F(4,5),F(19,20),F(1,10),F(1)) == ((F(4,5),F(191,200)),(F(1,20),F(7,25)))

relaxed_checks = 0
for li in range(11,21):
    l=F(li,20)
    for ui in range(20):
        u=F(ui,20)
        C,R = ranges(l,F(1),u)
        assert C[0] == (1-u)*l
        assert R[1] == 1-l+u*l
        assert (C[0]>R[1]) == (l>1/(2*(1-u)))
        if u>=F(1,2): assert C[0]<=R[1]
        relaxed_checks += 1
    assert ranges(l,F(1),F(1)) == ((F(0),F(1)),(F(0),F(1)))
assert ranges(F(9,10),F(1),F(1,10))[0][0] == F(81,100)
assert ranges(F(9,10),F(1),F(1,10))[1][1] == F(19,100)
assert F(1)/(2-F(1,10)) == F(10,19)
# Threshold equality is contact, not strict separation.
C,R=ranges(F(10,19),F(10,19),F(1,10),F(1)); assert C[0]==R[1]
C,R=ranges(F(5,9),F(1),F(1,10)); assert C[0]==R[1]
print(f'Fixed-accuracy cases: {fixed_checks}')
print(f'Bounded-accuracy cases: {uncertain_checks}')
print(f'Relaxed-category cases: {relaxed_checks}; w upper bound 1 checked separately')
print('Baseline thresholds, endpoint extrema and touching cases passed.')
print('Stipulated mathematics only; no experiential or empirical validation.')
