# ERDŐS–GRAHAM #203 — CANONICAL GOLD v1.0
## Theorem bank, computation bank, quarantine, formalization ledger, and live closure frontier

**Release date:** 2026-08-31  
**Target status:** OPEN  
**Purpose:** this is the internal action document. It is not a transcript and it is not a claim of closure.

---

# 0. SOURCE TARGET AND SCOPE REPAIR

Target investigated:

\[
\exists m\in\mathbb N,\quad \gcd(m,6)=1,\quad
\forall k,\ell\ge0,\quad m2^k3^\ell+1\text{ is composite}.
\]

## Permanent scope repair

A **finite prime-fibre cover** is a sufficient certificate for such an integer \(m\): choose one prime divisor fibre for each selected prime, synthesize phases geometrically, then use CRT to realize all prime residues simultaneously.

It is **not** currently established that every hypothetical EG203 witness admits a finite prime-fibre subcover.

Therefore the canonical architecture is typed:

```text
EG203
├─ NEGATED / COUNTEREXAMPLE CERTIFICATE BRANCH
│    finite prime-fibre cover → CRT(m) → EG203 witness
└─ DIRECT / UNIVERSAL BRANCH
     prove every m has a prime value somewhere
```

Forbidden promotion:

```text
FINITE PRIME-FIBRE CERTIFICATE BRANCH
≠
EQUIVALENT FORMULATION OF ALL EG203
```

MSL failure code: `FINITE_CERTIFICATE_TO_TARGET_EQUIVALENCE`.

---

# 1. CANONICAL STATUS VOCABULARY

```text
THEOREM
  derivation survived current audit

REPLAYED_COMPUTATION
  exact finite computation independently rerun in supplied release

ENGINE
  exact reduction / algorithm; has not closed EG203

OPEN
  promising bridge not proved

ROUTE_BANK
  method direction worth retaining; not theorem status

QUARANTINED
  invalid or overpromoted branch retained to prevent reuse

FORMAL_STATUS
  NOT_TARGETED | LEAN_READY | LEAN_GENERATED | KERNEL_CHECKED | KERNEL_FAILED
```

No `LEAN_GENERATED` result may be called formal proof until a pinned project builds it.

---

# 2. CORE REPRESENTATION BANK

## EG203-G1 — relation lattice — THEOREM

For prime \(p>3\), define

\[
R_p=\{(u,v)\in\mathbb Z^2:2^u3^v\equiv1\pmod p\}.
\]

The homomorphism

\[
\psi_p:\mathbb Z^2\to\langle2,3\rangle_p,
\qquad (u,v)\mapsto2^u3^v\pmod p
\]

has kernel \(R_p\). Hence

\[
\mathbb Z^2/R_p\cong\langle2,3\rangle_p,
\qquad [\mathbb Z^2:R_p]=n_p:=|\langle2,3\rangle_p|.
\]

For fixed \(m\) and selected prime \(p\nmid m\), the exponent pairs on which \(p\mid m2^k3^\ell+1\) form either no fibre or one coset \(v_p+R_p\).

**Scope:** theorem about one prime fibre. The finite-cover use is a sufficient certificate architecture, not a complete reformulation of EG203.

## EG203-G2 — finite phases are CRT-independent — THEOREM

For finitely many distinct selected primes, any realizable phase choice gives one congruence on \(m\) modulo each prime. Pairwise coprimality lets CRT realize all selected phase choices simultaneously.

```text
GEOMETRIC PHASE SYNTHESIS
→ CRT REALIZATION OF m
```

## EG203-G3 — generator-free state — THEOREM

Discrete logarithm coordinates are implementation coordinates. The canonical object is the relation lattice \(R_p\), exposing index, intersections, quotient structure, SNF, and annihilator data without generator dependence.

---

# 3. CANONICAL FINITE QUOTIENT / CHARACTER BANK

## EG203-G4 — common-kernel quotient — THEOREM

For finite selected prime set \(P\):

\[
\Lambda_P=\bigcap_{p\in P}R_p,
\qquad G_P=\mathbb Z^2/\Lambda_P.
\]

Coverage by all selected fibres is constant on \(\Lambda_P\)-cosets. Smith normal form yields

\[
G_P\cong C_{d_1}\times C_{d_2},\qquad d_1\mid d_2.
\]

This is the exact finite adversary state **for that selected finite pool**.

## EG203-G5 — cyclic-character level sets — THEOREM

Every selected prime induces a surjective character

\[
\chi_p:G_P\to C_{n_p}
\]

and its fibre is one level set

\[
C_p=\{x\in G_P:\chi_p(x)=c_p\}.
\]

Thus finite synthesis is:

\[
\exists(c_p)_{p\in P}\ \forall x\in G_P\ \exists p\in P:\chi_p(x)=c_p.
\]

## EG203-G6 — future-equivalence quotient — THEOREM

States identical under all future local observations are semantically identical for the current finite model and must be quotient-merged.

---

# 4. TORSION / LOCAL GEOMETRY BANK

## EG203-G7 — primary decomposition — THEOREM

If \(n_p=\prod_q q^{e_{p,q}}\), the fibre decomposes into local primary conditions. The covering predicate becomes OR-of-ANDs across components.

## EG203-G8 — local capacity — NECESSARY THEOREM

On a frozen outer branch, if surviving \(q\)-dependent fibres have total possible \(q\)-primary mass below one, that branch cannot close.

Permanent separator:

\[
\text{capacity}\ge1\not\Rightarrow\text{positional closure}.
\]

## EG203-G9 — local hole object — THEOREM

For frozen outer state and surviving set \(S\):

\[
HOLE_q(S)=\{y:\forall p\in S,\ y\notin C_{p,q}\}.
\]

`HOLE_q(S)=∅` is the exact local closure condition.

## EG203-G10 — torsion rank / slope — THEOREM

Modulo torsion prime \(q\), active local characters span rank \(\rho_q\in\{0,1,2\}\). Nonzero characters define projective slopes in \(\mathbb P^1(\mathbb F_q)\).

## EG203-G11 — planar torsion → affine plane — THEOREM

When \(\rho_q=2\), local state is \(AG(2,q)\cong\mathbb F_q^2\), and local fibre constraints are affine lines.

## EG203-G12 — affine-plane line-cover minimum — THEOREM

Any affine-line cover of \(AG(2,q)\) requires at least \(q\) lines. Equality forces one complete parallel class.

## EG203-G13 — two-slope criterion — THEOREM

For two independent coordinate slopes with available phase sets \(A,B\), the uncovered set is

\[
(\mathbb F_q\setminus A)\times(\mathbb F_q\setminus B).
\]

Closure occurs iff one slope family contains every phase.

## EG203-G14 — three-slope Cauchy–Davenport gate — THEOREM

For three normalized slopes with missing-phase sets \(M_\infty,M_0,M_1\), hole-free implies

\[
|M_\infty|+|M_0|+|M_1|\le q+1.
\]

Equivalent available-phase lower bound:

\[
|\Gamma_\infty|+|\Gamma_0|+|\Gamma_1|\ge2q-1.
\]

---

# 5. COVER / INTERSECTION BANK

## EG203-G15 — cover ≠ partition — PERMANENT LAW

The invalid identity

\[
\mathbf1_{\cup C_p}=\sum_p\mathbf1_{C_p}
\]

is quarantined unless disjointness is separately proved.

## EG203-G16 — private witnesses → indicator independence — THEOREM

An irredundant finite cover gives a private point for each selected fibre; evaluating indicators on private points yields an identity minor, so the indicators are linearly independent.

## EG203-G17 — individual coset Fourier support — THEOREM

For a coset \(v+R\) in a finite quotient, the Fourier support of its indicator is exactly \(R^\perp\). Combined with G16:

\[
|P|\le\left|\bigcup_{p\in P}R_p^\perp\right|.
\]

## EG203-G18/G19 — exact intersection oracle and density — THEOREM / ENGINE

A family of lattice cosets has nonempty intersection exactly when the corresponding integer-linear congruence system is consistent. SNF provides the consistency oracle. Nonempty intersections are cosets of \(\cap_iR_i\) and have density

\[
[\mathbb Z^2:\cap_iR_i]^{-1}.
\]

## EG203-G20 — intersection-poset Möbius verifier — ENGINE

Merge equal structured intersections and perform inclusion–exclusion/Möbius inversion over distinct intersection states. A finite family covers its exact quotient iff the computed union density equals one.

---

# 6. EXACT SEARCH ENGINE BANK

## EG203-G21 — exact synthesis game — THEOREM

\[
\exists c\ \forall x\ P(c,x)
\]

with phase variables in the master and uncovered quotient states in the adversary.

## EG203-G22 — finite CEGAR — ENGINE

```text
MASTER: choose phases satisfying accumulated witness cuts
ADVERSARY: find uncovered state x
COUNTEREXAMPLE: add exact cut requiring some fibre to cover x
ADVERSARY_UNSAT: exact cover certificate
MASTER_UNSAT: finite pool obstruction core
```

## EG203-G23 — translation symmetry — THEOREM

Translation of exponent states induces a coherent phase translation. Quotient phase assignments by this action before search; further quotienting may use automorphisms stabilizing the character multiset.

## EG203-G24/G25 — survivor-mask adversary / stateful elimination — ENGINE + HARD LAW

Local choices induce survivor masks. Only inclusion-minimal realizable masks matter to the adversary. A local component choice is a state transition, not a static deletion from the original pool.

## EG203-G26 — obstruction-core → character-first column generation — ENGINE

```text
UNSAT witness core X*
→ desired abstract cyclic character
→ arithmetic realization search
→ add realized prime column
→ resume exact CEGAR
```

## EG203-G27 — exponential-difference realization filter — NECESSARY FILTER

Compatible lifts of desired character relations force candidate realizing primes to divide explicit differences

\[
2^{b+sn}-3^{a+rn}.
\]

Divisibility is only a candidate generator; every candidate must pass exact relation-lattice/order verification.

---

# 7. REPLAYED COMPUTATIONAL BANK

## EG203-G28 — period 5040 census — REPLAYED COMPUTATION

For

\[
U_{5040}=\{p>3:n_p\mid5040\},
\]

the supplied replay reports:

```text
31 prime fibres
raw mass = 143/140
```

Equivalent fixed-period prime census:

\[
p\mid\gcd(2^{5040}-1,3^{5040}-1).
\]

## EG203-G29 — 5040 forced-overlap impossibility — THEOREM + REPLAYED ARITHMETIC

The \(p=5\) density is \(1/4\); the \(p=7\) density is \(1/6\). Removing either drops raw mass below one, so both are mandatory.

Their joint map has image size \(24\), so every phase pair intersects with density \(1/24\). Hence

\[
\operatorname{dens}\Big(\bigcup_{p\in U_{5040}}C_p\Big)
\le \frac{143}{140}-\frac1{24}
=\boxed{\frac{823}{840}<1}.
\]

Therefore the complete period-5040 finite fibre pool is impossible for every phase assignment.

## EG203-G30 — four-fibre overlap tax — REPLAYED COMPUTATION

For \(p\in\{5,7,11,13\}\), exhaustive enumeration of all \(2880\) phase assignments on the common period-60 torus reports

\[
\max\operatorname{dens}(C_5\cup C_7\cup C_{11}\cup C_{13})
=\frac{353}{720}.
\]

Raw mass is \(3/5\), so unavoidable overlap loss is

\[
\boxed{\frac{79}{720}}.
\]

Reusable upper bound for any larger family containing these four fibres:

\[
\operatorname{dens}(\cup P)
\le\sum_{p\in P}\frac1{n_p}-\frac{79}{720}.
\]

## EG203-G31 — low-index finite universe — REPLAYED COMPUTATION

Census:

```text
p ≤ 10^6
n_p ≤ 1000
238 fibres
total raw mass ≈ 1.8304875993372494
largest prime = 67033
same 238 already complete by p ≤ 10^5
```

This is a stable experimental finite universe. No cover was certified.

---

# 8. UNIVERSAL STRUCTURAL BANK FOR FINITE CERTIFICATES

## EG203-G32 — essential torsion multiplicity — THEOREM

In an irredundant finite prime-fibre cover, if torsion prime \(q\) occurs essentially, then freezing a non-\(q\) state leaves a full \(q\)-primary cover obligation. Each \(q\)-dependent fibre occupies at most \(1/q\) of that component. Therefore

\[
\boxed{\#\{p:q\mid n_p\}\ge q}.
\]

## EG203-G33 — congruence consequence — THEOREM

Since \(n_p\mid p-1\), every counted prime satisfies

\[
p\equiv1\pmod q.
\]

## EG203-G34 — largest-torsion pressure — THEOREM

If \(Q\) is the largest prime divisor appearing in any selected fibre order of a hypothetical irredundant finite certificate, then

\[
\boxed{\#\{p:Q\mid n_p\}\ge Q}.
\]

Interpretation: introducing largest torsion \(Q\) incurs a **multiplicity debt of at least \(Q\) fibres**.

No universal arithmetic upper bound below \(Q\) is currently proved.

---

# 9. GEMINI / ANALYTIC ROUTE BANK — STATUS-CORRECTED

These are retained because the independent agent attacked the opposite polarity. They are not promoted to theorem status unless stated.

| Route | Canonical status | Exact value |
|---|---|---|
| linear sieve / parity | `BLOCKED_CURRENT_TECHNIQUE` | identifies parity barrier for naive prime detection |
| almost-prime + Type-II | `OPEN` | plausible escalation; no theorem obtained |
| Bateman–Horn direct transfer | `INAPPLICABLE_AS_STATED` | classical polynomial schema does not directly type-check on exponential 2-parameter family |
| exponential-sum level of distribution | `BLOCKED_CURRENT_TECHNIQUE` | thin/lacunary ambient set is the specific obstacle |
| Baker / S-unit / large prime factor | `OPEN` | large prime factors do not themselves force primality |
| Romanoff-style 2-D density transfer | `QUARANTINED` | claimed theorem not established |
| positive density of good m | `TRANSFER_REQUIRED` | does not imply every m is good |
| \(\sqrt{\log m}\) first-witness scale | `HEURISTIC` | useful computational scale, not closure |
| direct Maynard/GPY transplant | `INAPPLICABLE_AS_STATED` | direct dense-set averaging infrastructure absent; not a theorem against all sparse variants |

## Conditional anti-result from the Romanoff audit

For primes on which both 2 and 3 are primitive roots, the proposed Romanoff-series summand collapses to \(1/p\). Under the standard GRH simultaneous-Artin framework, such primes have positive prime density, so the proposed convergence series should diverge rather than converge.

**Status:** `CONDITIONAL_RESULT`; this kills that specific convergence route, not EG203.

---

# 10. QUARANTINE — DO NOT REUSE WITHOUT NEW PROOF

```text
Q203-01  finite-cover iff EG203
          INVALID / SCOPE INFLATION

Q203-02  cover indicator = sum of fibre indicators
          INVALID unless disjoint partition is proved

Q203-03  static 238→93 torsion peel
          INVALID as static reduction; valid only as stateful branch transition

Q203-04  tested periodic families → all periodic covers through tested scale
          INVALID family-scope lift

Q203-05  Bateman-Horn name → exponential family asymptotic
          AUTHORITY_SCHEMA_MISMATCH

Q203-06  Romanoff 2-D positive-density theorem
          UNVERIFIED / quarantine

Q203-07  positive density → pointwise universality
          DENSITY_TO_POINTWISE

Q203-08  search saturation → no new mathematics
          SEARCH_STATE_AS_THEOREM

Q203-09  global dimension-two phase-transition theorem
          INVALID generalization; retain only exact local torsion geometry

Q203-10  standard Maynard transfer fails → all Maynard-type methods impossible
          ROUTE_BLOCK_AS_IMPOSSIBILITY
```

---

# 11. THE HYBRID FRONTIER — HIGHEST-VALUE OPEN BRIDGE

The two independent proof geometries now give a sharply typed hybrid target.

Finite geometry gives:

\[
Q\text{ essential largest torsion}
\Longrightarrow
\text{at least }Q\text{ distinct }Q\text{-dependent fibres}.
\]

The analytic/arithmetic side should therefore attack **cluster realizability**, not generic prime detection:

```text
HYBRID-H1
INPUT:
  largest torsion prime Q
  Q-primary slope/phase obligations
  maximal-torsion constraint on all selected n_p
  cross-component compatibility inherited from one finite certificate

TARGET:
  prove that no set of Q distinct arithmetic prime fibres
  can simultaneously realize the required Q-torsion geometry.
```

A raw bound on the number of primes \(p\equiv1\pmod Q\) is not the right question. The target is the much narrower set of primes whose **actual relation lattices and subgroup orders** realize a compatible torsion cluster inside one certificate.

### Bidirectional KBK

If arithmetic proves `<Q` compatible carriers: G34 detonates and kills that finite-certificate branch.

If arithmetic finds many compatible carriers: feed their exact character/slope signatures into CEGAR as a torsion-closed acquisition cluster instead of enumerating isolated primes.

This is the canonical cross-session frontier.

---

# 12. FORMALIZATION LEDGER

The supplied release reports a Lean-generated close attempt but not a kernel run in that environment. Therefore the import baseline is deliberately conservative.

| ID | theorem / artifact | project status | target formal status | dependency |
|---|---|---:|---:|---|
| L203-001 | relation lattice / kernel-coset equivalence | theorem banked | `KERNEL_CHECKED` | Mathlib group/subgroup basics |
| L203-002 | finite phase realization by CRT | theorem banked | `KERNEL_CHECKED` | CRT |
| L203-003 | canonical quotient by common kernel | theorem banked | `KERNEL_CHECKED` | subgroup quotient + SNF bridge |
| L203-004 | essential torsion multiplicity G32 | theorem banked | `KERNEL_CHECKED` | finite-cover local mass lemma |
| L203-005 | generic forced-overlap union upper bound | theorem banked | `KERNEL_CHECKED` | finite sets / cardinality |
| L203-006 | exact 5040 arithmetic closure | theorem + replay | `KERNEL_CHECKED` | L203-005 + exact constants |
| L203-007 | exact coset-intersection consistency | theorem/engine | `KERNEL_CHECKED` | integer linear systems / SNF |
| L203-008 | intersection-poset Möbius verifier | engine | `KERNEL_CHECKED` or small checker theorem | L203-007 |
| L203-009 | four-fibre `79/720` certificate | replayed computation | `KERNEL_CHECKED` | finite certificate / `decide` preferred if tractable |
| L203-010 | finite CEGAR soundness | engine | `KERNEL_CHECKED` | finite-domain semantics |

`KERNEL_CHECKED` above is the **goal state**, not a claim that this release ran Lean. The scaffold marks imported code as `LEAN_GENERATED` until your machine builds it.

---

# 13. COMPUTATION / RECEIPT LEDGER

Every computational contribution should ship four things:

```text
1. frozen input definition
2. deterministic generator/checker
3. raw output / certificate
4. SHA-256 receipt + exact claim boundary
```

Priority replays:

```text
C203-001  U_5040 census = 31 fibres, mass 143/140
C203-002  forced 5/7 overlap = 1/24, union ≤ 823/840
C203-003  4-fibre 2880 phase enumeration, max 353/720
C203-004  low-index 238-fibre census
C203-005  first full exact CEGAR over a frozen pool
```

---

# 14. IMMEDIATE CONTRIBUTION SEQUENCE

```text
COMMIT 1  repo skeleton + exact source target + status boundary
COMMIT 2  relation-lattice definitions + basic kernel lemmas
COMMIT 3  CRT phase realization
COMMIT 4  forced-overlap generic theorem + 5040 arithmetic theorem
COMMIT 5  essential torsion multiplicity theorem
COMMIT 6  deterministic replay scripts + receipts for G28-G31
COMMIT 7  canonical quotient / SNF bridge
COMMIT 8  exact intersection oracle
COMMIT 9  CEGAR engine with frozen semantics and witness cuts
COMMIT 10 first obstruction-core → character-first acquisition experiment
```

Do not start by importing every exploratory branch. Start with the smallest theorem spine that creates a trustworthy repository history.

---

# 15. CLOSURE CONDITIONS

## Negative / counterexample-certificate closure

```text
finite prime set P
+ exact phase cover of G_P
+ independent cover verifier
+ CRT realization of m
+ proof that every exponent pair is covered by a divisor prime
+ kernel-checked bridge
→ EG203 witness
```

## Positive / universal closure

A theorem of the form

\[
\forall m\ (\gcd(m,6)=1\Rightarrow\exists k,\ell:\ m2^k3^\ell+1\text{ prime})
\]

with every analytic authority bound to an exact theorem signature and every density/average statement bridged to the required pointwise quantifier.

## Current state

Neither closure exists. The strongest banked finite-certificate obstructions are:

```text
5040 pool impossible
79/720 universal overlap tax on {5,7,11,13}
essential q-torsion costs at least q q-dependent fibres
```

The strongest live architecture is:

```text
torsion-closed arithmetic fibre clusters
→ canonical quotient G_P
→ symmetry-reduced exact CEGAR
→ cover certificate OR obstruction core
→ character-first arithmetic realization
→ repeat
```
