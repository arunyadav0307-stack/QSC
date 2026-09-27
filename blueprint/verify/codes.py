"""Binary / q-ary cyclic code pairs C^perp <= C < D used as benchmark instances,
with independent checks of the chain condition and exact minimum distances
(via MacWilliams from the smaller dual where feasible).

All instances are taken from constructions that appear in the source papers:
  * n = 31 BCH chain [31,26],[31,21],[31,16]  (FTW 2013 Thms 12/13/17 family;
    also the codes named in the published T–N version, see Blueprint §19)
  * n = 31 quadratic-residue code and its supercodes (XYF 2014, Thm 4.5)
  * n = 63, 127 narrow-sense BCH codes (FTW 2013 Thms 12/13/17)
  * n = 15: C = <M_1>, D = F_2^15 (FTW Thm 13 boundary case)
"""
from math import comb
from polyfp import (minimal_polynomial_of_power, cyclotomic_cosets, prod, mul,
                    divmod_, mod, deg, xn_minus, reciprocal, trim)


def gen_from_cosets(n, reps, q=2):
    polys = [minimal_polynomial_of_power(n, i, q)[0] for i in reps]
    return prod(polys, q)


def is_dual_containing(g, n, q=2):
    """C = <g> contains C^perp  <=>  g | h*(x), h = (x^n - 1)/g."""
    h, r = divmod_(xn_minus(n, 1, q), g, q)
    assert not r
    return not mod(reciprocal(h, q), g, q)


def contains(gC, gD, q=2):
    """C = <gC> subset D = <gD>  <=>  gD | gC."""
    return not mod(gC, gD, q)


def codewords_of_cyclic(g, n):
    """All codewords (as int bitmasks) of the binary cyclic code <g>, k = n - deg g."""
    k = n - deg(g)
    gm = sum(1 << i for i, c in enumerate(g) if c)
    basis = [gm << i for i in range(k)]
    words = [0]
    for b in basis:
        words += [w ^ b for w in words]
    return words


def weight_distribution_via_dual(g, n):
    """Binary: weight distribution of <g> from that of its dual (MacWilliams)."""
    h, _ = divmod_(xn_minus(n, 1, 2), g, 2)
    gdual = reciprocal(h, 2)
    kd = n - deg(gdual)
    B = [0] * (n + 1)
    for w in codewords_of_cyclic(gdual, n):
        B[bin(w).count("1")] += 1
    size_dual = 2 ** kd
    A = []
    for j in range(n + 1):
        s = 0
        for i in range(n + 1):
            if B[i]:
                # Krawtchouk K_j(i)
                K = sum((-1) ** t * comb(i, t) * comb(n - i, j - t) for t in range(0, j + 1))
                s += B[i] * K
        assert s % size_dual == 0
        A.append(s // size_dual)
    return A


def min_distance(g, n, max_dual_dim=22):
    k = n - deg(g)
    if k == n:
        return 1
    if n - k <= max_dual_dim:
        A = weight_distribution_via_dual(g, n)
    elif k <= max_dual_dim:
        A = [0] * (n + 1)
        for w in codewords_of_cyclic(g, n):
            A[bin(w).count("1")] += 1
    else:
        return None  # not computed here -> OPEN (use MAGMA/Sage or codetables.de)
    return min(i for i in range(1, n + 1) if A[i])


def instance(name, n, repsC, repsD, source, q=2):
    gC = gen_from_cosets(n, repsC, q)
    gD = gen_from_cosets(n, repsD, q) if repsD else (1,)
    f, r = divmod_(gC, gD, q)
    assert not r
    return dict(name=name, n=n, q=q, gC=gC, gD=gD, f=f, source=source,
                kC=n - deg(gC), kD=n - deg(gD), repsC=repsC, repsD=repsD,
                dual_containing=is_dual_containing(gC, n, q), nested=contains(gC, gD, q))


INSTANCES = [
    # name, n, cosets of C, cosets of D, provenance
    ("BCH31-a", 31, [1, 3], [1], "FTW13 Thm12/13 (BCH, m=5); T–N TQE'26 codes"),
    ("BCH31-b", 31, [1, 3, 5], [1, 3], "FTW13 Thm12/13/17; T–N TQE'26 codes"),
    ("BCH31-c", 31, [1, 3, 5], [1], "FTW13 Thm17 (d1-d2>=4); T–N TQE'26 codes"),
    ("QR31-1", 31, [1, 5, 7], [1, 5], "XYF14 Thm 4.5, delete one factor (z=1)"),
    ("QR31-2", 31, [1, 5, 7], [1], "XYF14 Thm 4.5, delete two factors (z=2)"),
    ("BCH15", 15, [1], [], "FTW13 Thm13 boundary (D = F_2^15)"),
    ("BCH63-a", 63, [1, 3, 5], [1, 3], "FTW13 Thm12/13 (BCH, m=6)"),
    ("BCH63-b", 63, [1, 3, 5], [1], "FTW13 Thm17 (BCH, m=6)"),
    ("BCH63-c", 63, [1, 3, 5, 9], [1, 3], "dual-containing cyclic (cosets {1,3,5,9}), FTW13 framework"),
    ("BCH127-a", 127, [1, 3, 5], [1, 3], "FTW13 Thm12/13/14 (Mersenne prime 127)"),
    ("BCH127-b", 127, [1, 3, 5, 7], [1, 3], "FTW13 Thm12/13/14 (Mersenne prime 127)"),
]


def all_instances():
    return [instance(*row) for row in INSTANCES]


if __name__ == "__main__":
    for I in all_instances():
        dC = min_distance(I["gC"], I["n"])
        dD = min_distance(I["gD"], I["n"]) if I["repsD"] else 1
        print(f'{I["name"]:9s} n={I["n"]:3d} C=[{I["n"]},{I["kC"]},{dC}] D=[{I["n"]},{I["kD"]},{dD}] '
              f'r=deg f={deg(I["f"])} dual-containing={I["dual_containing"]} nested={I["nested"]}')
