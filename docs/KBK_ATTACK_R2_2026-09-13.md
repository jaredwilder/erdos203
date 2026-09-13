# Erdős–Graham #203 — KBK Attack R2 — repaired `d=8` closure

**Date:** 2026-09-13  
**Author:** Jared Wilder  
**Scope:** frozen `U_5040` extension program, `r=6`, exactly one `d=2` anchor, `p=23` mandatory, `p=47` excluded, `d=8` present, `d=3` absent, `d=6` absent.

Replay:

```bash
python tools/replay_d8_branch_2026_09_13.py
```

Receipt: [`receipts/replay-d8-branch-2026-09-13.json`](../receipts/replay-d8-branch-2026-09-13.json)

## 1. Complete `d=8` census

Let

```text
d = n / gcd(n,5040) = 8,
g = gcd(n,5040).
```

Then `n=8g` and `gcd(8g,5040)=g`. Hence `5040/g` is odd, so `16|g`, and therefore

```text
n | 40320.
```

Thus every `d=8` prime divides

```text
gcd(2^40320-1, 3^40320-1).
```

The replay verifies the complete factorization and recomputes `ord_p(2)`, `ord_p(3)`, and `n_p`. Exactly four primes have induced index `8`:

| p | n_p | ord_p(2) | ord_p(3) |
|---:|---:|---:|---:|
| 641 | 640 | 64 | 640 |
| 769 | 384 | 384 | 48 |
| 4481 | 4480 | 560 | 4480 |
| 26881 | 13440 | 960 | 4480 |

## 2. Exact restriction to the two anchor half-lattices

On the `p=193` anchor, the residual parity kernel has basis `(2,0),(0,1)`. The induced `d=8` image sizes are

```text
p641   : 8  -> relative density 1/8
p769   : 4  -> relative density 1/4
p4481  : 8  -> relative density 1/8
p26881 : 8  -> relative density 1/8
```

On the `p=20161` anchor, with kernel basis `(1,1),(0,2)`, all four induced images have size `8`, so every `d=8` fibre has relative density `1/8`.

This is the exact repair of the live-session gap: multiple `d=8` fibres are now included rather than silently excluded.

## 3. `p=20161` anchor dies locally

The four remaining tails must have local mass at least

```text
10/11.
```

With a `d=8` fibre present, the strongest possible local total is obtained by combining one `d=8` fibre at `1/8` with all three `d=4` fibres at `1/4` each:

```text
1/8 + 3/4 = 7/8 < 10/11.
```

Therefore the entire repaired `d=8`, no-`d3`, no-`d6` branch is impossible for anchor `p=20161`.

## 4. `p=193` anchor

If `p=769` is absent, every `d=8` fibre contributes only `1/8`; again

```text
1/8 + 3/4 = 7/8 < 10/11.
```

So `p=769` is mandatory.

With `p=769`, if at most one `d=4` fibre is present, the remaining two non-`d3/d6/d4/d8` fibres have local density at most `1/5`. Hence

```text
1/4 + 1/4 + 1/5 + 1/5
= 9/10
< 10/11.
```

Thus at least two `d=4` fibres are mandatory.

The strongest global mass compatible with that local forcing is then

```text
p769              1/384
strongest d4      1/448
second d4         1/576
strongest tail    1/75   (p601)
--------------------------------
total          4013/201600.
```

But the `p=193` branch requires

```text
1117/36960,
```

and the replay verifies

```text
4013/201600 < 1117/36960.
```

So the `p=193` branch also fails.

## Result

```text
r=6,
d2count=1,
p23 selected,
p47 excluded,
d8 present,
d3 absent,
d6 absent
→ IMPOSSIBLE.
```

The earlier live `d=8` proof remains quarantined because its reasoning omitted multiple `d=8` fibres. This document is a separate repaired proof with a complete arithmetic census and executable replay.

## Updated frontier

Within the one-`d=2`, non-`p47` branch, every survivor must now contain

```text
d=3 or d=6.
```

The next KBK target is therefore the `d=6`/no-`d3` corridor and the `d=3`-present arm. The equality-case/common-kernel/redundancy mechanism from the `p=47` closure remains the preferred attack before broad phase SAT.
