# Erdős–Graham #203 — KBK Attack R3 — the no-`d=3` side is closed

**Date:** 2026-09-13  
**Author:** Jared Wilder  
**Scope:** frozen `U_5040` extension program, `r=6`, exactly one induced-index-2 anchor, `p=23` mandatory, `p=47` excluded.

Replays:

```bash
python tools/replay_d8_branch_2026_09_13.py
python tools/replay_no_d3_branch_2026_09_13.py
```

Receipts:

- [`replay-d8-branch-2026-09-13.json`](../receipts/replay-d8-branch-2026-09-13.json)
- [`replay-no-d3-branch-2026-09-13.json`](../receipts/replay-no-d3-branch-2026-09-13.json)

## Headline

After the `p=47` subbranch was closed by `C3` partition rigidity and 6→5 cardinality descent, the remaining one-anchor branch split into `d=3`-present and no-`d=3` cases.

The no-`d=3` side is now closed completely.

Therefore:

```text
r=6,
d2count=1,
p23 mandatory,
p47 excluded
→ every surviving cover must contain d=3.
```

This is now backed by executable finite-census replays.

---

## 1. Exact `d=6` anchor restrictions

There are exactly two `d=6` fibres relevant to the campaign:

```text
p8641   n=4320
p12097  n=6048
```

Their exact restrictions to the two anchor half-lattices are:

```text
anchor p193:
  p8641  image size 3  -> rho=1/3
  p12097 image size 3  -> rho=1/3

anchor p20161:
  p8641  image size 6  -> rho=1/6
  p12097 image size 6  -> rho=1/6
```

This sharpens the live coarse treatment: the `p20161` anchor receives only `1/6`, not `1/3`, from either `d=6` fibre.

---

## 2. `p20161` + `d=6` closes immediately

With one `d=6` fibre, the other three tails must provide

```text
10/11 - 1/6 = 49/66.
```

Without `d=3`, if at most two `d=4` fibres are used, the maximum is

```text
1/4 + 1/4 + 1/5 = 7/10 < 49/66.
```

Hence all three `d=4` fibres are forced. Even with the stronger `d=6` mass `1/4320`, the total global mass is only

```text
1/4320 + 1/448 + 1/576 + 1/1344
= 299/60480
< 899/22176.
```

So the single-`d=6` branch dies globally.

With both `d=6` fibres, the remaining two tails would need

```text
19/33,
```

but two non-`d3` tails contribute at most `1/2`. Thus the two-`d6` branch dies locally.

Therefore the `p20161`, no-`d3`, `d6` side is closed.

---

## 3. `p193` + one `d=6`: exact finite Pareto census

Here each `d=6` fibre contributes `1/3`. The remaining three tails must provide

```text
19/33.
```

Since the other two tails contribute at most `1/4` each, every one of the three must individually contribute at least

```text
5/66.
```

That bounds the induced index to a finite set:

```text
odd  d <= 13,
even d <= 26,
```

with `d=2,3,6` excluded by branch scope.

The replay factors the complete finite arithmetic universes `gcd(2^(5040d)-1,3^(5040d)-1)` for every admissible `d`, recomputes exact orders and exact anchor restrictions, and enumerates every triple passing both the local and global gates.

Results:

```text
selected d6 = p12097:
  no surviving triple

selected d6 = p8641:
  exactly one surviving triple
  {p601, p101, p151}
```

This proves that the live knife-edge candidate really is the unique arithmetic survivor in the single-`d6`, no-`d3`, `p193` branch.

Its total mass is

```text
1/4320 + 1/75 + 1/100 + 1/150
= 653/21600
= 1117/36960 + 1/103950.
```

The margin is only `1/103950`.

---

## 4. The knife-edge survivor dies geometrically

Inside the `p193` anchor half-lattice:

- `p23` is an `11`-primary fibre;
- `p8641` is a `3`-primary fibre of density `1/3`;
- `p601,p101,p151` are three `5`-primary fibres, whose union has density at most `3/5`.

The `11`, `3`, and `5` primary states are independent. Therefore the uncovered density is at least

```text
(10/11) * (2/3) * (2/5)
= 8/33
> 0.
```

So the unique arithmetic survivor cannot cover.

This kills the single-`d6`, no-`d3`, `p193` branch completely.

---

## 5. `p193` + both `d=6` fibres

After paying for both `d=6` fibres, the final two tails need global mass

```text
3307/110880.
```

The global threshold forces at least one final tail to have order at most `67`; after the strongest possible order-43 tail, the other must have order at most `152`. The replay therefore performs a complete low-order census through `n=152` and checks exact local restrictions.

Exactly one arithmetic pair survives:

```text
{p53, p601}
```

with

```text
local mass = 1/13 + 1/5 = 18/65,
global mass = 1/52 + 1/75 = 127/3900.
```

It also dies geometrically. The two `d=6` fibres cover at most `2/3` of the `3`-primary state, while `p23`, `p53`, and `p601` impose independent `11`, `13`, and `5` primary conditions. Hence uncovered density is at least

```text
(1/3) * (10/11) * (12/13) * (4/5)
= 32/143
> 0.
```

Thus the two-`d6` branch is closed as well.

---

## 6. No `d=6`, no `d=8`

If `d=3`, `d=6`, and `d=8` are all absent, then with at most two `d=4` fibres the four-tail local ceiling is

```text
1/4 + 1/4 + 1/5 + 1/5
= 9/10
< 10/11.
```

So all three `d=4` fibres are forced. The strongest possible fourth repair tail gives

```text
1/448 + 1/576 + 1/1344 + 1/75
= 1819/100800,
```

below both anchor global thresholds. This branch is impossible.

The separate repaired `d=8` replay closes the remaining no-`d3`, no-`d6` possibility.

---

## Result

Combining the repaired `d=8` closure with the exact `d=6` replay gives

```text
ONE-d2 / p23 / non-p47 / r6:

no d3 + no d6 + no d8  -> CLOSED
no d3 + d8             -> CLOSED
no d3 + one d6         -> CLOSED
no d3 + two d6         -> CLOSED

therefore

d3 IS MANDATORY.
```

The one-`d=2` six-fibre frontier has now collapsed to the `d=3`-present arm.

## Next KBK attack

The next move should exploit the four projective `d=3` classes

```text
C01 = {109,433}
C10 = {271,757,7561}
C12 = {379,541,2161}
C11 = {15121,30241}
```

against the same mechanisms that killed `p=47`:

```text
mass pressure
→ local equality / near-equality
→ affine-plane direction rigidity
→ redundant fibre
→ cardinality descent.
```

Broad SAT should remain downstream of this structural attack.
