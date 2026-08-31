# EG203 internal-estate recovery — 2026-08-31

This note records stronger EG203 work recovered from the earlier research estate while
hardening this repository for public review. It exists to stop later work from being lost
or accidentally replaced by a weaker public summary.

Nothing below is promoted into the repository's main claim table merely because an old
memo said it happened. Promotion requires the original source or receipt to be restored
here and replayed against the stated boundary.

## Ready to recover as hard artifacts

### Bounded universal closure through m <= 10^6

The earlier EG203 formal corpus contained a theorem named
`EG203_nat_form_for_ordinary_m_up_to_1000000` in `EG203BoundedClosure.lean`:

```lean
theorem EG203_nat_form_for_ordinary_m_up_to_1000000 :
    ∀ m : Nat, 1 ≤ m → m ≤ 1000000 → Nat.Coprime m 6 →
      ∃ k l : Nat, Nat.Prime (m * 2 ^ k * 3 ^ l + 1)
```

The estate records this as kernel-verified by explicit witnesses and `native_decide`, with
`k+l <= 12`. This is a genuine bounded theorem, not evidence for the universal statement.

**Public promotion gate:** restore the original Lean source, pin its old toolchain/Mathlib
version, run the target, record `#print axioms`, then port or vendor it into this repository.

### Explicit prime-witness scale ladder

The earlier corpus also records explicit prime witnesses continuously across scale bands
through 10^19, including a 20-digit prime witness. This is strong stress evidence and useful
formal infrastructure, but it is not a universal theorem.

**Public promotion gate:** restore the scale files and receipts, verify each named witness,
and state the sampled/constructed scope exactly.

### Full direct empirical sweep through 10^10

A later estate record states that all 3,333,333,333 integers coprime to 6 in `[1,10^10]`
were tested for a prime witness, with zero failures and maximum first-prime diagonal 26 at
`m = 6,257,518,159`, witness `(k,l)=(16,10)`. The record also gives an aggregate receipt hash.

**Public promotion gate:** recover the 176 non-overlapping receipts and independent verifier
before putting this in the README. Until then, treat the number as a recovery lead, not a
repository-certified result.

## Later analytic frontier recovered from the estate

The June closure manuscripts were not the end of the EG203 analytic work. Later work moved
the live gap into a Kummer/PHNC distribution problem and produced several method-level
results.

### Density-zero exceptional set

The estate marks an unconditional density-zero theorem for the exceptional set as a gold
finding, with source recorded as `companion_gamma_fiber_local_density.tex`.

**Promotion gate:** recover the paper/source, verify every cited analytic input, and extract
the exact theorem statement and quantifiers before adding it to `CANONICAL_GOLD.md`.

### Discriminant barrier and Bilinear-Kummer equivalence

The estate records a theorem that a log-free zero-density approach based only on analytic
conductor is capped near

```text
ell << log Q / log log Q
```

because the cyclotomic Kummer discriminant has size `ell^(ell-2)`. The same paper identifies
the PHNC step with a named Type-II bilinear estimate (`TKB_ell`). These are method/barrier
theorems, not a proof of EG203.

The old audit also flags two zero-density theorem citations whose exact published theorem
locations still needed verification. That flag must remain attached when the paper is
recovered.

### Sharp PHNC dichotomy

The later technique ledger states an unconditional PHNC result in the low-ell range
`ell <= log Q / log log Q`, with the sole analytic seam moved to

```text
log Q / log log Q < ell < log Q.
```

This is potentially the most important recovered statement for the next universal attack.
It should not be promoted until the original Paper 17 source and its Thorner/Zaman inputs
are rechecked line-by-line.

## Formal reduction recovered, but not a closure

The earlier Lean corpus proves the exact equivalence

```lean
EG203Closed <-> NoProperOrdinaryInfiniteCRTShadow
```

and the implication from the named shadow-rigidity proposition to `EG203Closed`.
That is a valid exact reformulation/closure box. It is **not** an unconditional proof of
shadow rigidity, and later internal review correctly removed the old "closed by shadow
rigidity" headline.

If restored, this belongs in the repository as a formal reduction and regression guard, not
as the final theorem.

## Quarantined old claims

Do not revive these without a new proof:

- the old unconditional "shadow rigidity" headline;
- circular R11/R14/Iwaniec-style prime-count axioms;
- the chain-103 uniform `1/128` claim (an exact `m=19` counterexample was later recorded);
- any statement that finite prime-fibre cover is equivalent to EG203;
- any tested-family periodic-cover kill promoted to a universal theorem.

## Current best synthesis

The public repository currently contains a new exact coset-cover / relation-lattice attack
with replayed finite results. The recovered estate adds a different, older line of strength:

1. a hard bounded theorem through `m <= 10^6`;
2. large-scale explicit witness evidence;
3. later analytic/Kummer work that localizes a candidate universal closing seam.

These lines should be reunited, not treated as competing histories. The next full attack
should start from the union of both estates.
