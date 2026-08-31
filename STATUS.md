# Status

- Source target: **OPEN**.
- Finite prime-fibre certificate architecture: **sufficient branch**, not known
  equivalent to all of EG203 (`docs/QUARANTINE.md`, first entry).
- Banked session results (2026-08-31): relation-lattice geometry, canonical finite
  quotient for frozen finite pools, torsion multiplicity, forced-overlap obstructions,
  exact N=5040 pool kill, four-fibre overlap tax. Ledger: `CANONICAL_GOLD.md`.
- Computational claims G28–G31: **REPLAYED on 2026-08-31** by
  `tools/replay_eg203_gold.py`, verdict `ALL_MATCH`
  (`receipts/replay-eg203-gold-2026-08-31.json`). The G28 census is complete — the
  gcd(2^5040−1, 3^5040−1) factorization fully resolved during replay.
- Formal import status: **LEAN_GENERATED / NOT YET KERNEL-CHECKED HERE.** The Lean
  files are scaffold stubs; no theorem claim is made by their existence. Porting
  queue 203-001 … 203-008 (see README).
- Known missing from the original release package: a `Erdos203Gold.lean` close attempt
  was described in the session source document but was **not delivered** in the release
  zip; it is not in this repository and nothing here depends on it.
