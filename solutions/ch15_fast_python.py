"""Chapter 15 - Writing Python that fits the time limit."""
import bisect
import math
from collections import deque


# ==== EX 15.1 | Will it pass? Estimate before you code | Core
# PROMPT: Write `fits(n, cls)` returning True if an algorithm of class `cls` ("1", "logn", "n", "nlogn", "n2", "2n") on input size n needs at most 10^7 basic steps, a safe budget for one second of Python.
# EXAMPLE: `fits(10**5, "nlogn")` -> `True`; `fits(10**5, "n2")` -> `False`; `fits(20, "2n")` -> `True`
# BIGO: O(1).
# NOTE: Compiled languages manage roughly 10^8 to 10^9 simple steps per second; CPython manages roughly 10^7. Pick the algorithm with that in mind.
def fits(n, cls):
    raise NotImplementedError
# ==== END


# ==== EX 15.2 | Sets for membership | Core
# PROMPT: Write `count_hits(queries, items)` counting how many queries appear in items. Convert items to a set once.
# EXAMPLE: `count_hits([1, 5, 9], [9, 8, 1])` -> `2`
# BIGO: O(N + Q) with a set, O(N * Q) with `in` on a list.
def count_hits(queries, items):
    raise NotImplementedError
# ==== END


# ==== EX 15.3 | Precompute, then answer | Core
# PROMPT: Write `answer_range_sums(arr, queries)` answering each `(l, r)` inclusive sum query from one prefix-sum array.
# EXAMPLE: `answer_range_sums([3, 1, 4, 1, 5], [(0, 2), (1, 4)])` -> `[8, 11]`
# BIGO: O(N + Q) instead of O(N * Q).
def answer_range_sums(arr, queries):
    raise NotImplementedError
# ==== END


# ==== EX 15.4 | deque instead of pop(0) | Core
# PROMPT: Write `josephus(n, k)`: n people in a circle, every k-th person leaves; return the leaving order. Use `deque.rotate`.
# EXAMPLE: `josephus(7, 3)` -> `[3, 6, 2, 7, 5, 1, 4]`
# BIGO: O(N * k) with rotate; a list with `pop(0)` adds O(N) per removal.
def josephus(n, k):
    raise NotImplementedError
# ==== END


# ==== EX 15.5 | Sort once, search many times | Core
# PROMPT: Write `count_at_most(values, queries)` returning, for each query q, how many values are <= q. Sort once and use `bisect_right`.
# EXAMPLE: `count_at_most([5, 1, 9, 3], [0, 4, 10])` -> `[0, 2, 4]`
# BIGO: O((N + Q) log N) instead of O(N * Q).
def count_at_most(values, queries):
    raise NotImplementedError
# ==== END


# ==== EX 15.6 | Read big input fast | Core
# PROMPT: Write `big_sum(data)` for input "N, then N integers" that splits the whole text once and sums with `map(int, ...)`, avoiding a Python-level loop per line.
# EXAMPLE: `big_sum("3\n10 20\n30")` -> `60`
# BIGO: O(N). On a judge, read the text with `sys.stdin.buffer.read()` (see 1.8).
def big_sum(data):
    raise NotImplementedError
# ==== END


# ==== EX 15.7 | Build output once | Core
# PROMPT: Write `squares_output(n)` returning the squares of 1..n, one per line, as a single string built with `"\n".join`.
# EXAMPLE: `squares_output(3)` -> `"1\n4\n9"`
# BIGO: O(N). Calling `print` 10^5 times is several times slower than one write.
def squares_output(n):
    raise NotImplementedError
# ==== END


# ==== EX 15.8 | Iterative DFS with an explicit stack | Core
# PROMPT: Write `reachable(graph, start)` returning the set of nodes reachable from start using a list as a stack, so a path of 10^5 nodes does not hit the recursion limit.
# EXAMPLE: `reachable({1: [2], 2: [3], 3: [], 4: [1]}, 1)` -> `{1, 2, 3}`
# BIGO: O(V + E).
def reachable(graph, start):
    raise NotImplementedError
# ==== END
