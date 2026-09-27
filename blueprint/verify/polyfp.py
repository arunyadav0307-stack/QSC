"""Minimal, dependency-free polynomial arithmetic over a prime field F_p,
plus the extension field GF(p^m) needed to compute minimal polynomials.

Polynomials are tuples of ints (coefficient of x^0 first), always trimmed
(no trailing zeros); the zero polynomial is ().  Everything here is written
from first principles so that the verification does not depend on any
external computer-algebra system (MAGMA/Sage are used only as optional
cross-checks, see README).
"""
from functools import reduce
from itertools import product


def trim(a):
    a = list(a)
    while a and a[-1] == 0:
        a.pop()
    return tuple(a)


def deg(a):
    return len(a) - 1  # deg(()) = -1


def add(a, b, p):
    n = max(len(a), len(b))
    return trim(((a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)) % p
                for i in range(n))


def sub(a, b, p):
    return add(a, tuple((-x) % p for x in b), p)


def scal(c, a, p):
    return trim((c * x) % p for x in a)


def mul(a, b, p):
    if not a or not b:
        return ()
    r = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                r[i + j] = (r[i + j] + x * y) % p
    return trim(r)


def divmod_(a, b, p):
    """Return (q, r) with a = q*b + r, deg r < deg b."""
    if not b:
        raise ZeroDivisionError
    a = list(a)
    inv = pow(b[-1], p - 2, p)
    db = deg(b)
    q = [0] * max(len(a) - db, 0)
    for i in range(len(a) - 1, db - 1, -1):
        c = (a[i] * inv) % p
        if c:
            q[i - db] = c
            for j in range(db + 1):
                a[i - db + j] = (a[i - db + j] - c * b[j]) % p
    return trim(q), trim(a[:db] if db > 0 else [])


def mod(a, b, p):
    return divmod_(a, b, p)[1]


def monic(a, p):
    return scal(pow(a[-1], p - 2, p), a, p) if a else a


def gcd(a, b, p):
    while b:
        a, b = b, mod(a, b, p)
    return monic(a, p)


def xpow(k):
    return tuple([0] * k + [1])


def xn_minus(n, lam, p):
    """x^n - lam."""
    t = [0] * (n + 1)
    t[0] = (-lam) % p
    t[n] = 1
    return tuple(t)


def reciprocal(a, p):
    """Monic reciprocal a*(x) = a(0)^{-1} x^{deg a} a(1/x)."""
    r = trim(reversed(a))
    return monic(r, p)


def powmod(base, e, m, p):
    result = (1,)
    base = mod(base, m, p)
    while e:
        if e & 1:
            result = mod(mul(result, base, p), m, p)
        base = mod(mul(base, base, p), m, p)
        e >>= 1
    return result


def is_irreducible(f, p):
    """Rabin-style test via gcd(x^{p^i} - x, f) = 1 for i <= deg/2 (small degrees)."""
    d = deg(f)
    if d <= 0:
        return False
    if d == 1:
        return True
    x = (0, 1)
    xp = x
    for i in range(1, d // 2 + 1):
        xp = powmod(xp, p, f, p)
        if deg(gcd(f, sub(xp, x, p), p)) > 0:
            return False
    return True


def factor(f, p):
    """Complete factorisation of f (f(0) != 0) into monic irreducibles with
    multiplicity, by trial division over all monic irreducibles of increasing
    degree.  Only used for small degrees (<= ~12 over F_2, <= ~6 over F_3/F_5)."""
    f = monic(f, p)
    out = {}
    d = 1
    while deg(f) > 0:
        if 2 * d > deg(f):
            out[f] = out.get(f, 0) + 1
            break
        for coeffs in product(range(p), repeat=d):
            g = tuple(list(coeffs) + [1])
            if g[0] == 0 or not is_irreducible(g, p):
                continue
            while deg(f) >= d:
                q, r = divmod_(f, g, p)
                if r:
                    break
                out[g] = out.get(g, 0) + 1
                f = q
        d += 1
    return out


def poly_order(f, p):
    """ord(f) = least e >= 1 with f | x^e - 1 (requires f(0) != 0).
    Computed as the multiplicative order of x in F_p[x]/(f) by brute stepping
    (fine for the orders <= ~10^6 used here)."""
    assert f and f[0] % p != 0
    if deg(f) == 0:
        return 1
    x = (0, 1)
    cur = mod(x, f, p)
    e = 1
    one = (1,)
    while cur != one:
        cur = mod(mul(cur, x, p), f, p)
        e += 1
    return e


# ---------------------------------------------------------------- GF(p^m)
class GF:
    """GF(p^m) as F_p[x]/(prim), elements are trimmed tuples."""

    # Conventional primitive polynomials (binary), so that the labels M_i agree
    # with the source papers: x^4+x+1, x^5+x^2+1 (XYF, Example 1), x^6+x+1.
    DEFAULT = {(2, 3): (1, 1, 0, 1), (2, 4): (1, 1, 0, 0, 1), (2, 5): (1, 0, 1, 0, 0, 1),
               (2, 6): (1, 1, 0, 0, 0, 0, 1)}

    def __init__(self, p, m):
        self.p, self.m = p, m
        self.mod = self.DEFAULT.get((p, m)) or self._find_primitive()

    def _find_primitive(self):
        p, m = self.p, self.m
        N = p ** m - 1
        primes = [q for q in range(2, N + 1) if N % q == 0 and all(q % s for s in range(2, int(q ** .5) + 1))]
        for coeffs in product(range(p), repeat=m):
            f = tuple(list(coeffs) + [1])
            if f[0] == 0 or not is_irreducible(f, p):
                continue
            # x primitive?
            if all(powmod((0, 1), N // q, f, p) != (1,) for q in primes):
                return f
        raise RuntimeError("no primitive polynomial found")

    def mul(self, a, b):
        return mod(mul(a, b, self.p), self.mod, self.p)

    def power(self, e):
        return powmod((0, 1), e, self.mod, self.p)


def minimal_polynomial_of_power(n, i, p, lam_root_shift=None):
    """Minimal polynomial over F_p of beta^i, beta a primitive n-th root of unity
    (gcd(n,p)=1).  Returns (poly, coset)."""
    m = 1
    while pow(p, m, n) != 1 % n:
        m += 1
    F = GF(p, m)
    N = p ** m - 1
    step = N // n
    coset = []
    j = i % n
    while j not in coset:
        coset.append(j)
        j = (j * p) % n
    # product over coset of (X - beta^j), coefficients in GF(p^m)
    poly = [(1,)]  # list of GF elements, low -> high
    for j in coset:
        root = F.power(step * j)
        negroot = scal(p - 1, root, p)
        new = [()] * (len(poly) + 1)
        for k, c in enumerate(poly):
            new[k + 1] = add(new[k + 1], c, p)
            new[k] = add(new[k], F.mul(c, negroot), p)
        poly = new
    out = []
    for c in poly:
        assert deg(c) <= 0, "minimal polynomial not over the prime field"
        out.append(c[0] if c else 0)
    return trim(out), sorted(coset)


def cyclotomic_cosets(n, p):
    seen, cos = set(), []
    for i in range(n):
        if i in seen:
            continue
        c, j = [], i
        while j not in c:
            c.append(j)
            j = (j * p) % n
        cos.append(sorted(c))
        seen.update(c)
    return cos


def prod(polys, p):
    return reduce(lambda a, b: mul(a, b, p), polys, (1,))
