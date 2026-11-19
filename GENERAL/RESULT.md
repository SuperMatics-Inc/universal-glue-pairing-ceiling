# GENERAL: PROVED conditional causal extension; unrestricted shifts separated

## Verdict

- **PROVED.** A channel-wise holomorphic upper-half-plane normal effective frequency gives the complementary-DOS Harnack estimate `b1 >= 1 - 3(1-b0)`, even with arbitrary frequency-dependent real shifts and asymmetric DOS. The first-pair Schwarz-Pick condition is `|Z(i3w)-Z(iw)|^2 <= (4/3) Im Z(i3w) Im Z(iw)`. This is causality of the radial normal propagator in the energy-independent self-energy parameterization, not causality of the glue alone. Section 1 of [RIGOR.md](RIGOR.md) states the relation to the full relative real equation.
- **PROVED.** The centered ordered-edge reserve needs only the unit-box weights and that complementary-DOS inequality. Consequently, for finite reciprocal matched channels with the stated bounded normal rows, finite height-weighted moment norm rho, positive-energy spectral measure, eligible folded-normal dominance and PSD subtraction, `k_B T_lin < U sqrt(rho)` also holds on causal shifted normal branches. The exact non-sharp coefficient is `U = sqrt(6466219/3576050)/(2 pi)`.
- **PROVED.** For unrestricted externally prescribed real shifts, the full self-consistent imaginary equation and a finite nonzero box DOS do not improve the sharp coefficient `1/(pi sqrt(2))`. The positive finite-energy extremal family is defined by one fixed physical DOS and frequency-shift function at all temperatures for each member. An explicit rational witness exceeds U and necessarily fails Schwarz-Pick; it is not a causal or scalar relative-real counterexample.
- **OPEN.** The optimal causal shifted coefficient lies in `[C_infinity, U]`; the flat scalar soft family supplies the lower endpoint and its causal normal self-energy is exhibited in RIGOR.md. Any shifted-versus-centered excess remains open. Without established causal continuation, the coupled relative-real optimum retains the proved bracket `[C_infinity, 1/(pi sqrt(2))]`. No theorem here supplies causal continuation for every algebraic Matsubara solution.
- **CERTIFIED finite evidence only.** Exact rational determinant identities, Harnack/complement budgets, finite-DOS witness margins, inherited edge arithmetic and finite Lean identities replay with named coefficient/sign mutants rejected. These checks do not certify infinite-dimensional analytic continuation or replace the written proofs.

## Evidence and commands

All verification below was explicitly assigned by Main. No user-reported failure was rerun.

1. `python -I -B GENERAL/verify.py` from the slice parent, using Python 3.12: **exit 0**. Five pinned inherited evidence files match SHA-256. Five Python bases exit 0, 31 named mutants each exit 1 at a `REJECT:` guard, and three Lean files exit 0. Lean version invocation exits 0 and reports 4.35.0. Full output: [VERIFICATION.txt](VERIFICATION.txt).
2. A byte-exact clean copy of the candidate root, excluding the copied old PDF, was made under `D:/t/UNIV-GLUE/shifted-fold-clean/`. All 28 copied source/evidence files matched the candidate at admission. `sh D:/t/UNIV-GLUE/shifted-fold-run.sh`, containing the complete README replay block with the native Lean and Tectonic path wrappers: **exit 0**. Eleven Python bases exit 0; all 70 named mutants exit 1 at named guards; all six Lean files exit 0; `tectonic main.tex` exits 0. Evidence: [FOLD-SHIFTED-VERIFICATION.txt](FOLD-SHIFTED-VERIFICATION.txt). The clean-copy PDF was promoted byte-for-byte to the candidate.
3. PyMuPDF rendering and text-bound/link/glyph inspection: **exit 0**, 14 pages, no out-of-page text blocks, invalid internal destinations, replacement glyphs, or `??` reference markers detected. Every page was rendered and visually inspected. The new proposition/theorem is on page 6; the external-shift necessity discussion is on pages 7-8. Evidence: [FOLD-SHIFTED-VISUAL.json](FOLD-SHIFTED-VISUAL.json). Tectonic emits the existing Fontconfig message and underfull bibliography hbox warnings; the compiler exits 0, and actual rendering is intact. No warning is hidden.

The new primary replay checks 48 exact determinant instances and symbolic budget formulas at rational witnesses. The separately implemented replay checks 36 rational causal pairs and 216 pointwise Poisson comparisons. The inherited 1,008 centered edge matrices and these Harnack samples are not universal matrix certificates; the analytic arguments establish the universal claims.

## Local folded candidate and provenance

Candidate: `D:/dev/scratch/ceiling-20261118/UNIV-GLUE/note-shifted/`.

It is constructed from `release-bundle/` plus the accepted centered overlay, whose PDF SHA-256 is `338565e91754874b5583f53ae15829d8bb47c0a7cb75ea762168e03caed7d678`. Those frozen directories, `note/`, and `note-centered/` are untouched. The candidate adds GENERAL, changes the abstract/scope, and adds the conditional causal shifted theorem and the external-shift necessity remark. `refs.bib` is unchanged. The producer's source diff `FOLD-SHIFTED.diff` and relative-path byte pin manifest `FOLD-SHIFTED-PINS.json` live outside this bundle, in `D:/dev/scratch/ceiling-20261118/UNIV-GLUE/GENERAL/`, and are not shipped.

Built candidate PDF SHA-256: `e6f6ab735e3999a720482d5bd639f4a75c3bc45d994e168a5cdcc8a9845be2ed`.

The candidate is a local fold for review, not a publication. No branch or commit was created. No email, push, merge, deployment, public upload or paid compute occurred. Spend **$0**. Temporary clean-build and page-render files are deleted after the byte pins and evidence are retained.

## Scientific and literature boundaries

The moment is the reciprocal positive pairing-envelope moment in DOS-height measure, never an angular average or signed projected moment. Extra normal mass is harmless only under the specified folded comparison and causal branch hypotheses. Normal-state causality is imposed, not inferred from passivity of a screened interaction. The external witness deliberately drops causal continuation and the relative real equation; it establishes sharpness in that larger class only.

**[INFERENCE] prior work.** Schwarz-Pick and Harnack are classical. The earlier verified literature dossier is reused; a targeted metadata search covering 19 September through 19 November 2026 is not an exhaustive novelty proof. No priority claim is made. New paper-reader spawning is unavailable, and no new third-party full text was acquired. The unresolved prerequisites are scientific questions, not omitted reachable calculations: the actual coupled relative-real optimum, automatic causal continuation, and any causal shifted-versus-centered excess.

Checks skipped: no broad test suite, lint, formatter, GPU/CPU fit, physical jellium simulation, or full infinite-dimensional Lean formalization was run. No further novelty search or new-paper full-text intake was performed for this conditional classical-analysis extension.
