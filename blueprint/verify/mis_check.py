"""Independent check of the optimality statement (Theorem A, converse part):
for small f the maximum admissible marker set is computed by an exact
maximum-independent-set search on the 'confusability graph' built directly
from the definition (no orbit reasoning is used), and compared with N_f(L).

Admissibility (definition): M subset R_f is admissible for window length L if
the map (u, a) -> x^a u mod f, u in M, a in {0,...,L-1}, is injective.
"""
import sys
from polyfp import factor, xn_minus, prod, deg
from orbits import times_x_table, N_divisor


def confusability_graph(f, q, L):
    nxt = times_x_table(f, q)
    size = len(nxt)
    shifts = []  # shifts[u] = [u, xu, ..., x^{L-1}u]
    for u in range(size):
        s, v = [], u
        for _ in range(L):
            s.append(v)
            v = nxt[v]
        shifts.append(s)
    allowed = [u for u in range(size) if len(set(shifts[u])) == L]  # excludes 0 when L>1
    idx = {u: i for i, u in enumerate(allowed)}
    adj = [0] * len(allowed)
    for i, u in enumerate(allowed):
        Su = set(shifts[u])
        for j, w in enumerate(allowed):
            if j != i and Su & set(shifts[w]):
                adj[i] |= 1 << j
    return allowed, adj


def max_independent_set(adj):
    n = len(adj)
    best = [0]

    def popcount(x):
        return bin(x).count("1")

    def rec(cand, size):
        if size + popcount(cand) <= best[0]:
            return
        if not cand:
            best[0] = max(best[0], size)
            return
        # pick vertex of minimum degree inside cand (good for sparse graphs)
        v = min((i for i in range(n) if cand >> i & 1), key=lambda i: popcount(adj[i] & cand))
        # branch 1: take v
        rec(cand & ~adj[v] & ~(1 << v), size + 1)
        # branch 2: skip v (only useful if v has a neighbour in cand)
        if adj[v] & cand:
            rec(cand & ~(1 << v), size)

    rec((1 << n) - 1, 0)
    return best[0]


def components(adj):
    n, seen, comps = len(adj), 0, []
    for s in range(n):
        if seen >> s & 1:
            continue
        comp, frontier = 1 << s, 1 << s
        while frontier:
            v = (frontier & -frontier).bit_length() - 1
            frontier &= frontier - 1
            new = adj[v] & ~comp
            comp |= new
            frontier |= new
        seen |= comp
        comps.append([i for i in range(n) if comp >> i & 1])
    return comps


def mis_by_components(adj):
    """Generic graph fact: MIS(G) = sum of MIS over connected components."""
    total = 0
    for comp in components(adj):
        pos = {v: i for i, v in enumerate(comp)}
        sub = []
        for v in comp:
            m = 0
            for w in comp:
                if adj[v] >> w & 1:
                    m |= 1 << pos[w]
            sub.append(m)
        total += max_independent_set(sub)
    return total


def check(f, q, Ls):
    rows = []
    for L in Ls:
        allowed, adj = confusability_graph(f, q, L)
        m = mis_by_components(adj) if allowed else 0
        rows.append((L, m, N_divisor(f, q, L)))
    return rows


if __name__ == "__main__":
    cases = []
    fac7 = list(factor(xn_minus(7, 1, 2), 2))
    fac15 = list(factor(xn_minus(15, 1, 2), 2))
    fac21 = list(factor(xn_minus(21, 1, 2), 2))
    fac14 = factor(xn_minus(14, 1, 2), 2)
    # a few binary square-free and repeated-root f of degree <= 6
    cases.append(("x^3+x+1 (n=7)", (1, 1, 0, 1), 2))
    cases.append(("(x+1)(x^3+x+1) (n=7)", prod([(1, 1), (1, 1, 0, 1)], 2), 2))
    cases.append(("x^4+x+1 (n=15)", (1, 1, 0, 0, 1), 2))
    cases.append(("(x^2+x+1)(x^4+x+1) (n=15)", prod([(1, 1, 1), (1, 1, 0, 0, 1)], 2), 2))
    cases.append(("(x^2+x+1)(x^3+x+1) (n=21)", prod([(1, 1, 1), (1, 1, 0, 1)], 2), 2))
    cases.append(("x^5+x^2+1 (n=31)", (1, 0, 1, 0, 0, 1), 2))
    cases.append(("(x+1)^2(x^3+x+1) (n=14, repeated root)", prod([(1, 1), (1, 1), (1, 1, 0, 1)], 2), 2))
    cases.append(("(x+1)^3 (n=4/8, repeated root)", prod([(1, 1)] * 3, 2), 2))
    cases.append(("x^2+1 over F_3 (n=4, q=3)", (1, 0, 1), 3))
    cases.append(("(x+1)(x^2+1) over F_3 (n=4)", prod([(1, 1), (1, 0, 1)], 3), 3))
    ok = True
    for name, f, q in cases:
        emax = max(2, q ** deg(f) - 1)
        Ls = [L for L in range(2, min(emax, 16) + 1)]
        rows = check(f, q, Ls)
        bad = [r for r in rows if r[1] != r[2]]
        ok &= not bad
        print(f"{name:45s} q={q} deg={deg(f)}  L=2..{Ls[-1]}  exact-MIS == N_f(L): {not bad}")
        if bad:
            print("   mismatches:", bad)
    print("ALL OK" if ok else "FAILURES")
    sys.exit(0 if ok else 1)
