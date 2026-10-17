"""Chapter 2 - Numbers: integers, floats and the traps between them."""
import math


# ==== EX 2.1 | Floor division with negatives | Core
# PROMPT: Write `div_mod(a, b)` returning `(a // b, a % b)`. Predict the results for negative inputs before running it.
# EXAMPLE: `div_mod(7, 2)` -> `(3, 1)`; `div_mod(-7, 2)` -> `(-4, 1)`
# BIGO: O(1).
# NOTE: Python floors toward minus infinity, so `-7 // 2` is -4 and `-7 % 2` is 1. C++ and Java truncate toward zero and give -3 and -1.
def div_mod(a, b):
    raise NotImplementedError
# ==== END


# ==== EX 2.2 | Ceiling division without floats | Core
# PROMPT: Write `ceil_div(a, b)` for integers using only `//` (no `math.ceil`, no `/`).
# EXAMPLE: `ceil_div(7, 2)` -> `4`; `ceil_div(6, 3)` -> `2`; `ceil_div(-7, 2)` -> `-3`
# BIGO: O(1).
# NOTE: `math.ceil(a / b)` goes through a float and is wrong for large values such as `10**18 + 1`.
def ceil_div(a, b):
    raise NotImplementedError
# ==== END


# ==== EX 2.3 | Big integers for free | Core
# PROMPT: Write `factorial_digits(n)` returning how many digits n! has. Python ints never overflow, so compute it directly.
# EXAMPLE: `factorial_digits(10)` -> `7` (3628800); `factorial_digits(100)` -> `158`
# BIGO: Fine for n up to a few thousand; the number itself has O(n log n) digits.
def factorial_digits(n):
    raise NotImplementedError
# ==== END


# ==== EX 2.4 | Modular power and inverse | Core
# PROMPT: With `MOD = 10**9 + 7`, write `mod_pow(a, b)` using three-argument `pow` and `mod_inv(a)` using `pow(a, -1, MOD)`. Check that `a * mod_inv(a) % MOD == 1`.
# EXAMPLE: `mod_pow(2, 10)` -> `1024`; `mod_pow(2, 100)` -> `976371285`
# BIGO: O(log b) by repeated squaring.
# NOTE: `pow(a, b) % MOD` computes the full huge number first; `pow(a, b, MOD)` never does.
MOD = 10**9 + 7


def mod_pow(a, b):
    raise NotImplementedError


def mod_inv(a):
    raise NotImplementedError
# ==== END


# ==== EX 2.5 | Comparing floats safely | Core
# PROMPT: Write `close(a, b, eps=1e-9)` and show that `0.1 + 0.2 == 0.3` is False but `close(0.1 + 0.2, 0.3)` is True.
# EXAMPLE: `close(0.1 + 0.2, 0.3)` -> `True`
# BIGO: O(1).
# NOTE: `math.isclose` exists too; contest problems usually state an absolute or relative tolerance, so match theirs.
def close(a, b, eps=1e-9):
    raise NotImplementedError
# ==== END


# ==== EX 2.6 | Perfect squares with isqrt | Core
# PROMPT: Write `is_square(n)` with `math.isqrt`. Then explain why `int(n ** 0.5) ** 2 == n` can fail for large n.
# EXAMPLE: `is_square(49)` -> `True`; `is_square(10**30 + 1)` -> `False`; `is_square((10**15 + 3) ** 2)` -> `True`
# BIGO: O(1) for contest-sized numbers.
def is_square(n):
    raise NotImplementedError
# ==== END


# ==== EX 2.7 | Digit sum two ways | Core
# PROMPT: Write `digit_sum_str(n)` using `str` and `digit_sum_math(n)` using `% 10` and `// 10`. Both work for negative n by ignoring the sign.
# EXAMPLE: `digit_sum_str(9045)` -> `18`; `digit_sum_math(-123)` -> `6`
# BIGO: O(D) for D digits.
def digit_sum_str(n):
    raise NotImplementedError


def digit_sum_math(n):
    raise NotImplementedError
# ==== END


# ==== EX 2.8 | Reverse the digits | Core
# PROMPT: Write `reverse_int(n)` keeping the sign and dropping leading zeros.
# EXAMPLE: `reverse_int(1200)` -> `21`; `reverse_int(-345)` -> `-543`
# BIGO: O(D).
def reverse_int(n):
    raise NotImplementedError
# ==== END


# ==== EX 2.9 | Number bases | Core
# PROMPT: Write `to_base(n, b)` returning the digits of non-negative n in base b (2 to 36) as a string, and use `int(s, b)` to convert back. Compare with `bin`, `oct`, `hex`.
# EXAMPLE: `to_base(255, 16)` -> `"FF"`; `to_base(10, 2)` -> `"1010"`; `int("1010", 2)` -> `10`
# BIGO: O(log_b n).
DIGITS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def to_base(n, b):
    raise NotImplementedError
# ==== END


# ==== EX 2.10 | Rounding half up | Practice
# PROMPT: `round(2.5)` is 2 in Python (banker's rounding). Write `round_half_up(x)` for non-negative floats that returns 3 for 2.5, using `math.floor`.
# EXAMPLE: `round(2.5)` -> `2`; `round_half_up(2.5)` -> `3`; `round_half_up(2.4)` -> `2`
# BIGO: O(1).
def round_half_up(x):
    raise NotImplementedError
# ==== END
