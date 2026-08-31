import Lake
open Lake DSL

package erdos203 where

require mathlib from git
  "https://github.com/leanprover-community/mathlib4.git" @ "master-2026-05-31"

@[default_target]
lean_lib Erdos203All where
  roots := #[
    `Erdos203All, `Erdos203Source, `Erdos203RelationLattice, `Erdos203CRT,
    `Erdos203ForcedOverlap, `Erdos203TorsionMultiplicity, `Erdos203N5040,
    `Erdos203Intersection, `Erdos203CEGAR]
