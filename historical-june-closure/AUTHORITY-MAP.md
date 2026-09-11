# EG203 historical June 2026 proof package — authority map

**This is a historical proof-attempt archive, not an unconditional closure of Erdős–Graham #203.**

The recovered 2026-06-03 package contains **144 files**, including **125 Lean files**. Its own final README explicitly states that full EG203 is **not closed unconditionally in Lean**. The strongest `eg203_closed_atomic` theorem depends on Mathlib defaults plus two named mathematical-content axioms:

1. `V_family_singular_series_uniform_lower_bound`;
2. `wilder_2026_V_family_rosser_iwaniec`.

Those statements are not single published theorems quoted verbatim. The second is the package's composite specialization of cited analytic-number-theory inputs; the first is a structural uniform lower-bound assumption. The accompanying V-family manuscript was a preprint draft, not a peer-reviewed proof.

## Authority classes

### A. Unconditional / kernel-compositional mathematics

The historical package identifies the following as zero-new-mathematical-axiom infrastructure, subject to the usual distinction between ordinary kernel proofs and finite `native_decide` certificates:

- `chain-103/tier-0/`: moment laws, Size5, order facts, persistence, inverse-residue and Nat/ZMod bridge machinery;
- most retained `chain-103/R13/`: m-dependent density, Sylow/orbit-stabilizer, CRT and scaling infrastructure;
- retained nondeprecated `chain-103/R14/`: Buchstab identity/application, finite-range f(s) machinery, full-lattice/Sylow/period-lifting infrastructure, Mertens lemmas, V-family injectivity/size machinery, and Pappalardi finite-hypothesis discharge;
- `bounded/EG203BoundedClosure.lean`: the finite ordinary-m closure through 1,000,000, using `native_decide` in the certificate layer;
- `scale-ladder/`: finite prime-witness certificates at successively very large test scales;
- `source-pinned-540/`: 540 source-pinned finite frontier exceptions, again finite/certificate mathematics.

Finite certificates are **not** universal closure.

### B. Conditional closure layer

`closure/EG203AtomicCitations.lean` packages a full `EG203Closed` conclusion with axiom footprint

`[propext, Classical.choice, Quot.sound, V_family_singular_series_uniform_lower_bound, wilder_2026_V_family_rosser_iwaniec]`.

`closure/EG203PeerClosure.lean` uses the composite `eg203_analytic_NT_input` instead. These are valid conditional Lean compositions: they do **not** prove the named analytic inputs.

`closure/DischargeVFamily.lean` and `closure/EG203AnalyticDescentScaffold.lean` are scaffolding/bridge objects and must be cited with their assumptions visible.

### C. Deprecated/circular historical branch

The R14/Iwaniec history contains explicitly deprecated files/axiom shapes where the conclusion was essentially the conjecture itself, plus a previously inconsistent monotonicity-style axiom. The recovered package includes `chain-103/R14/Iwaniec/CIRCULAR-AXIOMS-DEPRECATED.md` precisely to prevent these from being mistaken for proof authority.

The package's own warning is decisive: historical theorems named like `eg203_closed_unconditional` that still inherit such axioms are **not unconditional proofs** merely because Lean accepts the term.

### D. Empirical layer

The historical project also recorded large Python/SymPy searches (billions of ordinary m in the original campaign narrative). Those are empirical evidence only. The present public authority map does not upgrade them to theorem status.

## Release policy

This directory exists so that the June 2026 proof attempt is inspectable without erasing mistakes. Use the current `erdos203`, `erdos203-obstruction-calculus`, and `eg203-kummer-papers` repositories for the later research state. Cite this historical package only with the authority class of the specific artifact.

A byte-level SHA-256 manifest of all 144 recovered files is released alongside this map. Large generated finite witness sources are represented in that manifest even when not duplicated as hand-curated theorem pages.
