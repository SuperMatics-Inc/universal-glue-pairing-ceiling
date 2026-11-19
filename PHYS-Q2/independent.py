"""Independent exact quadratic forms with untruncated normal rows."""
import argparse
from fractions import Fraction as F

p = argparse.ArgumentParser(description=__doc__)
p.add_argument('--mutant', choices=('ordered-copy', 'lock-factor', 'head-fold', 'flat-edge-sign'))
mode = p.parse_args().mutant
eta = (2, 3)
beta = (F(1, 2), F(1, 3))
wt = tuple(a*b for a, b in zip(eta, beta))
wh = (1, 3, 5)


def check(value, label):
    if not value:
        raise SystemExit(f'REJECT: {label}')


for t in (F(1, 9), F(1, 100), F(1, 10000)):
    def k(j):
        return 1/(t+j*j)

    def odd(n, m):
        return k(abs(n-m))-k(n+m+1)

    def even(n, m):
        return k(abs(n-m))+k(n+m+1)

    nrm_row = [k(0)+2*sum(k(j) for j in range(1, n+1)) for n in range(3)]
    rem = [nrm_row[n]-sum(odd(n, m) for m in range(3)) for n in range(3)]
    check(min(rem)>0, 'normal rows include the complement')

    for v in (((F(1), F(1, 5), F(-1, 63)),)*2,
              ((F(1), F(1, 5), F(-1, 63)), (F(1, 2), F(1, 5), F(-1, 63)))):
        support = range(3)
        edges = ((0, 1), (1, 0))
        bare = sum(wt[x]*wh[n]*v[x][n]**2 for x in range(2) for n in support)
        normal = sum(wt[x]*wt[y]*nrm_row[n]*v[x][n]**2 for x, y in edges for n in support)
        pair = sum(wt[x]*wt[y]*even(n,m)*v[x][n]*v[y][m]
                   for x, y in edges for n in support for m in support)
        # The Dirichlet construction visits the unordered angle pair exactly
        # once with both frequency axes. If the second angular orientation
        # is also visited, the factor 1/2 is necessary.
        x, y = edges[0]
        if mode == 'ordered-copy':
            edge_set = edges
        else:
            edge_set = edges[:1]
        cost = sum(wt[x]*wt[y]*odd(n, m)*(v[x][n]-v[y][m])**2
                   for x,y in edge_set for n in support for m in support)
        cost += sum(wt[x]*wt[y]*rem[n]*v[x][n]**2 for x,y in edges for n in support)
        reflection = sum(wt[x]*wt[y]*k(n+m+1)*v[x][n]*v[y][m]
                         for x,y in edges for n in support for m in support)
        check(bare+normal-pair == bare+cost-(1 if mode == 'head-fold' else 2)*reflection,
              'overlapping support and complement, full matched congruence')
        if v[0] == v[1]:
            # Normal K0 cancels exactly for common angular v.
            bare_scalar = sum(w*v[0][n]**2 for n,w in enumerate(wh))
            gain_scalar = sum((k(2*n+1)-2*sum(k(j) for j in range(1,n+1)))*v[0][n]**2
                              for n in support)
            gain_scalar += sum(even(n,m)*v[0][n]*v[0][m] for n in support for m in support if n!=m)
            check(bare+normal-pair == sum(wt)*bare_scalar-2*wt[0]*wt[1]*gain_scalar,
                  'common angular profile reduces to the scalar flat soft family')
        else:
            locked = wt[0]*wt[1]*odd(0,0)*(v[0][0]-v[1][0])**2
            if mode == 'lock-factor':
                locked /= 2
            check(t*(locked+k(1)/4)==F(1,4), 'same-frequency angular lock coefficient')

# Physical DOS weights need not give equal weighted masses at the two ends.
# q in the proof is sqrt(w)*v; this rational check instead expands in v.
flat_wt = (F(8, 5), F(1))
v = ((F(1), F(-1, 6), F(1, 7)), (F(1, 3), F(1, 8), F(-1, 9)))
for t in (F(1, 5), F(2)):
    def k(j):
        return 1/(t+j*j)

    R = [k(0)+2*sum(k(j) for j in range(1, n+1)) for n in range(3)]
    cross = sum((k(abs(n-m))+k(n+m+1))*v[0][n]*v[1][m]
                for n in range(3) for m in range(3))
    dr = sum(R[n]*v[0][n]*v[1][n] for n in range(3))
    axy = cross-dr
    lock = sum(R[n]*(v[0][n]-v[1][n])**2 for n in range(3))
    direct = sum(R[n]*(v[0][n]**2+v[1][n]**2) for n in range(3))-2*cross
    mass = flat_wt[0]*flat_wt[1]
    check(mass*direct == mass*((-1 if mode == 'flat-edge-sign' else 1)*lock-2*axy),
          'flat signed temporal split retains nonnegative angular normal row')
print('PASS: exact quadratic forms, complement, angular lock, and flat angular row split')
