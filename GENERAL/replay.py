"""Exact algebra for causal shifted weights and external-shift sharpness."""
from argparse import ArgumentParser
from fractions import Fraction as F
from itertools import product

p = ArgumentParser(description=__doc__)
p.add_argument('--mutant', choices=(
    'harnack-sign', 'pick-factor', 'complement', 'reserve-sign',
    'external-fold', 'tail-cost', 'moment-units', 'causal-admission',
))
bad = p.parse_args().mutant


def check(ok, label):
    if not ok:
        raise SystemExit('REJECT: ' + label)


count = 0
for k, u, v, x, y in product((F(3), F(5, 3)), (F(1), F(3, 2)),
                            (F(1, 2), F(1), F(2)), (F(-2), F(0)), (F(0), F(3))):
    A = k*u-v
    B = k*u*y-v*x
    C = k*u*(y*y+v*v)-v*(x*x+u*u)
    distance = (y-x)**2+(v-u)**2
    rhs = u*v*((k-1)**2*u*v-k*distance)
    if bad == 'harnack-sign':
        rhs = u*v*((k-1)**2*u*v+k*distance)
    check(A*C-B*B == rhs, 'Poisson quadratic determinant identity')
    check((v-k*u)*(k*v-u) == k*((v-u)**2-(k-1)**2*u*v/k),
          'width ratio factorization')
    count += 1

# Exact sharp Schwarz-Pick conversion, including its factor 4/3 for K=3.
k = F(3)
pseudo = ((k-1)/(k+1))**2
factor = 4*pseudo/(1-pseudo)
if bad == 'pick-factor':
    factor = F(3, 4)
check(factor == F(4, 3), 'first two Matsubara Schwarz-Pick coefficient')

alpha, r, lo = F(41, 50), F(19, 30), F(243, 370)
d = F(685881, 7152100)
d_plus = lo*(r*alpha/2-F(1, 9))/(alpha+lo/(6*r))
reserves = (F(2, 5)-F(59, 96)/(4*alpha), F(1, 10),
            1-2/(r+1/r), F(11, 12)-alpha, d_plus)
check(d_plus == F(685881, 6979600) and min(reserves) == F(121, 1261) > d,
      'causal shifted strict edge reserve')
q = 2*(1+d) if bad == 'reserve-sign' else 2*(1-d)
check(q == F(6466219, 3576050), 'improved coefficient square')
for b0 in (F(0), F(1, 2), F(9, 10), F(99, 100), F(1)):
    b1 = max(0, 1-3*(1-b0))
    if bad == 'complement':
        b1 = b0/3
    check(1-b0+d_plus*b1 >= d_plus, 'complementary Harnack head reserve')

# The family is analytic in delta; these exact checks certify formulas, not a scan proof.
for delta in (F(1, 4), F(1, 20), F(1, 100), F(1, 10000)):
    c, t = F(1, 2)+delta, delta
    eps = delta/(12*c)
    W = 2*(1+c/t+c*eps)/eps
    R = W/(2*eps)
    check(W/(2*R) == eps and (1+c/t+c*eps)/W == eps/2,
          'finite box and shifted-tail budgets')
    fold = 1 if bad == 'external-fold' else 2
    tail_cost = -c*eps if bad == 'tail-cost' else c*eps
    margin = fold*c*(1-eps)-(1+t)-tail_cost
    check(margin == 3*delta/4 > 0, 'external-shift head instability margin')
    # rho=c at 2*pi*tau=1, E^2=t, so K_j=c/(t+j^2).
    physical_moment = 2*c if bad == 'moment-units' else c
    check(physical_moment/(t+1) == c/(t+1), 'moment and temperature units')

c, t, eps = F(13, 25), F(1, 100), F(1, 1000)
W, R = F(54000), F(27000000)
L = W+R
D = c*(1/t+4)
check((1+c/t+c*eps)/W < eps and W/(2*R) == eps,
      'explicit finite-DOS weight bounds')
check(2*c-3*c*eps-(1+t) == F(711, 25000) > 0,
      'explicit external-shift instability')
check(c*q < 1, 'external shift exceeds the proved centered upper interval')
noncausal = L*L > F(4, 3)*(1+D)*(3+D)
if bad == 'causal-admission':
    noncausal = not noncausal
check(noncausal, 'witness cannot be admitted as a causal normal branch')
print(f'CERTIFIED {count} determinant identities, Harnack budgets and finite-DOS external family')
