"""Orbit census of <x> acting on R_f = F_q[x]/(f) and the marker-capacity
function N_f(L).

Three independent computations of N_f(L) are provided:
  * N_bruteforce : enumerate every u in R_f \\ {0}, trace its orbit under
                   u -> x*u mod f, and sum floor(|O|/L) over orbits.
  * N_divisor    : closed formula  sum_{g | f, g != 1} Phi_q(g)/ord(g) * floor(ord(g)/L)
                   (valid for every f with f(0) != 0, repeated roots allowed).
  * N_crt        : closed formula for square-free f = prod f_i,
                   sum_{S != {}} (prod_{i in S}(q^{d_i}-1)/e_S) * floor(e_S/L),
                   e_S = lcm_{i in S} ord(f_i).
(For L = 1 one extra marker u = 0 is admissible; that is added separately.)
"""
from math import gcd as igcd
from itertools import combinations, product
from functools import reduce

from polyfp import (mul, mod, deg, factor, poly_order, trim, prod)


def lcm(a, b):
    return a * b // igcd(a, b)


# ------------------------------------------------------------ encodings
def int_to_poly(u, q, r):
    c = []
    for _ in range(r):
        c.append(u % q)
        u //= q
    return trim(c)


def poly_to_int(a, q):
    v = 0
    for c in reversed(a):
        v = v * q + c
    return v


def times_x_table(f, q):
    """next[u] = index of x*u mod f, for all q^r residues u (r = deg f)."""
    r = deg(f)
    size = q ** r
    nxt = [0] * size
    lead_inv = pow(f[-1], q - 2, q)
    fc = list(f) + [0] * (r + 1 - len(f))
    for u in range(size):
        c = [0] + list(int_to_poly(u, q, r)) + [0] * r
        c = c[:r + 1]
        top = c[r]
        if top:
            t = (top * lead_inv) % q
            for j in range(r + 1):
                c[j] = (c[j] - t * fc[j]) % q
        nxt[u] = poly_to_int(trim(c[:r]), q)
    return nxt


def orbit_census(f, q):
    """Return dict {orbit_size: number_of_orbits} over R_f \\ {0}."""
    nxt = times_x_table(f, q)
    size = len(nxt)
    seen = bytearray(size)
    seen[0] = 1
    census = {}
    for u in range(1, size):
        if seen[u]:
            continue
        L = 0
        v = u
        while not seen[v]:
            seen[v] = 1
            v = nxt[v]
            L += 1
        assert v == u, "x must act as a permutation (f(0) != 0)"
        census[L] = census.get(L, 0) + 1
    return census


def N_from_census(census, L):
    return sum(cnt * (s // L) for s, cnt in census.items())


def N_bruteforce(f, q, L):
    return N_from_census(orbit_census(f, q), L) + (1 if L == 1 else 0)


# ------------------------------------------------------------ closed forms
def phi_poly(fac, q):
    """Polynomial Euler totient |(F_q[x]/(g))^*| from a factorisation {p_i: k_i}."""
    out = 1
    for p_i, k in fac.items():
        d = deg(p_i)
        out *= q ** (d * (k - 1)) * (q ** d - 1)
    return out


def ord_from_factorisation(fac, q):
    """ord(prod p_i^{k_i}) = lcm_i ord(p_i) * p^{t}, p = char, p^t >= max k_i
    (Lidl–Niederreiter, Thm 3.8/3.9).  Here q is prime so char = q."""
    e = 1
    kmax = 0
    for p_i, k in fac.items():
        e = lcm(e, poly_order(p_i, q))
        kmax = max(kmax, k)
    t = 0
    while q ** t < kmax:
        t += 1
    return e * q ** t


def divisors_from_factorisation(fac):
    items = list(fac.items())
    for exps in product(*[range(k + 1) for _, k in items]):
        yield {items[i][0]: e for i, e in enumerate(exps) if e > 0}


def N_divisor(f, q, L, fac=None):
    fac = fac or factor(f, q)
    total = 0
    for g in divisors_from_factorisation(fac):
        if not g:
            continue  # g = 1 corresponds to u = 0
        e = ord_from_factorisation(g, q)
        ph = phi_poly(g, q)
        assert ph % e == 0
        total += (ph // e) * (L and e // L)
    return total + (1 if L == 1 else 0)


def N_crt(f, q, L, fac=None):
    fac = fac or factor(f, q)
    assert all(k == 1 for k in fac.values()), "N_crt needs square-free f"
    polys = list(fac)
    data = [(deg(g), poly_order(g, q)) for g in polys]
    total = 0
    for s in range(1, len(data) + 1):
        for S in combinations(range(len(data)), s):
            eS = reduce(lcm, (data[i][1] for i in S), 1)
            num = reduce(lambda a, b: a * b, (q ** data[i][0] - 1 for i in S), 1)
            assert num % eS == 0
            total += (num // eS) * (eS // L)
    return total + (1 if L == 1 else 0)


def tn_affine_messages(r, L):
    """Number of marker (Z-side) messages available in T–N (arXiv:2409.11312v2)
    Thm 5 items 2-4/6 with Lemma 1/Lemma 3: y classical Z-side bits require
    d_sync = L <= r - y (y = 0 gives Fujiwara's L <= r).  For 2 <= L <= r this is
    2^(r-L); for L > r the T–N construction offers no synchronizable code."""
    if L < 2 or L > r:
        return 0
    return 2 ** (r - L)


# ------------------------------------------------------------ cyclotomic form
def coset_of(i, n, q):
    c, j = [], i % n
    while j not in c:
        c.append(j)
        j = (j * q) % n
    return sorted(c)


def N_from_cosets(n, q, reps, L):
    """N_f(L) for square-free f = prod_{i in reps} M_i(x) | x^n - 1, gcd(n,q)=1,
    computed ONLY from cyclotomic data: d_i = |C_i|, e_i = n / gcd(i, n).
    Works for any prime power q (no field arithmetic needed)."""
    from math import gcd as g
    cos = [coset_of(i, n, q) for i in reps]
    assert len({tuple(c) for c in cos}) == len(cos), "cosets must be distinct"
    data = [(len(c), n // g(c[0], n)) for c in cos]
    total = 0
    for s in range(1, len(data) + 1):
        for S in combinations(range(len(data)), s):
            eS = reduce(lcm, (data[i][1] for i in S), 1)
            num = reduce(lambda a, b: a * b, (q ** data[i][0] - 1 for i in S), 1)
            assert num % eS == 0
            total += (num // eS) * (eS // L)
    return total + (1 if L == 1 else 0)


def ord_from_cosets(n, q, reps):
    from math import gcd as g
    return reduce(lcm, (n // g(i, n) for i in reps), 1)
