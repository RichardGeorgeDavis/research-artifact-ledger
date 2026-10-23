#!/usr/bin/env python3
"""Reproduce stipulated examples only; no empirical or phenomenal validation."""
from itertools import permutations
from fractions import Fraction as F
points = {'a': (0,0,0), 'b': (1,0,0), 'c': (3,0,0),
          'n': (0,2,0), 'm': (0,-2,0), 'z': (0,1,3)}
def squared_distance(a,b):
    return sum((x-y)**2 for x,y in zip(points[a],points[b]))
placements = list(permutations(points,3))
metric=[]
ordinal=[]
for a,b,c in placements:
    d=(squared_distance(a,b),squared_distance(b,c),squared_distance(a,c))
    if d==(1,4,9): metric.append((a,b,c))
    if d[0]<d[1]<d[2]: ordinal.append((a,b,c))
assert len(placements)==120
assert metric==[('a','b','c')]
assert len(ordinal)==16
assert tuple(squared_distance('n',x) for x in 'abc')==(4,5,13)
assert tuple(squared_distance('m',x) for x in 'abc')==(4,5,13)
assert (squared_distance('n','z'),squared_distance('m','z'))==(10,18)
assert tuple(squared_distance(x,y) for x,y in [('b','a'),('a','n'),('b','n')])==(1,4,5)
def continuity(w): return w+(1-w)*F(9,10)
def reversal(w): return w+(1-w)*F(1,10)
assert continuity(F(1))==reversal(F(1))==1
assert (continuity(F(0)),continuity(F(1,10)))==(F(9,10),F(91,100))
assert (reversal(F(0)),reversal(F(1,10)))==(F(1,10),F(19,100))
print('Ordered injective placements: 120')
print('Exact metric placements: 1')
print('Ordinal placements: 16')
print('n/m squared-distance profiles to a,b,c: (4, 5, 13)')
print('Squared distances n-z, m-z: (10, 18)')
print('Continuity range: 0.90–0.91; reversal range: 0.10–0.19')
print('Stipulated mathematics only; no experiential or empirical validation.')
