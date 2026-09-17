# Erdős–Graham #203 — finite prime-fibre obstruction

The problem asks whether there exists an integer `m>=1`, `(m,6)=1`, such that

\[
2^k3^\ell m+1
\]

is composite for every `k,\ell>=0`.

This repository studies a sufficient construction using finitely many prime fibres. For a prime `p>3`, the exponent pairs eliminated by `p` form a coset of

\[
R_p=\{(u,v):2^u3^v\equiv1\pmod p\}.
\]

CRT makes the phase choices for distinct primes independent, turning the construction into a finite geometric covering problem followed by one arithmetic realization step.

## Main finite theorem

For the frozen 31-fibre `U_5040` base:

> **Any finite prime-fibre cover extending that base requires at least 12 outside prime fibres.**

The corrected replay includes the previously omitted induced-index classes `d=8` and `d=10` and still eliminates every extension using at most 11 outside fibres.

The exact replay is:

- [`docs/CANONICAL_R12_LOWER_BOUND_2026-09-14.md`](docs/CANONICAL_R12_LOWER_BOUND_2026-09-14.md) — theorem and proof architecture;
- [`tools/replay_r12_lower_bound_2026_09_14.py`](tools/replay_r12_lower_bound_2026_09_14.py) — executable exact calculation;
- [`receipts/replay-r12-lower-bound-2026-09-14.json`](receipts/replay-r12-lower-bound-2026-09-14.json) — matching receipt.

## Finite obstruction calculus

Let

```text
n_p = |<2,3> mod p|
d_p = n_p / gcd(n_p,5040)
```

and define

```text
L = 1/d_p          local density on a 5040 replica
O = d_p/n_p        replica occupancy
G = 1/n_p          global density
```

so

\[
G=LO.
\]

The frozen 31-fibre base has raw density

\[
143/140.
\]

A phase-independent overlap forced by `p=5` costs `257/1680`, so the base union has density at most

\[
1459/1680.
\]

Any repair family must therefore supply at least

\[
221/1680
\]

of additional global raw fibre mass.

For the low 3-coprime induced-index classes `d=2,4,5,7,8,10`, the combined replica occupancy of **every** available fibre is only

\[
53/140.
\]

The complete `d=11` census contains 24 fibres with direction multiplicities

```text
4,3,3,3,2,2,2,2,2,1
```

which rules out the equality case requiring eleven parallel `1/11` lines.

## Independent finite results

[`tools/replay_eg203_gold.py`](tools/replay_eg203_gold.py) recomputes four earlier exact calculations:

| result | value |
|---|---|
| primes `p>3` with `n_p | 5040` | **31 fibres**, raw density **143/140** |
| all phases for the `N=5040` fibre family | union density at most **823/840 < 1** |
| `{5,7,11,13}` core on the `60×60` torus | **2,880** assignments; maximum union density **353/720** |
| primes `p<=10^6` with `n_p<=1000` | **238 fibres**, raw density about **1.83048759933** |

## Reproduce

```bash
python tools/check_gold_arithmetic.py
python tools/replay_eg203_gold.py
python tools/replay_d8_branch_2026_09_13.py
python tools/replay_no_d3_branch_2026_09_13.py
python -m pip install sympy
python tools/replay_r12_lower_bound_2026_09_14.py
```

## Scope

The finite prime-fibre cover is a sufficient route to a YES solution of Erdős–Graham #203. A successful finite cover followed by CRT realization would solve the problem positively.

The converse is not proved: failure of this finite-cover construction would not by itself prove that no suitable `m` exists.

The headline finite obstruction theorems are presently computational/written results; they have not yet been formalized in Lean in this repository.

Author: Jared Wilder. License: Apache-2.0.
