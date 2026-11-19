"""Direct finite trials and cross-checks without importing the primary replay."""
from argparse import ArgumentParser
from fractions import Fraction


def require(condition, diagnostic):
    if not condition:
        raise SystemExit('REJECT: ' + diagnostic)


def main():
    parser = ArgumentParser(description=__doc__)
    parser.add_argument('--mutant', choices=('static-null', 'screening-diagonal', 'hard-normal', 'signed-budget', 'reciprocal-normal'))
    mode = parser.parse_args().mutant
    q = lambda j: Fraction(1, 1+j*j)
    values = {0: Fraction(1), **{k: Fraction(-1, 25) for k in range(25,50)}}
    if mode == 'static-null':
        values[49] = 0
    require(sum(values.values()) == 0, 'instantaneous rank-one annihilator')
    # For an individual row and j cutoff, the tail of the mass telescopes exactly.
    def complete_mass(n, s=60):
        require(s >= n, 'mass truncation includes diagonal')
        return sum(q(abs(n-m))-q(n+m+1) for m in range(s+1)) + sum(q(j) for j in range(s+1-n, s+n+2))
    diag = (q(0)+q(1) if mode != 'screening-diagonal' else q(0)-q(1)) - complete_mass(0)
    require(diag == Fraction(1,2), 'retained first diagonal after mass cancellation')
    gain = sum(values[n]*values[m]*(q(abs(n-m))+q(n+m+1)) for n in values for m in values)
    gain -= sum(complete_mass(n)*values[n]**2 for n in values)
    cost = sum((2*n+1)*v*v for n,v in values.items())
    require(gain > Fraction(1,4), 'exact plasmon trial gain')
    require(cost == 4 and 16*gain > cost, 'finite regulated model unstable at C_delta=16')

    # Direct angular-Rayleigh contraction with the antisymmetric vector (1,-1).
    v = [1, -1]
    A0 = [[Fraction(8),Fraction(1,8)],[Fraction(1,8),Fraction(8)]]
    A1 = [[Fraction(4),Fraction(8,65)],[Fraction(8,65),Fraction(4)]]
    full_pair = sum(v[x]*(A0[x][y]+A1[x][y])*v[y] for x in range(2) for y in range(2))
    row_mass = [1+sum(row) for row in A0]
    require(full_pair > sum(row_mass), 'antisymmetric trial against dominating normal mass')
    moment_soft = A0[0][0]
    moment_hard = A0[0][1]*(64 if mode != 'signed-budget' else 63)
    require(moment_soft-moment_hard == 0, 'signed moment cancellation')

    # Rational bound on a hard normal line using a different splitting index.
    M, R = 1500, (10000 if mode != 'hard-normal' else 1000)
    gain_normal = 4*Fraction(M*M, R*R+M*M) + Fraction(800,9*(2*M+1))
    require(gain_normal < Fraction(1,8), 'hard line gives little folded first-mode mass')

    # Independent stronger head witness: use the exact normal equal-index
    # decrement at the trial temperature, bounded s_B through b_B/s_B.
    tau = Fraction(101,100)
    s_A_cap = Fraction(1+4) + Fraction(1,10) + 1000/(1+10**4*tau*tau)
    N_B = 10**16 * (1 - 1/(1+tau*tau))
    require(Fraction(2*10**7, 9)/(tau*N_B) < Fraction(1,10**8), 'dominating normal mode empties partner DOS')
    require((4+4/(1+tau*tau))*(1-tau*s_A_cap/50) > s_A_cap, 'unmatched branch instability')
    D_A, D_B = 1000, Fraction(1,10**9) if mode != 'reciprocal-normal' else 1000
    adjoint_cross_sq = D_A*D_B*(1+Fraction(4,10000))**2
    require(adjoint_cross_sq < Fraction(1,100)**2, 'reciprocity with channel measures: geometric, not row, cross weight')
    print('PASS: independent rational trials; C_delta=16 beats the exact bare plasmon cost 4')


if __name__ == '__main__':
    main()
