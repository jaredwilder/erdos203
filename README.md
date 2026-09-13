# Erdős–Graham #203: finite prime-fibre obstruction calculus

**Exact structural results, reproducible finite computations, and search code for the finite prime-fibre covering approach to Erdős–Graham #203.** The strongest fully replayed August result is an exact impossibility theorem for the first common-period fibre family whose total raw density exceeds 1. A newer September structural campaign has now closed a substantial six-fibre subbranch by equality-case partition rigidity and cardinality descent.

For a prime `p>3`, the exponent pairs eliminated by `p` form one coset of the relation lattice

```text
R_p = {(u,v) : 2^u·3^v ≡ 1 (mod p)}.
```

CRT allows the coset choice for each prime to be selected independently, turning this approach into a finite geometric covering problem before the final arithmetic realization.

The source problem asks:

> Is there an integer `m>=1`, `(m,6)=1`, such that none of `2^k·3^ℓ·m+1` are prime for any `k,ℓ>=0`?

This repository studies one sufficient construction: a finite collection of prime fibres whose chosen cosets cover every exponent pair. That construction is not assumed to describe every possible solution of the full problem.

## September 13, 2026 KBK progress

The current structural release is [`docs/KBK_PROGRESS_2026-09-13.md`](docs/KBK_PROGRESS_2026-09-13.md).

Headline within the frozen 31-fibre `U_5040` extension program:

```text
r <= 5 outside fibres: closed
r = 6, d2count = 2: closed
r = 6, d2count = 1, p=47 subbranch: closed
```

The new `p=47` closure does not come from terminal phase brute force. Local mass saturation forces the final three fibres to be the three cosets of one common index-3 kernel; that makes `p=47` redundant and descends any alleged six-fibre cover to the already-impossible five-fibre case.

The September release also records two audit repairs explicitly: a corrected ternary restriction map for the `p=20161` anchor, and reopening of an earlier `d=8` compression that failed to account for multiple `d=8` fibres. New campaign claims are kept separate from the August replay bank until receipt hardening is complete.

## Exact finite results

All four results below are independently recomputed by [`tools/replay_eg203_gold.py`](tools/replay_eg203_gold.py), using exact rational arithmetic. The recorded output is in [`receipts/replay-eg203-gold-2026-08-31.json`](receipts/replay-eg203-gold-2026-08-31.json).

| id | statement | recomputed value |
|---|---|---|
| G28 | primes `p>3` with `n_p | 5040` | **31 fibres**, total raw density **143/140**; the relevant gcd factorization is complete |
| G29 | the `N=5040` fibre family cannot cover for **any** phase assignment | `p=5` and `p=7` are mandatory; joint image exactly **24**; union density at most `143/140 - 1/24 = 823/840 < 1` |
| G30 | all phase assignments for the `{5,7,11,13}` core on the `60×60` torus | all **2,880** assignments checked; maximum union density **353/720**; unavoidable overlap **79/720** |
| G31 | primes `p<=10^6` with `n_p<=1000` | **238 fibres**, total raw density about **1.83048759933…**; all already occur below `10^5`; largest prime **67033** |

**G29 is an exact impossibility theorem**, not merely an unsuccessful search: forced overlap proves that the first common-period fibre family with raw density above 1 still cannot cover the exponent torus.

G30 gives a reusable upper bound for any larger family containing the four-prime core.

## Mathematical representation

Let

```text
n_p = |<2,3> mod p|.
```

The relation lattice `R_p ⊂ Z²` has index `n_p`; each prime therefore eliminates one coset of density `1/n_p`. CRT controls the phase independently across primes.

The August theorem inventory is in [`CANONICAL_GOLD.md`](CANONICAL_GOLD.md), entries EG203-G1 through G34. The current audited research frontier is in [`docs/KBK_PROGRESS_2026-09-13.md`](docs/KBK_PROGRESS_2026-09-13.md). Historical derivation records are in [`docs/provenance/`](docs/provenance/).

## Lean formalization status

`Erdos203All.lean` and the module files currently provide the project structure for a Lean formalization, but the headline finite obstruction theorems above have **not yet been formalized in Lean in this repository**.

The planned order is:

```text
203-001 relation lattice          203-005 essential torsion multiplicity
203-002 CRT phase realization     203-006 canonical quotient / SNF
203-003 forced-overlap bound      203-007 exact coset intersections
203-004 exact N=5040 obstruction  203-008 search-soundness theorem + first receipt
```

Toolchain: `leanprover/lean4:v4.31.0-rc1`, Mathlib `master-2026-05-31`.

## Reproduce the computations

```bash
python tools/check_gold_arithmetic.py
python tools/replay_eg203_gold.py
```

For the Lean project structure:

```bash
elan toolchain install $(cat lean-toolchain)
lake exe cache get
lake build
```

GitHub Actions reruns the arithmetic computations from source rather than accepting the checked-in JSON receipt as proof by itself.

## Scope and research record

- [`CONTRIBUTING.md`](CONTRIBUTING.md) describes how theorem, computation, program, refutation, and audit contributions are recorded.
- [`docs/QUARANTINE.md`](docs/QUARANTINE.md) preserves earlier routes that were retracted or never proved, including the cover=partition Fourier identity, static torsion peel, an unsupported equivalence between finite covers and the full problem, and newly audited September live-derivation errors.
- [`docs/CEGAR_PROTOCOL.md`](docs/CEGAR_PROTOCOL.md) describes the exact iterative search procedure and the meaning of its UNSAT outcomes.

The finite prime-fibre construction is a sufficient route to a solution, not a proof that every possible #203 solution must arise that way. That is the boundary of this branch; it does not qualify G29 or G30 within their stated finite setting.

## Sibling repositories

| repository | contents |
|---|---|
| [erdos203](https://github.com/jaredwilder/erdos203) | this finite prime-fibre obstruction program |
| [erdos411](https://github.com/jaredwilder/erdos411) | Erdős–Graham #411 reduction/cascade/formal work |
| [erdos902](https://github.com/jaredwilder/erdos902) | Schütte/Erdős tournament theory and finite structure |

## References

- P. Erdős and R. L. Graham, *Old and new problems and results in combinatorial number theory*, Monographies de L'Enseignement Mathématique 28 (1980).
- [erdosproblems.com/203](https://www.erdosproblems.com/203)
- Research context: https://epassports.eu/research/erdos-graham-203

## License

Apache 2.0, following Mathlib.