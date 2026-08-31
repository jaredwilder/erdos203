# EG203 result recovery queue

This is the order for restoring earlier work into the live public corpus. The rule is simple:
we do not leave earned results buried in old packages, and we do not promote them until the
artifact that earned them is back under review.

## 1. Restore the m <= 10^6 Lean theorem

**Why first:** this is the strongest recovered result with a clean, finite claim boundary.

Recover `EG203BoundedClosure.lean` and the exact pinned environment in which
`EG203_nat_form_for_ordinary_m_up_to_1000000` was checked. Re-run the build and record
`#print axioms`. Then port the theorem and its witness data into this repository without
changing its statement.

Target public claim after replay:

> For every m <= 10^6 with gcd(m,6)=1, an explicit pair (k,l), k+l<=12, gives a prime
> m*2^k*3^l+1; the finite theorem is kernel-checked using the disclosed native-decide trust
> path.

## 2. Restore the exact shadow-equivalence Lean box

Recover the old `EG203ClosureLean.lean` theorem

```lean
EG203Closed <-> NoProperOrdinaryInfiniteCRTShadow
```

as a formal reduction/regression guard. Keep the parameter visible in the one-way closing
line. Do not call this the solution: the hard rigidity proposition was not proved there.

## 3. Restore and replay the direct sweep receipts

The estate records a complete direct sweep of the 3,333,333,333 ordinary m in `[1,10^10]`,
zero failures, maximum first-prime diagonal 26 at `m=6,257,518,159`, witness `(16,10)`, with
176 non-overlapping receipts and aggregate SHA-256
`c9efd4f76095dd5ac98013573d3feccafc969ec25876373fa260dfd9a7d2d15e`.

Do not publish that number as repository-certified until the receipt set and an independent
checker are restored and the aggregate hash matches.

## 4. Restore the Lean moment-law files

The technique estate records kernel-verified local obstruction identities, including mean-zero
and higher-moment laws. Recover the corresponding `EG203Formal` sources and
`RECEIPTS-2026-06-10.md`, then decide which results belong in `CANONICAL_GOLD.md`.

## 5. Recover Papers 15, 16, and 17 as a separate analytic lane

The later analytic program appears to have moved the universal frontier substantially beyond
the early closure manuscripts:

- discriminant barrier for conductor-only log-free zero-density methods;
- Bilinear-Kummer equivalence locating the PHNC step at a Type-II estimate;
- high-ell localization results;
- a sharp low-ell/unresolved-seam split around `ell log ell ~ log Q`.

Before public promotion, bind every theorem to its exact source and check every load-bearing
external theorem citation against the published paper. Earlier audits specifically flagged
some zero-density citations as needing exact theorem-location confirmation.

## 6. Reconcile the recovered analytic lane with the new coset-cover lane

Only after both estates are restored should the next full proof attack choose a route. The two
lanes answer different questions:

- the relation-lattice/coset machinery gives exact finite geometry, exact obstruction cores,
  and proof-producing search;
- the Kummer/PHNC lane attacks universal prime production analytically.

The next attack should start from their union, not from whichever repo happened to be newest.

## Never restore as a headline without a new proof

- unconditional "closed by shadow rigidity";
- circular R11/R14/Iwaniec prime-count assumptions;
- the chain-103 uniform 1/128 statement;
- finite-cover iff EG203;
- tested periodic-cover failures stated universally.
