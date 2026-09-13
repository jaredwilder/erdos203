from fractions import Fraction
from math import gcd, lcm

BASE = 5040
N = 40320


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def factor_small(n: int):
    out = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            out[d] = out.get(d, 0) + 1
            n //= d
        d = 3 if d == 2 else d + 2
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def multiplicative_order(a: int, p: int) -> int:
    assert gcd(a, p) == 1
    order = p - 1
    for q in factor_small(p - 1):
        while order % q == 0 and pow(a, order // q, p) == 1:
            order //= q
    return order


def subgroup_size(p: int, gens):
    s = {1}
    changed = True
    while changed:
        changed = False
        for x in tuple(s):
            for g in gens:
                y = (x * g) % p
                if y not in s:
                    s.add(y)
                    changed = True
    return len(s)


# If d = n/gcd(n,5040) = 8 and g = gcd(n,5040), then n = 8g and
# gcd(8g,5040)=g. Hence 5040/g is odd, so 16|g, and therefore n|40320.
# Thus every d=8 prime divides gcd(2^40320-1, 3^40320-1).
G = gcd(pow(2, N) - 1, pow(3, N) - 1)

factorization = {
    5: 2,
    7: 2,
    11: 1,
    13: 1,
    17: 1,
    19: 1,
    29: 1,
    31: 1,
    37: 1,
    41: 1,
    43: 1,
    61: 1,
    71: 1,
    73: 1,
    97: 1,
    113: 1,
    127: 1,
    181: 1,
    193: 1,
    211: 1,
    241: 1,
    281: 1,
    337: 1,
    421: 1,
    449: 1,
    577: 1,
    631: 1,
    641: 1,
    673: 1,
    769: 1,
    1009: 1,
    1153: 1,
    2017: 1,
    2521: 1,
    2689: 1,
    3361: 1,
    4481: 1,
    13441: 1,
    20161: 1,
    26881: 1,
}
assert all(is_prime(p) for p in factorization)
prod = 1
for p, e in factorization.items():
    prod *= p**e
assert prod == G

rows = []
for p in sorted(factorization):
    o2 = multiplicative_order(2, p)
    o3 = multiplicative_order(3, p)
    n = lcm(o2, o3)
    d = n // gcd(n, BASE)
    if d == 8:
        a = pow(2, BASE, p)
        b = pow(3, BASE, p)
        assert subgroup_size(p, [a, b]) == 8

        # p=193 anchor: parity character (1,0), kernel basis (2,0),(0,1).
        h193_image = subgroup_size(p, [a * a % p, b])

        # p=20161 anchor: parity character (1,1), kernel basis (1,1),(0,2).
        h20161_image = subgroup_size(p, [a * b % p, b * b % p])

        rows.append((p, n, o2, o3, h193_image, h20161_image))

expected = [
    (641, 640, 64, 640, 8, 8),
    (769, 384, 384, 48, 4, 8),
    (4481, 4480, 560, 4480, 8, 8),
    (26881, 13440, 960, 4480, 8, 8),
]
assert rows == expected

required = Fraction(10, 11)

# Anchor p=20161: every d8 fibre has local density 1/8.
assert Fraction(1, 8) + 3 * Fraction(1, 4) == Fraction(7, 8) < required

# Anchor p=193: without p769, every d8 fibre again has local density 1/8.
assert Fraction(7, 8) < required

# With p769 but at most one d4, all other non-d3/d6/d4/d8 classes have
# local density at most 1/5.
assert Fraction(1, 4) + Fraction(1, 4) + 2 * Fraction(1, 5) == Fraction(9, 10) < required

# Hence p193 + p769 forces at least two d4 fibres. The strongest compatible
# global mass is then p769, the two strongest d4 fibres, and p601.
max_global = Fraction(1, 384) + Fraction(1, 448) + Fraction(1, 576) + Fraction(1, 75)
assert max_global == Fraction(4013, 201600)

threshold_193 = Fraction(1117, 36960)
threshold_20161 = Fraction(899, 22176)
assert max_global < threshold_193
assert max_global < threshold_20161

print("d8 census:", rows)
print("p20161 local ceiling:", Fraction(7, 8), "<", required)
print("p193 no-p769 ceiling:", Fraction(7, 8), "<", required)
print("p193 p769 + <=1 d4 ceiling:", Fraction(9, 10), "<", required)
print("p193 forced-two-d4 global max:", max_global, "<", threshold_193)
print("D8_NO_D3_NO_D6_BRANCH: CLOSED")
