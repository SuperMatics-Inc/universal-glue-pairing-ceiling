"""Run this slice plus byte-pinned inherited edge evidence, laptop only."""
from pathlib import Path
import hashlib
import os
import subprocess
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
PINS = {
    'SHARP-Q2/replay.py': '1a685ed0b42b1884fabdb87a7b6d7dc3bdcdb18c005c1d72476dbe28209f1a32',
    'SHARP-Q2/Finite.lean': '725be43780f6fea2c001b94a850184b8aa5d70fda3dadac32e74bdc6c1f8ce59',
    'CENTERED-GAP/replay.py': '21f11783fcc37027003f7f39de7e5b1553771ce09d36982c417cbe7a70e060ef',
    'CENTERED-GAP/independent.py': 'a89de64b838ddd3a04b3fa107eb19f518e5385f29bfbb00170fe700a4b28b795',
    'CENTERED-GAP/Finite.lean': '1939a43393da543128f6136d0fd9200f315c276d8492512ce7e083661daf452f',
}
MUTANTS = {
    'GENERAL/replay.py': ('harnack-sign', 'pick-factor', 'complement', 'reserve-sign',
                          'external-fold', 'tail-cost', 'moment-units', 'causal-admission'),
    'GENERAL/independent.py': ('self-energy-sign', 'poisson-fold', 'endpoint-ratio'),
    'SHARP-Q2/replay.py': ('tail-reserve', 'head-tail-fold', 'tail-mass', 'head-lock',
                          'loss-budget', 'endpoint-factor', 'perron-ratio', 'soft-witness'),
    'CENTERED-GAP/replay.py': ('folded-numerator', 'upper-cone-sign', 'lower-cone-product',
                             'convolution-shift', 'head-determinant', 'middle-imbalance',
                             'drop-complement', 'edge-copy', 'exact-reserve'),
    'CENTERED-GAP/independent.py': ('erase-first-tail', 'double-mixed-pair', 'overfold-normal'),
}


def run(args, expected=0, guard=False):
    result = subprocess.run(args, cwd=ROOT, capture_output=True, text=True,
                            encoding='utf-8', errors='replace', timeout=90)
    output = result.stdout + result.stderr
    print(output, end='' if output.endswith('\n') else '\n', flush=True)
    print('COMMAND', subprocess.list2cmdline([str(x) for x in args]),
          'EXIT', result.returncode, flush=True)
    if result.returncode != expected or (guard and not any(
            line.startswith('REJECT: ') for line in output.splitlines())):
        raise SystemExit('REJECT: unexpected replay exit or missing mutant guard')


for rel, sha in PINS.items():
    if hashlib.sha256((ROOT/rel).read_bytes()).hexdigest() != sha:
        raise SystemExit('REJECT: inherited evidence byte pin ' + rel)
print('PASS all five inherited evidence byte pins', flush=True)
for rel in MUTANTS:
    run([sys.executable, '-I', '-B', str(ROOT/rel)])
count = 0
for rel, mutants in MUTANTS.items():
    for mutant in mutants:
        run([sys.executable, '-I', '-B', str(ROOT/rel), '--mutant', mutant], 1, True)
        count += 1
if count != 31:
    raise SystemExit('REJECT: mutant count')
lean = os.environ.get('LEAN_EXE', 'C:/Users/davis/.elan/toolchains/leanprover--lean4---v4.35.0/bin/lean.exe')
run([lean, '--version'])
for rel in ('GENERAL/Finite.lean', 'SHARP-Q2/Finite.lean', 'CENTERED-GAP/Finite.lean'):
    run([lean, '--threads=1', '--memory=500', str(ROOT/rel)])
print('CERTIFIED five Python bases, 31 named mutant rejections, three Lean files', flush=True)
