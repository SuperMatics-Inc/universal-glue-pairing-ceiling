# Shifted branches: causality, a sharper bracket, and the sharp external-shift relaxation

All statements concern the linearized Eliashberg normal branch, not a measured or thermodynamic transition. Temperatures are energies \(\tau=k_BT\). Every numerical-looking budget below is exact rational arithmetic unless expressly marked as a calculated decimal. No novelty or priority is claimed. The preceding note and release directories are frozen and are not modified by this slice.

## 1. Classes must be kept separate

Retain the reciprocal nonnegative matched model and its stability form from `../SHARP-Q2/RIGOR.md`. There are finitely many positive-height angular channels, energy-independent radial vertices, nonnegative positive-energy Lorentzian measures, bounded normal frequency rows, and moment-operator norm \(0<\rho<\infty\) in DOS-height measure. The normal width equation is
\[
 s_{n,x}=w_n+\sum_{m,y}\eta_y P^N_{nm}(x,y)b_{m,y},\qquad w_n=2n+1.
\]
The pairing kernel is the matched positive kernel or an eligible envelope whose odd-folded normal mass is dominated by \(P^N\). Eligible bounded PSD pairing-only subtractions are allowed. Each DOS is a fixed nonnegative function bounded by its channel height. No angular-average moment is substituted for \(\rho\).

**PROVED, imported:** without any information about real shifts or DOS realization, the independent-weight class \(0\le b_{n,x}\le1\) has sharp coefficient \(1/(\pi\sqrt2)\). This is the result of `../SHARP-Q2/RIGOR.md`, including strict exclusion for each fixed eligible positive-energy glue.

We distinguish three subclasses.

1. **Independent weights:** arbitrary numbers in the unit box.
2. **Externally prescribed shifts:** a fixed bounded finite DOS, arbitrary real shifts at the Matsubara points, and a self-consistent positive imaginary equation. No relative real equation or causal analytic continuation is imposed.
3. **Actual causal branches:** the DOS weights come from one channel-wise causal normal propagator at every tested temperature. In physical frequency variables, its effective normal frequency \(Z_x(z)=z-\Sigma_x(z)\) is a holomorphic upper-half-plane self-map, and \(Z_x(i\pi\tau w_n)/(\pi\tau)=x_{n,x}+is_{n,x}\). Thus \(x_n=-\chi_n/(\pi\tau)\) if the denominator is written as \(u_n^2+(\xi+\chi_n)^2\). This real-sign convention is immaterial to the distance estimates. The property is equivalent, in this energy-independent self-energy parameterization, to each radial propagator \(G_{x,\xi}(z)=[Z_x(z)-\xi]^{-1}\) being holomorphic with negative imaginary part. A self-energy with \(-\Sigma\) a Nevanlinna function is sufficient. Neither causality of the *glue alone* nor causality of an angularly averaged propagator establishes it for an arbitrary algebraic Matsubara branch. For solutions of the full normal problem the relative real equation is an additional required equation, not a substitute for the analytic self-map hypothesis.

The larger class of positive reflected branches satisfying the coupled relative real equation, but without an established causal continuation, is not silently identified with class 3. Its sharp constant remains OPEN.

## 2. PROVED: Harnack control with arbitrary frequency-dependent real shifts

Let \(Z\) be a holomorphic upper-half-plane self-map. Schwarz-Pick applied at \(i\omega\) and \(iK\omega\), \(K>1\), gives
\[
 |Z(iK\omega)-Z(i\omega)|^2
 \le\frac{(K-1)^2}{K}\Im Z(iK\omega)\Im Z(i\omega).
 \tag{H}
\]
Indeed, their pseudohyperbolic distance is at most \((K-1)/(K+1)\). Squaring \(|z_1-z_0|/|z_1-\bar z_0|\), and using \(|z_1-\bar z_0|^2=|z_1-z_0|^2+4u_0u_1\), yields (H). Constant self-maps satisfy the same estimate.

Here is a direct finite algebra proof of the needed Poisson comparison, so no unproved inference from the width ratio is used. Write \(z_j=x_j+iu_j\), with \(u_j>0\), and let \(q_a(z)=u/[(a-x)^2+u^2]\). Under (H),
\[
 K^{-1}q_a(z_0)\le q_a(z_1)\le Kq_a(z_0)\quad(a\in\mathbb R).\tag{P}
\]
For the upper inequality, clear the positive denominators. The resulting quadratic in \(a\) is
\[
 A a^2-2B a+C,
\quad A=Ku_0-u_1,\quad B=Ku_0x_1-u_1x_0,
\quad C=Ku_0(x_1^2+u_1^2)-u_1(x_0^2+u_0^2).
\]
Its determinant identity is
\[
 AC-B^2=K u_0u_1\left[\frac{(K-1)^2}{K}u_0u_1-(x_1-x_0)^2-(u_1-u_0)^2\right].\tag{D}
\]
Condition (H) implies \(u_0/K\le u_1\le Ku_0\), by factoring the width-only quadratic. Thus \(A\ge0\). For \(A>0\), complete the square: \(A(a-B/A)^2+(AC-B^2)/A\ge0\). If \(A=0\), (H) forces \(x_1=x_0\); then \(B=0\) and \(C=u_0u_1(Ku_1-u_0)>0\). Swap the endpoints to prove the lower inequality. This proof applies pointwise to every real energy, including DOS asymmetry and nonconstant real shifts.

Normalize the channel DOS to \(0\le r_x(a)\le1\), and set
\[
 b_{n,x}=\pi^{-1}\int r_x(a)q_a(z_{n,x})\,da.
\]
Integrate (P) both against \(r_x\) and its complementary DOS \(1-r_x\). Integrability of the complement is unnecessary: its Poisson integral is finite because it is bounded, and the full Poisson integral equals \(\pi\). At adjacent Matsubara frequencies \(K=w_{n+1}/w_n\),
\[
 K^{-1}b_{n,x}\le b_{n+1,x}\le Kb_{n,x},\qquad
 K^{-1}(1-b_{n,x})\le1-b_{n+1,x}\le K(1-b_{n,x}).\tag{C}
\]
In particular,
\[
 \boxed{b_{1,x}\ge1-3(1-b_{0,x}).}\tag{C0}
\]
This step does not assume that widths are monotone, that shifts are zero, or that DOS shapes agree across channels. It also shows why the independent-weight head mask cannot be approached on causal branches: if \(b_0\to1\), then \(b_1\to1\), not zero.

## 3. PROVED: the improved coefficient applies to causal shifted branches

Define exact constants
\[
 d=685881/7152100,\quad d_+=685881/6979600,\quad
 \delta_* =\min\{8369/39360,\ 1/10,\ 121/1261,\ 29/300,\ d_+\}.
\]
Every entry in this minimum is strictly larger than \(d\), and \(d_+<1/3\).

The purely algebraic ordered-edge argument in `../CENTERED-GAP/RIGOR.md` §2 needs only unit-box weights and (C0), not the centered normal-map proof in its §1. We spell out the dependency and the reserve steps. For one atom, put \(t=(E/(2\pi\tau))^2>0\), \(k_j=(t+j^2)^{-1}\), \(p_{nm}=k_{|n-m|}-k_{n+m+1}\), and \(S_{nm}=k_{|n-m|}+k_{n+m+1}\). For any angular allocation \(r>0\), let \(B_r=r^{-1}\|g_x\|^2+r\|g_y\|^2\). The ordered contribution is
\[
 I_{xy}=\sum_{n,m}b_{n,x}b_{m,y}\{p_{nm}(|v_{n,x}|^2+|v_{m,y}|^2)-2S_{nm}\Re(\bar v_{n,x}v_{m,y})\},\quad g_{n,x}=\sqrt{w_n b_{n,x}}v_{n,x}.
\]
Separate affine dependence permits independent Bernoulli masks on each endpoint; even a loop first uses the two-copy inequality. Zero trial amplitudes at omitted frequencies discard only nonnegative normal cost.

The tail Hankel norm is less than \(1/12\). Allocate \(\alpha=41/50\) of the tail cost to head-tail square completions, retaining \(29/300\). The identity \((S^2-p^2)/(w_mp)=4/w_m^2\) proves no completion loss in either direction for \(1/3\le r\le3\). For other allocations the head loss is at most \((59/96)/(4\alpha)\). The two-head matrix is
\[
 H_0=\begin{pmatrix}1+\beta r&-\beta-u\\-\beta-u&1+\beta/r\end{pmatrix},\quad u=(1+t)^{-1},\quad \beta=u^2/[2(1-u)].
\]
It has lower bounds \((1-u)I\) and \((1-2/(r+r^{-1}))I\). These give the reserves \(8369/39360\) outside \([1/3,3]\), \(1/10\) when \(t\ge1/9\) inside that interval, and \(121/1261\) when \(r\) lies outside \([19/30,30/19]\) in the remaining range.

In the last range \(0<t<1/9\), \(19/30\le r\le30/19\), keep the active head to opposing frequency 1 completion. Its head reserve is
\[
 D_1=\frac{p(r\alpha/2-1/9)}{\alpha+p/(6r)},\quad
 p=k_1-k_2\in[243/370,3/4].
\]
Writing \(a=r\alpha/2-1/9>0\) and \(z=\alpha+p/(6r)>0\) gives
\(\partial_pD_1=a\alpha/z^2>0\) and
\(\partial_rD_1=p[(\alpha/2)z+ap/(6r^2)]/z^2>0\).
Its exact minimum is therefore \(d_+\). When the opposing head is absent the reserve is one. Averaging these contributions using (C0) leaves at least
\[
 1-b_{0,y}+d_+b_{1,y}\ge d_++(1-3d_+)(1-b_{0,y})\ge d_+.
\]
The opposing endpoint is treated identically, with no interchannel DOS correlation assumption. Consequently
\[
 B_r+I_{xy}/2\ge\delta_* B_r.\tag{E}
\]
The infinite tail estimates and completion bounds are written fully in `../SHARP-Q2/RIGOR.md` §2 and the centered edge proof. Those analytic inputs are not replaced by matrix samples. The two unchanged finite replay files are hash-pinned by `verify.py` and replayed there, including their named coefficient/sign mutants.

For finite channels take a positive superharmonic vector \(h\) for the moment operator at any \(R'>\rho\), for example the positive resolvent construction from `../SHARP-Q2/RIGOR.md` §3. Allocate \(r=h_x/h_y\), integrate (E) with the reciprocal measure and the ordered-edge factor \(1/2\), and retain the two endpoint allocations. The resulting form satisfies
\[
 Q\ge\left[1-\frac{2(1-\delta_*)R'}{(2\pi\tau)^2}\right]\|g\|^2.
\]
Choose \(R'\downarrow\rho\); since \(\delta_*>d\), there is a stability interval starting strictly below
\[
 \boxed{\tau_{\rm lin}<U\sqrt\rho,\qquad U=\frac{\sqrt{6466219/3576050}}{2\pi}.}\tag{U}
\]
The same bound holds above that interval by the moment bound. Bounded normal rows convert the bare-form gap to a gap in the symmetrized pairing coordinates. Extra odd-folded normal dominance contributes a nonnegative diagonal, and a PSD pairing subtraction contributes a nonnegative form. Thus neither changes the exclusion on the actual causal branch. The relevant envelope must preserve the pairing symmetry sector; a signed channel moment is not a positive budget.

**OPEN:** the sharp coefficient on causal shifted branches is in \([C_\infty,U]\), by the centered scalar soft family and (U). Nothing here proves an excess above the centered optimum, or equality of those two optima. The result does not prove causal continuation for every coupled relative-real Matsubara solution. For that larger class the proved bracket remains \([C_\infty,1/(\pi\sqrt2)]\).

**PROVED, lower-endpoint admissibility:** this class allows bounded constant DOS, not only finite-mass boxes. The imported flat scalar soft family is causal. For a flat electronic spectral density and one positive-energy boson, the retarded normal self-energy has the thermally weighted spectral form
\[
 \Sigma(z)=\int\gamma(dE)\int A\,d\xi\left[
 \frac{n_B(E)+f(\xi)}{z-\xi+E}
 +\frac{n_B(E)+1-f(\xi)}{z-\xi-E}\right],
 \quad \gamma\ge0.
\]
Here \(K(i\nu)=\lambda E^2/(E^2+\nu^2)\) is the dimensionless Einstein transfer, so \(\gamma=\lambda E\,\delta_E/(2A)\); the DOS height is not counted twice. The real integral is taken with the standard real Cauchy subtraction; its imaginary part converges absolutely since its bounded density multiplies \(\Im z/|z-a|^2\). Both thermal coefficients are nonnegative, so \(\Im\Sigma(z)\le0\), and \(Z=z-\Sigma\) is an upper-half-plane self-map. Reflection of \(\xi\) interchanges the two terms because \(f(-\xi)=1-f(\xi)\), so the normal branch is centered on the imaginary axis. The fermionic partial-fraction sum of the positive Einstein transfer and \((i\omega_m-\xi)^{-1}\) gives exactly these two terms: the two sums have numerators \(-[n_B+1-f]\) and \(n_B+f\), while the Lorentzian pole decomposition has opposite signs. The flat energy integral of a causal propagator is \(-i\pi A\,\operatorname{sgn}\omega_m\), independent of its width. Hence this self-energy solves the matched flat normal equation and its real equation; it is not an arbitrary interpolant assigned to the widths. The accepted scalar soft-limit comparison supplies onsets approaching \(C_\infty\sqrt\rho\), establishing the lower endpoint for the causal class. No finite-mass causal approximation theorem is needed for this lower bound.


## 4. PROVED: a finite-DOS external-shift extremal family

The sharp independent-weight coefficient remains optimal even if one requires a single fixed finite-mass box DOS and self-consistency of the *imaginary* equation at each family member. It is the externally prescribed real shifts, not a zero DOS tail, that realize the relaxation.

Work at fixed \(\tau=1/(2\pi)\), so \(\pi\tau=1/2\), and let the moment be \(\rho=c\). For \(0<\delta\le1/4\), put
\[
 c=1/2+\delta,\quad t=\delta,\quad \epsilon=\delta/(12c),\quad
 W=\frac{2(1+c/t+c\epsilon)}{\epsilon},\quad
 R=\frac{W}{2\epsilon},\quad L=W+R.
\]
All are finite and positive. In dimensionless energy use DOS \(r(a)=1_{[-W,W]}(a)\), transfer \(K_j=c/(t+j^2)\), and prescribe \(x_0=0\), \(x_{n\ge1}=L\). The physical boson energy is \(E=\sqrt t\); \(K_j=\rho/[E^2+(2\pi\tau j)^2]\), so no factor of \(2\) or \(\pi\) is omitted from the moment. Physical box halfwidth and shift magnitudes are \(W/2\) and \(L/2\). Reflected negative frequencies use the same real shifts and opposite widths.

To define one model at every temperature, keep the physical DOS halfwidth \(W/2\), moment \(c\), and energy \(\sqrt t\) fixed, and prescribe the physical effective real center \(\Re Z(i\omega)=(L/2)1_{\{|\omega|\ge1\}}\). At the test temperature \(\tau=1/(2\pi)\), the first positive Matsubara frequency is \(1/2\), while all remaining frequencies are at least \(3/2\). Dividing those fixed real centers by \(\pi\tau=1/2\) gives exactly \(x_0=0\), \(x_{n\ge1}=L\). At other temperatures use the same step function and the same fixed DOS, not a rescaled family member. The imaginary contraction still applies at every positive temperature. Thus the instability at the test temperature is a legitimate lower bound on that model's onset, not just a collection of unrelated temperature-specific weights.

For any positive width \(s\), the off-center Poisson weight obeys
\[
 b(s,L)\le\frac{2Ws}{\pi(R^2+s^2)}\le\frac{W}{\pi R}\le\epsilon,
\]
using \(s/(R^2+s^2)\le1/(2R)\) and \(\pi>2\). At the head,
\(b(s,0)=(2/\pi)\arctan(W/s)\ge1-s/W\).
The exact odd row is \(\sum_{m\ge0}P_{0m}=K_0\), and its tail is \(\sum_{m\ge1}P_{0m}=K_1\). Hence the self-consistent head width is at most
\(s_0\le1+c/t+c\epsilon/(1+t)\le1+c/t+c\epsilon\), and \(b_0\ge1-\epsilon/2\ge1-\epsilon\).

A full positive imaginary solution exists uniquely at these externally imposed shifts. The full normal row is at most \(D=c(1/t+4)\), since \(\sum_{j\ge1}j^{-2}\le2\). The normal update sends the box \(w_n\le s_n\le w_n+D\) into itself. For fixed real center the pointwise Poisson derivative obeys \(|s\partial_s b|\le b\). In coordinates \(y_n=\log(s_n/w_n)\), the update is a contraction on the closed bounded box in \(\ell^\infty\), with Lipschitz constant at most \(D/(1+D)<1\). Positivity, all frequency sums and the finite-support test are therefore on a full untruncated imaginary branch, not a truncated solve.

For the single head trial \(v_0=1\), \(v_{n\ge1}=0\), the exact matched form is
\[
 Q/b_0=1+\sum_{m\ge1}P_{0m}b_m-2K_1b_0
 \le1+\frac{c\epsilon}{1+t}-\frac{2c(1-\epsilon)}{1+t}.
\]
Its negative margin has numerator
\[
 2c-3c\epsilon-(1+t)=3\delta/4>0.
\]
Thus the prescribed-shift model is unstable at the test temperature and
\(\tau_{\rm lin}/\sqrt\rho\ge1/(2\pi\sqrt c)\).
As \(\delta\downarrow0\), this ratio approaches \(1/(\pi\sqrt2)\), the imported universal upper bound for that class. This proves its sharp supremum with strictly positive finite-energy glue and strictly positive Poisson weights at every frequency. Each family member has a finite nonzero DOS; no single DOS is held fixed across all family members.

For an explicit strict comparison to the *proved centered upper bound*, choose
\(c=13/25\), \(t=1/100\), \(\epsilon=1/1000\), \(W=54000\), \(R=27000000\), \(L=27054000\). These need not equal the preceding asymptotic-family formulas. Here \((1+c/t+c\epsilon)/W<\epsilon\), and
\[
 2c-3c\epsilon-(1+t)=711/25000>0,\qquad
 c\,(6466219/3576050)<1.
\]
The latter exact inequality implies \(1/(2\pi\sqrt c)>U\). This is a strict instability beyond the entire proved centered upper interval **in the external-shift class only**.

This witness has no causal normal continuation. The same row bound gives \(s_0\le1+D\), \(s_1\le3+D\), while \(|x_1-x_0|=L\). Its parameters satisfy the exact inequality
\[
 L^2>\frac43(1+D)(3+D).
\]
Therefore it violates the necessary Schwarz-Pick condition (H) at the first two Matsubara points, regardless of the widths in that box. It also cannot satisfy the scalar relative real equation: the already proved scalar case-(e) ceiling would contradict its strict head instability above \(U>C_\infty\). That final exclusion imports the scalar theorem, not a new general real-equation bound.

## 5. Trust boundary and prior work

**PROVED:** (P), (C), the conditional causal shifted extension (U), and the finite-DOS external-shift extremal construction are fully argued above. **CERTIFIED** applies only to the finite rational/Lean replay evidence named in `RESULT.md`, not to analytic continuation, infinite-operator compactness or the imported scalar theorem. No floating-point fit or measured material enters any result.

**[INFERENCE] prior-work assessment:** Schwarz-Pick and Harnack are classical. The independent-weight sharp coefficient is already in the preceding slice and in the scalar arbitrary-shift discussion of the finite-band companion. The actual-causal branch condition is an added hypothesis, not a result establishing all normal branches as causal. The earlier verified literature comparison remains in `../RESULT.md` §3: Moussa-Cohen DOI `10.1103/PhysRevB.74.094520`, KAY arXiv `2409.00532`, Kondratev DOI `10.5281/zenodo.22848039`, Rens arXiv `2611.20496`, GSI Theorems 7-10, and the finite-band companion DOI `10.5281/zenodo.24364879`. No imported scientific claim beyond those already checked sources is needed here.

A targeted metadata search on 19 November 2026 covering 19 September through 19 November returned the GSI note and Rens preprint, but does not establish absence of prior art. Primary links: https://generalised.si/research/superconducting-tc-ceiling and https://arxiv.org/abs/2611.20496 . No new third-party full text was acquired or read in this slice. Paper-reader spawning is unavailable; no novelty claim is made. This local fold candidate is prepared at Main's request; there is no outward release.
