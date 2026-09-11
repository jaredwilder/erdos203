# Erdős–Graham Problem #203 — finite prime-fibre obstruction calculus

**Exact structural results, replayed finite computations, and a reproducible search engine for the finite prime-fibre cover architecture in Erdős–Graham #203.** The strongest current result in this branch is an exact impossibility theorem for the first common-period shell whose raw fibre mass exceeds 1.

For a prime `p > 3`, the exponents killed by `p` form one coset of the relation lattice
`R_p = {(u,v) : 2^u·3^v ≡ 1 (mod p)}`. Phase choices are independently selectable by CRT, turning this branch into a finite geometric covering problem before arithmetic realization.

The source problem asks:

> Is there an integer m ≥ 1 with (m,6) = 1 such that none of 2^k·3^ℓ·m + 1 are
> prime, for any k, ℓ ≥ 0?

This repository studies one sufficient certificate architecture: a finite set of prime fibres whose chosen cosets cover every exponent pair. The architecture is not assumed equivalent to the full problem; the exact branch scope is recorded in `docs/QUARANTINE.md`.

## Replayed computational results

All four computational gold claims are **independently replayed on commit** by
[`tools/replay_eg203_gold.py`](tools/replay_eg203_gold.py) (Python stdlib, exact
rational arithmetic; receipt in
[`receipts/replay-eg203-gold-2026-08-31.json`](receipts/replay-eg203-gold-2026-08-31.json),
verdict `ALL_MATCH`):

| id | claim | replayed value |
|---|---|---|
| G28 | census of primes p > 3 with n_p \| 5040 | **31 fibres**, raw mass **143/140** (complete: the gcd(2^5040−1, 3^5040−1) factorization fully resolved) |
| G29 | the N=5040 pool cannot cover, for **any** phase assignment | p=5, p=7 fibres mandatory; joint image exactly **24**; union ≤ 143/140 − 1/24 = **823/840 < 1** |
| G30 | {5,7,11,13} core, all **2880** phase assignments on the 60×60 torus | max union density **353/720**; unavoidable overlap tax **79/720** |
| G31 | census p ≤ 10⁶ with n_p ≤ 1000 | **238 fibres**, raw mass ≈ **1.83048759933…**; all 238 already occur below **10⁵** (none are added for 10⁵ < p ≤ 10⁶); largest census prime **67033** |

**G29 is a theorem, not a failed search:** the first common-period shell whose raw mass exceeds 1 is exactly impossible by forced overlap. G30 supplies a reusable phase-universal upper bound for any pool containing those four fibres.

## The representation

For a prime p > 3, let n_p = |⟨2,3⟩ mod p| and let R_p ⊂ ℤ² be the relation lattice
{(u,v) : 2^u·3^v ≡ 1 (mod p)}. The exponent pairs killed by p form one coset of R_p of
density 1/n_p, and the phase (which coset) is freely and independently selectable per
prime by CRT - so cover synthesis is finite geometry first, arithmetic realization
second. The full theorem/engine ledger is [`CANONICAL_GOLD.md`](CANONICAL_GOLD.md)
(items EG203-G1 … G34), with session provenance in
[`docs/provenance/`](docs/provenance/).

## Formalization state

The Lean spine (`Erdos203All.lean` and the module files) is a **scaffold**: the modules
compile-ready structure is in place, but **no theorem is formalized here yet**
(`LEAN_GENERATED / NOT KERNEL-CHECKED`). The porting queue, in order:

```text
203-001 relation lattice          203-005 essential torsion multiplicity
203-002 CRT phase realization     203-006 canonical quotient / SNF
203-003 forced-overlap bound      203-007 exact coset intersections
203-004 exact N=5040 kill         203-008 CEGAR soundness + first receipt
```

Toolchain pin: `leanprover/lean4:v4.31.0-rc1`, Mathlib `master-2026-05-31` (matching
the sibling repository [erdos902](https://github.com/jaredwilder/erdos902)).

## Verify

```bash
python tools/check_gold_arithmetic.py     # the two load-bearing fractions
python tools/replay_eg203_gold.py         # full G28–G31 replay (~2 min)
```

```bash
elan toolchain install $(cat lean-toolchain)
lake exe cache get
lake build                                # kernel gate for the (currently empty) spine
```

GitHub Actions runs the Lean scaffold build and both arithmetic replay checks on pushes
and pull requests. The checked-in JSON receipt remains the frozen release record; CI
recomputes the claims from source rather than trusting that file.

## Scope and discipline

- [`CONTRIBUTING.md`](CONTRIBUTING.md) - every tracked contribution is a THEOREM /
  COMPUTATION / ENGINE / KILL / AUDIT with explicit family scope and axiom footprint.
- [`docs/QUARANTINE.md`](docs/QUARANTINE.md) - retracted or never-proved routes
  (cover=partition Fourier identity, static torsion peel, finite-cover ⟺ EG203, …)
  that must not be reused without new proof.
- [`docs/CEGAR_PROTOCOL.md`](docs/CEGAR_PROTOCOL.md) - the exact master/adversary
  search loop and what its two UNSAT outcomes certify.

The finite prime-fibre architecture is a sufficient certificate shape, not an equivalence to every possible #203 witness. That is the remaining boundary of this repository, not a qualification on G29/G30 themselves.

## Sibling repositories

| repo | target | status |
|---|---|---|
| [erdos203](https://github.com/jaredwilder/erdos203) | Erdős–Graham #203 | finite prime-fibre obstruction frontier (this repo) |
| [erdos411](https://github.com/jaredwilder/erdos411) | Erdős–Graham #411 (r=2) | reduction + cascade + ω-ladder |
| [erdos902](https://github.com/jaredwilder/erdos902) | Erdős #902 (Schütte) | classical bounds and finite structure kernel-checked |

## References

- P. Erdős and R. L. Graham, *Old and new problems and results in combinatorial
  number theory*, Monographies de L'Enseignement Mathématique 28 (1980).
- [erdosproblems.com/203](https://www.erdosproblems.com/203) - problem page.
- Research context: [epassports.eu/research/erdos-graham-203](https://epassports.eu/research/erdos-graham-203).

## License

Apache 2.0, following Mathlib.