# Erdős–Graham #203 — KBK Progress Release — 2026-09-13

**Author:** Jared Wilder  
**Target status:** OPEN  
**Branch:** finite prime-fibre construction extending the frozen 31-fibre `U_5040` base  
**Release status:** research release; structural claims below survived the session audit, but claims not already covered by the August replay suite are not yet promoted to `REPLAYED_COMPUTATION` in `CANONICAL_GOLD.md`.

## Headline

The six-outside-fibre search has acquired a rigid structural obstruction.

Within the branch having exactly one induced-index-2 outside fibre, the prime `p=23` is forced. If `p=47` is also selected, then the final three fibres are forced into an exact three-way index-3 partition of the anchor residual half-lattice. Equality forces a common index-3 kernel. That makes `p=47` redundant, so any alleged six-fibre cover descends to a five-fibre cover. The previously established `r<=5` obstruction then kills the entire `p=47` subbranch.

In symbols, the key KBK chain is

```text
mass saturation
→ equality case
→ common kernel
→ exact C3 partition
→ redundant fibre
→ cardinality descent 6 → 5
→ contradiction.
```

This is a structural closure; it does not rely on enumerating every phase assignment in the terminal branch.

---

## 1. Frozen architecture

For each prime `p>3`, let

```text
psi_p(u,v) = 2^u 3^v mod p,
R_p = ker psi_p,
n_p = |<2,3>_p|.
```

A selected prime contributes one realizable coset of `R_p`. Distinct prime phases are CRT-independent. A finite selected family covering `Z^2` gives a sufficient CRT certificate for an Erdős–Graham #203 witness.

The frozen base consists of the 31 fibres with `n_p | 5040`; its raw mass is

```text
143/140.
```

This finite-cover branch remains only a sufficient construction route; it is not asserted to be equivalent to the full Erdős–Graham problem.

---

## 2. Phase-independent overlap tax and universal base deficit

A stronger overlap certificate than the original `{5,7}` obstruction was recovered during the campaign.

Anchor `p=5` has a phase-independent surjective pair product map with 20 partners in the 31-fibre base. Summing the forced pair overlaps gives the star tax

```text
257/1680.
```

Therefore every phase assignment for the complete frozen base satisfies

```text
dens(B) <= 143/140 - 257/1680 = 1459/1680,
```

hence every finite extension must repair a deficit of at least

```text
221/1680.
```

This converts the extension problem into a simultaneous global-mass and local-geometry problem.

---

## 3. Induced-index calculus

For an outside fibre of order `n`, define

```text
d = n / gcd(n,5040).
```

On a fixed replicated base cell, its relative density is `1/d`. After restricting to an index-2 anchor residual half-lattice `H`, an even index can gain at most the parity factor, giving the local density filter

```text
rho_H(d) <= gcd(2,d)/d.
```

The campaign recovered exact small-index classes, including:

```text
d=2: exactly p=193, p=20161

d=3 projective classes:
  C01 = {109,433}
  C10 = {271,757,7561}
  C12 = {379,541,2161}
  C11 = {15121,30241}

d=4: exactly {449,1153,2689}

d=6: exactly {8641,12097}
```

This finite low-index structure is what makes cardinality closure possible.

---

## 4. Cardinality wall

Within the frozen-base extension program, the campaign has closed every extension using at most five outside fibres:

```text
r <= 5  → impossible.
```

Thus any finite cover extending the complete `U_5040` base must use at least six outside fibres.

The six-fibre branch with two induced-index-2 fibres has also been closed.

Current six-fibre split:

```text
r=6
├─ d2count=2   CLOSED
├─ d2count=1   ACTIVE, strongly reduced
└─ d2count=0   OPEN
```

---

## 5. Exactly one d=2 anchor: p=23 is mandatory

Fix one anchor from `{193,20161}`. Five outside tails remain.

Combining the universal base deficit with the anchor contribution shows that the low-order prime `p=23` is mandatory. After selecting it, four tails remain and must satisfy both a global mass gate and the local anchor-half-space gate

```text
sum rho_H(d_i) >= 10/11.
```

This is the main Pareto tension: globally cheap fibres tend to have poor induced index, while high-local-density fibres tend to have large order and negligible global mass.

---

## 6. Complete closure of the p=47 subbranch

Assume `p=47` is also selected.

After `p=23` and `p=47`, the final three fibres must cover enough of the anchor half-space to supply

```text
219/253.
```

A fibre whose induced index is divisible by 23 is too sparse; therefore the final three induced indices are coprime to 23. The `p=47` condition is then independent of their union inside `H`. Consequently `p=47` plus the final-three union covers `H` iff the final three fibres already cover `H`.

Every non-`d=2` final fibre has local density at most `1/3`. Since three fibres must cover all of `H`, equality is forced:

```text
rho_1 = rho_2 = rho_3 = 1/3,
```

and the total mass equals the union mass. Therefore the three cosets are pairwise disjoint.

Three relative index-3 cosets in a rank-two lattice can be pairwise disjoint and cover the lattice only when they are the three phases of one common index-3 kernel. Hence the final three fibres form an exact `C3` partition.

The exact `d=6` ternary character matching is

```text
p=8641  ↔ C12,
p=12097 ↔ C10.
```

The pure-`d=3` and mixed `d=3/d=6` possibilities reduce to a finite family, but no terminal phase enumeration is needed: because the final three already cover `H`, `p=47` is redundant.

Removing `p=47` from any alleged six-outside-fibre cover therefore gives a five-outside-fibre cover, contradicting the `r<=5` obstruction.

### Result

```text
r=6,
d2count=1,
p23 selected,
p47 selected
→ IMPOSSIBLE.
```

This is the strongest new structural result of the September 13 campaign.

---

## 7. Non-p47 frontier

After the closure above, the one-anchor branch becomes

```text
p23 mandatory,
p47 impossible,
four remaining tails,
global mass gate load-bearing,
local gate sum rho_H >= 10/11 load-bearing.
```

A clean sub-closure is already available: if no `d=3`, `d=6`, or `d=8` fibre is selected, the local gate forces all three `d=4` fibres. Their maximum possible global mass, even with the strongest available `d=5` tail, is

```text
1/448 + 1/576 + 1/1344 + 1/75
= 1819/100800,
```

which is below the required global threshold for either anchor. That architecture is impossible.

The surviving frontier is therefore concentrated in the `d=3`, `d=6`, and repaired `d=8` arms.

A particularly sharp arithmetic endpoint appears in the no-`d=3`, single-`d=6`, `p=193` route:

```text
{8641, 601, 101, 151}
```

has total mass

```text
1/4320 + 1/75 + 1/100 + 1/150
= 653/21600,
```

exceeding the relevant global threshold by only

```text
1/103950.
```

This is a frontier candidate, **not yet a certified unique survivor**; its uniqueness reduction requires a complete low-order census replay.

---

## 8. Audit repairs and quarantine

This release deliberately records two repairs rather than hiding them.

### 8.1 Corrected p=20161 restriction map

For the anchor half-lattice `u+v ≡ 0 (mod 2)` with basis

```text
(1,1), (0,2),
```

a ternary character `(a,b)` restricts as

```text
(a,b) ↦ (a+b, 2b) mod 3.
```

An earlier live derivation printed a different intermediate map. The important class matching survives the correction:

```text
8641 ↔ C12,
12097 ↔ C10.
```

### 8.2 d=8 branch reopened

A live compression claimed that, with a `d=8` fibre and at most one `d=4`, the two remaining fibres contributed at most `1/5` each. That silently excluded the possibility of additional `d=8` fibres.

Therefore the claims labelled in the live campaign as the pure-`d=8` closure are **retracted**. The repaired `d=8` family remains open and must be attacked with the complete `d=8` census/geometry.

### 8.3 Execution labels

Some live-session blocks were labelled `TOOL_RAN` although no external computation tool had actually been invoked in those turns. Those labels are not receipts. Exact arithmetic was subsequently spot-replayed during the audit, but this document does not promote unreplayed campaign computations to repository receipt status.

---

## 9. KBK extraction

The main reusable mathematical mechanism discovered here is

```text
forced overlap
→ global deficit
→ induced-index pressure
→ cardinality minimum
→ equality-case local saturation
→ common-kernel rigidity
→ redundant fibre
→ cardinality descent.
```

The crucial lesson is to attack equality cases before launching phase SAT. In the `p=47` branch, this converted what looked like a finite search over many phase assignments into a short structural contradiction.

The same pattern should now be tested aggressively against the remaining `d=3` and repaired `d=8` branches.

---

## 10. Next attack

The next campaign should begin from the cleaned frontier, not from the retracted live state:

1. replay the complete low-order outside-fibre census supporting the `p601/p101/p151` forcing;
2. enumerate the complete `d=8` census and exact anchor restrictions;
3. test the knife-edge `{8641,601,101,151}` geometry if it survives census replay;
4. attack the `d=3`-present arm using affine-plane/common-kernel equality and redundancy descent before broad SAT;
5. only after the one-`d=2` branch is closed, enter `d2count=0`.

The target remains open. The finite prime-fibre completion space, however, is substantially more constrained than in the August 31 release.
