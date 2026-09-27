#!/usr/bin/env bash
# Regenerates every file in ../results from scratch (pure Python 3, no dependencies).
set -euo pipefail
cd "$(dirname "$0")"
python3 codes.py                 > ../results/codes.txt
python3 tables.py                > ../results/tables.md
python3 mis_check.py             > ../results/mis_check.txt
python3 simulate.py 3000         > ../results/simulation.txt
python3 affine.py                > ../results/affine.txt
python3 tn_counterexample.py     > ../results/tn_counterexample.txt
python3 prop_uniform.py          > ../results/prop_uniform.txt
echo "done; see ../results/"
