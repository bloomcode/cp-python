"""Chapter 13 - Bit manipulation."""


# ==== EX 13.1 | Get, set, clear and toggle a bit | Core
# PROMPT: Write `get_bit(x, i)`, `set_bit(x, i)`, `clear_bit(x, i)` and `toggle_bit(x, i)` using `1 << i` with `&`, `|`, `& ~` and `^`.
# EXAMPLE: `x = 0b1010`: `get_bit(x, 1)` -> `1`; `set_bit(x, 0)` -> `11`; `clear_bit(x, 3)` -> `2`; `toggle_bit(x, 2)` -> `14`
# BIGO: O(1).
def get_bit(x, i):
    raise NotImplementedError


def set_bit(x, i):
    raise NotImplementedError


def clear_bit(x, i):
    raise NotImplementedError


def toggle_bit(x, i):
    raise NotImplementedError
# ==== END


# ==== EX 13.2 | Count set bits three ways | Core
# PROMPT: Write `popcount_str(x)` with `bin(x).count("1")`, `popcount_loop(x)` with Kernighan's `x &= x - 1`, and compare with `int.bit_count()` (Python 3.10+).
# EXAMPLE: `popcount_loop(0b101101)` -> `4`; `(255).bit_count()` -> `8`
# BIGO: Kernighan's loop runs once per set bit.
def popcount_str(x):
    raise NotImplementedError


def popcount_loop(x):
    raise NotImplementedError
# ==== END


# ==== EX 13.3 | Power of two | Core
# PROMPT: Write `is_power_of_two(n)` in one expression with `n & (n - 1)`.
# EXAMPLE: `is_power_of_two(64)` -> `True`; `is_power_of_two(96)` -> `False`; `is_power_of_two(0)` -> `False`
# BIGO: O(1).
def is_power_of_two(n):
    raise NotImplementedError
# ==== END


# ==== EX 13.4 | Enumerate subsets with a bitmask | Core
# PROMPT: Write `all_subsets(items)` looping `mask` from 0 to `2**n - 1` and including item i when bit i of mask is set.
# EXAMPLE: `all_subsets(['a', 'b'])` -> `[[], ['a'], ['b'], ['a', 'b']]`
# BIGO: O(2^N * N).
def all_subsets(items):
    raise NotImplementedError
# ==== END


# ==== EX 13.5 | The lonely number with XOR | Core
# PROMPT: Every number appears twice except one. Write `lonely(nums)` using XOR (`x ^ x == 0`, `x ^ 0 == x`).
# EXAMPLE: `lonely([4, 1, 2, 1, 2])` -> `4`
# BIGO: O(N) time, O(1) space.
def lonely(nums):
    raise NotImplementedError
# ==== END


# ==== EX 13.6 | Lowest set bit | Core
# PROMPT: Write `lowest_bit(x)` returning the value of the lowest set bit with `x & -x`, and `highest_bit_index(x)` with `x.bit_length() - 1`.
# EXAMPLE: `lowest_bit(12)` -> `4`; `highest_bit_index(12)` -> `3`
# BIGO: O(1).
# NOTE: `x & -x` is the step used by Fenwick trees, which you will meet in contest data structures.
def lowest_bit(x):
    raise NotImplementedError


def highest_bit_index(x):
    raise NotImplementedError
# ==== END


# ==== EX 13.7 | Fixed-width binary strings | Core
# PROMPT: Write `to_bits(x, width)` returning a zero-padded binary string using `format(x, f"0{width}b")`, and `from_bits(s)` using `int(s, 2)`.
# EXAMPLE: `to_bits(5, 8)` -> `"00000101"`; `from_bits("1101")` -> `13`
# BIGO: O(width).
def to_bits(x, width):
    raise NotImplementedError


def from_bits(s):
    raise NotImplementedError
# ==== END


# ==== EX 13.8 | Subset sum by brute force | Practice
# PROMPT: Write `can_make(nums, target)` that tries every bitmask and returns True if some subset sums to target.
# EXAMPLE: `can_make([3, 34, 4, 12, 5, 2], 9)` -> `True`; `can_make([3, 34, 4], 30)` -> `False`
# BIGO: O(2^N * N). Use it to check a smarter solution on small inputs.
def can_make(nums, target):
    raise NotImplementedError
# ==== END
