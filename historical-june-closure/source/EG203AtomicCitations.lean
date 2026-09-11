import EG203Formal.EG203PeerClosure

/-!
# EG#203 — historical atomic citation decomposition (2026-06-02)

This file is released for historical audit. It is a **conditional composition**, not an unconditional proof of EG203. The two load-bearing mathematical-content axioms in the recovered final state are visible below.
-/

namespace EG203AtomicCitations

open EG203PeerClosure

/-- Historical citation-interface axiom. Retained for audit; not asserted here to be a verbatim published theorem. -/
axiom pappalardi_1995_index_distribution :
 ∃ (c : ℕ → ℝ), (∀ d, 0 < c d) ∧
 (∀ d, 1 ≤ d → c d ≤ (1 : ℝ) / ((d : ℝ) ^ 2))

/-- Historical citation-interface axiom for the positive-density primitive-root input. -/
axiom heath_brown_1986_thm1_positive_density_2_3_6 :
 ∃ (δ : ℝ), 0 < δ ∧ δ ≤ 1

/-- LOAD-BEARING HISTORICAL AXIOM. The recovered package describes this as a composite V-family Rosser–Iwaniec lower-bound statement backed by an author preprint draft, not a single published theorem quoted verbatim. -/
axiom wilder_2026_V_family_rosser_iwaniec :
 ∃ (c : ℝ) (D₀ : ℕ), 0 < c ∧
 ∀ m : ℕ, Ordinary m → ∀ D : ℕ, D₀ ≤ D →
 c * bateman_horn_singular_series_V m * (D : ℝ) ≤ (primeCountInBox m D : ℝ)

/-- LOAD-BEARING HISTORICAL AXIOM. Uniform lower bound for the V-family singular series. -/
axiom V_family_singular_series_uniform_lower_bound :
 ∃ (c₀ : ℝ), 0 < c₀ ∧
 ∀ m : ℕ, Ordinary m → c₀ ≤ bateman_horn_singular_series_V m

/-- Statement matching the composite analytic input used by the peer-closure file. -/
def eg203_analytic_NT_input_statement : Prop :=
 ∃ (c : ℝ) (D₀ : ℕ), 0 < c ∧
 ∀ m : ℕ, Ordinary m →
  0 < bateman_horn_singular_series_V m ∧
  ∀ D : ℕ, D₀ ≤ D →
  (c * bateman_horn_singular_series_V m * (D : ℝ)) ≤ (primeCountInBox m D : ℝ)

/-- Conditional discharge of the composite input from the two load-bearing historical axioms above. -/
theorem eg203_analytic_NT_input_from_atomic_citations :
 eg203_analytic_NT_input_statement := by
 unfold eg203_analytic_NT_input_statement
 obtain ⟨c, D₀, hc, hcount⟩ := wilder_2026_V_family_rosser_iwaniec
 obtain ⟨c₀, hc₀, hSm⟩ := V_family_singular_series_uniform_lower_bound
 refine ⟨c, D₀, hc, ?_⟩
 intro m hm
 refine ⟨?_, ?_⟩
 · exact lt_of_lt_of_le hc₀ (hSm m hm)
 · intro D hD
   exact hcount m hm D hD

/-- Historical conditional full closure. Its theorem term is valid **assuming the declared axioms**; it is not an unconditional proof of those axioms. -/
theorem eg203_closed_atomic : EG203Closed := by
 obtain ⟨c, D₀, hc, h⟩ := eg203_analytic_NT_input_from_atomic_citations
 intro m hm
 obtain ⟨hBH_pos, hcount⟩ := h m hm
 set BH := bateman_horn_singular_series_V m with hBH_def
 have hcBH_pos : 0 < c * BH := mul_pos hc hBH_pos
 set D := max D₀ (Nat.ceil (1 / (c * BH)) + 1) with hD_def
 have hD₀ : D₀ ≤ D := le_max_left _ _
 have hcountD : c * BH * (D : ℝ) ≤ (primeCountInBox m D : ℝ) := hcount D hD₀
 have hD_geq_inv : (1 / (c * BH)) ≤ (D : ℝ) := by
  calc (1 / (c * BH) : ℝ)
   ≤ (Nat.ceil (1 / (c * BH)) : ℝ) := Nat.le_ceil _
   _ ≤ ((Nat.ceil (1 / (c * BH)) + 1 : ℕ) : ℝ) := by push_cast; linarith
   _ ≤ (D : ℝ) := by exact_mod_cast le_max_right _ _
 have h_one_le : 1 ≤ c * BH * (D : ℝ) := by
  have key : c * BH * (1 / (c * BH)) ≤ c * BH * (D : ℝ) :=
   mul_le_mul_of_nonneg_left hD_geq_inv (le_of_lt hcBH_pos)
  rw [mul_one_div, div_self (ne_of_gt hcBH_pos)] at key
  exact key
 have hcountge1_real : (1 : ℝ) ≤ (primeCountInBox m D : ℝ) := h_one_le.trans hcountD
 have hcountge1_nat : 1 ≤ primeCountInBox m D := by exact_mod_cast hcountge1_real
 exact witness_of_positive_count m D hcountge1_nat

end EG203AtomicCitations
