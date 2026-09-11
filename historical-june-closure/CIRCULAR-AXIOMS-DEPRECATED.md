# CIRCULAR AXIOMS — DEPRECATED 2026-06-02

Consolidation index of the five circular axiom files identified in the recovered June 2026 EG203 R14 proof attempt.

## TL;DR

Five historical axiom files shipped assumptions whose **conclusion is, modulo cosmetic bounds, Erdős–Graham #203 itself**. Asserting them amounts to assuming the conjecture. Downstream “closures” that merely destructure and repack those axioms are therefore not proofs of EG203.

The honest closure architecture is **count bound + count-to-existence composition**, not existence-form axioms.

## The five circular axiom shapes

1. `iwaniec_1980_thm_1_V_family_kappa_zero` — historical `R14/IwaniecLinearSieveVFamily.lean`.
2. `iwaniec_v_family_minimal_kappa_zero` — historical `R14/Iwaniec/IwaniecAxiomMinimal.lean`.
3. `iwaniec_v_family_numeric_evaluation` — historical `R14/Iwaniec/IwaniecMinimalNumericAxiom.lean`.
4. `iwaniec_1980_thm_1_abstract_linear_sieve_lower_bound` — historical `R14/Iwaniec/IwaniecAxiomDecomposition.lean`.
5. `iwaniec_1980_thm_1_tightened_κ_zero` — historical `R14/Iwaniec/IwaniecAxiomTightened.lean`.

Their conclusions take forms such as

- `∃ k l, Nat.Prime (V m k l)`;
- bounded variants of the same existential;
- `∃ a ∈ A, Nat.Prime a` where `A` is the V-family sieve set.

Those are precisely the existence content that EG203 asks one to prove.

## Related but distinct count-bound interface

The later `IwaniecAxiomNonCircular.lean` changed the interface to a **count lower bound** rather than an EG203 existential. This is structurally noncircular, but the recovered audit still records placeholder/truth-matching issues in that historical implementation: a placeholder Mertens product, a vacuous κ=0 premise in an earlier form, and a piecewise `f(s)` whose out-of-range branch was zero. Therefore “noncircular interface” must not be read as “published theorem proved.”

## A vacuous auxiliary axiom

The historical decomposition also included a Pappalardi-labeled statement of the form

`∀ q prime ≥ 5, ∃ d, d ≥ (q-1)/2 ∧ d ∣ (q-1)`.

Taking `d=q-1` makes this trivially true, so it carries no substantive sieve information.

## Consequence for downstream files

Historical files with names such as `EG203UnconditionalClosure.lean`, `EG203KeystoneFinal.lean`, `EG203NumericKeystone.lean`, `EG203CleanComposition.lean`, and the tightened/decomposed closure variants may still type-check because the axioms exist. **Type-checking does not remove circularity.**

The audit's authoritative mathematical conclusion is:

> EG203 closure in the circular R14 branch is NOT proved. What is proved there is that EG203 follows from an axiom whose conclusion is EG203.

The circular branch is retained publicly as an autopsy and regression guard so it cannot silently return as proof authority.
