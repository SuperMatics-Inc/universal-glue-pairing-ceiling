"""Exact guards for the coupled centered soft limit and anisotropic flat DOS."""
import argparse
from fractions import Fraction as F

MUTANTS = ('normal-sign', 'head-tail-factor', 'tail-reserve', 'collapse-strict',
           'effective-mass', 'flat-hard-alt', 'flat-cross-tail', 'flat-soft-trial')
p = argparse.ArgumentParser(description=__doc__)
p.add_argument('--mutant', choices=MUTANTS)
mode = p.parse_args().mutant


def check(value, label):
    if not value:
        raise SystemExit(f'REJECT: {label}')


def kernel(t, j):
    return 1 / (t + j*j)


for t in (F(1, 10**4), F(1, 7), F(2)):
    for n in range(8):
        cap = 24
        p_diag = kernel(t, 0) - kernel(t, 2*n+1)
        check(t*p_diag == 1 - t*kernel(t, 2*n+1), 'static normal coefficient')
        sign = 1 if mode == 'normal-sign' else -1
        row = sum(kernel(t, abs(n-m)) + sign*kernel(t, n+m+1) for m in range(cap+1))
        remainder = sum(kernel(t, j) for j in range(cap-n+1, cap+n+2))
        check(row + remainder == kernel(t, 0) + 2*sum(kernel(t, j) for j in range(1, n+1)),
              'odd normal row with exact remainder')

head = F(25, 48) + 2*(F(1, 32) + F(1, 64))
head_margin = F(3, 4) if mode == 'head-tail-factor' else F(4, 5)
check(head == F(59, 96) < head_margin**2, 'head-to-tail square sum')
tail = sum(F(1, (m+2)**2*(2*m+1)) for m in range(1, 17)) + F(1, 4*16**2)
check(tail < F(1, 12), 'scalar tail Hankel Schur margin')
fold = 3 if mode == 'tail-reserve' else 2
check(head_margin + F(fold, 12) == F(29, 30) < 1, 'residual norm budget')

eta, beta = (2, 3), (F(1, 2), F(1, 3))
B = sum(q*b for q, b in zip(eta, beta))
# The reciprocal cross edge is 1, with no loops; L beta = (1, 1).
check((eta[1]*beta[1], eta[0]*beta[0]) == (1, 1), 'positive static profile')
gamma = F(1) if mode == 'collapse-strict' else F(11, 10)
# The strict inequality required in the min-ratio proof rejects both a ray
# of the positive profile and directions with either minimizing endpoint.
for a, b in ((F(1), F(1)), (F(2, 9), F(3, 7)), (F(3, 7), F(2, 9))):
    check(not (a >= gamma*b and b >= gamma*a), 'collapsed component min ratio')
J = (2*eta[0]*eta[1]*beta[0]*beta[1])
B_eff = sum(q*b*b for q, b in zip(eta, beta)) if mode == 'effective-mass' else B
check(J/B_eff == 1 and J/B_eff < F(6, 5), 'effective moment divides by one power of beta')

# The negative flat temporal endpoint uses the normal row, not the pairing row.
hard = 2*(kernel(F(1, 3), 1) - (0 if mode == 'flat-hard-alt' else kernel(F(1, 3), 2))
          + kernel(F(1, 3), 3))
check(hard == F(114, 91) < F(13, 10) and (hard + F(3, 2))/3 < F(13, 10),
      'negative flat temporal bound for hard lines')
tail_cap = F(38, 45)
check((F(31, 18) + F(5, 2))/5 == tail_cap
      and (F(31, 18) + F(7, 2))/7 < tail_cap, 'flat Fourier tail cap')
check(F(25, 48) < F(7, 4)*F(1, 3), 'flat two-head negative semidefinite budget')
cross = sum((F(1, (m-n)**2) + F(1, (m+n+1)**2))**2/F((2*m+1)*(2*n+1))
            for n in (0, 1) for m in range(2, 5))
cross += F(2*(2 if mode == 'flat-cross-tail' else 1), 3*3**4)
check(cross == F(58670711, 489888000) < F(1, 8) < F(3, 10)*(F(13, 10)-tail_cap),
      'flat two-head cross remainder and completion')
v = (F(1), F(1, 5), F(1, 16))
diag = sum((F(1, (2*n+1)**2) - 2*sum(F(1, j*j) for j in range(1, n+1)))*v[n]**2
           for n in range(3))
mixed = sum((F(1, (m-n)**2) + F(1, (m+n+1)**2))*v[n]*v[m]
            for m in range(3) for n in range(m))
lower_margin = diag + (1 if mode == 'flat-soft-trial' else 2)*mixed
lower_margin -= F(13, 10)*sum((2*n+1)*v[n]**2 for n in range(3))
check(lower_margin == F(247, 48000) > 0, 'soft positive spectral top beats negative cap')
print('PASS: exact odd rows, active profile, collapse, residual and flat temporal margins')
