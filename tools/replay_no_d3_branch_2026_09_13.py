from fractions import Fraction
from itertools import combinations
from math import gcd, lcm

BASE = 5040


def sieve(n):
    mark = bytearray(b"\x01") * (n + 1)
    mark[:2] = b"\x00\x00"
    for p in range(2, int(n**0.5) + 1):
        if mark[p]:
            mark[p*p:n+1:p] = b"\x00" * (((n - p*p)//p) + 1)
    return [i for i in range(2, n + 1) if mark[i]]


PRIMES = sieve(400000)


def factor_gcd_exp(N):
    G = gcd(pow(2, N) - 1, pow(3, N) - 1)
    r = G
    factors = {}
    for p in PRIMES:
        while r % p == 0:
            factors[p] = factors.get(p, 0) + 1
            r //= p
        if r == 1:
            break
    assert r == 1, (N, r)
    return factors


def factor_small(n):
    out = {}
    for p in PRIMES:
        if p*p > n:
            break
        while n % p == 0:
            out[p] = out.get(p, 0) + 1
            n //= p
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def order(a, p):
    r = p - 1
    for q in factor_small(p - 1):
        while r % q == 0 and pow(a, r//q, p) == 1:
            r //= q
    return r


def subgroup_size(p, gens):
    seen = {1}
    stack = [1]
    while stack:
        x = stack.pop()
        for g in gens:
            y = x * g % p
            if y not in seen:
                seen.add(y)
                stack.append(y)
    return len(seen)


def fibre_row(p):
    o2 = order(2, p)
    o3 = order(3, p)
    n = lcm(o2, o3)
    d = n // gcd(n, BASE)
    A = pow(2, BASE, p)
    B = pow(3, BASE, p)
    assert subgroup_size(p, [A, B]) == d
    h193 = subgroup_size(p, [A*A % p, B])
    h201 = subgroup_size(p, [A*B % p, B*B % p])
    return (p, n, d, h193, h201, o2, o3)


d6_rows = {p: fibre_row(p) for p in (8641, 12097)}
assert d6_rows[8641][1:5] == (4320, 6, 3, 6)
assert d6_rows[12097][1:5] == (6048, 6, 3, 6)

TH193 = Fraction(1117, 36960)
TH201 = Fraction(899, 22176)
LOCAL = Fraction(10, 11)

# p20161 anchor, no d3: one d6 contributes 1/6.
assert LOCAL - Fraction(1,6) == Fraction(49,66)
assert 2*Fraction(1,4) + Fraction(1,5) == Fraction(7,10) < Fraction(49,66)
d4_mass = Fraction(1,448) + Fraction(1,576) + Fraction(1,1344)
max_201_single_d6 = Fraction(1,4320) + d4_mass
assert max_201_single_d6 == Fraction(299,60480)
assert max_201_single_d6 < TH201

# Two d6 on p20161 die locally.
assert LOCAL - 2*Fraction(1,6) == Fraction(19,33)
assert 2*Fraction(1,4) < Fraction(19,33)

# p193, single d6: each remaining tail must contribute at least 5/66.
assert LOCAL - Fraction(1,3) - 2*Fraction(1,4) == Fraction(5,66)
candidate_ds = [4,5,7,8,9,10,11,12,13,14,16,18,20,22,24,26]

rows = {}
for d in candidate_ds:
    factors = factor_gcd_exp(d * BASE)
    for p in factors:
        if p <= 3:
            continue
        row = fibre_row(p)
        if row[2] == d:
            rows[p] = row

excluded = {23,47,193,20161,8641,12097}
candidates = []
for p,row in rows.items():
    _,n,d,h193,h201,_,_ = row
    rho = Fraction(1,h193)
    if p not in excluded and rho >= Fraction(5,66):
        candidates.append((p,n,d,rho))
candidates.sort()


def single_d6_survivors(n6):
    need_mass = TH193 - Fraction(1,n6)
    need_local = LOCAL - Fraction(1,3)
    out = []
    for tri in combinations(candidates,3):
        local = sum((x[3] for x in tri), Fraction())
        if local < need_local:
            continue
        mass = sum((Fraction(1,x[1]) for x in tri), Fraction())
        if mass < need_mass:
            continue
        out.append((tri, local, mass))
    return out


s8641 = single_d6_survivors(4320)
s12097 = single_d6_survivors(6048)
assert len(s8641) == 1
assert tuple(x[0] for x in s8641[0][0]) == (101,151,601)
assert s8641[0][1] == Fraction(3,5)
assert s8641[0][2] == Fraction(3,100)
assert len(s12097) == 0

candidate_total = Fraction(1,4320) + Fraction(3,100)
assert candidate_total == Fraction(653,21600)
assert candidate_total - TH193 == Fraction(1,103950)

# Geometry kill for {8641,601,101,151}: C11 × C3 × 5-primary independence.
uncovered_single = Fraction(10,11) * Fraction(2,3) * Fraction(2,5)
assert uncovered_single == Fraction(8,33) > 0

# p193, two d6: global mass forces at least one of the last two tails to n<=67.
need_pair_mass = TH193 - Fraction(1,4320) - Fraction(1,6048)
assert need_pair_mass == Fraction(3307,110880)
assert 2*Fraction(1,68) < need_pair_mass
assert Fraction(1,43) + Fraction(1,153) < need_pair_mass
assert Fraction(1,43) + Fraction(1,152) >= need_pair_mass

# Complete low-order census through n=152.
low = {}
for n0 in range(1,153):
    for p in factor_gcd_exp(n0):
        if p <= 3 or p in low:
            continue
        row = fibre_row(p)
        if row[1] <= 152:
            low[p] = row

pair_candidates = []
for p,row in low.items():
    _,n,d,h193,_,_,_ = row
    if d in (1,2,3,6) or p in excluded:
        continue
    pair_candidates.append((p,n,d,Fraction(1,h193)))
pair_candidates.sort()

pair_survivors = []
need_pair_local = LOCAL - 2*Fraction(1,3)
assert need_pair_local == Fraction(8,33)
for a,b in combinations(pair_candidates,2):
    mass = Fraction(1,a[1]) + Fraction(1,b[1])
    local = a[3] + b[3]
    if mass >= need_pair_mass and local >= need_pair_local:
        pair_survivors.append((a,b,mass,local))

assert len(pair_survivors) == 1
a,b,mass,local = pair_survivors[0]
assert {a[0],b[0]} == {53,601}
assert mass == Fraction(127,3900)
assert local == Fraction(18,65)

# Geometry kill: two d6 fibres occupy at most 2/3 of the 3-primary state;
# C11, C13, C5 factors are independent.
uncovered_pair = Fraction(1,3) * Fraction(10,11) * Fraction(12,13) * Fraction(4,5)
assert uncovered_pair == Fraction(32,143) > 0

# No d6, no d3, no d8: all three d4 are forced, then global mass fails.
assert 2*Fraction(1,4) + 2*Fraction(1,5) == Fraction(9,10) < LOCAL
no_d368_mass = d4_mass + Fraction(1,75)
assert no_d368_mass == Fraction(1819,100800)
assert no_d368_mass < TH193
assert no_d368_mass < TH201

print("d6 rows:", d6_rows)
print("p20161 no-d3 d6 branch: CLOSED")
print("p193 single-d6 survivors:", s8641, s12097)
print("single-d6 candidate uncovered lower bound:", uncovered_single)
print("p193 two-d6 pair survivors:", pair_survivors)
print("two-d6 candidate uncovered lower bound:", uncovered_pair)
print("no-d3/no-d6/no-d8 branch: CLOSED")
print("Combined with replay_d8_branch_2026_09_13.py: D3_MANDATORY")
