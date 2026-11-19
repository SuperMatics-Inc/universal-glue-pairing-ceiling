import Std

namespace CenteredSoft

theorem head_budget : (25/48 : Rat) + 2*(1/32+1/64) = 59/96 := by native_decide

theorem head_margin : (59/96 : Rat) < (4/5 : Rat)^2 := by native_decide

theorem tail_margin :
    ((List.range 16).map (fun m => 1/(((m+3 : Nat)^2*(2*m+3) : Nat) : Rat))).sum +
      1/(4*16^2) < (1/12 : Rat) := by native_decide

theorem residual_budget : (4/5 : Rat) + 2*(1/12) = 29/30 := by native_decide

theorem reciprocal_profile : (3 : Rat)*(1/3) = 1 ∧ (2 : Rat)*(1/2) = 1 := by native_decide

theorem effective_moment : (2*2*3*(1/2)*(1/3) : Rat)/(2*(1/2)+3*(1/3)) = 1 := by native_decide

end CenteredSoft

namespace AnisotropicFlat

theorem hard_alternation :
    2*(3/4 - 3/13 + 3/28 : Rat) = 114/91 ∧
      (114/91 : Rat) < 13/10 ∧ ((114/91 : Rat)+3/2)/3 < 13/10 := by native_decide

theorem negative_tail :
    ((31/18 : Rat) + 5/2)/5 = 38/45 ∧
      ((31/18 : Rat) + 7/2)/7 < 38/45 := by native_decide

def h (n m : Nat) : Rat :=
  (1/(((m-n)^2 : Nat) : Rat) + 1/(((m+n+1)^2 : Nat) : Rat))^2 /
    (((2*n+1)*(2*m+1) : Nat) : Rat)

theorem head_margin : (25/48 : Rat) < (7/4)*(1/3) := by native_decide

theorem cross_exact :
    h 0 2 + h 0 3 + h 0 4 + h 1 2 + h 1 3 + h 1 4 + (2/243 : Rat) =
      (58670711/489888000 : Rat) := by native_decide

theorem cross_margin :
    (58670711/489888000 : Rat) < 1/8 ∧
      (1/8 : Rat) < (3/10)*(13/10-38/45) := by native_decide

theorem positive_soft_trial :
    (1 : Rat) + (1/9-2)*(1/5)^2 + (1/25-5/2)*(1/16)^2 +
      2*((1+1/4)*(1/5) + (1/4+1/9)*(1/16) + (1+1/16)*(1/5)*(1/16)) -
      (13/10)*(1+3*(1/5)^2+5*(1/16)^2) = 247/48000 := by native_decide

end AnisotropicFlat
