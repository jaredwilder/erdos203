/-
 EG203BoundedClosure.lean — 2026-06-01

 BOUNDED kernel-checked closure of Erdős–Graham #203.
 This is NOT the universal EG203 closure.
-/

import Mathlib.Data.Nat.Prime.Basic
import Mathlib.Tactic

namespace EG203BoundedClosure

def V (m k l : Nat) : Nat := m * 2 ^ k * 3 ^ l + 1

def EG203BoundedDecidable (N D : Nat) : Prop :=
 ∀ m : Fin (N + 1),
 1 ≤ m.val →
 Nat.Coprime m.val 6 →
 ∃ k : Fin (D + 1), ∃ l : Fin (D + 1),
 k.val + l.val ≤ D ∧ Nat.Prime (V m.val k.val l.val)

instance (N D : Nat) : Decidable (EG203BoundedDecidable N D) := by
 unfold EG203BoundedDecidable
 exact inferInstance

theorem EG203_holds_for_ordinary_m_up_to_200_diag_14 :
 EG203BoundedDecidable 200 14 := by native_decide

#print axioms EG203_holds_for_ordinary_m_up_to_200_diag_14

theorem EG203_holds_for_ordinary_m_up_to_1000_diag_14 :
 EG203BoundedDecidable 1000 14 := by native_decide

#print axioms EG203_holds_for_ordinary_m_up_to_1000_diag_14

theorem EG203_holds_for_ordinary_m_up_to_5000_diag_16 :
 EG203BoundedDecidable 5000 16 := by native_decide

#print axioms EG203_holds_for_ordinary_m_up_to_5000_diag_16

theorem EG203_nat_form_for_ordinary_m_up_to_200 :
 ∀ m : Nat, 1 ≤ m → m ≤ 200 → Nat.Coprime m 6 →
 ∃ k l : Nat, Nat.Prime (V m k l) := by
 intro m h1 hN hcop
 have hbnd : m < 201 := by omega
 obtain ⟨k, l, _, hprime⟩ :=
  EG203_holds_for_ordinary_m_up_to_200_diag_14 ⟨m, hbnd⟩ h1 hcop
 exact ⟨k.val, l.val, hprime⟩

#print axioms EG203_nat_form_for_ordinary_m_up_to_200

theorem EG203_nat_form_for_ordinary_m_up_to_1000 :
 ∀ m : Nat, 1 ≤ m → m ≤ 1000 → Nat.Coprime m 6 →
 ∃ k l : Nat, Nat.Prime (V m k l) := by
 intro m h1 hN hcop
 have hbnd : m < 1001 := by omega
 obtain ⟨k, l, _, hprime⟩ :=
  EG203_holds_for_ordinary_m_up_to_1000_diag_14 ⟨m, hbnd⟩ h1 hcop
 exact ⟨k.val, l.val, hprime⟩

#print axioms EG203_nat_form_for_ordinary_m_up_to_1000

theorem EG203_nat_form_for_ordinary_m_up_to_5000 :
 ∀ m : Nat, 1 ≤ m → m ≤ 5000 → Nat.Coprime m 6 →
 ∃ k l : Nat, Nat.Prime (V m k l) := by
 intro m h1 hN hcop
 have hbnd : m < 5001 := by omega
 obtain ⟨k, l, _, hprime⟩ :=
  EG203_holds_for_ordinary_m_up_to_5000_diag_16 ⟨m, hbnd⟩ h1 hcop
 exact ⟨k.val, l.val, hprime⟩

#print axioms EG203_nat_form_for_ordinary_m_up_to_5000

theorem EG203_holds_for_ordinary_m_up_to_10000_diag_18 :
 EG203BoundedDecidable 10000 18 := by native_decide

#print axioms EG203_holds_for_ordinary_m_up_to_10000_diag_18

theorem EG203_nat_form_for_ordinary_m_up_to_10000 :
 ∀ m : Nat, 1 ≤ m → m ≤ 10000 → Nat.Coprime m 6 →
 ∃ k l : Nat, Nat.Prime (V m k l) := by
 intro m h1 hN hcop
 have hbnd : m < 10001 := by omega
 obtain ⟨k, l, _, hprime⟩ :=
  EG203_holds_for_ordinary_m_up_to_10000_diag_18 ⟨m, hbnd⟩ h1 hcop
 exact ⟨k.val, l.val, hprime⟩

#print axioms EG203_nat_form_for_ordinary_m_up_to_10000

theorem EG203_holds_for_ordinary_m_up_to_50000_diag_10 :
 EG203BoundedDecidable 50000 10 := by native_decide

#print axioms EG203_holds_for_ordinary_m_up_to_50000_diag_10

theorem EG203_nat_form_for_ordinary_m_up_to_50000 :
 ∀ m : Nat, 1 ≤ m → m ≤ 50000 → Nat.Coprime m 6 →
 ∃ k l : Nat, Nat.Prime (V m k l) := by
 intro m h1 hN hcop
 have hbnd : m < 50001 := by omega
 obtain ⟨k, l, _, hprime⟩ :=
  EG203_holds_for_ordinary_m_up_to_50000_diag_10 ⟨m, hbnd⟩ h1 hcop
 exact ⟨k.val, l.val, hprime⟩

#print axioms EG203_nat_form_for_ordinary_m_up_to_50000

theorem EG203_holds_for_ordinary_m_up_to_100000_diag_12 :
 EG203BoundedDecidable 100000 12 := by native_decide

#print axioms EG203_holds_for_ordinary_m_up_to_100000_diag_12

theorem EG203_nat_form_for_ordinary_m_up_to_100000 :
 ∀ m : Nat, 1 ≤ m → m ≤ 100000 → Nat.Coprime m 6 →
 ∃ k l : Nat, Nat.Prime (V m k l) := by
 intro m h1 hN hcop
 have hbnd : m < 100001 := by omega
 obtain ⟨k, l, _, hprime⟩ :=
  EG203_holds_for_ordinary_m_up_to_100000_diag_12 ⟨m, hbnd⟩ h1 hcop
 exact ⟨k.val, l.val, hprime⟩

#print axioms EG203_nat_form_for_ordinary_m_up_to_100000

theorem EG203_holds_for_ordinary_m_up_to_200000_diag_12 :
 EG203BoundedDecidable 200000 12 := by native_decide

#print axioms EG203_holds_for_ordinary_m_up_to_200000_diag_12

theorem EG203_nat_form_for_ordinary_m_up_to_200000 :
 ∀ m : Nat, 1 ≤ m → m ≤ 200000 → Nat.Coprime m 6 →
 ∃ k l : Nat, Nat.Prime (V m k l) := by
 intro m h1 hN hcop
 have hbnd : m < 200001 := by omega
 obtain ⟨k, l, _, hprime⟩ :=
  EG203_holds_for_ordinary_m_up_to_200000_diag_12 ⟨m, hbnd⟩ h1 hcop
 exact ⟨k.val, l.val, hprime⟩

#print axioms EG203_nat_form_for_ordinary_m_up_to_200000

theorem EG203_holds_for_ordinary_m_up_to_300000_diag_12 :
 EG203BoundedDecidable 300000 12 := by native_decide

#print axioms EG203_holds_for_ordinary_m_up_to_300000_diag_12

theorem EG203_nat_form_for_ordinary_m_up_to_300000 :
 ∀ m : Nat, 1 ≤ m → m ≤ 300000 → Nat.Coprime m 6 →
 ∃ k l : Nat, Nat.Prime (V m k l) := by
 intro m h1 hN hcop
 have hbnd : m < 300001 := by omega
 obtain ⟨k, l, _, hprime⟩ :=
  EG203_holds_for_ordinary_m_up_to_300000_diag_12 ⟨m, hbnd⟩ h1 hcop
 exact ⟨k.val, l.val, hprime⟩

#print axioms EG203_nat_form_for_ordinary_m_up_to_300000

theorem EG203_holds_for_ordinary_m_up_to_500000_diag_12 :
 EG203BoundedDecidable 500000 12 := by native_decide

#print axioms EG203_holds_for_ordinary_m_up_to_500000_diag_12

theorem EG203_nat_form_for_ordinary_m_up_to_500000 :
 ∀ m : Nat, 1 ≤ m → m ≤ 500000 → Nat.Coprime m 6 →
 ∃ k l : Nat, Nat.Prime (V m k l) := by
 intro m h1 hN hcop
 have hbnd : m < 500001 := by omega
 obtain ⟨k, l, _, hprime⟩ :=
  EG203_holds_for_ordinary_m_up_to_500000_diag_12 ⟨m, hbnd⟩ h1 hcop
 exact ⟨k.val, l.val, hprime⟩

#print axioms EG203_nat_form_for_ordinary_m_up_to_500000

theorem EG203_holds_for_ordinary_m_up_to_750000_diag_13 :
 EG203BoundedDecidable 750000 13 := by native_decide

#print axioms EG203_holds_for_ordinary_m_up_to_750000_diag_13

theorem EG203_nat_form_for_ordinary_m_up_to_750000 :
 ∀ m : Nat, 1 ≤ m → m ≤ 750000 → Nat.Coprime m 6 →
 ∃ k l : Nat, Nat.Prime (V m k l) := by
 intro m h1 hN hcop
 have hbnd : m < 750001 := by omega
 obtain ⟨k, l, _, hprime⟩ :=
  EG203_holds_for_ordinary_m_up_to_750000_diag_13 ⟨m, hbnd⟩ h1 hcop
 exact ⟨k.val, l.val, hprime⟩

#print axioms EG203_nat_form_for_ordinary_m_up_to_750000

theorem EG203_holds_for_ordinary_m_up_to_1000000_diag_13 :
 EG203BoundedDecidable 1000000 13 := by native_decide

#print axioms EG203_holds_for_ordinary_m_up_to_1000000_diag_13

theorem EG203_nat_form_for_ordinary_m_up_to_1000000 :
 ∀ m : Nat, 1 ≤ m → m ≤ 1000000 → Nat.Coprime m 6 →
 ∃ k l : Nat, Nat.Prime (V m k l) := by
 intro m h1 hN hcop
 have hbnd : m < 1000001 := by omega
 obtain ⟨k, l, _, hprime⟩ :=
  EG203_holds_for_ordinary_m_up_to_1000000_diag_13 ⟨m, hbnd⟩ h1 hcop
 exact ⟨k.val, l.val, hprime⟩

#print axioms EG203_nat_form_for_ordinary_m_up_to_1000000

-- Historical note: the 1.5M native_decide attempt overflowed the stack;
-- the 1M finite certificate was the production ceiling of this file.

end EG203BoundedClosure
