import Std

namespace SharpQ2

theorem difference_of_squares (a b : Int) :
    (a+b)^2 - (a-b)^2 = 4*a*b := by grind

theorem adjacent_squares (m : Int) :
    (m+1)^2 - m^2 = 2*m+1 := by grind

theorem locked_head_det (A x y z u : Int) (h : x*y = z*z) :
    (A+x)*(A+y) - (z+u)^2 = A*A - u*u + A*(x+y) - 2*z*u := by
  grind

theorem mask_interpolation (u v a b c d : Int) :
    (1-u)*(1-v)*a + u*(1-v)*(a+b) + (1-u)*v*(a+c) + u*v*(a+b+c+d)
      = a+u*b+v*c+u*v*d := by grind

theorem reserve : (11 : Rat)/12 - 5/6 = 1/12 := by native_decide

theorem balanced_cross : (2 : Rat)/3 < 5/6 := by native_decide

theorem determinant_floor : (16 : Rat)/25-1+(8/5)*((4/5)*(10/3)-2) > 0 := by
  native_decide

theorem imbalanced_margin : (1 : Rat)/5 - ((25/48+3/32)/(4*(5/6))) = 1/64 := by
  native_decide

end SharpQ2
