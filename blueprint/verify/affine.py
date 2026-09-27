"""Additive (affine) vs. non-additive marker sets.

For small r = deg f, compute by exhaustive search
    y_aff(L) = max { dim V : A = a + V  (V an F_2-subspace of R_f) is admissible }
and compare with  log2 N_f(L)  (optimal, possibly non-additive) and with the
T–N (arXiv:2409.11312v2, Thm 5 item 4 / Lemma 3) value  y_TN(L) = r - L.

This quantifies how much of the gain comes from (i) using ord(f) instead of the
degree argument, and (ii) allowing non-additive (union-of-cosets) marker sets.
"""
import math
from itertools import product
from polyfp import deg
from orbits import times_x_table, N_divisor


def subspaces(r, y):
    """Yield bases (lists of int vectors) of all y-dim subspaces of F_2^r
    in reduced row-echelon form."""
    from itertools import combinations
    for pivots in combinations(range(r), y):
        free_positions = []
        for i, pcol in enumerate(pivots):
            free_positions.append([c for c in range(pcol + 1, r) if c not in pivots])
        nfree = sum(len(fp) for fp in free_positions)
        for bits in product((0, 1), repeat=nfree):
            it = iter(bits)
            basis = []
            for i, pcol in enumerate(pivots):
                v = 1 << pcol
                for c in free_positions[i]:
                    if next(it):
                        v |= 1 << c
                basis.append(v)
            yield basis


def span(basis):
    S = [0]
    for b in basis:
        S += [s ^ b for s in S]
    return S


def admissible(A, shifts_of, L):
    seen = set()
    for u in A:
        for v in shifts_of[u]:
            if v in seen:
                return False
            seen.add(v)
    return True


def best_affine_dim(f, L):
    r = deg(f)
    nxt = times_x_table(f, 2)
    shifts_of = []
    for u in range(2 ** r):
        s, v = [], u
        for _ in range(L):
            s.append(v)
            v = nxt[v]
        shifts_of.append(s)
    ymax = int(math.floor(math.log2((2 ** r - 1) / L))) if L <= 2 ** r - 1 else -1
    for y in range(ymax, -1, -1):
        for basis in subspaces(r, y):
            V = span(basis)
            Vset = set(V)
            reps, covered = [], set()
            for a in range(2 ** r):
                if a in covered:
                    continue
                reps.append(a)
                covered.update(a ^ v for v in V)
            for a in reps:
                A = [a ^ v for v in V]
                if admissible(A, shifts_of, L):
                    return y
    return None  # not even a single marker (L > max orbit size)


if __name__ == "__main__":
    cases = [("n=15, f=x^4+x+1 (BCH15)", (1, 1, 0, 0, 1)),
             ("n=31, f=M5 (BCH31-b)", (1, 1, 1, 0, 1, 1)),
             ("n=63, f=M5 (BCH63-a)", None)]
    from codes import all_instances
    inst = {I["name"]: I for I in all_instances()}
    cases[2] = ("n=63, f=M5 (BCH63-a)", inst["BCH63-a"]["f"])
    for name, f in cases:
        r = deg(f)
        print(f"\n{name}: r = {r}")
        print(" L | y_TN=r-L | best affine y | log2 N_f(L) | N_f(L)")
        for L in range(2, min(2 ** r - 1, 20) + 1):
            yA = best_affine_dim(f, L)
            N = N_divisor(f, 2, L)
            yTN = r - L if L <= r else None
            print(f"{L:2d} | {str(yTN):8s} | {str(yA):13s} | {math.log2(N) if N else float('-inf'):11.3f} | {N}")


def tn_family_max_L(f, y):
    """T–N Q4 marker family (arXiv v2, Thm 5 item 4): u(x) = 1 + sum_{m=2}^{y+1} c_m x^{m-1}.
    Return the largest window L for which this affine family is admissible
    (exact, by direct check), to separate 'sharper analysis of the T–N family'
    from 'better marker design'."""
    r = deg(f)
    A = [1 ^ (sum(((c >> i) & 1) << (i + 1) for i in range(y))) for c in range(2 ** y)]
    nxt = times_x_table(f, 2)
    best = 0
    for L in range(1, 2 ** r):
        shifts_of = {}
        for u in A:
            s, v = [], u
            for _ in range(L):
                s.append(v)
                v = nxt[v]
            shifts_of[u] = s
        if admissible(A, shifts_of, L):
            best = L
        else:
            break
    return best


def report_tn_family():
    from codes import all_instances
    inst = {I["name"]: I for I in all_instances()}
    for name in ("BCH15", "BCH31-b", "BCH31-c", "BCH63-a", "BCH63-c"):
        f = inst[name]["f"]
        r = deg(f)
        print(f"\n{name}: r={r}   y | T–N Lemma-3 window (r-y) | exact max window of the same family | N_f-optimal window for 2^y markers")
        for y in range(0, r - 1):
            Lt = tn_family_max_L(f, y)
            # largest L with N_f(L) >= 2^y
            Lopt = max(L for L in range(1, 2 ** r) if N_divisor(f, 2, L) >= 2 ** y)
            print(f"   {y:2d} | {r - y:3d} | {Lt:4d} | {Lopt:4d}")


if __name__ == "__main__":
    report_tn_family()
