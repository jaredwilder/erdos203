# Canonical corrected finite-cover lower bound — 2026-09-14

Author: Jared Wilder

## Scope

This note replaces the raw late-session R44–R51 transcript as the canonical statement of the September finite-cover lower-bound result.

Let `U_5040` be the frozen 31-fibre base family. Any finite prime-fibre cover can be augmented by the primes in `U_5040` using independent CRT phase choices, so an obstruction to covers extending `U_5040` gives a genuine lower bound on the number of additional fibres needed by this finite-cover construction.

The result proved and replayed here is:

> **Theorem.** Any finite prime-fibre cover extending `U_5040` requires at least **12 outside prime fibres**.

This is a theorem about the finite prime-fibre construction. It is **not** by itself a solution of the full Erdős–Graham #203 problem, because no theorem is currently assumed that every hypothetical #203 witness admits a finite prime-fibre subcover.

## Corrections to the live transcript

The raw MSL stream is not the proof record. Two corrections are load-bearing:

1. Several late rounds grouped all remaining 3-coprime induced indices after `d=5,7` into `d>=11`, omitting the genuine classes `d=8` and `d=10`.
2. Several displayed rational values were mistyped. In particular the complete `d=5` replica-occupancy total is

```text
53/240
```

not `47/210`.

The replay script explicitly restores `d=8` and `d=10` and recomputes the exact arithmetic from scratch.

## Three-resource calculus

For a prime fibre with order

```text
n = |<2,3> mod p|
```

and induced index

```text
d = n / gcd(n,5040),
```

write

```text
L = 1/d                 local density on a 5040 replica
O = d/n                 fraction of 5040 replicas the fibre can meet
G = 1/n                 global density
```

Then

```text
G = L * O.
```

This identity is the compression behind the proof. A family must simultaneously supply enough local covering power, enough replica occupancy, and enough global mass.

## Frozen base deficit

The 31 base fibres have raw density

```text
143/140.
```

The phase-independent `p=5` overlap star forces overlap tax

```text
257/1680,
```

hence every phase assignment of the base has union density at most

```text
1459/1680.
```

Therefore every outside repair family must have global raw mass at least

```text
221/1680.
```

## Exact low induced-index censuses

The corrected replay computes complete censuses by using the fact that `d=n/gcd(n,5040)` implies `n | d*5040`, factoring

```text
gcd(2^(d*5040)-1, 3^(d*5040)-1),
```

and filtering by exact multiplicative orders.

| d | exact fibre count | total replica occupancy |
|---:|---:|---:|
| 2 | 2 | 53/2520 |
| 4 | 3 | 19/1008 |
| 5 | 16 | 53/240 |
| 7 | 10 | 389/5040 |
| 8 | 4 | 1/28 |
| 10 | 3 | 5/1008 |
| 11 | 24 | — |

The combined replica occupancy of **all** fibres in the six low 3-coprime classes `d=2,4,5,7,8,10` is only

```text
53/140.
```

## Corrected signature pruning

The replay treats the signature

```text
(E, d2, d4, d5, d7, d8, d10, z)
```

where `E` counts fibres with `3 | d` and `z` counts 3-coprime fibres with `d>=11`.

For `E<=8`, every `E` fibre has replica occupancy at most `1/9`, so all selected `E` fibres miss a common 5040 replica. Exact low-class occupancy bounds then permit a second erasure certificate.

The corrected coarse survivor counts are:

```text
r=8   : 0
r=9   : 1      (E=9)
r=10  : 8      (seven E=9 signatures, one E=10 signature)
r=11  : 37     (E in {0,9,10,11})
```

No signature with `1<=E<=8` survives at `r=11`.

## Closing r=9 and r=10

Every `E` fibre has order at least `108`.

For `r=9`, the only coarse survivor is nine `E` fibres, whose global mass is at most

```text
9/108 = 1/12 < 221/1680.
```

For `r=10`, the exact nine cheapest `E` orders are

```text
108, 162, 216, 270, 378, 486, 540, 648, 648.
```

Their mass is

```text
2273/68040.
```

Even adding the cheapest possible non-`E` outside fibre, of order `11`, gives

```text
93043/748440 < 221/1680.
```

The ten-`E` case is smaller. Thus `r<=10` is impossible.

## Closing r=11: E=0 equality face

The corrected signature certificate leaves exactly one `E=0` face:

```text
11 fibres, all 3-coprime, all with d>=11.
```

Local density is at most `11*(1/11)=1`, so a cover forces equality term-by-term: all eleven fibres must have `d=11`.

The complete `d=11` census contains exactly 24 fibres. Their induced `C_11` projective direction multiplicities are

```text
4,3,3,3,2,2,2,2,2,1.
```

Eleven affine lines in `F_11^2`, each of density `1/11`, can cover the plane with total mass exactly one only if they are pairwise disjoint. Pairwise-disjoint affine lines are parallel. Hence a cover would require eleven `d=11` fibres in one projective direction.

The exact census supplies at most four.

Contradiction.

## Closing r=11: E=9 equality escape

Let the nine `E` fibres have replica occupancies `O_i<=1/9`.

If

```text
sum O_i < 1,
```

then some 5040 replica is missed by all nine. The remaining two outside fibres would have to cover that replica. Each has local density at most `1/2`, so equality forces both exact `d=2` fibres. Their induced halfspaces have independent normals and union density only `3/4`, contradiction.

Therefore survival forces

```text
O_1=...=O_9=1/9.
```

A complete census of all `E` fibres with `n<=1080` contains 15 fibres and none has occupancy `1/9`. Hence every one of the nine equality-escape fibres has `n>1080`, so their total global mass is strictly less than

```text
1/120.
```

The remaining two fibres must therefore contribute more than

```text
221/1680 - 1/120 = 69/560.
```

A complete census of non-`E` outside fibres with `n<=31` gives only

```text
p=23, n=11, d=11
p=47, n=23, d=23.
```

If the second order were at least 32, the two-fibre mass would be at most `1/11+1/32 < 69/560`. Thus the pair is forced to be `{23,47}`.

But its local capacity is only

```text
1/11 + 1/23 = 34/253 < 1.
```

Contradiction.

## Closing r=11: E=10 and E=11

The eleven cheapest `E` orders begin

```text
108,162,216,270,378,486,540,648,648,648,756.
```

The ten-`E` plus one non-`E` optimistic mass and the eleven-`E` mass are both below `221/1680`. Hence both faces are impossible.

## Conclusion

All corrected `r<=11` signatures are impossible. Therefore:

```text
finite prime-fibre extension lower bound = 12 outside fibres.
```

## Reproduce

```bash
python -m pip install sympy
python tools/replay_r12_lower_bound_2026_09_14.py
```

Expected verdict:

```text
"verdict": "ALL_MATCH"
"finite_extension_lower_bound": 12
```

Recorded receipt:

```text
receipts/replay-r12-lower-bound-2026-09-14.json
```

## Research boundary

This lower bound is now a pruning theorem, not the project objective. The next program is explicitly directed at a **close of #203**, beginning with synthesis of an actual finite cover and, if found, immediate CRT realization of an explicit integer `m`.
