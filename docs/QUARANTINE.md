# Quarantine

Do not reuse without a new proof: finite-cover iff EG203; cover=partition Fourier identity; static torsion peel; tested-family→universal lift; direct Bateman-Horn transfer; unverified Romanoff 2-D theorem; density→pointwise; search-saturation theorem; global dimensional phase-transition theorem.

## 2026-09-13 audit additions

The following live-campaign artifacts are explicitly quarantined.

### Incorrect intermediate restriction map for the `p=20161` anchor

For the half-lattice `u+v ≡ 0 (mod 2)` with basis `(1,1),(0,2)`, the correct restriction of a ternary character `(a,b)` is

```text
(a,b) -> (a+b, 2b) mod 3.
```

A live MSL round printed a different intermediate map. Do not reuse that map. The derived class matching `8641 ↔ C12` and `12097 ↔ C10` survives the correction.

### Retracted pure-`d=8` closure

The live claims corresponding to the `K403/K404` compression are not valid. The argument bounded two remaining tails by `1/5` without excluding additional `d=8` fibres. Multiple `d=8` fibres were therefore omitted.

Status:

```text
pure-d8 / no-d3 / no-d6 branch = OPEN
```

until the complete `d=8` census and exact anchor geometry are replayed.

### Invalid execution metadata

Several live MSL blocks were labelled `TOOL_RAN` even though no external computation tool had run in those turns. Those labels are not receipts and must not be cited as computational verification. Arithmetic promoted to the replay bank requires a real repository script/receipt or another explicit independent execution record.
