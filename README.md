# What a glue moment bounds in linear Eliashberg theory

`main.tex` and `refs.bib` are the source for `main.pdf`. `RIGOR.md` and the five proof subdirectories give the analytic arguments and their scope. The paper is [10.5281/zenodo.24372930](https://doi.org/10.5281/zenodo.24372930), with [replay supplement 10.5281/zenodo.24372929](https://doi.org/10.5281/zenodo.24372929) and [source repository](https://github.com/SuperMatics-Inc/universal-glue-pairing-ceiling). The admitted shifted-fold PDF was `e6f6ab735e3999a720482d5bd639f4a75c3bc45d994e168a5cdcc8a9845be2ed`; release staging fills only its three publication macros. The sharp scalar result is imported from the finite-band companion [preprint](https://doi.org/10.5281/zenodo.24364879), with its own [supplement](https://doi.org/10.5281/zenodo.24364881). The strict non-sharp bound U = sqrt(6466219/3576050)/(2 pi) covers centered finite-channel reciprocal reduced models and shifted normal branches only under channel-wise radial-normal causal continuation and bounded normal frequency rows at each tested temperature. A causal interaction alone is insufficient: the effective normal frequency must be an upper-half-plane self-map. Relative-real sharpness and any shifted-versus-centered excess remain OPEN. Unrestricted external shifts have sharp coefficient 1/(pi sqrt(2)); their extremal witness fails Schwarz-Pick. This is a linearized onset bound, not an exact Hamiltonian or measured transition temperature. The preprint is not peer reviewed.

The eleven Python replay programs use only the standard library. Their finite rational checks and the six Lean files do not formalize the infinite-dimensional proofs or the imported theorem. In particular, the 1,008 centered edge matrices and the finite Harnack comparisons are sample checks, not universal certificates; the analytic arguments carry those proofs. To check all of the bundled finite evidence, run the following from a **clean copy** of this directory with Python 3.12, Lean 4.35.0, and Tectonic on `PATH`. Each base replay and each Lean invocation must exit 0; each of the 70 mutants must exit 1 at a named `REJECT:` guard. `tectonic main.tex` must exit 0; independent builds can differ in PDF metadata. `GENERAL/verify.py` is a narrower, bounded runner of five bases, 31 mutants and three Lean files; it additionally checks five inherited byte pins and is not a substitute for the complete commands below.

```sh
set -eu
export PYTHONDONTWRITEBYTECODE=1
for file in replay.py independent.py SHARP-Q2/replay.py SHARP-Q2/independent.py \
            PLASMON-W/replay.py PHYS-Q2/replay.py PHYS-Q2/independent.py \
            CENTERED-GAP/replay.py CENTERED-GAP/independent.py \
            GENERAL/replay.py GENERAL/independent.py; do
    python -I -B "$file"
    printf 'PASS base %s (exit 0)\n' "$file"
done

count=0
reject_all() {
    file=$1; shift
    for mutation in "$@"; do
        if [ "$file" = PLASMON-W/replay.py ]; then
            set -- "$mutation"
        else
            set -- --mutant "$mutation"
        fi
        rc=0
        result=$(python -I -B "$file" "$@" 2>&1) || rc=$?
        if [ "$rc" -ne 1 ] || ! printf '%s\n' "$result" | grep -q '^REJECT: '; then
            printf 'Unexpected mutant result: %s %s (exit %s)\n%s\n' "$file" "$mutation" "$rc" "$result" >&2
            return 1
        fi
        printf 'PASS mutant %s %s (exit 1): %s\n' "$file" "$mutation" "$result"
        count=$((count + 1))
    done
}
reject_all replay.py loss-sign fs-jacobian fold-sign hankel-cap moment-fold bulk-fold cross-cap sumzero partner-line dos-aggregation
reject_all independent.py static-null screening-diagonal hard-normal signed-budget reciprocal-normal
reject_all SHARP-Q2/replay.py tail-reserve head-tail-fold tail-mass head-lock loss-budget endpoint-factor perron-ratio soft-witness
reject_all SHARP-Q2/independent.py omit-head-lock extra-reflection undressed-gain no-soft-margin missing-ordered-copy
reject_all PLASMON-W/replay.py head-fold partner-diagonal ratio-endpoint tail-row tail-spread static-sign omitted-normal
reject_all PHYS-Q2/replay.py normal-sign head-tail-factor tail-reserve collapse-strict effective-mass flat-hard-alt flat-cross-tail flat-soft-trial
reject_all PHYS-Q2/independent.py ordered-copy lock-factor head-fold flat-edge-sign
reject_all CENTERED-GAP/replay.py folded-numerator upper-cone-sign lower-cone-product convolution-shift head-determinant middle-imbalance drop-complement edge-copy exact-reserve
reject_all CENTERED-GAP/independent.py erase-first-tail double-mixed-pair overfold-normal
reject_all GENERAL/replay.py harnack-sign pick-factor complement reserve-sign external-fold tail-cost moment-units causal-admission
reject_all GENERAL/independent.py self-energy-sign poisson-fold endpoint-ratio
[ "$count" -eq 70 ]
printf 'PASS all %s mutant rejections\n' "$count"

lean --version
for file in Finite.lean SHARP-Q2/Finite.lean PLASMON-W/Finite.lean PHYS-Q2/Finite.lean CENTERED-GAP/Finite.lean GENERAL/Finite.lean; do
    lean "$file"
    printf 'PASS Lean %s (exit 0)\n' "$file"
done
tectonic --keep-logs main.tex
printf 'PASS Tectonic (exit 0)\n'
```

## Licenses and provenance

Replay code, finite Lean files and proof documentation are licensed under Apache-2.0. The manuscript source, bibliography and PDF are licensed under CC-BY-4.0. The license exceptions are stated in `LICENSE`.

AI agents generated proofs, certificates, code, and manuscript drafts and edits under D. Rens' direction and review.
