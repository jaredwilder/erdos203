# Claim Ledger

Start with IDs L203-001 through L203-010 from `CANONICAL_GOLD.md`. Every status change gets a commit SHA and axiom/receipt entry.

## 2026-09-13 structural release

These claims are published in `docs/KBK_PROGRESS_2026-09-13.md`. They are scope-limited to the frozen `U_5040` finite-extension program and are not claims of a solution to the full Erdős–Graham #203 problem.

| id | status | statement |
|---|---|---|
| L203-011 | SESSION_AUDITED | `p=5` star forces overlap tax `257/1680`, giving base ceiling `1459/1680` and extension deficit `221/1680` |
| L203-012 | SESSION_AUDITED | every frozen-base extension with at most five outside fibres is impossible |
| L203-013 | SESSION_AUDITED | six-outside-fibre branch with two induced-index-2 fibres is impossible |
| L203-014 | SESSION_AUDITED | with exactly one induced-index-2 anchor, `p=23` is mandatory |
| L203-015 | SESSION_AUDITED | in the one-anchor six-fibre branch, every subbranch containing `p=47` is impossible by index-3 partition rigidity and cardinality descent |
| L203-016 | SESSION_AUDITED | no-`d3/d6/d8` branch forces all three `d=4` fibres and then fails the global mass gate |
| L203-017 | FRONTIER_ONLY | `{8641,601,101,151}` is a knife-edge arithmetic candidate in the `p=193`, single-`d6`, no-`d3` route; uniqueness not yet certified |
| L203-018 | RETRACTED | live pure-`d8` closure (`K403/K404`) omitted possible additional `d=8` fibres |
| L203-019 | REPAIRED | correct `p=20161` ternary restriction map is `(a,b)->(a+b,2b) mod 3`; the class matches `8641↔C12`, `12097↔C10` survive |

`SESSION_AUDITED` is intentionally weaker than `REPLAYED_COMPUTATION`: promotion requires repository-level replay/receipt hardening.
