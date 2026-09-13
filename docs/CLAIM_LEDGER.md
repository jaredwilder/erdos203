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

Receipts:

- `receipts/replay-d8-branch-2026-09-13.json`
- `receipts/replay-no-d3-branch-2026-09-13.json`

`SESSION_AUDITED` remains intentionally weaker than `REPLAYED_COMPUTATION` and should not be silently promoted without a repository-level replay/receipt or formal proof.
