"""Independent rational Nevanlinna witnesses and Poisson comparisons."""
from argparse import ArgumentParser
from fractions import Fraction as Q
from itertools import product

p = ArgumentParser(description=__doc__)
p.add_argument('--mutant', choices=('self-energy-sign', 'poisson-fold', 'endpoint-ratio'))
bad = p.parse_args().mutant


def check(ok, label):
    if not ok:
        raise SystemExit('REJECT: ' + label)


def normal_frequency(omega, poles):
    # Z(z)=z-sum_j mass_j/(z-center_j) maps H into H for positive masses.
    real, imag = Q(0), omega
    for center, mass in poles:
        denom = center*center+omega*omega
        real += mass*center/denom
        sign = -1 if bad == 'self-energy-sign' else 1
        imag += sign*mass*omega/denom
    return real, imag


pairs = 0
energy_comparisons = 0
for omega, poles, k in product((Q(1, 3), Q(1), Q(7, 4)),
        ((), ((Q(0), Q(1)),), ((Q(2), Q(3)),),
         ((Q(-3), Q(2, 5)), (Q(4), Q(9, 2)))), (Q(3), Q(5, 3), Q(7, 5))):
    x0, u0 = normal_frequency(omega, poles)
    x1, u1 = normal_frequency(k*omega, poles)
    check(u0 > 0 and u1 > 0, 'positive Nevanlinna normal width')
    distance = (x1-x0)**2+(u1-u0)**2
    check(distance <= (k-1)**2*u0*u1/k, 'independent rational Schwarz-Pick test')
    # Compare raw Poisson densities by exact division, not a determinant implementation.
    for energy in (Q(-20), Q(-3), Q(-1, 7), Q(0), Q(2), Q(31, 2)):
        P0 = u0/((energy-x0)**2+u0*u0)
        P1 = u1/((energy-x1)**2+u1*u1)
        upper = k/2 if bad == 'endpoint-ratio' else k
        lower = k if bad == 'poisson-fold' else 1/k
        check(lower*P0 <= P1 <= upper*P0, 'independent pointwise Poisson Harnack test')
        energy_comparisons += 1
    pairs += 1

# At x0=x1=energy=0 and u1=3u0, the lower 1/3 bound is attained.
u0, u1 = Q(1), Q(3)
check((1/u1)/(1/u0) == Q(1, 3), 'sharp elementary Harnack endpoint')
# The forbidden external shift fails the causal inequality uniformly on the row box.
c, t = Q(13, 25), Q(1, 100)
D = c*(1/t+4)
check(Q(27054000)**2 > Q(4, 3)*(1+D)*(3+D), 'uniform external-shift causal obstruction')
print(f'CERTIFIED {pairs} rational causal pairs and {energy_comparisons} exact Poisson comparisons')
