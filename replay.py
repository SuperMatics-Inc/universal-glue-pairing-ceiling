"""Rational coefficient certificates. A specified mutant must fail an assertion."""
from argparse import ArgumentParser
from fractions import Fraction as F
from itertools import product


def check(name, condition):
    if not condition:
        raise SystemExit(f"REJECT: {name}")


def main():
    parser = ArgumentParser(description=__doc__)
    parser.add_argument('--mutant', choices=('loss-sign', 'fs-jacobian', 'fold-sign',
                                            'hankel-cap', 'moment-fold', 'bulk-fold',
                                            'cross-cap', 'sumzero', 'partner-line',
                                            'dos-aggregation'))
    mutant = parser.parse_args().mutant

    # Paired boundary atoms, evaluated at z=i nu, are real after addition.
    for energy, nu, atom in product((F(1, 3), F(2)), (F(0), F(7, 4)), (F(3, 2),)):
        denom = energy**2 + nu**2
        loss = (-1 if mutant != 'loss-sign' else 1) * 2 * atom * energy / denom
        check('retarded pole sign and weight', loss == atom * (-energy / denom - energy / denom))
    k, q, hbar, mass = F(3, 2), F(4, 5), F(7, 3), F(5, 2)
    eps = lambda p: (hbar * p)**2 / (2 * mass)
    check('kinetic f-sum', eps(k + q) + eps(k - q) - 2 * eps(k) == hbar**2 * q**2 / mass)
    # On a unit Fermi sphere the change of variable q*dq/(2*k_F^2) integrates to 1.
    check('angular Jacobian', F(2**2, 8 if mutant == 'fs-jacobian' else 4) == 1)

    # Sum distinct DOS on a discrete energy grid; the squared single-fiber
    # Cooper norm and the normal integral must both use the same measure.
    channel_weight = (F(1, 2), F(2, 3))
    dos = ((F(4), F(0), F(1)), (F(0), F(6), F(2)))
    energies = (-1, 0, 1)
    width, shift = F(3, 2), F(1, 4)
    den = [width**2 + (e + shift)**2 for e in energies]
    aggregate = [sum(w*row[j] for w, row in zip(channel_weight, dos)) for j in range(3)]
    if mutant == 'dos-aggregation':
        aggregate[0] = sum(row[0] for row in dos)
    split = sum(w*row[j]/den[j] for w, row in zip(channel_weight, dos) for j in range(3))
    check('sector Cooper fiber compression', sum(a/d for a, d in zip(aggregate, den)) == split)
    check('summed DOS height can improve budget', max(aggregate) < sum(w*max(row) for w, row in zip(channel_weight, dos)))

    # Independent expansion of the gain/stability form on two angles x two positive modes.
    fibers = list(product(range(2), repeat=2))
    b = (F(3, 4), F(1, 7), F(1, 2), F(5, 9))
    v = (F(-2), F(3, 2), F(1, 7), F(4))
    transfer = lambda j, x, y: F(1 + x + y, 1 + j*j)
    expanded = folded = sum((2*n+1) * b[a] * v[a]**2 for a, (n, _) in enumerate(fibers))
    for a, (n, x) in enumerate(fibers):
        for z, (m, y) in enumerate(fibers):
            D, H = transfer(abs(n-m), x, y), transfer(n+m+1, x, y)
            P = D-H
            expanded += b[a] * b[z] * (P*v[a]**2 - (D+H)*v[a]*v[z])
            folded += b[a]*b[z] * (P*(v[a]-v[z])**2/2 - (1 if mutant == 'fold-sign' else 2)*H*v[a]*v[z])
    check('folded sign and factor', expanded == folded)

    kmax = 16
    tail = sum(F(1, (2*m+1)*(m+2)**2) for m in range(1, kmax+1)) + F(1, 4*kmax**2)
    cross = sum(F(1, (2*m+1)*(m+1)**4) for m in range(1, kmax+1)) + F(1, 8*kmax**4)
    a = F(113, 110) if mutant != 'hankel-cap' else F(112, 110)
    check('tail row sum', tail < F(1, 12))
    check('cross square sum', cross < F(1, 40))
    check('Hankel Schur gap', (a-1)*(a-F(1, 12)) > F(1, 40))
    check('row cross Schur gap', F(25, 72)/(1-F(1, 12)) == F(25, 66) < 1)
    for m in range(1, 14):
        for t in (F(0), F(1, 5), F(3, 2), F(99)):
            u, v = t+m*m, t+(m+1)**2
            kernel_ratio = (1/u+1/v)**2 / ((2*m+1)*(1/u-1/v))
            cap = F(25, 37) if mutant == 'cross-cap' else F(25, 36)
            check('cross estimate identity and maximum', kernel_ratio == F(4,(2*m+1)**2)+1/(u*v) <= cap)
    # tau=3, symbolic pi replaced by an arbitrary positive rational P: normal term
    # tau*u/(u^2+e^2), divided by P*tau, versus compensated b=(P*tau)*u/(u^2+e^2).
    tau, P, u, e = F(3), F(22, 7), F(200, 3), F(7, 5)
    b_bulk = P*tau*u/(u*u+e*e)
    leading = 1/(P**2*tau) if mutant != 'bulk-fold' else 1/(P*tau)
    check('bulk prefactor', tau*u/((u*u+e*e)*P*tau) == leading*b_bulk)

    soft, hard = [F(8, 1+j*j) for j in (0, 1)], [F(8, 64+j*j) for j in (0, 1)]
    normal = 1+soft[0]+hard[0]
    signed = (sum(soft)+(-1 if mutant != 'moment-fold' else 1)*sum(hard))/normal
    check('zero signed moment witness', signed == F(6111, 4745) > 1)
    normal_cap = 1 + F(4, 101) + F(800, 9*2001)
    b_lower = 1 - normal_cap/50
    check('raw dominance mass and gap', normal_cap < F(11, 10) and b_lower > F(489, 500) and 4*b_lower/normal_cap > F(978, 275))
    check('static sign-changing witness', 4*(1-F(2,100)) == F(98,25) > 1)
    N = 25 if mutant != 'sumzero' else 24
    check('plasmon static-null gain margin', 1-N*F(1,25) == 0 and F(1,2)-F(12,N) > 0)
    test_tau = F(101,100)
    l_cross, eps = 1000, F(1,10**9)
    width_A, width_B = 100, 10**7
    normal_B = 10**16 if mutant != 'partner-line' else 10**12
    check('baseline partner remains broad', 4*1000*(40 + 2*eps) < width_B)
    check('baseline stable at all tau >= 1', max(F(20,40), 20*F(2*width_A,9*1000)) + F(1,100) < 1)
    check('baseline reciprocal cross norm', l_cross*eps*(1+F(4,10**4))**2 < F(1,100)**2)
    check('enhanced partner suppressed', F(4*width_B,9*normal_B) < F(1,10**4)**2)
    active_width = 1+4+l_cross*F(1,10**4)+l_cross/(1+10**4*test_tau**2)
    active_weight = 1-2*test_tau*active_width/width_A
    check('enhanced active mode unstable', active_width < F(26,5) and active_weight > F(89,100) and (4+4/(1+test_tau**2))*active_weight > active_width)
    print(f'PASS: exact rational certificates; tail<{F(1,12)}, cross<{F(1,40)}, Hankel<{a}')


if __name__ == '__main__':
    main()
