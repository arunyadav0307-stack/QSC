"""Explicit additive (affine) marker set for BCH31-b ([31,16,7] < [31,21,5], f = M_5,
r = 5) with window L = d_sync = 5 and 2^2 = 4 marker messages, i.e. y = 2 Z-side
classical bits at d_sync = 5, versus y + d_sync <= r = 5 in T–N Thm 5 / Cor 2.
The set is found by exhaustive search (affine.py) and then re-verified by the
label-level decoder of simulate.py with the marker set replaced by this set."""
import random
from itertools import product
from polyfp import deg
from codes import all_instances
from orbits import times_x_table, int_to_poly
from affine import subspaces, span, admissible
from simulate import MarkerCode


def find_affine(f, L, y):
    r = deg(f)
    nxt = times_x_table(f, 2)
    sh = []
    for u in range(2 ** r):
        s, v = [], u
        for _ in range(L):
            s.append(v); v = nxt[v]
        sh.append(s)
    for basis in subspaces(r, y):
        V = span(basis)
        for a in range(2 ** r):
            A = [a ^ v for v in V]
            if admissible(A, sh, L):
                return a, basis, A
    return None


def poly_str(u):
    terms = [("1" if i == 0 else ("x" if i == 1 else f"x^{i}")) for i in range(u.bit_length()) if u >> i & 1]
    return " + ".join(terms) or "0"


if __name__ == "__main__":
    I = {J["name"]: J for J in all_instances()}["BCH31-b"]
    f, L, y = I["f"], 5, 2
    a, basis, A = find_affine(f, L, y)
    print("f =", poly_str(sum(c << i for i, c in enumerate(f))))
    print("affine marker set A = a + span(basis):  a =", poly_str(a), "; basis =", [poly_str(b) for b in basis])
    print("elements (u(x) mod f):", [poly_str(u) for u in A])
    # re-verify with the label-level decoder (exhaustive over messages, shifts; random codewords/errors)
    code = MarkerCode(I, L)
    # replace optimal marker set by A: decoding must map s back to (u, theta)
    lookup = {}
    for idx, u in enumerate(A):
        # window syndrome is s = x^{-theta} u with -theta in [-a_r, a_l]; start at x^{-a_r} u
        e = len(code.orbits[code.orbit_of[u]])
        v = u
        for _ in range((e - code.ar) % e):
            v = code.nxt[v]
        for k in range(-code.ar, code.al + 1):
            assert v not in lookup
            lookup[v] = (idx, -k)
            v = code.nxt[v]
    table = code.syndrome_table(2)
    rng = random.Random(7)
    ok = tot = 0
    from simulate import pmod_mask, pdiv_mask
    for idx, u in enumerate(A):
        for theta in range(-code.al, code.ar + 1):
            for _ in range(200):
                c = code.random_C_word(rng)
                v = c ^ code.marker_word(u)
                ext = code.extended_block(v)
                start = code.al + theta
                W = sum(b << i for i, b in enumerate(ext[start:start + code.n]))
                for p in rng.sample(range(code.n), rng.randint(0, 2)):
                    W ^= 1 << p
                e = table[pmod_mask(W, code.gD, code.dD)]
                q, rem = pdiv_mask(W ^ e, code.gD, code.dD)
                s = pmod_mask(q, code.f, code.r)
                tot += 1
                ok += lookup.get(s) == (idx, theta)
    print(f"label-level check with <=2 bit flips: {ok}/{tot} correct")
    print(f"T–N accounting (Q4-type, X-side m_X = r = 5): r_g + m + d_sync = 0 + (5 + {y}) + {L} = {5 + y + L}  vs  2(k_D-k_C) = 10")
