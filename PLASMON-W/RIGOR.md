# No cutoff-uniform onset bound in a fixed projected box

**PROVED.** Fix a positive halfwidth \(W\), a positive plasmon energy \(E_p\), and the height-normalized centered DOS \(\boldsymbol1_{[-W,W]}\). Consider the constant harmonic of the on-shell projected screened plasmon model. Its matched retarded transfers are \(C g_j\), its instantaneous repulsion is \(C\), and
\[
 g_j=\frac{t}{t+j^2},\quad t=\frac{E_p^2}{(2\pi\tau)^2},\quad \tau=k_BT>0,
\]
where \(g_0=1\). For every fixed \(\tau\ge\sqrt{12}\,E_p/(2\pi)\), the positive centered normal solution is linearly unstable for all sufficiently large \(C\). In particular \(k_BT_{\rm lin}(C)\to\infty\). Here \(C\) is a dimensionless projected transfer strength, proportional to \(\log(2k_F/\delta)\) for this plasmon model with forward cutoff \(\delta\). The box and plasmon energy do not vary with the cutoff. This is a property of the reduced matched equation, not of unprojected jellium, and not a failure of a bound stated using the diverging *total* projected moment \(CE_p^2\).

## 1. A uniform bound on the normal Poisson weights

For positive Matsubara indices set \(w_n=2n+1\), \(p_{nm}=g_{|n-m|}-g_{n+m+1}\ge0\), and \(L=\sum_{j\ge1}g_j\le 2t\). The last inequality uses \(\sum_{j\ge1}j^{-2}\le1+\int_1^\infty u^{-2}du=2\). The real equation is zero by symmetry. Work with the centered width \(s_n=u_n/(\pi\tau)\),
\[
 s_n=w_n+C\sum_{m\ge0}p_{nm} b_m,
 \qquad b_n=b(s_n),\quad b(s)=\frac2\pi\arctan\frac{W}{\pi\tau s}.
\]
Telescoping the two sums gives \(\sum_m p_{nm}=1+2\sum_{j=1}^n g_j\le1+2L\). The positive normal map sends \(w_n\le s_n\le w_n+C(1+2L)\) into itself. For any \(s>0\), \(|d\log b/d\log s|\le1\), since \(\arctan z\ge z/(1+z^2)\) for \(z\ge0\). Along geometric interpolation of two widths, the log normal-map derivatives in absolute value sum to at most \(C(1+2L)/(1+C(1+2L))<1\). The box in the variables \(\log(s_n/w_n)\) is complete in the sup norm, so there is one positive centered solution by contraction, for each finite \(C\). The instantaneous odd term cancels in the reflected equation.

Let \(a=2W/(\pi^2\tau)>0\) and \(B=\sup_m b_m\). Since \(s b(s)\le a\) and \(s_n\ge C(1-g_1)b_n\) by the diagonal \(p_{nn}\ge1-g_1\),
\[
 B^2\le\frac{a}{C(1-g_1)},\qquad s_n\le w_n+C(1+2L)B.
\]
For an explicit threshold set \(d=W/(\pi\tau)\), \(p=1-g_1\), and let
\[
 C>\frac{1}{ap}\max\left\{100d^2,\ (44\cdot255)^2,\ \frac{576}{g_1^2}\right\}.
\]
The inequality \(\arctan z\ge z/(1+z^2)\) gives \(s b(s)\ge a s^2/(s^2+d^2)\). Combining it with \(s_n\ge Cp b_n\) gives \(s_n^2+d^2\ge Cap\) and hence \(s_n b_n\ge(99/100)a\) by the first threshold term. If \(w_n\le255\), the second threshold term and \(B s_n\le B w_n+C(1+2L)B^2\) give
\[
 \frac{B}{b_n}\le\frac{100}{99}\left(\frac{1+2L}{p}+\frac{255}{\sqrt{Cap}}\right)
 \le\frac{100}{99}\left(\frac{16}{11}+\frac1{44}\right)<\frac32.
\]
Here \((1+2L)/p\le(1+4t)/(1-t)\le16/11\). The denominator index is restricted to the fixed trial set below; the numerator still takes the supremum over the entire frequency line. Similarly the width upper bound gives \(1/b_n\le(100/99)(p/44+1+2L)\sqrt{C/(ap)}\) on the trial set, using \(w_n/\sqrt{Cap}\le1/44\).

## 2. A sign-changing frequency trial in the static null space

For a finite test \(y=bv\), the instantaneous cost is \(2C|\sum_n y_n|^2\), and the matched stability form in these variables is
\[
 Q(y)=\sum_n\frac{w_n}{b_n}|y_n|^2 - C\mathcal G(y) +2C\left|\sum_n y_n\right|^2,
\]
\[
 \mathcal G(y)=\sum_{n,m\ge0}(g_{|n-m|}+g_{n+m+1})\Re(\overline y_n y_m)
       -\sum_n |y_n|^2 \sum_m p_{nm}\frac{b_m}{b_n}.
\]
These coefficients follow from the even anomalous fold and the odd normal fold. In symmetrized gap variables \(f_n=\sqrt{s_n/b_n}\,y_n\) this is \(\langle f,(I-\mathcal A)f\rangle\). For finite \(C\) and \(W\), the retarded transfer is summable and the static form is bounded in these variables: \(\sum_n b_n/s_n\le a\sum_n w_n^{-2}<\infty\). Thus a strictly negative finite trial proves linear instability.

Take \(N=64\), \(y_0=1\), \(y_m=-1/N\) for \(N\le m<2N\), zero otherwise. Its static cost is zero. The diagonal of \(\mathcal G\) after its matching same-frequency normal term is
\[
 2g_{2n+1}-\sum_{m\ne n} p_{nm}\frac{b_m}{b_n}.
\]
At the head, \(\sum_{m\ne0}p_{0m}=g_1\) exactly, so this is at least \(g_1/2\) for \(C\) sufficiently large as above. On each active tail index it is at least \(-3L\), because \(\sum_{m\ne n}p_{nm}\le2L\). Tail cross terms are nonnegative. Head to tail costs at most \(4L/N\) including both orders, since \(\sum_{m=N}^{2N-1}(g_m+g_{m+1})\le2L\). It follows that
\[
 \mathcal G(y)\ge \frac{g_1}{2}-\frac{7L}{N}>\frac{g_1}{4}>0,
\]
as \(L/g_1\le2(1+t)\le13/6\) and \(7(13/6)/64<1/4\). The sum \(\sum_n w_n|y_n|^2=4\) exactly, and \(1+2L\le4/3\), so the bare cost is less than \(6\sqrt{C/(ap)}\). The third term of the coupling threshold makes this smaller than \(C g_1/4\). Thus \(Q(y)<0\) for every \(C\) above the displayed threshold at this \(\tau\). Since the test temperature can be arbitrarily large, the claimed limit follows. No statement is made about removing the cutoff from an operator, or about reassigning the divergent forward sector between normal and pairing equations.
