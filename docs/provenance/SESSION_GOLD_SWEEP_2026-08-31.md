# EG203 SESSION GOLD SWEEP — 2026-08-31

## Scope

Target investigated in this session:

\[
\exists m\in\mathbb N,\ \gcd(m,6)=1,\ \forall k,\ell\ge 0,\quad 2^k3^\ell m+1\ \text{composite}.
\]

This document is a theorem/reduction/computation ledger, not a claim that EG203 is closed.

Status vocabulary used here:

- **THEOREM** — derivation survived the session audit.
- **REPLAYED COMPUTATION** — exact finite computation rerun independently in the release package.
- **ENGINE** — exact reduction or algorithm whose correctness is established, but whose run has not closed EG203.
- **OPEN** — promising statement or bridge not yet proved.
- **RETRACTED** — invalid branch preserved to prevent reuse.

---

# I. CORE REPRESENTATION GOLD

## G1. Prime fibres are relation-lattice cosets — THEOREM

For every prime \(p>3\), define

\[
R_p:=\{(u,v)\in\mathbb Z^2:2^u3^v\equiv1\pmod p\}.
\]

The map

\[
\psi_p:\mathbb Z^2\to\langle2,3\rangle_p,
\qquad
(u,v)\mapsto 2^u3^v\pmod p
\]

is a group homomorphism with kernel \(R_p\). Hence

\[
\mathbb Z^2/R_p\cong\langle2,3\rangle_p,
\qquad
[\mathbb Z^2:R_p]=n_p:=|\langle2,3\rangle_p|.
\]

For fixed \(m\) with \(p\nmid m\), the exponent pairs for which \(p\mid 2^k3^\ell m+1\) are either empty or one coset of \(R_p\); because \(-m^{-1}\in\langle2,3\rangle_p\) is exactly the phase-realizability condition, a selected phase gives

\[
C_p=v_p+R_p.
\]

Load-bearing consequence:

\[
\boxed{\text{EG203 becomes a finite arithmetic coset-cover problem in }\mathbb Z^2.}
\]

---

## G2. Prime phases are jointly free by CRT — THEOREM

For a finite set of distinct primes \(P\), any choice of one residue target

\[
r_p\in\langle2,3\rangle_p
\]

for each \(p\in P\) determines a congruence

\[
m\equiv-r_p^{-1}\pmod p.
\]

The moduli are pairwise coprime, so CRT realizes all phase choices simultaneously by one integer \(m\).

Therefore the finite cover synthesis may treat the phase of each selected prime fibre as an independent categorical variable; CRT is applied only after the cover is found.

This is a critical separation:

\[
\boxed{\text{GEOMETRIC COVER SYNTHESIS}\quad\to\quad\text{CRT REALIZATION OF }m.}
\]

---

## G3. Generator-free formulation — THEOREM

Discrete-log coordinates \((a_p,b_p,c_p)\) are optional implementation coordinates. The canonical arithmetic object is \(R_p\) itself.

This removes generator choice from the mathematical state and exposes:

- finite index;
- intersections;
- quotient structure;
- Smith normal form;
- annihilators/characters;
- exact coset consistency.

KBK climb:

```text
DISCRETE-LOG STRIPE
→ relation lattice
→ generator-free coset geometry
→ exact integer-linear intersection machinery
```

---

# II. FINITE QUOTIENT / CHARACTER GOLD

## G4. Canonical adversary quotient — THEOREM

For a finite selected prime set \(P\), let

\[
\Lambda_P:=\bigcap_{p\in P}R_p.
\]

Every fibre \(v_p+R_p\) is constant on \(\Lambda_P\)-cosets. Hence coverage is constant on the finite quotient

\[
G_P:=\mathbb Z^2/\Lambda_P.
\]

Smith normal form gives

\[
G_P\cong C_{d_1}\times C_{d_2},\qquad d_1\mid d_2.
\]

Thus the exact finite adversary state is not an arbitrary \(N\times N\) torus but a canonical two-generator finite abelian group.

---

## G5. Every prime fibre is a cyclic-character level set — THEOREM

The quotient map induced by \(\psi_p\) is a surjective character

\[
\chi_p:G_P\to C_{n_p}
\]

and the fibre is

\[
C_p=\{x\in G_P:\chi_p(x)=c_p\}.
\]

So the finite problem is exactly:

\[
\boxed{\text{cover }C_{d_1}\times C_{d_2}\text{ by level sets of arithmetic cyclic characters}.}
\]

---

## G6. Future-equivalence quotient — THEOREM

If two exponent states have identical values under all local characters used by the current model, they have identical future coverage behavior. Their difference belongs to the common kernel. The quotient by this kernel is therefore lossless.

This was the session's first concrete proof that MSL needed generic `FUTURE_EQUIVALENCE` / `CANONICAL_QUOTIENT` vocabulary.

---

# III. TORSION / LOCAL GEOMETRY GOLD

## G7. Primary decomposition of a fibre — THEOREM

If

\[
n_p=\prod_q q^{e_{p,q}},
\]

then the congruence defining the prime fibre decomposes by CRT into local primary conditions:

\[
C_p=\bigcap_{q\mid n_p}C_{p,q}.
\]

Therefore the cover predicate has OR-of-ANDs form:

\[
\forall x,\qquad \bigvee_p\bigwedge_q C_{p,q}(x_q).
\]

---

## G8. Local capacity obstruction — THEOREM (necessary only)

Freeze all non-\(q\) coordinates. Let \(S_q\) be the prime fibres still alive. If their total possible \(q\)-primary mass is less than one, the branch cannot be completed by any choice of the remaining \(q\)-state.

The session correctly upgraded this from a heuristic residual statistic to a mathematical obstruction, then immediately discovered its limitation:

\[
\boxed{\text{capacity}\ge1\text{ does not imply positional closure}.}
\]

That failure forced the next object.

---

## G9. Exact local hole object — THEOREM

For a frozen outer state, define the local hole set

\[
HOLE_q(S):=\{y:\forall p\in S,\ y\notin C_{p,q}\}.
\]

Then

\[
HOLE_q(S)=\varnothing
\]

is exactly the condition that every \(q\)-lift of that outer state is covered.

Global cover is equivalent to absence of such holes on every frozen branch.

KBK climb:

```text
RESIDUAL DENSITY
→ LOCAL CAPACITY
→ capacity fails to encode overlap
→ HOLE_SET
→ exact local closure
```

---

## G10. Torsion rank / slope classifier — THEOREM

Modulo a torsion prime \(q\), each local character has a coefficient vector

\[
(a_p,b_p)\in\mathbb F_q^2.
\]

Let \(M_q\) be their span. Then

\[
\rho_q:=\dim_{\mathbb F_q}M_q\in\{0,1,2\}.
\]

Equivalently, each nonzero local character has projective slope

\[
\sigma_q(p)=[a_p:b_p]\in\mathbb P^1(\mathbb F_q).
\]

One active slope gives rank one; two distinct slopes give rank two.

This distinguishes genuinely one-dimensional torsion from planar torsion.

---

## G11. Planar torsion becomes finite affine-line geometry — THEOREM

When \(\rho_q=2\), choose two independent slopes as coordinates. The reduced mod-\(q\) primary state becomes

\[
AG(2,q)\cong\mathbb F_q^2,
\]

and every local fibre projects to an affine line.

Therefore local closure questions become exact finite-geometry line-cover questions.

---

## G12. Minimum affine-line cover — THEOREM

Any cover of \(AG(2,q)\) by affine lines uses at least \(q\) lines.

If exactly \(q\) lines cover the plane, they must be pairwise disjoint, hence all parallel, hence form one complete parallel class.

This theorem later becomes the engine behind the essential-torsion multiplicity result.

---

## G13. Two-slope exact criterion — THEOREM

If the only two available slopes are independent coordinate directions with available phase sets \(A,B\subseteq\mathbb F_q\), the uncovered set is

\[
(\mathbb F_q\setminus A)\times(\mathbb F_q\setminus B).
\]

Hence the two-slope local cover closes iff one of the two slope families contains every phase.

---

## G14. Three-slope Cauchy–Davenport obstruction — THEOREM

Normalize three distinct slopes so that their missing-phase conditions are

\[
\alpha\in M_\infty,\qquad
\beta\in M_0,\qquad
\alpha+\beta\in M_1.
\]

Hole-free implies

\[
(M_\infty+M_0)\cap M_1=\varnothing.
\]

For prime \(q\), Cauchy–Davenport gives

\[
|M_\infty+M_0|\ge\min(q,|M_\infty|+|M_0|-1),
\]

so hole-free forces

\[
\boxed{|M_\infty|+|M_0|+|M_1|\le q+1.}
\]

Equivalently, the three available-phase sets satisfy

\[
|\Gamma_\infty|+|\Gamma_0|+|\Gamma_1|\ge2q-1.
\]

This is a genuine additive-combinatorics local gate.

---

# IV. COVER / INTERSECTION GOLD

## G15. Cover is not partition — HARD RETAINED LESSON

The flow produced an attractive but invalid Fourier chain by implicitly replacing

\[
\mathbf 1_{\cup C_p}
\]

with

\[
\sum_p\mathbf 1_{C_p}.
\]

That replacement is valid for a disjoint partition, not an arbitrary cover.

The entire descendant chain that claimed global phase-weight uniformity was retracted.

This failure directly motivated canonical law `COVER_PARTITION_COLLAPSE`.

---

## G16. Private witnesses imply indicator-function independence — THEOREM

For an irredundant finite cover, each fibre has a private point belonging to it and no other selected fibre. Evaluating the fibre indicators on those private points yields an identity minor. Therefore the fibre-indicator functions are linearly independent.

---

## G17. Valid Fourier support theorem for an individual coset — THEOREM

For a coset \(v+R\) in a finite quotient, the Fourier support of its indicator is exactly the annihilator \(R^\perp\).

Combined with G16:

\[
\boxed{|P|\le\left|\bigcup_{p\in P}R_p^\perp\right|.}
\]

This is a legitimate global Fourier constraint because it uses Fourier analysis of individual indicators, not an invalid partition identity.

---

## G18. Exact coset-intersection oracle — THEOREM / ENGINE

A finite family of cosets

\[
v_i+R_i
\]

has nonempty intersection iff the corresponding integer linear congruence system is consistent. Writing lattice bases converts this to an integer linear system; Smith normal form gives an exact consistency test.

If nonempty,

\[
\bigcap_i(v_i+R_i)=v_I+\bigcap_iR_i.
\]

---

## G19. Exact intersection density — THEOREM

When the intersection is nonempty,

\[
\operatorname{dens}\left(\bigcap_i(v_i+R_i)\right)
=
\frac{1}{[\mathbb Z^2:\bigcap_iR_i]}.
\]

---

## G20. Intersection-poset Möbius certificate — THEOREM / ENGINE

Because many subsets of fibres can yield the same structured intersection coset, exact inclusion–exclusion can be aggregated over the poset of distinct intersection states.

Thus a finite prime-fibre family covers iff its exact union density, computed by Möbius inversion on that intersection poset, equals one.

This is an independent exact verifier for a candidate phase cover.

KBK climb:

```text
COVER ≠ PARTITION
→ preserve overlap
→ exact intersection oracle
→ intersection-state merge
→ Möbius cover certificate
```

---

# V. EXACT SEARCH-ENGINE GOLD

## G21. Phase synthesis is an exact \(\exists c\forall x\) game — THEOREM

For a fixed finite prime set:

\[
\exists(c_p)_p\ \forall x\in G_P\ \exists p:\chi_p(x)=c_p.
\]

This directly supports a master/adversary formulation.

---

## G22. Exact CEGAR loop — ENGINE

Master:

- choose prime phases satisfying accumulated witness cuts.

Adversary:

- seek \(x\in G_P\) missed by every selected fibre.

If the adversary finds \(x\), add the exact cut requiring some prime to cover \(x\).

If adversary is UNSAT, the current phase assignment is an exact cover.

If master is UNSAT, the current prime pool cannot satisfy all accumulated exact witness obligations; an UNSAT core can be extracted.

Finite-domain termination is exact.

---

## G23. Phase translation symmetry — THEOREM

Translation \(x\mapsto x+d\) induces

\[
c_p\mapsto c_p+\chi_p(d).
\]

The joint character map on \(G_P\) is injective by construction of the common kernel, so every translation orbit of phase assignments has size \(|G_P|\).

Therefore raw phase space

\[
\prod_p n_p
\]

can be quotient by a factor \(|G_P|\) before search, with further quotienting available from automorphisms stabilizing the character multiset.

---

## G24. Survivor-mask adversary — THEOREM / ENGINE

For each independent torsion component, each local state induces a mask of fibres surviving that component. An exponent state is globally uncovered iff one can choose one realizable mask per component whose intersection is empty.

Thus the adversary may operate on bitmasks rather than raw torus points.

If \(M\subseteq M'\) are two masks realizable by the same component, \(M'\) is never better for the adversary; only inclusion-minimal masks need be retained.

---

## G25. Stateful elimination law — THEOREM / RETRACTION REPAIR

A local torsion choice can annihilate a subset of fibres, but the choice also fixes that component for all surviving fibres. Therefore it is a state transition, not a static pool deletion.

The session initially treated a \(238\to93\) peel as static. That inference was retracted.

Correct state:

\[
(ALIVE,UNUSED)
\to
(ALIVE',UNUSED\setminus\{q\}).
\]

This directly motivated canonical hard law `STATEFUL_TO_STATIC`.

---

## G26. Obstruction-core → character-first column generation — ENGINE

If a finite phase master becomes UNSAT, retain a small witness set \(X^*\) that the current prime characters cannot simultaneously cover.

Search abstractly for a cyclic character

\[
\chi_{n,a,b}(k,\ell)=ak+b\ell\pmod n
\]

whose best phase contains as many points of \(X^*\) as possible.

Only after finding the desired abstract geometry does arithmetic realization search for a prime having that relation character.

This reverses blind prime enumeration:

```text
obstruction core
→ desired character
→ arithmetic realization
→ new prime column
→ resume exact CEGAR
```

---

## G27. Exponential-difference realization filter — THEOREM (necessary filter)

If an actual prime realizes a character represented by \((n,a,b)\), compatible lifts satisfy a relation of the form

\[
2^{b+sn}\equiv3^{a+rn}\pmod p.
\]

Hence candidate realizing primes occur among prime divisors of explicit lifted exponential differences

\[
2^{b+sn}-3^{a+rn}.
\]

Each candidate must still pass the exact relation-lattice/order test; divisibility alone is not sufficient.

---

# VI. REPLAYED COMPUTATIONAL GOLD

All results in this section are independently replayed by `replay_eg203_gold.py` in this release.

## G28. Exact \(N=5040\) census — REPLAYED COMPUTATION

Let

\[
U_{5040}=\{p>3:n_p\mid5040\}.
\]

Equivalent arithmetic census:

\[
p\mid\gcd(2^{5040}-1,3^{5040}-1).
\]

Replay result:

- 31 prime fibres.
- Exact raw mass:

\[
\sum_{p\in U_{5040}}\frac1{n_p}=\frac{143}{140}.
\]

This is the first tested common-period shell in the session with raw mass exceeding one.

---

## G29. \(N=5040\) is impossible by forced overlap — THEOREM + REPLAYED COMPUTATION

The \(p=5\) fibre has density \(1/4\); the \(p=7\) fibre has density \(1/6\).

Removing either fibre leaves raw mass below one:

\[
\frac{143}{140}-\frac14<1,
\qquad
\frac{143}{140}-\frac16<1.
\]

Hence both are mandatory in any hypothetical cover from this pool.

The joint map to the two subgroup coordinates has exact image size

\[
4\cdot6=24,
\]

so every pair of phases intersects with density

\[
\frac1{24}.
\]

Therefore

\[
\operatorname{dens}\left(\bigcup_{p\in U_{5040}}C_p\right)
\le
\frac{143}{140}-\frac1{24}
=
\frac{823}{840}
<1.
\]

Thus:

\[
\boxed{U_{5040}\text{ cannot cover for any phase assignment}.}
\]

This is an exact pool-impossibility theorem, not a failed search.

---

## G30. Four-fibre core exact overlap loss — REPLAYED COMPUTATION

For \(p\in\{5,7,11,13\}\), the common period is 60 and there are exactly

\[
4\cdot6\cdot10\cdot12=2880
\]

phase assignments.

Exhaustive enumeration of all 2880 assignments over the 3600-point \(60\times60\) torus gives

\[
\max_c\operatorname{dens}(C_5\cup C_7\cup C_{11}\cup C_{13})
=
\frac{353}{720}.
\]

Raw mass of those four fibres is

\[
\frac14+\frac16+\frac1{10}+\frac1{12}=\frac35.
\]

Therefore every phase assignment loses at least

\[
\boxed{\frac35-\frac{353}{720}=\frac{79}{720}}
\]

of raw density to overlap inside this four-fibre core.

For any larger family containing these same four fibres, a valid union upper bound is

\[
\operatorname{dens}(\cup P)
\le
\sum_{p\in P}\frac1{n_p}-\frac{79}{720}.
\]

This is a reusable phase-universal overlap certificate.

---

## G31. Low-index prime universe census — REPLAYED COMPUTATION

Census condition:

\[
p\le10^6,
\qquad
n_p=|\langle2,3\rangle_p|\le1000.
\]

Replay result:

- 238 prime fibres.
- Total raw mass approximately

\[
1.8304875993372494.
\]

- The exact same 238 fibres are already complete by \(p\le10^5\); the largest prime in the census is 67033.

This is a stable finite universe suitable for exact CEGAR experiments, but no cover was certified in the session.

---

# VII. UNIVERSAL STRUCTURAL GOLD FROM THE PROOF HUNT

## G32. Essential torsion multiplicity theorem — THEOREM

Consider an irredundant finite prime-fibre cover. Fix a torsion prime \(q\) occurring in at least one selected fibre.

Let

\[
P_0:=\{p:q\nmid n_p\},
\qquad
P_1:=\{p:q\mid n_p\}.
\]

Because the cover is irredundant and \(P_1\ne\varnothing\), \(P_0\) cannot already cover the whole state space. Hence there is a frozen non-\(q\) state not covered by any fibre in \(P_0\).

On that frozen branch, the fibres in \(P_1\) must cover the entire \(q\)-primary component.

Each \(q\)-dependent fibre occupies at most a \(1/q\) fraction of that primary component. Therefore fewer than \(q\) such fibres cannot cover it.

Thus

\[
\boxed{
\#\{p:q\mid n_p\}\ge q.
}
\]

This theorem is deliberately stated as a necessary condition, not as a closure theorem.

---

## G33. Congruence consequence — THEOREM

Since \(n_p\mid p-1\), every prime counted in G32 satisfies

\[
p\equiv1\pmod q.
\]

Therefore any irredundant certificate using essential \(q\)-torsion contains at least \(q\) distinct selected primes congruent to \(1\pmod q\).

---

## G34. Largest-torsion pressure — THEOREM

Let \(Q\) be the largest prime divisor of any selected fibre order \(n_p\) in a hypothetical irredundant certificate. Then G32 applies to \(Q\):

\[
\boxed{
\#\{p:Q\mid n_p\}\ge Q.
}
\]

This creates a strong design rule for positive searches: introducing a new large torsion prime incurs a multiplicity debt of at least \(Q\) fibres.

It does **not** by itself yield a contradiction; no universal upper bound \(<Q\) on such primes was proved.

---

# VIII. KBK CLIMBS — SESSION MAP

## KBK-1 — SEARCH OVER \(m\) → COVER GEOMETRY

```text
integer witness search
→ divisibility fibres
→ affine congruence
→ relation lattice cosets
→ phase synthesis + CRT
```

Gain: removes the giant integer \(m\) from the hard part of the search.

## KBK-2 — COMMON PERIOD → CANONICAL QUOTIENT

```text
N×N torus
→ common relation kernel Λ
→ G=Z²/Λ
→ SNF C_d1×C_d2
```

Gain: state-space size becomes algebraically canonical.

## KBK-3 — DENSITY → POSITIONAL HOLES

```text
raw density
→ local capacity
→ overlap counterexample
→ HOLE_SET
→ exact local lift closure
```

Gain: replaces scalar residuals with exact witnesses.

## KBK-4 — FLAT PHASE SEARCH → TORSION GEOMETRY

```text
phase modulo n_p
→ primary decomposition
→ torsion rank
→ projective slopes
→ AG(2,q) line cover
→ additive-combinatorics constraints
```

Gain: converts opaque phase behavior into reusable local theorems.

## KBK-5 — COVER/PARTITION FAILURE → INTERSECTION ALGEBRA

```text
invalid Fourier cover identity
→ retraction
→ individual coset Fourier support only
→ SNF intersection oracle
→ intersection poset
→ Möbius verifier
```

Gain: exact overlap handling without laundering a cover into a partition.

## KBK-6 — FAILED PHASE ASSIGNMENT → CEGAR

```text
optimizer residual
→ exact adversary witness
→ witness cut
→ finite CEGAR
→ UNSAT obstruction core
```

Gain: every failed candidate becomes a formal obligation.

## KBK-7 — POOL UNSAT → CHARACTER-FIRST PRIME ACQUISITION

```text
obstruction core X*
→ best abstract cyclic character
→ arithmetic realization
→ exponential-difference factor candidates
→ exact relation-lattice test
```

Gain: asks arithmetic for the geometry the proof actually lacks.

## KBK-8 — STATIC PEEL ERROR → STATEFUL ADVERSARY

```text
sparse torsion peel
→ invalid static deletion detected
→ survivor masks
→ alive/unused state
→ dominated-mask pruning
→ monotone memoized adversary
```

Gain: exact pruning without losing the semantics of previous component choices.

## KBK-9 — RAW MASS FIRST CROSSING → FORCED-OVERLAP KILL

```text
D(5040)>1
→ mandatory 5/7 fibres
→ unavoidable 1/24 intersection
→ union upper bound 823/840
→ exact N=5040 impossibility
```

Gain: first numerical “promising frontier” converted into a theorem explaining why it cannot work.

## KBK-10 — ISOLATED NEW TORSION → MULTIPLICITY DEBT

```text
hypothetical irredundant cover
→ freeze non-q branch
→ q-primary cover obligation
→ at most 1/q per q-dependent fibre
→ at least q q-dependent fibres
```

Gain: positive search should acquire torsion-closed clusters, not isolated clever primes.

---

# IX. RETRACTED / QUARANTINED BRANCHES

## R1. Global Fourier phase-uniformity branch — RETRACTED

Invalid root:

\[
\mathbf1_{\cup C_p}=\sum_p\mathbf1_{C_p}.
\]

Consequences such as uniform phase histograms and “every active slope must contain all phases” are not established for ordinary covers.

Do not reuse descendants without a new proof that explicitly handles overlaps.

## R2. Static \(238\to93\) torsion peel — RETRACTED AS STATIC REDUCTION

Choosing a torsion state that kills certain fibres also constrains every survivor. It is valid as one adversary branch transition, not as deletion from the original prime universe.

## R3. Minimal-cover full-parallel-class classification — OPEN, NOT THEOREM

The session explored the possibility that every minimum-cardinality cover by cyclic-kernel cosets must be one complete character foliation. This was not proved.

## R4. Maximal torsion contradiction — OPEN, NOT THEOREM

G34 would yield a contradiction if one could prove fewer than \(Q\) realizable selected fibres can carry the largest torsion prime \(Q\). No such universal bound was proved.

---

# X. LEAN-CLOSE PRIORITY

Highest-value formalization order:

1. `relationLattice` / kernel-coset equivalence.
2. independent phase realization by CRT.
3. canonical finite quotient by common kernel.
4. essential torsion multiplicity theorem G32.
5. generic forced-overlap union upper bound.
6. arithmetic closure of the exact \(N=5040\) inequalities.
7. SNF/coset-intersection bridge, preferably using existing Mathlib subgroup/quotient infrastructure where practical.

The release contains `Erdos203Gold.lean`, a Lean-ready close attempt for the arithmetic and abstract inequality core. **It was not kernel-checked in this ChatGPT environment because Lean is not installed here.** Its formal status is therefore `LEAN_GENERATED`, never `KERNEL_CHECKED`.

---

# XI. CURRENT PROOF FRONTIER

No EG203 witness \(m\) was obtained.

The strongest current positive architecture is:

\[
\text{torsion-closed arithmetic fibre clusters}
\to
G_P
\to
symmetry-reduced exact CEGAR
\to
\begin{cases}
ADVERSARY\_UNSAT &\Rightarrow \text{cover}\to CRT(m),\\
MASTER\_UNSAT &\Rightarrow X^*\to\text{character-first new columns}.
\end{cases}
\]

The strongest current negative structural information is:

- \(N=5040\) is exactly impossible;
- the \(\{5,7,11,13\}\) core carries at least \(79/720\) unavoidable overlap loss;
- any essential torsion prime \(q\) costs at least \(q\) selected \(q\)-dependent fibres.

That is the clean session state to carry forward.
