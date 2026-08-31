# ERDŐS RESEARCH REPOSITORY CONTRIBUTION PROTOCOL v1.0

Every tracked contribution must be one of:

```text
THEOREM
COMPUTATION
ENGINE
KILL
AUDIT
FORMAL_HARDENING
SOURCE_BINDING
```

Commit/PR body template:

```text
TARGET:
CLAIM:
TYPE:
FAMILY_SCOPE:
STATUS_BEFORE:
STATUS_AFTER:
DEPENDENCIES:
FORMAL_STATUS:
AXIOM_FOOTPRINT:
COMPUTATION_RECEIPTS:
NEGATIVE_CONTROLS:
BOUNDARY:
KBK_NEXT:
```

No commit may use `closed`, `proved`, `formalized`, `UNSAT`, or `verified` without specifying the exact object/family and checker that earns the word.

For computational results, freeze inputs before output and hash both input and certificate.

For Lean results, root `lake build` must import the module, and headline theorem axiom output belongs in the receipt or module footer.
