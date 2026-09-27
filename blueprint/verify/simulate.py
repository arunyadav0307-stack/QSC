"""Computational-basis ('label-level') simulation of the proposed marker-hybrid
QSC decoder:  encode (quantum part abstracted as a uniformly random codeword
c in C), add the marker w_u = u(x) g_D(x) chosen from the optimal marker set,
pad as in Fujiwara (2013) / T–N (2024) (copy last a_l / first a_r positions),
misalign by theta in [-a_l, a_r], add <= t_D = floor((d_D-1)/2) bit flips on the
n-qubit window, then
   1. D-syndrome  -> bit-error estimate (lookup of coset leaders of weight <= t_D)
   2. C-syndrome  -> s in R_f  (the Z(p~_j) outcomes of T–N, eq. (56))
   3. orbit normal-form decoder -> (message index, theta).
Because every basis label in the superposition gives the same syndromes, the
label-level simulation reproduces exactly the classical information that the
quantum syndrome measurements reveal (T–N §3.2, FTW §II); it does NOT simulate
phase errors / logical fidelity (those parts are unchanged from Fujiwara/T–N).
"""
import random
from itertools import combinations
from polyfp import deg, divmod_, mod, mul, trim
from orbits import times_x_table, int_to_poly, poly_to_int


def to_mask(a):
    return sum(1 << i for i, c in enumerate(a) if c)


def from_mask(m, n):
    return trim([(m >> i) & 1 for i in range(n)])


def pmod_mask(v, g_mask, dg):
    """v mod g over F2 with polynomials as int masks."""
    while v and v.bit_length() - 1 >= dg:
        v ^= g_mask << (v.bit_length() - 1 - dg)
    return v


def pdiv_mask(v, g_mask, dg):
    q = 0
    while v and v.bit_length() - 1 >= dg:
        s = v.bit_length() - 1 - dg
        q |= 1 << s
        v ^= g_mask << s
    return q, v


def pmul_mask(a, b):
    r = 0
    while b:
        if b & 1:
            r ^= a
        a <<= 1
        b >>= 1
    return r


def cyc(v, n):
    full = (1 << n) - 1
    return v & full


class MarkerCode:
    def __init__(self, I, L, al=None):
        self.n, self.I, self.L = I["n"], I, L
        self.gC, self.gD, self.f = to_mask(I["gC"]), to_mask(I["gD"]), to_mask(I["f"])
        self.dC, self.dD, self.r = deg(I["gC"]), deg(I["gD"]), deg(I["f"])
        self.al = (L - 1) // 2 if al is None else al
        self.ar = L - 1 - self.al
        # orbit structure of R_f
        nxt = times_x_table(I["f"], 2)
        self.nxt = nxt
        self.orbit_of, self.index_in_orbit, self.orbits = {}, {}, []
        seen = set([0])
        for u in range(1, 2 ** self.r):
            if u in seen:
                continue
            orb, v = [], u
            while v not in seen:
                seen.add(v)
                orb.append(v)
                v = nxt[v]
            oid = len(self.orbits)
            self.orbits.append(orb)
            for k, v in enumerate(orb):
                self.orbit_of[v], self.index_in_orbit[v] = oid, k
        # optimal marker set: x^{jL} * base, j < floor(e/L)
        self.markers = []
        for oid, orb in enumerate(self.orbits):
            e = len(orb)
            for j in range(e // L):
                self.markers.append((oid, j, orb[j * L]))
        self.rank = {m[2]: i for i, m in enumerate(self.markers)}

    # -- quantum-free label-level pieces
    def random_C_word(self, rng):
        k = self.n - self.dC
        a = rng.getrandbits(k)
        return pmul_mask(a, self.gC)  # degree < n automatically

    def marker_word(self, u):
        return pmul_mask(u, self.gD)  # deg < deg f + deg gD = deg gC < n

    def extended_block(self, v):
        n, al, ar = self.n, self.al, self.ar
        bits = [(v >> i) & 1 for i in range(n)]
        return bits[n - al:] + bits + bits[:ar]

    def decode_window(self, W, table):
        n = self.n
        synd = pmod_mask(W, self.gD, self.dD)
        e = table.get(synd)
        if e is None:
            return None
        Wc = W ^ e
        q, rem = pdiv_mask(Wc, self.gD, self.dD)
        assert rem == 0, "corrected window must lie in D"
        s = pmod_mask(q, self.f, self.r)
        if s == 0:
            return None
        oid, k = self.orbit_of[s], self.index_in_orbit[s]
        e_len = len(self.orbits[oid])
        # window = x^{-theta} * (c + w_u);  s = x^{-theta} * x^{jL} * base
        # k = jL - theta (mod e);  -theta in [-a_r, a_l]
        kp = (k + self.ar) % e_len
        j = kp // self.L
        minus_theta = kp - j * self.L - self.ar
        if j >= e_len // self.L:
            return None
        u = self.orbits[oid][j * self.L]
        return self.rank[u], -minus_theta

    def syndrome_table(self, t):
        n, table = self.n, {0: 0}
        for w in range(1, t + 1):
            for pos in combinations(range(n), w):
                e = sum(1 << p for p in pos)
                s = pmod_mask(e, self.gD, self.dD)
                assert s not in table, "t exceeds unique-decoding radius of D"
                table[s] = e
        return table


def run(I, L, trials, t, seed=0):
    rng = random.Random(seed)
    code = MarkerCode(I, L)
    table = code.syndrome_table(t)
    n = code.n
    ok = 0
    for _ in range(trials):
        msg = rng.randrange(len(code.markers))
        u = code.markers[msg][2]
        c = code.random_C_word(rng)
        v = c ^ code.marker_word(u)
        ext = code.extended_block(v)
        theta = rng.randint(-code.al, code.ar)
        start = code.al + theta
        wbits = ext[start:start + n]
        W = sum(b << i for i, b in enumerate(wbits))
        # bit flips inside the window
        wt = rng.randint(0, t)
        for p in rng.sample(range(n), wt):
            W ^= 1 << p
        out = code.decode_window(W, table)
        if out == (msg, theta):
            ok += 1
    return len(code.markers), ok, trials


if __name__ == "__main__":
    from codes import all_instances
    import sys
    trials = int(sys.argv[1]) if len(sys.argv) > 1 else 2000
    for I in all_instances():
        if I["name"] not in ("BCH31-a", "BCH31-b", "BCH31-c", "QR31-1", "BCH63-a", "BCH63-c"):
            continue
        tD = {"BCH31-a": 1, "BCH31-b": 2, "BCH31-c": 1, "QR31-1": 2, "BCH63-a": 2, "BCH63-c": 2}[I["name"]]
        emax = max(len(o) for o in MarkerCode(I, 1).orbits)
        for L in sorted(set([2, 3, 5, deg(I["f"]), deg(I["f"]) + 1, emax // 2, emax])):
            M, ok, tr = run(I, L, trials, tD, seed=L)
            print(f'{I["name"]:8s} L={L:3d}  |M|={M:5d}  t_D={tD}  success {ok}/{tr}')
