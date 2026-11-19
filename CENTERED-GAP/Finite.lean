import Std

namespace CenteredGap

theorem reflected_numerator (x y : Int) :
    (x + y)^2 - (x - y)^2 = 4*x*y := by
  grind

theorem upper_cone_sign (u v z t : Int) :
    ((u + z + t)^2 - 4*u*z) - ((v + z + t)^2 - 4*v*z) =
      -(v-u)*(u+v-2*z+2*t) := by
  grind

theorem lower_cone_sign (u v z t : Int) :
    v*((u + z + t)^2 - 4*u*z) - u*((v + z + t)^2 - 4*v*z) =
      (v-u)*((z+t)^2-u*v) := by
  grind

theorem convolution_partial_fractions (j h t : Int) :
    (j^2 + (j+h)^2 + 2*t) + 2*(-j^2-h*j+t) = h^2+4*t := by
  grind

theorem head_determinant (u A B R : Int) (mass : 2*(1-u)*B = u^2) :
    2*(1-u)*(A^2-u^2+B*(A*R-2*u)) = 2*(1-u)*A^2+u^2*(A*R-2) := by
  calc
    _ = 2*(1-u)*(A^2-u^2)+(2*(1-u)*B)*(A*R-2*u) := by grind
    _ = _ := by rw [mass]; grind

theorem all_other_reserves :
    (2/5-(59/96)/(4*(41/50)) : Rat) = 8369/39360 ∧
      (8369/39360 : Rat) > 19/200 ∧ (1/10 : Rat) > 19/200 ∧
      (1-2/(19/30+30/19) : Rat) = 121/1261 ∧ (121/1261 : Rat) > 19/200 ∧
      (11/12-41/50 : Rat) = 29/300 ∧ (29/300 : Rat) > 19/200 := by
  native_decide

theorem first_tail_reserve :
    ((243/370 : Rat)*((19/30)*(41/50)/2-1/9)/((41/50)+(3/4)/(6*(19/30)))) =
        685881/7152100 ∧
      (685881/7152100 : Rat) > 19/200 ∧ (685881/7152100 : Rat) < 1/3 := by
  native_decide

theorem two_endpoint_onset :
    (2*(1-19/200) : Rat) = 181/100 ∧ (181/100 : Rat) < 2 := by
  native_decide

theorem unrounded_coefficient :
    ((243/370 : Rat)*((19/30)*(41/50)/2-1/9)/((41/50)+(243/370)/(6*(19/30)))) =
        685881/6979600 ∧
      (685881/6979600 : Rat) > 685881/7152100 ∧
      (121/1261 : Rat) > 685881/7152100 ∧ (29/300 : Rat) > 685881/7152100 ∧
      (1/10 : Rat) > 685881/7152100 ∧ (8369/39360 : Rat) > 685881/7152100 ∧
      (2*(1-685881/7152100) : Rat) = 6466219/3576050 := by
  native_decide

end CenteredGap
