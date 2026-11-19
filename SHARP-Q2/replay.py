"""Exact rational guards for the endpoint-pair norm bound."""
from argparse import ArgumentParser
from fractions import Fraction as F


def require(name, predicate):
    if not predicate:
        raise SystemExit(f"REJECT: {name}")


def main():
    p = ArgumentParser(description=__doc__)
    p.add_argument('--mutant', choices=('tail-reserve', 'head-tail-fold', 'tail-mass',
                                       'head-lock', 'loss-budget', 'endpoint-factor',
                                       'perron-ratio', 'soft-witness'))
    bad = p.parse_args().mutant

    cutoff = 16
    tail_cap = sum(F(1, (2*m+1)*(m+2)**2) for m in range(1, cutoff+1)) + F(1, 4*cutoff**2)
    tail_reserve = F(1, 10) if bad == 'tail-reserve' else F(1, 12)
    alpha = F(5, 6)
    require('tail covers completion and reserve', 1-tail_cap > F(11, 12) >= alpha+tail_reserve)
    for m in range(1, 9):
        w = 2*m+1
        for t in (F(1, 400), F(1, 4), F(1), F(88)):
            a, d = 1/(t+m*m), 1/(t+(m+1)**2)
            S, P = a+d, a-d
            multiplier = 3 if bad == 'head-tail-fold' else 4
            require('exact head-tail determinant threshold', (S*S-P*P)/(w*P) == F(multiplier, w*w))
    require('balanced range, worst lower endpoint', alpha > F(2, 3))
    r, t, w = F(1, 3), F(1, 200), 3
    left, right = 1/(t+1), 1/(t+4)
    S, P = left+right, left-right
    tail_mass = F(0) if bad == 'tail-mass' else P/(2*r*w)
    require('retain both normal diagonals in completion', (r*P/2)*(alpha+tail_mass) > S*S/(4*w))
    lock = F(3, 10) if bad == 'head-lock' else F(8, 5)
    determinant_floor = F(16, 25)-1 + lock*(F(4, 5)*F(10, 3)-2)
    require('imbalanced head PSD via angular lock', determinant_floor > 0)
    loss_budget = (F(25, 48)+F(3, 32))/(4*alpha)
    residual = F(1, 63) if bad == 'loss-budget' else F(1, 64)
    require('imbalance covers head-tail losses', loss_budget == F(59, 320) and F(1, 5)-loss_budget >= residual)

    # Symmetric moment kernel with norm 9, row maximum 11, and positive
    # Perron vector h=(3,1). Allocate each ordered edge once at each endpoint.
    moment = ((8, 3), (3, 0))
    h = (3, 1)
    g2 = (4, 9)
    rho = 9
    for i in range(2):
        require('positive eigenvector gives norm allocation', sum(moment[i][j]*h[j] for j in range(2)) == rho*h[i])
    total = 0
    for i in range(2):
        for j in range(2):
            ratio = F(h[j], h[i]) if bad == 'perron-ratio' else F(h[i], h[j])
            value = g2[i]/ratio+g2[j]*ratio
            total += moment[i][j]*value
    endpoints = 1 if bad == 'endpoint-factor' else 2
    require('ordered endpoint budget', total == endpoints*rho*sum(g2))
    require('nonnegative kernel need not have constant row', max(map(sum, moment)) > rho)

    c = F(1, 2)+F(1, 200)
    t = F(1, 20) if bad == 'soft-witness' else F(1, 200)
    require('independent-weight relaxation has a strict head instability', 0<t<2*c-1 and 1-2*c/(1+t)<0)
    print('PASS: exact tail, completion, angular allocation, and relaxed sharpness')


if __name__ == '__main__':
    main()
