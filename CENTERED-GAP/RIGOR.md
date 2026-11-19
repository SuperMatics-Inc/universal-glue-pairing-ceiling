# A uniform gap below the independent-weight bound on centered branches

**PROVED.** Keep the finite reciprocal angular model, moment norm \(\rho\), bounded folded normal rows, and stability form of [SHARP-Q2](../SHARP-Q2/RIGOR.md). On the actual centered branch the DOS in each channel may be any nonnegative integrable even profile bounded by its channel height. No real shifts, common spectral softening, or matching of widths is needed. For \(\rho>0\),
\[
 k_BT_{\rm lin}< U\sqrt{\rho},\qquad
 U=\frac1{2\pi}\sqrt{\frac{6466219}{3576050}}\simeq0.2140146706293698.
\]
The bound also applies to a centered normal kernel that is a positive reciprocal Lorentzian mixture with bounded rows and dominates the pairing envelope after folding. A bounded PSD pairing-only subtraction is harmless. This narrows the bracket on centered branches at arbitrary finite glue energies, but does not reach \(C_\infty\). It does not apply to frequency-dependent real shifts.
The valid upper coefficient \(U\) is not asserted to be sharp. The best coefficient on this centered class is **OPEN** within \([C_\infty,U]\), with \(C_\infty\) the exact scalar spectral constant.

## 1. Every centered branch obeys a two-sided Poisson-weight slope bound

Put \(w_n=2n+1\). For one unit line \(t>0\), write \(k_j=(j^2+t)^{-1}\), \(p_{nm}=k_{n-m}-k_{n+m+1}\), \(x=n+1/2\), and \(y=m+1/2\). Then
\[
 p_{nm}=w_n w_m/D(x,y),\quad D(x,y)=((x-y)^2+t)((x+y)^2+t).
\]
Let \(C_t=\sum_{j\in\mathbb Z}k_j\). Two exact row identities are
\[
 \sum_{m\ge0}p_{nm}\frac{w_m}{w_n}=C_t,\qquad
 \sum_{m\ge0}p_{nm}\frac{w_n}{w_m}=C_t\frac{w_n^2}{w_n^2+4t}.
\]
For the first identity, reflect \(m\mapsto-m-1\) to get the full-line convolution on the odd affine sequence \(2m+1\), cut at \(-M-1\le m\le M\), and reindex about \(n\). The finite shift of the cutoff changes finitely many boundary terms of order \(M^{-1}\); the odd terms in the symmetric transfer interval cancel. The reflected sum itself is absolutely convergent. For the second identity, reflecting the even denominator gives half the full-line sum with entries \(k_j k_{j+h}\), \(h=w_n>0\). Direct partial fractions give
\[
 (h^2+4t)k_jk_{j+h}=k_j+k_{j+h}+\frac{2}{h}\big[(j+h)k_{j+h}-jk_j\big].
\]
The bracket sums to zero by a symmetric cutoff, with a boundary error of order \(M^{-1}\).

Let \(x'=x+1\), \(u=x^2\), \(u'=(x')^2\). The sign of \(D(x',y)^{-1}-D(x,y)^{-1}\) is the sign of \(-(u+u'-2y^2+2t)\). The sign of \(u'/D(x',y)-u/D(x,y)\) is that of \((y^2+t)^2-uu'\). Each row difference therefore changes sign only from negative to positive as \(m\) increases. For the first row identity the difference in total mass is zero; integrating against any decreasing nonnegative sequence gives a nonpositive difference. For the second the total mass increases; integrating against an increasing nonnegative sequence gives a nonnegative difference. In each case subtract the test value at the sign change, after which the sign of every remaining summand is fixed. If all row differences have one sign, the conclusion follows from the total and termwise signs. Below these weighted sums converge absolutely because the Poisson weights are bounded and the original rows sum to \(k_0+2\sum_{j=1}^n k_j\).

Call a positive width sequence admissible for this step if \(s_n/w_n\) is nonincreasing and \(w_n s_n\) is nondecreasing. The Poisson function of a nonzero DOS satisfies \(|s b'(s)|\le b(s)\) by differentiating the Poisson kernel. Thus between successive \(n\), \(|\log(b_{n+1}/b_n)|\le|\log(s_{n+1}/s_n)|\le \log(w_{n+1}/w_n)\). In particular \(b_n/w_n\) is nonincreasing and \(w_n b_n\) is nondecreasing (both also hold if the DOS vanishes). In the centered normal update \(s'_n=w_n+\sum_{m,y}\eta_y P^N_{nm}(x,y)b_{m,y}\), apply the first weighted comparison to \(s'_n/w_n\) with test \(b_{m,y}/w_m\); apply the second to \(w_n s'_n\) with test \(w_m b_{m,y}\). The comparisons survive nonnegative spectral and angular integration. The bare contributions are respectively constant and increasing. Starting at \(s_n=w_n\), every iterate is admissible. On the positive box \(w_n\le s_{n,x}\le w_n+R\), with a common finite row bound \(R\), the normal update in log variables is a contraction of rate at most \(R/(1+R)\): its absolute derivative row is at most the normal contribution divided by the full updated width. Hence the unique branch is the limit, and
\[
 \boxed{\displaystyle\frac{w_n}{w_{n+1}}b_{n,x}\le b_{n+1,x}\le\frac{w_{n+1}}{w_n}b_{n,x}}.
\]
The same log-Lipschitz bound applies to the Poisson average of the bounded complementary DOS \(1-r_x\), which need not be integrable. The kernel derivative is locally dominated by an integrable function for positive widths; an identically zero Poisson average satisfies the resulting nonlogarithmic inequalities trivially. Since the Poisson kernel integrates to 1, \(1-b_{1,x}\le3(1-b_{0,x})\) and \(1-b_{1,x}\ge(1-b_{0,x})/3\). We will use \(b_{1,x}\ge1-3(1-b_{0,x})\).

## 2. Retain the first unavoidable head-to-tail cost

Use the ordered edge contribution \(I_{xy}(t)\) and allocated bare cost \(B_r\) of [SHARP-Q2](../SHARP-Q2/RIGOR.md), §2, at any \(r>0\). Consider finite trial support, with frequencies 0 and 1 also included (assign zero amplitudes if absent). Discarding further frequencies only drops nonnegative normal diagonals. With fixed \(v\), represent the weights by independent Bernoulli masks (the two endpoints independently, even for a loop). The binary rescalings are \(a_n=g_{x,n}/\sqrt r\), \(d_n=\sqrt r\,g_{y,n}\), zero at inactive coordinates. Use the same tail-to-tail bound \(1/12\) from SHARP-Q2 and allocate \(\alpha=41/50\) to the head-tail completions, retaining \(11/12-\alpha=29/300\) of the tail norm. The positivity determinant still has threshold \(\alpha\ge2/(r w_m^2)\), so no head-tail losses occur in either direction for \(1/3\le r\le3\). The bound for all \(r,t\) on the possible head-tail loss per head is \((59/96)/(4\alpha)\), by summing the squared mixed column as in SHARP-Q2.

For the two heads present, their matrix is
\[
 H_0=\begin{pmatrix}1+\beta r&-\beta-u\\-\beta-u&1+\beta/r\end{pmatrix},\qquad
 \beta=\frac1{2t(1+t)}=\frac{u^2}{2(1-u)},\quad u=\frac1{1+t}.
\]
It obeys \(H_0\succeq(1-u)I\) by dropping the positive rank-one term. A second bound, uniform in \(t\), is \(H_0\succeq(1-2/R)I\) where \(R=r+r^{-1}\). Indeed, for \(a=2/R\) the first shifted diagonal is positive and
\[
 2(1-u)\det(H_0-(1-a)I)=2(1-u)a^2+u^2(aR-2)>0 .
\]
If the opposing head is absent the present head retains its unit bare cost before its own head-tail completions.

* For \(r\notin[1/3,3]\), \(R\ge10/3\). The net head reserve is at least \(2/5-(59/96)/(4\alpha)=8369/39360\).
* For \(r\in[1/3,3]\) and \(t\ge1/9\), the head reserve is at least \(1/10\), by \(1-u\ge1/10\). There is no completion loss.
* For \(r\in[1/3,3]\setminus[19/30,30/19]\) and \(0<t<1/9\), the head reserve is at least \(1-2/(19/30+30/19)=121/1261\), again without completion loss.
* In the remaining range \(r\in[19/30,30/19]\), \(0<t<1/9\), the two active heads have \(H_0\succeq0\). When an active head meets an active opposing frequency 1, the completed square for that pair leaves the extra positive head diagonal
  \[
   D_1=\frac{p\,[r\alpha/2-1/9]}{\alpha+p/(6r)},\qquad p=k_1-k_2 .
  \]
  Use the identity \((S^2-p^2)/(3p)=4/9\), with \(S=k_1+k_2\). The bounds \(p\in[243/370,3/4]\) and \(r\in[19/30,30/19]\) first give \(D_1\ge d=685881/7152100\). For strict slack, \(D_1\) increases in \(p\) and in \(r\) on this rectangle: the positive factor \(r\alpha/2-1/9\) increases in \(r\), the denominator decreases in \(r\), and \(p/(\alpha+p/(6r))\) increases in \(p\). Thus \(D_1\ge d_+=685881/6979600>d\), in both directions. Every other completion has nonnegative margin. The head receives unit reserve when the opposing head is absent, and at least \(d_+\) when the opposing frequency 1 is active, including when both reserves apply. Its own head norm is independent of the opposing mask. Thus for the \(x\)-head the averaged reserve is at least

  **Monotonicity proof.** Set \(a(r)=r\alpha/2-1/9>0\) and \(z(p,r)=\alpha+p/(6r)>0\). Direct differentiation of \(D_1=pa/z\) gives
  \[
   \partial_p D_1=\frac{a\alpha}{z^2}>0,\qquad
   \partial_r D_1=\frac{p[(\alpha/2)z+ap/(6r^2)]}{z^2}>0 .
  \]
  Thus evaluating at \(p=243/370\), \(r=19/30\) gives the stated exact \(d_+\). This bound is symmetric under exchanging the endpoints, which replaces \(r\) by \(1/r\) within the same interval.
  \[
  1-b_{0,y}+d_+\,b_{1,y}\ \ge\
  d_++(1-3d_+)(1-b_{0,y})\ \ge\ d_+ ,
  \]
  by the complementary DOS bound and \(d_+<1/3\). Interchange the endpoints for the other head. No correlation assumption on the actual DOS between angles is used for this algebraic averaging.

The minimum \(\delta_*\) of the five explicit reserves (the four cases, using \(d_+\) for the last, and the tail) is strictly greater than \(d=685881/7152100\). Thus \(B_r+I_{xy}(t)/2\ge\delta_* B_r\) for the actual weights. The reserve is uniform in the atom energy, angles, DOS and bare allocation. Allocate \(r=h(x)/h(y)\) for a strictly positive superharmonic \(h\) at any upper norm bound \(R'>\rho\) as in [SHARP-Q2](../SHARP-Q2/RIGOR.md), §3. Ordered integration gives \(Q\ge[1-2(1-\delta_*)R'/(2\pi\tau)^2]\|g\|^2\); take \(R'\downarrow\rho\). This yields the strict bound in the statement because \(2(1-\delta_*)<2(1-d)=6466219/3576050\). Extra folded normal dominance only adds a diagonal cost. The replays check the finite algebra, not the whole infinite form. No material or measured quantities are used.
