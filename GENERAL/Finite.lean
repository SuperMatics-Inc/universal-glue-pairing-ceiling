import Std

namespace ShiftedGlue

theorem poisson_determinant (k u v x y : Int) :
    (k*u-v)*(k*u*(y^2+v^2)-v*(x^2+u^2)) - (k*u*y-v*x)^2 =
      u*v*((k-1)^2*u*v-k*((y-x)^2+(v-u)^2)) := by
  grind

theorem width_factorization (k u v : Int) :
    (v-k*u)*(k*v-u) = k*(v-u)^2-(k-1)^2*u*v := by
  grind

theorem complementary_reserve_identity (b d : Int) :
    1-b+d*(1-3*(1-b)) = d+(1-3*d)*(1-b) := by
  grind

theorem exact_causal_budget :
    (2*(1-685881/7152100) : Rat) = 6466219/3576050 ∧
      (121/1261 : Rat) > 685881/7152100 ∧
      (685881/6979600 : Rat) > 685881/7152100 := by
  native_decide

theorem explicit_external_witness :
    (2*(13/25)-3*(13/25)*(1/1000)-(1+1/100) : Rat) = 711/25000 ∧
      (711/25000 : Rat) > 0 ∧
      ((13/25)*(6466219/3576050) : Rat) < 1 ∧
      ((1+(13/25)/(1/100)+(13/25)*(1/1000))/54000 : Rat) < 1/1000 ∧
      ((27054000 : Rat)^2) > (4/3)*(1+(13/25)*(100+4))*(3+(13/25)*(100+4)) := by
  native_decide

end ShiftedGlue
