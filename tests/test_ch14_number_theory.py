import math

from ch14_number_theory import (MOD, arith_sum, count_multiples, divisors, ext_gcd, factorize, gcd, inverse_mod, is_prime,
                                lcm, make_ncr, mod_sub, sieve, sum_of_products_mod)


def test_ex_14_1():
    for a in range(1, 60):
        for b in range(1, 60):
            assert gcd(a, b) == math.gcd(a, b) and lcm(a, b) == math.lcm(a, b)


def test_ex_14_2():
    assert is_prime(97) and not is_prime(1) and is_prime(1_000_000_007) and is_prime(2) and not is_prime(91)


def test_ex_14_3():
    assert sieve(30) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] and len(sieve(10**6)) == 78498 and sieve(1) == []
    primes = set(sieve(500))
    assert all((p in primes) == all(p % d for d in range(2, math.isqrt(p) + 1)) for p in range(2, 500))


def test_ex_14_4():
    assert factorize(360) == {2: 3, 3: 2, 5: 1} and factorize(97) == {97: 1} and factorize(1) == {}


def test_ex_14_5():
    assert divisors(36) == [1, 2, 3, 4, 6, 9, 12, 18, 36] and divisors(1) == [1]


def test_ex_14_6():
    ncr = make_ncr(100)
    assert ncr(5, 2) == 10 and ncr(100, 50) == 538992043 and ncr(3, 5) == 0
    assert all(ncr(n, r) == math.comb(n, r) % MOD for n in range(40) for r in range(n + 1))


def test_ex_14_7():
    assert sum_of_products_mod([10**9, 2], [10**9, 3]) == 55 and mod_sub(1, 3) == 1000000005


def test_ex_14_8():
    assert arith_sum(1, 1, 100) == 5050 and arith_sum(3, 4, 5) == sum(3 + 4 * i for i in range(5))
    assert count_multiples(10, 30, 7) == 3 and count_multiples(1, 7, 7) == 1


def test_ex_14_9():
    g, x, y = ext_gcd(30, 12)
    assert g == 6 and 30 * x + 12 * y == 6
    assert inverse_mod(3, 10) == 7 and inverse_mod(4, 10) is None
