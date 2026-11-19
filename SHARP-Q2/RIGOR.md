# An optimal norm ceiling for the independent-weight relaxation

**PROVED.** On the matched reciprocal angle-dependent model of `../RIGOR.md` §3, let \(d\eta=N_{\max}d\mu\), let \(d\mathfrak m_{xy}(E)\) be the reciprocal nonnegative moment measures on \(0<E<\infty\), and write \(\mathcal M\) for the nonnegative-kernel moment operator. Suppose it is bounded on \(L^2(d\eta)\), with norm \(0<\rho<\infty\), and that the transfers have bounded frequency row sums as in that section. Assume an ordinary sigma-finite channel measure, measurable kernels, and an actual positive reflected normal branch with the matched imaginary equation and weights \(0\le b_n(x)\le1\). The relative real equation is not used. Put \(\tau=k_BT\). Then
\[
 \tau_{\rm lin}<\frac{\sqrt\rho}{\pi\sqrt{2}}.
\]
The coefficient is optimal if independent \(b_n(x)\in[0,1]\) are allowed instead of a normal DOS branch. Thus for the actual coupled problem the sharp norm coefficient lies in \([C_\infty,1/(\pi\sqrt2)]\); the lower endpoint is inherited from the sharp scalar case (e). Whether it is the answer remains **OPEN**. In particular the proof below does not produce a physical counterexample to \(C_\infty\).

## 1. Normal cancellation and the pair contribution

Use positive frequencies \(n\ge0\), \(w_n=2n+1\). For an energy \(E>0\) at temperature \(\tau\), put \(t=(E/(2\pi\tau))^2\), \(k_j=1/(t+j^2)\), \(h_{nm}=k_{n+m+1}\), \(p_{nm}=k_{|n-m|}-h_{nm}\ge0\), and \(S_{nm}=p_{nm}+2h_{nm}\). These are frequency matrices for the **unit dimensionless moment**. The actual transfer from the atom is \((2\pi\tau)^{-2} k_j\,d\mathfrak m_{xy}(E)\). Set \(g_{x,n}=\sqrt{w_n b_n(x)}v_{x,n}\), where \(v\) is the variable after cancellation of the matched local odd mass. Modulus and even fold upper bound the full-line pairing operator, as in the parent proof. The stability form in the folded variables is
\[
 Q=\int\|g_x\|^2d\eta(x)+\frac{1}{2(2\pi\tau)^2}\iint\int I_{xy}(t)\,d\mathfrak m_{xy}(E)\,d\eta(x)d\eta(y),
\]
where the single ordered-edge contribution satisfies
\[
 I_{xy}(t)=\sum_{n,m} b_n(x)b_m(y)\big[p_{nm}(|v_{x,n}|^2+|v_{y,m}|^2)-2 S_{nm}\Re(\bar v_{x,n}v_{y,m})\big].
\]
Reciprocity explains the factor \(1/2\) on ordered edges. For a loop \(x=y\) in a discrete measure this formula still holds; the two endpoints can first be treated independently before setting their profiles equal. One can first use finite frequency support; a zero trial on an omitted frequency contributes only a nonnegative normal diagonal to the retained coordinates.

## 2. An edge bound at unit allocation

**PROVED.** For every \(r>0\) define the allocated bare cost
\[
 B_r=r^{-1}\|g_x\|^2+r\|g_y\|^2,\qquad
 \delta(t)=\min\{1/64,t/(1+t)\}.
\]
Then \(B_r+\tfrac12 I_{xy}(t)\ge\delta(t)B_r\) for arbitrary independent weights in \([0,1]\). To check it, keep \(v\) fixed. The difference is separately affine in each of the endpoint weights. Reduce it to binary weights by averaging over independent Bernoulli endpoint weights on the finite support (even for a loop, use the two-copy inequality before identifying endpoints). In the binary case only active coordinates are present. Rescale them to \(a_n=g_{x,n}/\sqrt r\), \(d_n=\sqrt r\,g_{y,n}\), so \(B_r=\|a\|^2+\|d\|^2\). A pair with two active coordinates contributes
\[
 \tfrac12 p_{nm}\left(\frac{r|a_n|^2}{w_n}+\frac{r^{-1}|d_m|^2}{w_m}\right)
   -S_{nm}\frac{\Re(\bar a_nd_m)}{\sqrt{w_nw_m}} .
\]
An inactive coordinate deletes the whole corresponding interaction, rather than just its gain.

**Tail against tail.** For \(n,m\ge1\), drop the nonnegative \(p\) difference square. The remaining contribution with the tail bare cost is at least \((11/12)(\|a_{\rm t}\|^2+\|d_{\rm t}\|^2)\). Indeed the tail Hankel norm with entries \(h_{nm}/\sqrt{w_nw_m}\) is \(<1/12\): compare it to the soft tail and use Schur weights \(1/\sqrt{w_n}\), whose worst row sum is \(\sum_{m\ge1}[(2m+1)(m+2)^2]^{-1}\). Sum through 16 and enclose the remainder by \(1/(4\cdot16^2)\). The product estimate uses \(2\|a_{\rm t}\|\|d_{\rm t}\|\le\|a_{\rm t}\|^2+\|d_{\rm t}\|^2\) because \(r\) cancels in the cross term.

**Head against tail.** Reserve \(1/12\) of the tail bare norm and complete the square with the other \(\alpha=5/6\). Every tail coordinate has at most one opposing head. For an active \(a_0,d_m\), \(m\ge1\), the form to complete is
\[
 \frac{r p}{2}|a_0|^2+\left(\alpha+\frac{p}{2r w_m}\right)|d_m|^2-\frac{S}{\sqrt{w_m}}\Re(\bar a_0 d_m),
 \quad p=k_m-k_{m+1},\quad S=k_m+k_{m+1} .
\]
The square completion loses at most \(E(r,t)|a_0|^2\) after summing over active \(m\ge1\), where
\[
 0\le E(r,t)\le\sum_{m\ge1}\left[\frac{S^2}{4w_m(\alpha+p/(2r w_m))}-\frac{r p}{2}\right]_+ .
\]
For the other direction replace \(r\) by \(1/r\). Each term on the right vanishes when \(\alpha\ge 2/(r w_m^2)\): this is exactly the determinant condition because \((S^2-p^2)/(w_m p)=4/w_m^2\), independently of \(t\). In particular there are no losses from either direction for \(1/3\le r\le3\), since \(2/(9/3)=2/3<5/6\). For all \(r,t\) each head's loss is bounded by \(59/320\). In fact \(\sum_{m\ge1} S^2/w_m\le25/48+2\sum_{m\ge2}m^{-5}\le25/48+3/32=59/96\), using the first term exactly at \(t=0\), bounding \(S\le2/m^2\), and integrating \(u^{-5}\) from 2. Multiply this bound by \(1/(4\alpha)=3/10\).

**Head against head.** If one head is absent, its opposing head simply has its full bare cost, minus the above loss. If both are present their matrix before these losses is
\[
 H_0=\begin{pmatrix}1+\beta r&-\beta-u\\-\beta-u&1+\beta/r\end{pmatrix},
 \quad \beta=\frac1{2t(1+t)},\quad u=\frac1{1+t}.
\]
It is \(I-u\bigl(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\bigr)\) plus the PSD rank-one \(\beta\) term. Thus in the balanced range \([1/3,3]\) it leaves at least \(1-u=t/(1+t)\); there are no head-tail losses. In the other range \(H_0\succeq I/5\). For \(t\ge1/4\) this is immediate from \(u\le4/5\). For \(t<1/4\) use \(\beta\ge8/5\), \(r+r^{-1}\ge10/3\), and test \(H_0-I/5\) by its positive first diagonal and determinant:
\[
 \det(H_0-I/5)=16/25-u^2+\beta[(4/5)(r+r^{-1})-2u]\ge-9/25+(8/5)(2/3)>0.
\]
After either directional loss it leaves at least \(1/5-59/320=1/64\). This treats all head masks, also if neither head is active. Adding the tail reserve proves the edge bound. The soft value \(t=0\) was used only to bound positive-transfer tails and is not an atom allowed in the model.

## 3. Angular allocation: keep the norm, not the maximum row

Set \(\mathcal M_\delta(\tau)\) to be the nonnegative symmetric kernel whose entry is \(\int[1-\delta((E/(2\pi\tau))^2)]d\mathfrak m_{xy}(E)\). It is bounded by \(\mathcal M\) in the entrywise order, which controls the top and the absolute norm of nonnegative kernels. For any \(R>\|\mathcal M_\delta(\tau)\|\), choose \(h=(I-\mathcal M_\delta/R)^{-1}\phi\) with a strictly positive \(\phi\in L^2(d\eta)\); a sigma-finite measure admits such a \(\phi\). The positive Neumann series gives \(0<h<\infty\) a.e. and \(\mathcal M_\delta h\le R h\). Choose \(r=h(x)/h(y)\) separately for each edge. Integrating \(I_{xy}\ge-2[1-\delta(t)]B_r\) and using symmetry yields
\[
 Q\ge \|g\|^2-\frac{2}{(2\pi\tau)^2}\int\|g_x\|^2\frac{(\mathcal M_\delta h)(x)}{h(x)}d\eta(x)
 \ge\left(1-\frac{2R}{(2\pi\tau)^2}\right)\|g\|^2 .
\]
The factor two comes from the two endpoints, not from an additional frequency fold. This proves stability when \((2\pi\tau)^2>2\|\mathcal M_\delta(\tau)\|\) by choosing an intermediate \(R\). All lower bounds apply first to bounded finite-support tests and then to the stable form by density; the allocated bare integrals are finite by superharmonicity. In symmetrized gap variables the bare norm \(\|g\|^2\) controls the gap norm by the positive-width row bound, so the inequality excludes a marginal spectral top as well. This argument also works with extra nonnegative folded normal mass and PSD pairing subtraction, although the claim here only needs the matched equations.

For the strict onset statement, let \(\tau_*=\sqrt\rho/(\pi\sqrt2)\), \(\tau_+\!=2\tau_*\), and choose a fixed physical cutoff \(E_0>0\) small enough that \(E_0^2\|K_0\|<\rho/2\). The soft moment operator for \(0<E<E_0\) has norm at most \(E_0^2\|K_0\|\) by entrywise domination; \(K_0(x,y)=\int E^{-2}d\mathfrak m_{xy}\) is bounded by the assumed row condition. For \(\tau\le\tau_+\), the remainder has \(\delta(t)\ge d_0:=\delta((E_0/(2\pi\tau_+))^2)>0\). Thus \(\|\mathcal M_\delta(\tau)\|\le(1-d_0)\rho+d_0\rho/2<\rho\) uniformly there. There is a common stability interval starting strictly below \(\tau_*\); the simpler \(\|\mathcal M_\delta\|\le\rho\) suffices above \(\tau_+\). If \(\rho=0\), the nonnegative kernel has no pairing component and there is no instability.

## 4. Exact comparison class and limitations

For a scalar relaxed model with \(b_0=1\), all \(b_{m>0}=0\), and a single Einstein transfer, the head stability test is precisely \(1-2c/(1+t)\), \(c=\rho/(2\pi\tau)^2\). It is negative for any \(c>1/2\) with \(0<t<2c-1\). Thus no smaller norm coefficient can follow from the imaginary equation and the box constraint on independent weights alone. Such weights are not admissible Poisson averages of a fixed nonzero DOS: every positive-width Poisson kernel is positive at all energies. The example is a genuine obstruction to a proof that uses no further branch information, not a counterexample to the original matched ceiling. The earlier norm bound improves from \(\sqrt{113/55}/(2\pi)\) to \(1/(\pi\sqrt2)\); unlike the preceding maximum-row estimate, this upgrade does not require an upper bound on the moment row in terms of \(\rho\).
