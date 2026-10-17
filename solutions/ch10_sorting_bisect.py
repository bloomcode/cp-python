"""Chapter 10 - Sorting with keys, and binary search with bisect."""
import bisect
from functools import cmp_to_key


# ==== EX 10.1 | Multi-key sort | Core
# PROMPT: Write `leaderboard(rows)` for `(name, score)` tuples: highest score first, ties in alphabetical order, using one `sorted` call with a tuple key.
# EXAMPLE: `leaderboard([("bo", 80), ("al", 95), ("cy", 80)])` -> `[('al', 95), ('bo', 80), ('cy', 80)]`
# BIGO: O(N log N).
def leaderboard(rows):
    raise NotImplementedError
# ==== END


# ==== EX 10.2 | Stability: sort twice | Core
# PROMPT: Write `by_dept_then_age(people)` for `(name, dept, age)` tuples: sort by age first, then stably by dept. Explain why the order of the two sorts matters.
# EXAMPLE: `[("a", "ops", 40), ("b", "dev", 30), ("c", "ops", 25)]` -> names `['b', 'c', 'a']`
# BIGO: O(N log N). Python's sort is stable: equal keys keep their existing order.
def by_dept_then_age(people):
    raise NotImplementedError
# ==== END


# ==== EX 10.3 | Custom comparison with cmp_to_key | Practice
# PROMPT: Write `largest_number(nums)`: arrange non-negative integers to form the largest number, as a string. Compare two numbers a, b by which of `str(a)+str(b)` or `str(b)+str(a)` is bigger.
# EXAMPLE: `largest_number([3, 30, 34, 5, 9])` -> `"9534330"`; `largest_number([0, 0])` -> `"0"`
# BIGO: O(N log N) comparisons.
def largest_number(nums):
    raise NotImplementedError
# ==== END


# ==== EX 10.4 | Argsort | Core
# PROMPT: Write `argsort(arr)` returning the indices that would sort `arr`, using `sorted(range(len(arr)), key=arr.__getitem__)`.
# EXAMPLE: `argsort([30, 10, 20])` -> `[1, 2, 0]`
# BIGO: O(N log N).
def argsort(arr):
    raise NotImplementedError
# ==== END


# ==== EX 10.5 | Count values in a range with bisect | Core
# PROMPT: Write `count_between(sorted_arr, lo, hi)` returning how many values fall in [lo, hi], using `bisect_left` and `bisect_right`.
# EXAMPLE: `count_between([1, 3, 3, 5, 8, 13], 3, 8)` -> `4`
# BIGO: O(log N) per query on a sorted list.
def count_between(sorted_arr, lo, hi):
    raise NotImplementedError
# ==== END


# ==== EX 10.6 | Keep a list sorted with insort | Core
# PROMPT: Write `sorted_stream(values)` that inserts each value into a sorted list with `bisect.insort` and records the current median (lower middle for even sizes) after each insert.
# EXAMPLE: `sorted_stream([5, 2, 8, 1, 9])` -> `[5, 2, 5, 2, 5]`
# BIGO: O(log N) to find the spot, O(N) to shift, so O(N^2) total. Fine for N up to about 10^4.
def sorted_stream(values):
    raise NotImplementedError
# ==== END


# ==== EX 10.7 | Binary search on the answer | Core
# PROMPT: Write `min_speed(piles, hours)`: the smallest integer speed k such that eating `ceil(p / k)` hours per pile finishes within `hours`. Binary-search k between 1 and max(piles).
# EXAMPLE: `min_speed([3, 6, 7, 11], 8)` -> `4`; `min_speed([30, 11, 23, 4, 20], 5)` -> `30`
# BIGO: O(N log M) for M = max(piles). Search the answer space whenever "is k enough?" is easy to check and monotonic.
def min_speed(piles, hours):
    raise NotImplementedError
# ==== END


# ==== EX 10.8 | A reusable first-true search | Practice
# PROMPT: Write `first_true(lo, hi, pred)` returning the smallest x in [lo, hi] with `pred(x)` true (pred goes False...False, True...True), or `hi + 1` if none. Use it for integer square root.
# EXAMPLE: `first_true(0, 100, lambda x: x * x >= 50)` -> `8`
# BIGO: O(log (hi - lo)) calls to pred.
def first_true(lo, hi, pred):
    raise NotImplementedError
# ==== END


# ==== EX 10.9 | Coordinate compression | Practice
# PROMPT: Write `compress(arr)` replacing each value with its rank among the distinct values (0-based), using a sorted set and a dict.
# EXAMPLE: `compress([100, 5, 100, 42])` -> `[2, 0, 2, 1]`
# BIGO: O(N log N). Lets you index arrays by values up to 10^9 using only N slots.
def compress(arr):
    raise NotImplementedError
# ==== END
