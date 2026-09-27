"""Numerical check of Proposition C2 (uniform-orbit case): for prime n >= 7, binary,
f | (x^n-1)/(x-1) of degree r = k*ord_n(2) (all orbits of R_f \\ {0} have size n), so
N_f(L) = ((2^r-1)/n) * floor(n/L).  Claim: log2 N_f(L) + L > r for 2 <= L <= r,
i.e. |M| * 2^L > 2^r (strictly beats y + d_sync <= r of T–N Lemma 3 / Cor 2).
Exact integer arithmetic: check N * 2^L > 2^r."""
def is_prime(n):
    return n > 1 and all(n % p for p in range(2, int(n ** .5) + 1))
def ordmod(q, n):
    k, v = 1, q % n
    while v != 1:
        v = v * q % n; k += 1
    return k
bad = checked = 0
for n in range(7, 600):
    if not is_prime(n): continue
    o = ordmod(2, n)
    for r in range(o, n, o):
        for L in range(2, r + 1):
            N = (2 ** r - 1) // n * (n // L)
            checked += 1
            if not N * 2 ** L > 2 ** r:
                bad += 1; print("FAIL", n, r, L)
print(f"checked {checked} (n prime in [7,600), r = k*ord_n(2) < n, 2 <= L <= r): failures = {bad}")
