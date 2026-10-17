"""Chapter 8 - Functions, closures and recursion."""
import sys
from functools import lru_cache


# ==== EX 8.1 | Default and keyword arguments | Core
# PROMPT: Write `power(base, exp=2)` and call it positionally, with the default, and with `exp=` as a keyword.
# EXAMPLE: `power(5)` -> `25`; `power(2, 10)` -> `1024`; `power(exp=3, base=2)` -> `8`
# BIGO: O(1) calls; the work is in `**`.
def power(base, exp=2):
    raise NotImplementedError
# ==== END


# ==== EX 8.2 | The mutable default trap | Core
# PROMPT: Write `add_item(item, bucket=None)` that returns a list containing the item, creating a fresh list when none is passed. Explain what `bucket=[]` would do instead.
# EXAMPLE: `add_item(1)` -> `[1]`; a second `add_item(2)` -> `[2]`, not `[1, 2]`
# BIGO: O(1).
# NOTE: Default values are created once, when `def` runs. A `[]` default is shared by every call that omits the argument.
def add_item(item, bucket=None):
    raise NotImplementedError
# ==== END


# ==== EX 8.3 | *args and **kwargs | Core
# PROMPT: Write `average(*nums)` that accepts any number of values, and `describe(**info)` returning `"key=value"` pairs sorted by key, joined with `", "`.
# EXAMPLE: `average(2, 4, 9)` -> `5.0`; `describe(b=2, a=1)` -> `"a=1, b=2"`
# BIGO: O(N).
def average(*nums):
    raise NotImplementedError


def describe(**info):
    raise NotImplementedError
# ==== END


# ==== EX 8.4 | Lambdas as sort keys | Core
# PROMPT: Write `by_second(pairs)` sorting tuples by their second item, then by the first, with a lambda.
# EXAMPLE: `by_second([(1, 'b'), (2, 'a'), (0, 'b')])` -> `[(2, 'a'), (0, 'b'), (1, 'b')]`
# BIGO: O(N log N).
def by_second(pairs):
    raise NotImplementedError
# ==== END


# ==== EX 8.5 | Closures and nonlocal | Core
# PROMPT: Write `make_counter()` returning a function that returns 1, 2, 3, ... on successive calls, keeping its count in an enclosing variable updated with `nonlocal`.
# EXAMPLE: `c = make_counter(); c(), c(), c()` -> `1, 2, 3`
# BIGO: O(1) per call.
def make_counter():
    raise NotImplementedError
# ==== END


# ==== EX 8.6 | Write a memoizing decorator | Practice
# PROMPT: Write a decorator `memoize(fn)` that caches results in a dict keyed by the argument tuple, and use it on a recursive `ways(n)`: the number of ways to climb n stairs taking 1 or 2 steps.
# EXAMPLE: `ways(10)` -> `89`; `ways(80)` returns at once
# BIGO: O(N) with the cache, O(2^N) without.
def memoize(fn):
    raise NotImplementedError


def ways(n):
    raise NotImplementedError
# ==== END


# ==== EX 8.7 | lru_cache does it for you | Core
# PROMPT: Write `grid_paths(r, c)` (moves right or down from the top-left to the bottom-right of an r by c grid) decorated with `@lru_cache(maxsize=None)`.
# EXAMPLE: `grid_paths(3, 3)` -> `6`; `grid_paths(16, 16)` -> `155117520`
# BIGO: O(R * C).
@lru_cache(maxsize=None)
def grid_paths(r, c):
    raise NotImplementedError
# ==== END


# ==== EX 8.8 | Recursion depth limits | Core
# PROMPT: Write `depth_sum(n)` recursively (n + depth_sum(n - 1)) and `depth_sum_iter(n)` with a loop. Raise the limit with `sys.setrecursionlimit(10**6)` and note that very deep recursion can still crash the interpreter.
# EXAMPLE: Both give `500500` for n = 1000; at n = 100000 prefer the loop
# BIGO: O(N) time; recursion also uses O(N) stack.
# NOTE: Python's default limit is 1,000 frames. Contest solutions that recurse deeply (DFS on 10^5 nodes) should go iterative (15.8).
sys.setrecursionlimit(10**6)


def depth_sum(n):
    raise NotImplementedError


def depth_sum_iter(n):
    raise NotImplementedError
# ==== END


# ==== EX 8.9 | Functions as values | Practice
# PROMPT: Write `compose(f, g)` returning a function that computes f(g(x)), and `apply_n(f, n, x)` that applies f to x n times.
# EXAMPLE: `compose(str, abs)(-5)` -> `"5"`; `apply_n(lambda v: v * 2, 10, 1)` -> `1024`
# BIGO: O(N) for apply_n.
def compose(f, g):
    raise NotImplementedError


def apply_n(f, n, x):
    raise NotImplementedError
# ==== END
