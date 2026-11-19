import Std

namespace PlasmonW

theorem folded_diagonal (g b : Int) : b + g - (b - g) = 2*g := by grind

theorem ratio_endpoint : (1 + 4*(1/12 : Rat))/(1-1/12) = 16/11 := by native_decide

theorem ratio_margin : (16/11 : Rat) < 3/2 := by native_decide

theorem tail_margin : ((3/2 : Rat)*2+4)*2*(1+1/12)/64 < 1/4 := by native_decide


theorem explicit_ratio : (100/99 : Rat)*(16/11+1/44) < 3/2 := by native_decide

theorem explicit_bare_cost : 4*(100/99 : Rat)*(1/44+4/3) < 6 := by native_decide

theorem explicit_coupling : (4*6 : Nat)^2 = 576 := by decide
theorem static_null : (1 : Rat) - 64*(1/64) = 0 := by native_decide

end PlasmonW
