import math

from ch02_numbers import (MOD, ceil_div, close, digit_sum_math, digit_sum_str, div_mod, factorial_digits, is_square,
                          mod_inv, mod_pow, reverse_int, round_half_up, to_base)


def test_ex_2_1():
    assert div_mod(7, 2) == (3, 1) and div_mod(-7, 2) == (-4, 1)


def test_ex_2_2():
    for a in range(-20, 21):
        for b in (1, 2, 3, 7, -3):
            assert ceil_div(a, b) == math.ceil(a / b)
    assert ceil_div(10**18 + 1, 1) == 10**18 + 1


def test_ex_2_3():
    assert factorial_digits(10) == 7 and factorial_digits(100) == 158


def test_ex_2_4():
    assert mod_pow(2, 10) == 1024 and mod_pow(2, 100) == 976371285
    assert 123456 * mod_inv(123456) % MOD == 1


def test_ex_2_5():
    assert 0.1 + 0.2 != 0.3 and close(0.1 + 0.2, 0.3) and not close(0.1, 0.2)


def test_ex_2_6():
    assert is_square(49) and not is_square(10**30 + 1) and is_square((10**15 + 3) ** 2) and not is_square(-4)


def test_ex_2_7():
    assert digit_sum_str(9045) == 18 == digit_sum_math(9045) and digit_sum_math(-123) == 6


def test_ex_2_8():
    assert reverse_int(1200) == 21 and reverse_int(-345) == -543


def test_ex_2_9():
    assert to_base(255, 16) == "FF" and to_base(10, 2) == "1010" and to_base(0, 2) == "0"
    assert int(to_base(123456, 7), 7) == 123456


def test_ex_2_10():
    assert round(2.5) == 2 and round_half_up(2.5) == 3 and round_half_up(2.4) == 2
