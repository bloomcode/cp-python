"""Chapter 12 - itertools and functools: brute force without writing loops."""
import math
import operator
from functools import reduce
from itertools import accumulate, chain, combinations, groupby, islice, count, permutations, product


# ==== EX 12.1 | permutations | Core
# PROMPT: Write `numbers_from_digits(digits)` returning every distinct number formed by using all the digits once, sorted. Use `itertools.permutations`.
# EXAMPLE: `numbers_from_digits([1, 2, 1])` -> `[112, 121, 211]`
# BIGO: O(N! * N). Practical up to N = 8 or so.
def numbers_from_digits(digits):
    raise NotImplementedError
# ==== END


# ==== EX 12.2 | combinations | Core
# PROMPT: Write `k_subsets_with_sum(nums, k, target)` returning all k-element combinations (as tuples, in generation order) that sum to target.
# EXAMPLE: `k_subsets_with_sum([1, 2, 3, 4, 5], 2, 6)` -> `[(1, 5), (2, 4)]`
# BIGO: O(C(N, k) * k).
def k_subsets_with_sum(nums, k, target):
    raise NotImplementedError
# ==== END


# ==== EX 12.3 | product | Core
# PROMPT: Write `dice_sum_counts(n)` returning a dict of total to number of ways when rolling n six-sided dice, using `product(range(1, 7), repeat=n)`.
# EXAMPLE: `dice_sum_counts(2)[7]` -> `6`; `sum(dice_sum_counts(3).values())` -> `216`
# BIGO: O(6^N).
def dice_sum_counts(n):
    raise NotImplementedError
# ==== END


# ==== EX 12.4 | accumulate | Core
# PROMPT: Write `prefix(arr)` with `accumulate` (starting from 0, so the result has N + 1 values), and `running_best(arr)` with `accumulate(arr, max)`.
# EXAMPLE: `prefix([3, 1, 4])` -> `[0, 3, 4, 8]`; `running_best([2, 1, 5, 3])` -> `[2, 2, 5, 5]`
# BIGO: O(N).
def prefix(arr):
    raise NotImplementedError


def running_best(arr):
    raise NotImplementedError
# ==== END


# ==== EX 12.5 | groupby | Core
# PROMPT: Write `runs(s)` returning `(char, length)` for each run of equal characters using `groupby`. Then explain why groupby on unsorted data does not group all equal items together.
# EXAMPLE: `runs("aaabccdddd")` -> `[('a', 3), ('b', 1), ('c', 2), ('d', 4)]`
# BIGO: O(N).
# NOTE: `groupby` only merges neighbours. Sort first if you want one group per key.
def runs(s):
    raise NotImplementedError
# ==== END


# ==== EX 12.6 | chain | Core
# PROMPT: Write `merge_all(lists)` that concatenates any number of lists with `chain.from_iterable`, and `interleave(a, b)` alternating items of two equal-length lists.
# EXAMPLE: `merge_all([[1], [2, 3], []])` -> `[1, 2, 3]`; `interleave([1, 3], [2, 4])` -> `[1, 2, 3, 4]`
# BIGO: O(total items).
def merge_all(lists):
    raise NotImplementedError


def interleave(a, b):
    raise NotImplementedError
# ==== END


# ==== EX 12.7 | reduce | Core
# PROMPT: Write `product_of(nums)` with `reduce(operator.mul, nums, 1)` and `gcd_of(nums)` with `reduce(math.gcd, nums)`.
# EXAMPLE: `product_of([2, 3, 7])` -> `42`; `gcd_of([12, 18, 30])` -> `6`
# BIGO: O(N) operations. `math.prod` and `math.gcd(*nums)` (3.9+) do the same.
def product_of(nums):
    raise NotImplementedError


def gcd_of(nums):
    raise NotImplementedError
# ==== END


# ==== EX 12.8 | Lazy sequences with count and islice | Practice
# PROMPT: Write `first_n_primes(n)` that walks `count(2)`, filters primes with a simple test, and takes n with `islice`.
# EXAMPLE: `first_n_primes(6)` -> `[2, 3, 5, 7, 11, 13]`
# BIGO: About O(n * sqrt(p_n)) for the trial-division test.
def first_n_primes(n):
    raise NotImplementedError
# ==== END


# ==== EX 12.9 | Brute force every subset | Practice
# PROMPT: Write `closest_subset_sum(nums, target)` returning the subset sum closest to target (prefer the smaller sum on ties), trying every size with `combinations`.
# EXAMPLE: `closest_subset_sum([8, 3, 5, 11], 15)` -> `14`; `closest_subset_sum([8, 3, 5, 11], 16)` -> `16`
# BIGO: O(2^N * N). Fine for N up to about 20.
def closest_subset_sum(nums, target):
    raise NotImplementedError
# ==== END
