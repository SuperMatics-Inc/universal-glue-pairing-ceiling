"""Exact finite checks for PLASMON-W/RIGOR.md. No normal-branch approximation."""
from fractions import Fraction as F
import sys


MUTANTS = {"head-fold", "partner-diagonal", "ratio-endpoint", "tail-row",
           "tail-spread", "static-sign", "omitted-normal"}
mode = sys.argv[1] if len(sys.argv) == 2 else None
if mode is not None and mode not in MUTANTS:
    raise SystemExit(f"unknown mutation: {mode}")


def check(condition, label):
    if not condition:
        raise SystemExit(f"REJECT: {label}")


t_max = F(1, 12)
ratio = F(3, 2) if mode != "ratio-endpoint" else F(16, 11)
upper = (1 + 4*t_max) / (1 - t_max)
check(upper == F(16, 11) and upper < ratio, "strict width-ratio endpoint")
N = 64 if mode != "tail-spread" else 60
row = 2 if mode != "tail-row" else 1
# Coefficients of the loss in units of L: diagonal and two ordered cross terms.
loss = ratio*row + 4
check(loss == 7 and loss*2*(1+t_max)/N < F(1, 4),
      "integral tail loss leaves a quarter of the head")
check(F(100, 99)*(upper+F(1, 44)) < ratio, "explicit width-ratio margin")
check(4*F(100, 99)*(F(1, 44)+1+4*t_max) < 6, "explicit bare-cost margin")
check(576 == (4*6)**2, "explicit coupling factor")

for t in (F(1, 12), F(1, 13), F(1, 1000)):
    g = [t/(t+j*j) for j in range(4*N+1)]
    active = {0: F(1), **{n: F(-1, N) for n in range(N, 2*N)}}
    check(max(2*n+1 for n in active) == 255 and
          sum((2*n+1)*y*y for n,y in active.items()) == 4,
          "static-null trial bare sum")
    static = sum(active.values()) if mode != "static-sign" else sum(map(abs, active.values()))
    check(static == 0, "instantaneous null")
    # Synthetic admissible weight ratios on finite support. Beyond the explicit
    # range b is constant; the infinite residual row telescopes exactly.
    M = 2*N
    b = [F(6 + m % 4, 9) for m in range(M)]
    b_tail = F(5, 6)
    normal, pair, diag, cross = F(0), F(0), F(0), F(0)
    for n, y in active.items():
        p = [g[abs(n-m)]-g[n+m+1] for m in range(M)]
        residual = sum(g[M-n:M+n+1])
        check(sum(p)+residual == 1+2*sum(g[1:n+1]), "odd row telescope")
        if n == 0:
            check(sum(p[1:])+residual == g[1], "head off-diagonal row")
        check(p[n] == 1-g[2*n+1], "reflected normal diagonal")
        off_row = sum(p[m]*b[m] for m in range(M) if m != n) + residual*b_tail
        normal += y*y*(sum(u*v for u,v in zip(p,b)) +
                       (0 if mode == "omitted-normal" else residual*b_tail))/b[n]
        fold = (-1 if mode == "head-fold" and n == 0 else 1)
        refl = (1 if mode == "partner-diagonal" else 2)
        diag += y*y*(refl*g[2*n+1]-off_row/b[n])
        for m,z in active.items():
            pair += y*z*(g[abs(n-m)]+fold*g[n+m+1])
            if m != n:
                cross += y*z*(g[abs(n-m)]+g[n+m+1])
    check(pair-normal == diag+cross, "matched diagonal cancellation")
    check(pair-normal > g[1]/4, "positive static-free gain")

print("CERTIFIED finite identities: width-ratio margin, odd rows, static-null gain")
