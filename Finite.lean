import Std

namespace UniversalGlue

-- The folded transfer index is always strictly larger than the direct index.
theorem direct_lt_reflected (n m : Nat) : n - m + (m - n) < n + m + 1 := by
  omega

-- A symmetric pair contributes precisely one square after folding.
theorem paired_dirichlet (p h v w : Int) :
    p * v * v + p * w * w - 2 * (p + 2*h) * v * w =
    p * (v-w) * (v-w) - 4*h*v*w := by
  grind

-- Rational enclosures for head/tail comparisons.
theorem hankel_head_margin : (113/110-1 : Rat) * (113/110-1/12) > 1/40 := by
  native_decide

theorem fractional_head_tail_cost : (25/72 : Rat) / (1-1/12) = 25/66 := by
  native_decide

theorem fractional_head_tail_margin : (25/66 : Rat) < 1 := by
  native_decide

-- These are exact coefficient checks, not proofs of the model's analytic hypotheses.
theorem cross_cap_at_soft_head :
    ((1 : Rat) + 1/4)^2 / (3*(1-1/4)) = 25/36 := by
  native_decide

theorem equal_moments : (8 : Rat) * 1 = (1/8) * 64 := by
  native_decide

theorem signed_sector_is_unstable :
    ((8+4-1/8-8/65 : Rat) / (1+8+1/8)) = 6111/4745 ∧ (6111/4745 : Rat) > 1 := by
  native_decide

theorem hard_normal_line_bound : (1 + 4/101 + 800/(9*2001) : Rat) < 11/10 := by
  native_decide

theorem static_null_trial : (1 : Rat) - 25/25 = 0 ∧ (1/2-12/25 : Rat) > 0 := by
  native_decide

theorem dominant_normal_can_raise_onset_head : (59/10 * (89/100) : Rat) > 26/5 := by
  native_decide

end UniversalGlue
