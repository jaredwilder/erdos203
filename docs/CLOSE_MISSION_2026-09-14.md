# EG203 CLOSE MISSION — 2026-09-14

Author: Jared Wilder

## Mission

**Close Erdős–Graham #203.**

The finite-cover lower bound `r>=12` is now a pruning theorem. It is not the objective.

From this point forward, a round that merely proves `r>=13`, `r>=14`, or another one-step cardinality improvement does **not** count as mission completion and should not become the organizing principle of the campaign.

The primary route is constructive:

> Find a finite prime-fibre cover of `Z^2`, seal its phases, realize those phases simultaneously by CRT, and output an explicit integer `m` with `(m,6)=1` such that every `2^k 3^l m + 1` has a proper selected prime divisor.

If the finite-cover route is impossible, the mission changes only after a theorem proves that impossibility at structural scale. The campaign must not drift into an endless staircase of lower bounds.

## Terminal YES certificate

A YES close requires all of the following in one frozen release:

1. A finite prime set `P`, `p>3`.
2. For each `p in P`, an exact relation lattice / kernel `R_p` and one chosen coset.
3. A proof that the selected cosets cover every `(k,l) in Z_{>=0}^2`; preferably prove the periodic cover on the full finite quotient induced by the intersection of the kernels.
4. A sealed phase assignment before CRT realization.
5. An exact CRT solution `m mod M`, `M=product(P)` together with `m≡1 mod 6`.
6. A positive representative satisfying `m+1 > max(P)`.
7. Verification that for every exponent pair, one selected prime divides `2^k 3^l m+1` and is a proper divisor.
8. An independent replay program that recomputes the kernels, cover, CRT residue, and proper-divisor condition from the published certificate.
9. No hidden search state is accepted as proof. The frozen certificate must be sufficient to replay the close from scratch.

## Terminal NO certificate

A NO close of the **full problem** requires more than showing that finite covers fail.

One of the following must be obtained:

- a direct proof that no admissible `m` exists; or
- a theorem showing that every hypothetical #203 witness necessarily yields a finite prime-fibre subcover, combined with a proof that no finite prime-fibre cover exists.

Until such a bridge exists, `NO FINITE COVER` is not `NO #203 WITNESS`.

## Current proven launch state

The campaign begins from:

```text
base raw mass                    = 143/140
phase-independent base ceiling   = 1459/1680
required outside global mass     = 221/1680
finite-cover outside lower bound = 12
```

For a fibre with order `n` and induced index `d=n/gcd(n,5040)`, use the canonical three-resource vector

```text
L = 1/d
O = d/n
G = 1/n
G = L*O
```

where `L` is local covering power, `O` is replica occupancy, and `G` is global mass.

Exact low-index censuses are frozen for `d=2,4,5,7,8,10,11`. The combined occupancy of every fibre in the six low 3-coprime classes `2,4,5,7,8,10` is only `53/140`.

## Primary attack: construct the cover

### A. Build the candidate frontier, not a small-prime dump

Generate fibres by their exact tuple

```text
(p, n, d, L, O, G, kernel, induced character, intersection data)
```

and keep candidates that are Pareto-competitive in at least one of:

- local covering power `L`;
- replica occupancy `O`;
- global mass `G`;
- new projective direction / quotient geometry;
- unusually favorable intersections with the current uncovered set.

Do not rank candidates by `p` or `n` alone.

### B. Search phases directly

The search variable is the **coset phase**, not merely the prime subset.

For each candidate prime set:

1. compute the finite common quotient induced by the intersection of the selected kernels;
2. encode one phase choice per prime;
3. require every quotient point to be covered;
4. solve by SAT / exact-cover / ILP / CEGAR;
5. extract either a concrete phase assignment or a machine-checkable UNSAT core.

The search must target a complete cover from the first iteration.

### C. Start at r=12 but do not become attached to r=12

`r=12` is the first legal cardinality and therefore the first synthesis target.

If exact search proves `r=12` UNSAT, immediately use the UNSAT cores to derive reusable structural constraints and launch `r=13` synthesis in the same campaign. A one-step lower bound is bookkeeping, not the goal.

Search continues upward until either:

- a cover is found; or
- a structural theorem kills an infinite family of cardinalities / signatures and changes the route fundamentally.

### D. Once a cover appears, stop theory expansion

The first exact cover candidate triggers certification mode immediately:

```text
freeze primes
freeze phases
hash certificate
recompute quotient coverage independently
CRT -> m
verify gcd(m,6)=1
choose m+1>max(P)
verify all selected divisibility rules
publish
```

No further aesthetic optimization is allowed to delay certification of a valid witness.

## Secondary attack: theorem extraction from UNSAT

Every UNSAT result must be mined for structure. The preferred theorem forms are:

- mandatory direction multiplicity;
- mandatory low-index class count;
- unavoidable overlap tax;
- replica-occupancy deficit;
- equality rigidity on `F_q^2`;
- descent showing a fibre is redundant;
- a general inequality in `(L,O,G)` that eliminates a whole family of signatures.

A theorem is valuable only if it shrinks the future synthesis space materially. Avoid branch-specific prose proofs that cannot be reused.

## Parallel workstreams

### SEARCH

- enumerate Pareto candidate fibres;
- perform exact phase synthesis;
- preserve SAT/UNSAT certificates;
- enlarge candidate universe adaptively from uncovered quotient points.

### THEORY

- convert UNSAT cores into signature-independent lemmas;
- search for stronger base overlap certificates beyond the current `p=5` star;
- derive global inequalities coupling `L`, `O`, and `G`;
- investigate whether finite-cover existence can be forced or ruled out abstractly.

### CERTIFICATION

- independent verifier with no search heuristics;
- exact integer arithmetic only;
- deterministic CRT realization;
- proper-divisor and positivity checks;
- publication packet generated directly from the frozen certificate.

### FULL-PROBLEM BRIDGE

In parallel, investigate the missing converse:

> Does every #203 witness admit a finite prime-fibre subcover?

A proof of this statement would turn a global no-finite-cover theorem into a full negative solution. A counterexample mechanism would tell us that finite-cover search cannot by itself settle the problem negatively.

This bridge is strategically important, but it must not distract from the constructive finite-cover attack unless the synthesis route is structurally killed.

## Round contract

Every round must produce at least one of:

- a strictly better complete-cover candidate;
- a certified finite cover;
- an UNSAT certificate over a materially larger search universe;
- a reusable theorem that removes an infinite / parametrically large family of candidates;
- a full-problem bridge result.

The following do **not** qualify as round success by themselves:

- `r>=13`;
- another hand-built branch tree;
- another census with no synthesis consequence;
- another observation that some family has density below one;
- another speculative phase pattern.

## Search escalation policy

1. Exact `r=12` synthesis on the strongest current Pareto pool.
2. CEGAR: uncovered quotient points generate new candidate requirements.
3. Expand candidate pool by new `(L,O,G,direction)` Pareto points, not arbitrary prime bounds.
4. If `r=12` UNSAT, extract the core theorem and continue directly to `r=13`.
5. Repeat until a cover is found or the finite-cover route receives a genuinely global obstruction.

The campaign stops only at a terminal certificate.

## Canonical files

Use:

```text
docs/CANONICAL_R12_LOWER_BOUND_2026-09-14.md
tools/replay_r12_lower_bound_2026_09_14.py
receipts/replay-r12-lower-bound-2026-09-14.json
```

Do not use the raw R44–R51 transcript as proof input except for historical mining.

## Mission sentence

**We are no longer trying to prove that small covers fail. We are trying to produce the cover, realize the integer, and close #203.**
