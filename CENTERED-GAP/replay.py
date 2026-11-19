"""Finite coefficient and sign checks for the centered width cone and gap."""
from argparse import ArgumentParser
from fractions import Fraction as F
from itertools import product

parser = ArgumentParser(description=__doc__)
parser.add_argument('--mutant', choices=(
    'folded-numerator', 'upper-cone-sign', 'lower-cone-product', 'convolution-shift',
    'head-determinant', 'middle-imbalance', 'drop-complement', 'edge-copy',
    'exact-reserve',
))
bad = parser.parse_args().mutant


def check(condition, label):
    if not condition:
        raise SystemExit(f'REJECT: {label}')


for n, m, t in product(range(6), range(9), (F(1, 50), F(1, 4), F(8))):
    x, y = F(2*n+1, 2), F(2*m+1, 2)
    u, up = x*x, (x+1)**2
    denom = lambda z: ((z-y)**2+t)*((z+y)**2+t)
    D, Dp = denom(x), denom(x+1)
    k = lambda j: 1/(t+j*j)
    sign = -1 if bad == 'folded-numerator' else 1
    check((k(n-m)-k(n+m+1))*D == sign*4*x*y, 'positive reflected numerator')
    sign = 1 if bad == 'upper-cone-sign' else -1
    check(D-Dp == sign*(up-u)*(u+up-2*y*y+2*t), 'upper-cone kernel crossing')
    negative = u*u if bad == 'lower-cone-product' else u*up
    check(up*D-u*Dp == (up-u)*((y*y+t)**2-negative), 'lower-cone kernel crossing')

for j, h, t in product(range(-6, 7), (1, 3, 7), (F(1, 50), F(3, 2))):
    k = lambda a: 1/(t+a*a)
    shift = F(1 if bad == 'convolution-shift' else 2, h)
    rhs = k(j)+k(j+h)+shift*((j+h)*k(j+h)-j*k(j))
    check((h*h+4*t)*k(j)*k(j+h) == rhs, 'shifted convolution decomposition')

reserve = F(19, 200)
alpha = F(41, 50)
for r, t, a in product((F(1, 60), F(1), F(19, 30), F(3)), (F(1, 100), F(1, 9), F(4)),
                       (F(2, 5), F(1, 2), F(19, 20))):
    u = 1/(1+t)
    beta = 1/(2*t*(1+t))
    det = (a+beta*r)*(a+beta/r)-(beta+u)**2
    head = 1 if bad == 'head-determinant' else 2
    check(2*(1-u)*det == 2*(1-u)*a*a + u*u*(a*(r+1/r)-head), 'exact head determinant')
far = F(2, 5)-F(59, 96)/(4*alpha)
tail = F(11, 12)-alpha
near = F(5, 8) if bad == 'middle-imbalance' else F(19, 30)
mid = 1-2/(near+1/near)
check(far == F(8369, 39360) and tail == F(29, 300) and mid == F(121, 1261),
      'far, intermediate and retained tail reserves')
check(min(far, tail, mid, F(1, 10)) > reserve and alpha > F(2, 3), 'non-soft budgets')
lo = F(243, 370)
hi = F(3, 4)
check(lo == 3/((1+F(1, 9))*(4+F(1, 9))), 'first transfer cap at positive energy')
D1 = lo*(near*alpha/2-F(1, 9))/(alpha+hi/(6*near))
check(D1 == F(685881, 7152100) and reserve < D1 < F(1, 3), 'first tail forces a positive head reserve')
sharp_tail = lo*(near*alpha/2-F(1, 9))/(alpha+lo/(6*near))
exact_budget = F(2)*(1-D1)
if bad == 'exact-reserve':
    exact_budget = F(2)*(1+D1)
check(sharp_tail == F(685881, 6979600) and min(far, tail, mid, F(1, 10), sharp_tail) > D1,
      'strict slack at the unrounded reserve')
check(exact_budget == F(6466219, 3576050), 'unrounded onset coefficient squared')
for b0 in (F(0), F(1, 40), F(1, 2), F(1)):
    b1 = b0/3 if bad == 'drop-complement' else max(0, 1-3*(1-b0))
    check(1-b0+D1*b1 >= D1, 'average using the complementary DOS')
copy = 1 if bad == 'edge-copy' else 2
check(copy*(1-reserve) == F(181, 100) < 2, 'two endpoint costs and onset units')
print('CERTIFIED finite signs, single crossings, convolution and uniform reserve')
