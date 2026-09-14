# Claim Ledger

Start with IDs L203-001 through L203-010 from `CANONICAL_GOLD.md`. Every status change gets a commit SHA and axiom/receipt entry.

## 2026-09-13 structural release

These claims are scope-limited to the frozen `U_5040` finite-extension program and are not claims of a solution to the full Erdős–Graham #203 problem.

| id | status | statement |
|---|---|---|
| L203-011 | SESSION_AUDITED | `p=5` star forces overlap tax `257/1680`, giving base ceiling `1459/1680` and extension deficit `221/1680` |
| L203-012 | SESSION_AUDITED | every frozen-base extension with at most five outside fibres is impossible |
| L203-013 | SESSION_AUDITED | six-outside-fibre branch with two induced-index-2 fibres is impossible |
| L203-014 | SESSION_AUDITED | with exactly one induced-index-2 anchor, `p=23` is mandatory |
| L203-015 | SESSION_AUDITED | in the one-anchor six-fibre branch, every subbranch containing `p=47` is impossible by index-3 partition rigidity and cardinality descent |
| L203-016 | REPLAYED_COMPUTATION | no-`d3/d6/d8` branch forces all three `d=4` fibres and then fails the global mass gate; replayed in `tools/replay_no_d3_branch_2026_09_13.py` |
| L203-017 | REPLAYED_COMPUTATION | `{8641,601,101,151}` is the unique arithmetic survivor in the `p=193`, single-`d6`, no-`d3` route and is killed geometrically with uncovered density at least `8/33` |
| L203-018 | RETRACTED | live pure-`d8` closure (`K403/K404`) omitted possible additional `d=8` fibres; do not reuse that proof |
| L203-019 | REPAIRED | correct `p=20161` ternary restriction map is `(a,b)->(a+b,2b) mod 3`; the class matches `8641↔C12`, `12097↔C10` survive |
| L203-020 | REPLAYED_COMPUTATION | repaired complete `d=8` census is `{641,769,4481,26881}`; the no-`d3`, no-`d6`, `d8`-present branch is closed by `tools/replay_d8_branch_2026_09_13.py` |
| L203-021 | REPLAYED_COMPUTATION | in the one-`d2`, `p23`, non-`p47`, six-fibre branch, absence of `d=3` is impossible; hence every survivor must contain a `d=3` fibre |
| L203-022 | REPLAYED_COMPUTATION | with both `d=6` fibres on the `p=193` anchor, the unique arithmetic final pair is `{53,601}` and it is killed geometrically with uncovered density at least `32/143` |

## 2026-09-14 corrected canonical release

The raw late-session R44–R51 stream is historical mining material, not the canonical proof record. It repeatedly omitted the valid 3-coprime classes `d=8` and `d=10` from a residual `d>=11` bucket and contained several mistyped rational values. The September 14 replay corrects the classification before promoting any headline claim.

| id | status | statement |
|---|---|---|
| L203-023 | REPLAYED_COMPUTATION | complete corrected censuses for `d=2,4,5,7,8,10,11` have exact fibre counts `2,3,16,10,4,3,24` |
| L203-024 | REPLAYED_COMPUTATION | total replica occupancies for `d=2,4,5,7,8,10` are respectively `53/2520, 19/1008, 53/240, 389/5040, 1/28, 5/1008`; combined total `53/140` |
| L203-025 | REPLAYED_COMPUTATION | complete `d=11` induced `C_11` direction multiplicities are `4,3,3,3,2,2,2,2,2,1`, so an eleven-line equality cover is impossible |
| L203-026 | REPLAYED_COMPUTATION | complete `3|d` census through `n<=1080` has 15 fibres; the eleven cheapest orders are `108,162,216,270,378,486,540,648,648,648,756` and none has replica occupancy `1/9` |
| L203-027 | REPLAYED_COMPUTATION | the only non-`E` outside fibres with `n<=31` are `(p,n,d)=(23,11,11)` and `(47,23,23)` |
| L203-028 | REPLAYED_COMPUTATION | corrected coarse signature enumeration, explicitly retaining `d=8` and `d=10`, has zero survivors at `r=8`, only `E=9` at `r=9`, only `E>=9` at `r=10`, and only `E in {0,9,10,11}` at `r=11` |
| L203-029 | REPLAYED_COMPUTATION | every finite prime-fibre cover extending `U_5040` requires **at least 12 outside fibres** |
| L203-030 | MISSION_CONTRACT | future work is directed at a terminal close: exact finite-cover synthesis plus CRT realization for a YES, or a structural impossibility theorem plus the missing finite-subcover bridge for a full NO; one-step lower-bound increases are pruning only |

Canonical replay:

- `tools/replay_r12_lower_bound_2026_09_14.py`
- `receipts/replay-r12-lower-bound-2026-09-14.json`
- `docs/CANONICAL_R12_LOWER_BOUND_2026-09-14.md`
- `docs/CLOSE_MISSION_2026-09-14.md`

Earlier September receipts remain:

- `receipts/replay-d8-branch-2026-09-13.json`
- `receipts/replay-no-d3-branch-2026-09-13.json`

`SESSION_AUDITED` remains intentionally weaker than `REPLAYED_COMPUTATION` and should not be silently promoted without a repository-level replay/receipt or formal proof.
