#!/usr/bin/env python3
"""
Replays the corrected September 14, 2026 finite-cover lower-bound state for EG203.

Requires:
    python -m pip install sympy

This script deliberately includes d=8 and d=10 as separate 3-coprime classes.
It computes:
  * exact d in {2,4,5,7,8,10,11} censuses;
  * exact replica-occupancy totals;
  * the complete d=11 direction census;
  * the complete 3|d low-order census for n<=1080;
  * the complete non-E outside census for n<=31;
  * corrected coarse signature survivors for r=8,9,10,11;
  * exact mass gates used to close r<=11.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from math import gcd, lcm
import json
import sympy as sp

BASE_PERIOD = 5040
BASE_DEFICIT = Fraction(221, 1680)
LOW_D = (2, 4, 5, 7, 8, 10)

def fp(x):
    return f"{x.numerator}/{x.denominator}"

def fibre_data(p):
    o2 = int(sp.n_order(2, p))
    o3 = int(sp.n_order(3, p))
    n = lcm(o2, o3)
    d = n // gcd(n, BASE_PERIOD)
    return o2, o3, n, d

def census_d(d):
    # If n/gcd(n,5040)=d then n | d*5040.
    N = d * BASE_PERIOD
    G = gcd(pow(2, N) - 1, pow(3, N) - 1)
    fac = sp.factorint(G)
    out = []
    for p in sorted(fac):
        if p <= 3:
            continue
        o2, o3, n, dd = fibre_data(p)
        if dd == d:
            out.append({
                "p": p, "n": n, "ord2": o2, "ord3": o3,
                "occupancy": Fraction(d, n),
            })
    out.sort(key=lambda x: (x["n"], x["p"]))
    return out, fac

def char_dir_11(p):
    A = pow(2, BASE_PERIOD, p)
    B = pow(3, BASE_PERIOD, p)
    gen = A if A != 1 else B
    def dlog(x):
        y = 1
        for k in range(11):
            if y == x:
                return k
            y = (y * gen) % p
        raise RuntimeError("C11 discrete log failure")
    a, b = dlog(A), dlog(B)
    if a:
        return (1, (b * pow(a, -1, 11)) % 11)
    return (0, 1)

def e_census(limit=1080):
    # 3|d implies v_3(n)>=3, hence 27|n.
    seen = {}
    for N in range(27, limit + 1, 27):
        G = gcd(pow(2, N) - 1, pow(3, N) - 1)
        for p in sp.factorint(G):
            if p <= 3:
                continue
            o2, o3, n, d = fibre_data(p)
            if n <= limit and d % 3 == 0:
                seen[p] = (n, d, o2, o3)
    return sorted(
        [{"p": p, "n": v[0], "d": v[1], "ord2": v[2], "ord3": v[3]}
         for p, v in seen.items()],
        key=lambda x: (x["n"], x["p"])
    )

def non_e_outside_census(limit=31):
    seen = {}
    for N in range(1, limit + 1):
        G = gcd(pow(2, N) - 1, pow(3, N) - 1)
        for p in sp.factorint(G):
            if p <= 3:
                continue
            o2, o3, n, d = fibre_data(p)
            if n <= limit and d > 1 and d % 3 != 0:
                seen[p] = (n, d, o2, o3)
    return sorted(
        [{"p": p, "n": v[0], "d": v[1], "ord2": v[2], "ord3": v[3]}
         for p, v in seen.items()],
        key=lambda x: (x["n"], x["p"])
    )

def top_sum(xs, k):
    vals = sorted((x["occupancy"] for x in xs), reverse=True)
    return sum(vals[:k], Fraction())

def corrected_survivors(r, census):
    # Signature: (E,d2,d4,d5,d7,d8,d10,z), z means 3-coprime d>=11.
    # For E<=8 the E fibres miss a common 5040-replica because each has occupancy<=1/9.
    out = []
    for E in range(r + 1):
        for a in range(min(len(census[2]), r - E) + 1):
            for b in range(min(len(census[4]), r - E - a) + 1):
                for t in range(min(len(census[5]), r - E - a - b) + 1):
                    for s in range(min(len(census[7]), r - E - a - b - t) + 1):
                        for h in range(min(len(census[8]), r - E - a - b - t - s) + 1):
                            for j in range(min(len(census[10]), r - E - a - b - t - s - h) + 1):
                                z = r - E - a - b - t - s - h - j
                                if E <= 8:
                                    local = (
                                        a*Fraction(1,2) + b*Fraction(1,4)
                                        + t*Fraction(1,5) + s*Fraction(1,7)
                                        + h*Fraction(1,8) + j*Fraction(1,10)
                                        + z*Fraction(1,11)
                                    )
                                    if local < 1:
                                        continue
                                    erase_occ = (
                                        E*Fraction(1,9)
                                        + top_sum(census[2], a)
                                        + top_sum(census[4], b)
                                        + top_sum(census[5], t)
                                        + top_sum(census[7], s)
                                        + top_sum(census[8], h)
                                        + top_sum(census[10], j)
                                    )
                                    # If erased classes miss a replica, z alone must cover it.
                                    if erase_occ < 1 and Fraction(z,11) < 1:
                                        continue
                                out.append((E,a,b,t,s,h,j,z))
    return out

def main():
    census = {}
    census_factor_counts = {}
    for d in (2,4,5,7,8,10,11):
        census[d], fac = census_d(d)
        census_factor_counts[d] = len(fac)

    expected_counts = {2:2,4:3,5:16,7:10,8:4,10:3,11:24}
    assert {d:len(census[d]) for d in expected_counts} == expected_counts

    expected_occ = {
        2: Fraction(53,2520),
        4: Fraction(19,1008),
        5: Fraction(53,240),
        7: Fraction(389,5040),
        8: Fraction(1,28),
        10: Fraction(5,1008),
    }
    for d, want in expected_occ.items():
        got = sum((x["occupancy"] for x in census[d]), Fraction())
        assert got == want, (d, got, want)
    low_occ_total = sum(expected_occ.values(), Fraction())
    assert low_occ_total == Fraction(53,140)

    dirs = defaultdict(list)
    for x in census[11]:
        dirs[char_dir_11(x["p"])].append(x["p"])
    direction_mults = sorted((len(v) for v in dirs.values()), reverse=True)
    assert direction_mults == [4,3,3,3,2,2,2,2,2,1]

    E = e_census()
    assert len(E) == 15
    E_orders = [x["n"] for x in E]
    assert E_orders[:11] == [108,162,216,270,378,486,540,648,648,648,756]
    assert all(Fraction(x["d"], x["n"]) != Fraction(1,9) for x in E)

    nonE31 = non_e_outside_census()
    assert [(x["p"],x["n"],x["d"]) for x in nonE31] == [(23,11,11),(47,23,23)]

    survivors = {r: corrected_survivors(r, census) for r in (8,9,10,11)}
    assert survivors[8] == []
    assert survivors[9] == [(9,0,0,0,0,0,0,0)]
    assert all(sig[0] >= 9 for sig in survivors[10])
    assert set(sig[0] for sig in survivors[11]) == {0,9,10,11}
    assert [sig for sig in survivors[11] if sig[0] == 0] == [(0,0,0,0,0,0,0,11)]

    e9_mass = sum((Fraction(1,n) for n in E_orders[:9]), Fraction())
    e10_mass = sum((Fraction(1,n) for n in E_orders[:10]), Fraction())
    e11_mass = sum((Fraction(1,n) for n in E_orders[:11]), Fraction())
    assert e9_mass == Fraction(2273,68040)
    assert e10_mass == Fraction(1189,34020)
    assert e11_mass == Fraction(617,17010)

    # r=9 and r=10 global gates.
    assert 9*Fraction(1,108) < BASE_DEFICIT
    assert e9_mass + Fraction(1,11) < BASE_DEFICIT

    # r=11 E10/E11 gates.
    assert e10_mass + Fraction(1,11) < BASE_DEFICIT
    assert e11_mass < BASE_DEFICIT

    # r=11 E9 equality escape:
    # if nine E occupancies do not sum to <1, each must equal 1/9.
    # E census shows no such fibre below/equal 1080, hence total E mass <1/120.
    complement_need = BASE_DEFICIT - Fraction(1,120)
    assert complement_need == Fraction(69,560)
    assert Fraction(1,11) + Fraction(1,32) < complement_need
    assert Fraction(1,11) + Fraction(1,23) > complement_need
    assert Fraction(1,11) + Fraction(1,23) == Fraction(34,253) < 1

    receipt = {
        "verdict": "ALL_MATCH",
        "base_deficit": fp(BASE_DEFICIT),
        "exact_census_counts": {str(d):len(census[d]) for d in census},
        "exact_low_class_occupancy_totals": {str(d):fp(expected_occ[d]) for d in expected_occ},
        "combined_low_nonE_occupancy": fp(low_occ_total),
        "d11_direction_multiplicities": direction_mults,
        "d11_max_parallel_multiplicity": max(direction_mults),
        "E_n_le_1080_count": len(E),
        "E_11_cheapest_orders": E_orders[:11],
        "nonE_n_le_31": [(x["p"],x["n"],x["d"]) for x in nonE31],
        "corrected_signature_survivor_counts": {str(r):len(survivors[r]) for r in survivors},
        "corrected_signature_survivor_E_values": {
            str(r):dict(sorted(Counter(sig[0] for sig in survivors[r]).items()))
            for r in survivors
        },
        "e9_mass": fp(e9_mass),
        "e10_mass": fp(e10_mass),
        "e11_mass": fp(e11_mass),
        "r11_E9_complement_mass_threshold": fp(complement_need),
        "finite_extension_lower_bound": 12,
        "scope": "finite prime-fibre covers after adjoining U_5040; not a solution of full EG203",
    }
    print(json.dumps(receipt, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
