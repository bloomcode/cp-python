"""Chapter 4 - Control flow and loops."""


# ==== EX 4.1 | FizzBuzz | Core
# PROMPT: Write `fizzbuzz(n)` returning a list for 1..n: `"Fizz"` for multiples of 3, `"Buzz"` for 5, `"FizzBuzz"` for both, otherwise the number as a string.
# EXAMPLE: `fizzbuzz(5)` -> `['1', '2', 'Fizz', '4', 'Buzz']`
# BIGO: O(N).
def fizzbuzz(n):
    raise NotImplementedError
# ==== END


# ==== EX 4.2 | for ... else | Core
# PROMPT: Write `first_multiple(nums, k)` returning the index of the first multiple of k, or -1, using a `for` loop with an `else` clause instead of a flag variable.
# EXAMPLE: `first_multiple([5, 7, 12, 9], 3)` -> `2`; `first_multiple([5, 7], 3)` -> `-1`
# BIGO: O(N).
# NOTE: The `else` of a loop runs only when the loop finished without `break`.
def first_multiple(nums, k):
    raise NotImplementedError
# ==== END


# ==== EX 4.3 | while loop: Collatz steps | Core
# PROMPT: Write `collatz_steps(n)`: halve even numbers, map odd n to 3n + 1, and count steps until n is 1.
# EXAMPLE: `collatz_steps(6)` -> `8`; `collatz_steps(1)` -> `0`
# BIGO: No known bound; that is why it needs `while`, not `for`.
def collatz_steps(n):
    raise NotImplementedError
# ==== END


# ==== EX 4.4 | Nested loops: multiplication table | Core
# PROMPT: Write `times_table(n)` returning an n by n list of lists where row i, column j holds (i + 1) * (j + 1).
# EXAMPLE: `times_table(3)` -> `[[1, 2, 3], [2, 4, 6], [3, 6, 9]]`
# BIGO: O(N^2).
def times_table(n):
    raise NotImplementedError
# ==== END


# ==== EX 4.5 | range with a step | Core
# PROMPT: Write `evens_down(n)` returning the even numbers from n (or n - 1 if n is odd) down to 0, using a single `range` call.
# EXAMPLE: `evens_down(7)` -> `[6, 4, 2, 0]`
# BIGO: O(N).
def evens_down(n):
    raise NotImplementedError
# ==== END


# ==== EX 4.6 | enumerate and zip | Core
# PROMPT: Write `rank_lines(names, scores)` returning lines like `"1. ann: 90"` using `zip` to pair the lists and `enumerate(..., start=1)` for the rank.
# EXAMPLE: `rank_lines(["ann", "bo"], [90, 75])` -> `['1. ann: 90', '2. bo: 75']`
# BIGO: O(N).
def rank_lines(names, scores):
    raise NotImplementedError
# ==== END


# ==== EX 4.7 | Pattern printing | Core
# PROMPT: Write `pyramid(n)` returning n lines of a centred star pyramid, the classic warm-up.
# EXAMPLE: `pyramid(3)` -> `['  *', ' ***', '*****']`
# BIGO: O(N^2) characters.
def pyramid(n):
    raise NotImplementedError
# ==== END


# ==== EX 4.8 | break and continue | Core
# PROMPT: Write `sum_until_negative(nums)`: add numbers in order, skip zeros with `continue`, and stop at the first negative with `break`.
# EXAMPLE: `sum_until_negative([4, 0, 3, -1, 10])` -> `7`
# BIGO: O(N).
def sum_until_negative(nums):
    raise NotImplementedError
# ==== END


# ==== EX 4.9 | match statement | Practice
# PROMPT: Write `calc(op, a, b)` with a `match` statement for `"+"`, `"-"`, `"*"`, `"/"` (integer floor division) and a default case that raises `ValueError`.
# EXAMPLE: `calc("*", 6, 7)` -> `42`; `calc("/", 7, 2)` -> `3`
# BIGO: O(1). Needs Python 3.10 or newer; check your judge's version.
def calc(op, a, b):
    raise NotImplementedError
# ==== END
