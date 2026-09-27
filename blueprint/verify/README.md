# Verification scripts for BLUEPRINT.md

These are pure Python 3 scripts with no third-party dependencies. `./run_all.sh` regenerates everything in `../results/` in about 20 s.

| script | what it checks | output |
|---|---|---|
| `polyfp.py` | F_p[x] arithmetic, factorisation of x^n−1, multiplicative order ord(f), minimal polynomials, cyclotomic cosets | library |
| `orbits.py` | orbit census of u ↦ x·u on R_f = F_q[x]/(f). Computes N_f(L) in four independent ways: brute force, the divisor formula, the CRT formula, and the cyclotomic-coset formula (works for any prime power q) | library |
| `codes.py` | benchmark instances (defining sets taken from the source-paper families), dual-containment and nesting checks, minimum distances via MacWilliams | `codes.txt` |
| `tables.py` | Tables T1–T4 of the blueprint: instances, N_f(L) vs FTW / T–N / the upper bound, largest window for 2^y markers, q-ary instances | `tables.md` |
| `mis_check.py` | proves optimality by exhaustive search on small cases. It computes an exact maximum independent set of the confusability graph, which is built from the definition of admissibility and uses no orbit theory, then compares it with N_f(L). Includes repeated-root f and q = 3 | `mis_check.txt` |
| `simulate.py` | label-level (computational-basis) Monte-Carlo run of the full synchronisation-plus-message decoder. Covers misalignment in [−a_l, a_r] and up to t_D bit flips | `simulation.txt` |
| `affine.py` | maximum additive (affine) marker set compared with the optimal non-additive N_f(L). Also gives the exact maximum window of the T–N marker family | `affine.txt` |
| `tn_counterexample.py` | an explicit affine (stabilizer-type) marker set for BCH31-b with y = 2 bits at d_sync = 5, re-verified by the decoder | `tn_counterexample.txt` |
| `prop_uniform.py` | exact integer check of Proposition C2 (uniform-orbit case) for all primes 7 ≤ n < 600 | `prop_uniform.txt` |
