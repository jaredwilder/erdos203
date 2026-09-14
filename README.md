# Erdős–Graham #203: finite prime-fibre obstruction and synthesis program

**Exact structural results, reproducible finite computations, and a terminal synthesis program for the finite prime-fibre route to Erdős–Graham #203.**

For a prime `p>3`, the exponent pairs eliminated by `p` form one coset of the relation lattice

```text
R_p = {(u,v) : 2^u·3^v ≡ 1 (mod p)}.
```

CRT allows the coset choice for distinct primes to be selected independently, turning a finite-witness construction into a geometric covering problem before final arithmetic realization.

The source problem asks:

> Is there an integer `m>=1`, `(m,6)=1`, such that none of `2^k·3^ℓ·m+1` are prime for any `k,ℓ>=0`?

This repository studies a sufficient construction: a finite collection of prime fibres whose selected cosets cover every exponent pair. That construction is not assumed to describe every possible solution of the full problem.

## September 14, 2026 canonical state

The corrected September replay now proves:

> **Any finite prime-fibre cover extending the frozen 31-fibre `U_5040` base requires at least 12 outside prime fibres.**

The late live transcript contained a real classification bug: several branches omitted the valid 3-coprime induced-index classes `d=8` and `d=10`. The canonical replay restores those classes, recomputes the exact low-index censuses, and still closes every extension with at most 11 outside fibres.

Canonical release:

- [`docs/CANONICAL_R12_LOWER_BOUND_2026-09-14.md`](docs/CANONICAL_R12_LOWER_BOUND_2026-09-14.md) — corrected theorem and proof architecture.
- [`tools/replay_r12_lower_bound_2026_09_14.py`](tools/replay_r12_lower_bound_2026_09_14.py) — executable replay, including `d=8` and `d=10`.
- [`receipts/replay-r12-lower-bound-2026-09-14.json`](receipts/replay-r12-lower-bound-2026-09-14.json) — `ALL_MATCH` receipt.
- [`docs/CLOSE_MISSION_2026-09-14.md`](docs/CLOSE_MISSION_2026-09-14.md) — terminal campaign contract: synthesize a cover, realize `m`, and close #203 rather than continuing a lower-bound treadmill.

The corrected replay recomputes complete censuses for `d=2,4,5,7,8,10,11`. The combined replica occupancy of **every** fibre in the six low 3-coprime classes `d=2,4,5,7,8,10` is only

```text
53/140.
```

The complete `d=11` census contains 24 fibres. Their induced `C_11` direction multiplicities are

```text
4,3,3,3,2,2,2,2,2,1,
```

which kills the eleven-line equality face because an exact cover by eleven `1/11` affine lines would require eleven parallel fibres.

The campaign is now explicitly **constructive-first**: `r>=13`, `r>=14`, etc. are pruning information, not the objective. The next target is an exact phase synthesis beginning at `r=12`, followed immediately by CRT realization and independent verification if a cover is found.

## Core calculus

Let

```text
n_p = |<2,3> mod p|
d_p = n_p / gcd(n_p,5040).
```

For a fibre define

```text
L = 1/d_p          local density on a 5040 replica
O = d_p/n_p        replica occupancy
G = 1/n_p          global density
```

so that

```text
G = L*O.
```

This three-resource identity is the main structural compression used by the corrected lower-bound proof and by the synthesis search.

The frozen 31-fibre base has raw density `143/140`. A phase-independent `p=5` overlap star forces overlap tax `257/1680`, hence base union density at most `1459/1680`. Every outside repair family must therefore contribute at least

```text
221/1680
```

of global raw fibre mass.

## Earlier September research releases

- [`docs/KBK_PROGRESS_2026-09-13.md`](docs/KBK_PROGRESS_2026-09-13.md)
- [`docs/KBK_ATTACK_R2_2026-09-13.md`](docs/KBK_ATTACK_R2_2026-09-13.md)
- [`docs/KBK_ATTACK_R3_2026-09-13.md`](docs/KBK_ATTACK_R3_2026-09-13.md)

These are retained as research history. Where they overlap the September 14 canonical release, the corrected September 14 replay controls.

## August exact finite results

The four August results below are independently recomputed by [`tools/replay_eg203_gold.py`](tools/replay_eg203_gold.py), using exact rational arithmetic. The recorded output is in [`receipts/replay-eg203-gold-2026-08-31.json`](receipts/replay-eg203-gold-2026-08-31.json).

| id | statement | recomputed value |
|---|---|---|
| G28 | primes `p>3` with `n_p | 5040` | **31 fibres**, total raw density **143/140**; the relevant gcd factorization is complete |
| G29 | the `N=5040` fibre family cannot cover for **any** phase assignment | `p=5` and `p=7` are mandatory; joint image exactly **24**; union density at most `143/140 - 1/24 = 823/840 < 1` |
| G30 | all phase assignments for the `{5,7,11,13}` core on the `60×60` torus | all **2,880** assignments checked; maximum union density **353/720**; unavoidable overlap **79/720** |
| G31 | primes `p<=10^6` with `n_p<=1000` | **238 fibres**, total raw density about **1.83048759933…**; all already occur below `10^5`; largest prime **67033** |

## Lean formalization status

`Erdos203All.lean` and the module files currently provide the project structure for a Lean formalization, but the headline finite obstruction theorems have **not yet been formalized in Lean in this repository**.

## Reproduce the computations

```bash
python tools/check_gold_arithmetic.py
python tools/replay_eg203_gold.py
python tools/replay_d8_branch_2026_09_13.py
python tools/replay_no_d3_branch_2026_09_13.py
python -m pip install sympy
python tools/replay_r12_lower_bound_2026_09_14.py
```

## Scope and research record

- [`docs/CLAIM_LEDGER.md`](docs/CLAIM_LEDGER.md) is the live status ledger.
- [`docs/QUARANTINE.md`](docs/QUARANTINE.md) preserves retracted or superseded routes.
- [`docs/CEGAR_PROTOCOL.md`](docs/CEGAR_PROTOCOL.md) records the iterative exact-search protocol.
- [`docs/CLOSE_MISSION_2026-09-14.md`](docs/CLOSE_MISSION_2026-09-14.md) defines the terminal success criteria.

The finite prime-fibre construction is a sufficient route to a solution, not presently a proof that every possible #203 solution must arise that way. A constructive finite cover plus CRT realization would give a full YES solution; a negative result about finite covers alone would not give a full NO solution without an additional finite-subcover theorem.

## Sibling repositories

| repository | contents |
|---|---|
| [erdos203](https://github.com/jaredwilder/erdos203) | this finite prime-fibre obstruction and synthesis program |
| [erdos411](https://github.com/jaredwilder/erdos411) | Erdős–Graham #411 reduction/cascade/formal work |
| [erdos902](https://github.com/jaredwilder/erdos902) | Schütte/Erdős tournament theory and finite structure |

## References

- P. Erdős and R. L. Graham, *Old and new problems and results in combinatorial number theory*, Monographies de L'Enseignement Mathématique 28 (1980).
- [erdosproblems.com/203](https://www.erdosproblems.com/203)
- Research context: https://epassports.eu/research/erdos-graham-203

## License

Apache 2.0, following Mathlib.
