"""Independent exact finite-edge checks, including actual head/tail ratio tests."""
from argparse import ArgumentParser
from fractions import Fraction as F
from itertools import product

parser = ArgumentParser(description=__doc__)
parser.add_argument('--mutant', choices=('erase-first-tail', 'double-mixed-pair', 'overfold-normal'))
bad = parser.parse_args().mutant


def require(condition, label):
    if not condition:
        raise SystemExit(f'REJECT: {label}')


def psd(A):
    for j in range(len(A)):
        pivot = A[j][j]
        if pivot < 0:
            return False
        if pivot == 0:
            if any(A[j][i] for i in range(j+1, len(A))):
                return False
            continue
        for u in range(j+1, len(A)):
            for v in range(j+1, len(A)):
                A[u][v] -= A[u][j]*A[j][v]/pivot
    return True


def edge_matrix(left, right, t, r):
    # Rational coordinates are the v's rather than the normalized g's.
    profiles = (left, right)
    N = len(left)
    R = [[F(0) for _ in range(2*N)] for _ in range(2*N)]
    for j, side in enumerate(profiles):
        for n, b in enumerate(side):
            R[j*N+n][j*N+n] = F(181, 200)*(2*n+1)*b*(r if j else 1/r)
    for n, m in product(range(N), repeat=2):
        b = left[n]*right[m]
        direct, reflected = 1/(t+(n-m)**2), 1/(t+(n+m+1)**2)
        signed = direct-reflected
        if bad == 'overfold-normal':
            signed -= reflected
        R[n][n] += b*signed/2
        R[N+m][N+m] += b*signed/2
        cross = -b*(direct+reflected)/2
        if bad == 'double-mixed-pair':
            cross *= 2
        R[n][N+m] += cross
        R[N+m][n] += cross
    return R


first_tail = (F(1), F(0 if bad == 'erase-first-tail' else 1), F(0), F(0))
soft = (F(3, 4), F(1, 4), F(1, 5), F(1, 7))
profiles = (first_tail, soft, (F(1),)*4, (F(0),)*4, (F(1, 4), F(3, 4), F(1, 2), F(2, 3)),
            (F(2, 3), F(2, 9), F(1, 7), F(1, 6)))
count = 0
for left, right, t, r in product(profiles, profiles, (F(1, 1000), F(1, 16), F(1, 3), F(8)),
                                 (F(1, 100), F(1, 3), F(2, 3), F(1), F(3, 2), F(3), F(100))):
    label = f'exact centered edge PSD at t={t}, r={r}, left={left}, right={right}'
    require(psd(edge_matrix(left, right, t, r)), label)
    count += 1
print(f'CERTIFIED {count} exact finite centered edge matrices')
