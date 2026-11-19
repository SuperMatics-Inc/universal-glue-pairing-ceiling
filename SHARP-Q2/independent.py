"""Independent exact assembly, zero-pivot LDL, and reciprocal unfolding checks."""
from argparse import ArgumentParser
from fractions import Fraction as Q
from itertools import product


def check(label, condition):
    if not condition:
        raise SystemExit(f"REJECT: {label}")


def positive(A):
    """Schur elimination in-place on an exact symmetric finite matrix."""
    for k, row in enumerate(A):
        pivot = row[k]
        if pivot < 0 or (pivot == 0 and any(row[k+1:])):
            return False
        if pivot == 0:
            continue
        for i in range(k+1, len(A)):
            for j in range(i, len(A)):
                A[i][j] -= row[i]*row[j]/pivot
    return True


def edge_check(left, right, ratio, t, bad):
    # Stay in v coordinates: no square roots or use of the analytic Schur caps.
    dims = [(a, n, b) for a, side in enumerate((left, right)) for n, b in enumerate(side) if b]
    M = [[Q(0) for _ in dims] for _ in dims]
    margin = Q(1, 64) if bad == 'no-soft-margin' else min(Q(1, 64), t/(1+t))
    for i, (a, n, b) in enumerate(dims):
        M[i][i] += (1-margin)*b*(2*n+1)*(ratio if a else 1/ratio)
        if a:
            continue
        for j, (z, m, d) in enumerate(dims):
            if not z:
                continue
            B, F = 1/(t+(n-m)**2), 1/(t+(n+m+1)**2)
            if bad != 'omit-head-lock' or n+m != 0:
                M[i][i] += b*d*(B-F)/2
                M[j][j] += b*d*(B-F)/2
            folded = B+(2 if bad == 'extra-reflection' else 1)*F
            M[i][j] = -folded*(1 if bad == 'undressed-gain' else b*d)/2
    return positive(M)


def main():
    p = ArgumentParser(description=__doc__)
    p.add_argument('--mutant', choices=('omit-head-lock', 'extra-reflection', 'undressed-gain',
                                       'no-soft-margin', 'missing-ordered-copy'))
    bad = p.parse_args().mutant
    cases = 0
    profiles = ((1, 0, 0, 0), (0, 1, 0, 0), (1, 1, 1, 1), (0, 0, 0, 0),
                (1, 0, 1, 0), (0, 1, 0, 1), (Q(1, 3), Q(1, 4), Q(2, 3), 0))
    for left, right, r, t in product(profiles, profiles,
                                    (Q(1, 60), Q(1, 3), Q(1), Q(3), Q(60)),
                                    (Q(1, 1000), Q(1, 4), Q(3), Q(40))):
        check(f'finite edge PSD: {left}, {right}, r={r}, t={t}', edge_check(left, right, r, t, bad))
        cases += 1

    # Compare the ordered edge formula with directly assembled angular-frequency
    # normal diagonal and anomalous terms, including a diagonal angular loop.
    moment = ((Q(1), Q(2, 3)), (Q(2, 3), Q(0)))
    b = ((Q(2, 3), Q(1, 2)), (Q(3, 4), Q(1, 3)))
    v = ((Q(1, 2), Q(-3, 4)), (Q(5, 9), Q(7, 12)))
    t = Q(5, 11)
    ordered = direct = Q(0)
    for x, y, n, m in product(range(2), repeat=4):
        D = 1/(t+(n-m)**2)
        H = 1/(t+(n+m+1)**2)
        coeff = moment[x][y]*b[x][n]*b[y][m]
        direct += coeff*((D-H)*v[x][n]**2-(D+H)*v[x][n]*v[y][m])
        edge = coeff*((D-H)*(v[x][n]**2+v[y][m]**2)-2*(D+H)*v[x][n]*v[y][m])
        if bad != 'missing-ordered-copy' or x <= y:
            ordered += edge/2
    check('reciprocal unordered/ordered factors', direct == ordered and direct != 0)
    print(f'PASS: {cases} exact finite edge matrices and independent ordered-pair assembly')


if __name__ == '__main__':
    main()
