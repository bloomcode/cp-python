"""Chapter 14 - Math and number theory for contests."""
import math

MOD = 10**9 + 7


# ==== EX 14.1 | GCD and LCM | Core
# PROMPT: Write `gcd(a, b)` with Euclid's algorithm (no `math.gcd`) and `lcm(a, b)` from it. Compare with `math.gcd` and `math.lcm`.
# EXAMPLE: `gcd(84, 36)` -> `12`; `lcm(4, 6)` -> `12`
# BIGO: O(log min(a, b)).
def gcd(a, b):
    raise NotImplementedError


def lcm(a, b):
    raise NotImplementedError
# ==== END


# ==== EX 14.2 | Primality by trial division | Core
# PROMPT: Write `is_prime(n)` checking divisors up to `math.isqrt(n)`, skipping even numbers after 2.
# EXAMPLE: `is_prime(97)` -> `True`; `is_prime(1)` -> `False`; `is_prime(1_000_000_007)` -> `True`
# BIGO: O(sqrt N).
def is_prime(n):
    raise NotImplementedError
# ==== END


# ==== EX 14.3 | Sieve of Eratosthenes | Core
# PROMPT: Write `sieve(n)` returning all primes up to n with a `bytearray` of flags and slice assignment to cross out multiples from p*p.
# EXAMPLE: `sieve(30)` -> `[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]`; `len(sieve(10**6))` -> `78498`
# BIGO: O(N log log N). Slice assignment keeps it fast enough for N = 10^7 in Python.
def sieve(n):
    raise NotImplementedError
# ==== END


# ==== EX 14.4 | Prime factorization | Core
# PROMPT: Write `factorize(n)` returning a dict of prime to exponent by trial division up to sqrt(n).
# EXAMPLE: `factorize(360)` -> `{2: 3, 3: 2, 5: 1}`; `factorize(97)` -> `{97: 1}`
# BIGO: O(sqrt N).
def factorize(n):
    raise NotImplementedError
# ==== END


# ==== EX 14.5 | All divisors in O(sqrt N) | Core
# PROMPT: Write `divisors(n)` returning the sorted divisors, collecting both i and n // i for each i up to sqrt(n).
# EXAMPLE: `divisors(36)` -> `[1, 2, 3, 4, 6, 9, 12, 18, 36]`
# BIGO: O(sqrt N).
def divisors(n):
    raise NotImplementedError
# ==== END


# ==== EX 14.6 | nCr modulo a prime | Core
# PROMPT: Write `make_ncr(maxn)` that precomputes factorials and inverse factorials mod 10^9 + 7 and returns a function `ncr(n, r)` answering in O(1).
# EXAMPLE: `ncr = make_ncr(100)`: `ncr(5, 2)` -> `10`; `ncr(100, 50)` -> `538992043`
# BIGO: O(maxn) to precompute, O(1) per query.
# NOTE: Compute the top inverse with `pow(fact[maxn], MOD - 2, MOD)` (Fermat) and walk downward: `inv[i - 1] = inv[i] * i`.
def make_ncr(maxn):
    raise NotImplementedError
# ==== END


# ==== EX 14.7 | Keep answers under the modulus | Core
# PROMPT: Write `sum_of_products_mod(a, b)` returning the sum of `a[i] * b[i]` mod 10^9 + 7, reducing as you go. Then write `mod_sub(x, y)` that never returns a negative.
# EXAMPLE: `sum_of_products_mod([10**9, 2], [10**9, 3])` -> `55`; `mod_sub(1, 3)` -> `1000000005`
# BIGO: O(N).
# NOTE: Python's `%` already returns a non-negative result for a positive modulus; in other languages you must add MOD before `%`.
def sum_of_products_mod(a, b):
    raise NotImplementedError


def mod_sub(x, y):
    raise NotImplementedError
# ==== END


# ==== EX 14.8 | Formulas instead of loops | Core
# PROMPT: Write `arith_sum(a, d, n)` for the first n terms of an arithmetic series and `count_multiples(lo, hi, k)` counting multiples of k in [lo, hi], both in O(1).
# EXAMPLE: `arith_sum(1, 1, 100)` -> `5050`; `count_multiples(10, 30, 7)` -> `3`
# BIGO: O(1) each, instead of O(N) loops.
def arith_sum(a, d, n):
    raise NotImplementedError


def count_multiples(lo, hi, k):
    raise NotImplementedError
# ==== END


# ==== EX 14.9 | Extended Euclid | Stretch
# PROMPT: Write `ext_gcd(a, b)` returning `(g, x, y)` with `a*x + b*y == g`, and use it to find a modular inverse when the modulus is not prime.
# EXAMPLE: `ext_gcd(30, 12)` -> `g = 6` with `30*x + 12*y == 6`; inverse of 3 mod 10 is `7`
# BIGO: O(log min(a, b)).
def ext_gcd(a, b):
    raise NotImplementedError


def inverse_mod(a, m):
    raise NotImplementedError
# ==== END
