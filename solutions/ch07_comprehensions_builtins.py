"""Chapter 7 - Comprehensions, generators and built-in functions."""


# ==== EX 7.1 | Filter inside a comprehension | Core
# PROMPT: Write `even_squares(nums)` returning the squares of the even numbers only, in one list comprehension.
# EXAMPLE: `even_squares([1, 2, 3, 4])` -> `[4, 16]`
# BIGO: O(N).
def even_squares(nums):
    raise NotImplementedError
# ==== END


# ==== EX 7.2 | Conditional expression inside a comprehension | Core
# PROMPT: Write `clamp_all(nums, lo, hi)` replacing values below lo with lo and above hi with hi, using `a if cond else b` inside the comprehension.
# EXAMPLE: `clamp_all([-5, 3, 12], 0, 10)` -> `[0, 3, 10]`
# BIGO: O(N).
# NOTE: A trailing `if` filters items out; an `if ... else` before the `for` transforms every item.
def clamp_all(nums, lo, hi):
    raise NotImplementedError
# ==== END


# ==== EX 7.3 | map and filter | Core
# PROMPT: Write `positive_ints(tokens)` that converts string tokens with `map(int, ...)` and keeps positives with `filter`.
# EXAMPLE: `positive_ints(["3", "-1", "0", "8"])` -> `[3, 8]`
# BIGO: O(N). Both return lazy iterators; wrap them in `list` to see the result.
def positive_ints(tokens):
    raise NotImplementedError
# ==== END


# ==== EX 7.4 | any and all | Core
# PROMPT: Write `all_positive(nums)` with `all`, `has_zero(nums)` with `any`, and `has_duplicate(nums)` using `len(set(...))`.
# EXAMPLE: `all_positive([1, 2])` -> `True`; `has_zero([3, 0])` -> `True`; `has_duplicate([1, 2, 1])` -> `True`
# BIGO: O(N); `any` and `all` stop early.
# NOTE: `all([])` is True and `any([])` is False.
def all_positive(nums):
    raise NotImplementedError


def has_zero(nums):
    raise NotImplementedError


def has_duplicate(nums):
    raise NotImplementedError
# ==== END


# ==== EX 7.5 | min and max with a key | Core
# PROMPT: Write `longest_word(words)` (first one wins on ties) and `closest_to_zero(nums)` (prefer the positive on ties), both with `key=`.
# EXAMPLE: `longest_word(["hi", "hello", "howdy"])` -> `"hello"`; `closest_to_zero([-4, 2, -2, 5])` -> `2`
# BIGO: O(N).
def longest_word(words):
    raise NotImplementedError


def closest_to_zero(nums):
    raise NotImplementedError
# ==== END


# ==== EX 7.6 | sorted versus list.sort | Core
# PROMPT: Write `sorted_copy(arr)` that leaves `arr` untouched and `sort_in_place(arr)` that sorts it descending and returns `None`, like `list.sort`.
# EXAMPLE: `a = [3, 1, 2]; sorted_copy(a)` -> `[1, 2, 3]` and `a` is still `[3, 1, 2]`
# BIGO: O(N log N) each. `sorted` needs O(N) extra for the copy.
# NOTE: `arr = arr.sort()` sets arr to None, a classic bug.
def sorted_copy(arr):
    raise NotImplementedError


def sort_in_place(arr):
    raise NotImplementedError
# ==== END


# ==== EX 7.7 | Generator expressions save memory | Core
# PROMPT: Write `sum_of_squares(n)` for 1..n using a generator expression inside `sum(...)` (no list is built).
# EXAMPLE: `sum_of_squares(10)` -> `385`
# BIGO: O(N) time, O(1) memory. The list version needs O(N) memory.
def sum_of_squares(n):
    raise NotImplementedError
# ==== END


# ==== EX 7.8 | Write a generator function | Core
# PROMPT: Write a generator `fib_gen()` that yields Fibonacci numbers forever, and `first_fibs(n)` that takes n of them.
# EXAMPLE: `first_fibs(8)` -> `[0, 1, 1, 2, 3, 5, 8, 13]`
# BIGO: O(1) per value.
def fib_gen():
    raise NotImplementedError


def first_fibs(n):
    raise NotImplementedError
# ==== END


# ==== EX 7.9 | zip for pairs of neighbours | Core
# PROMPT: Write `differences(arr)` returning `arr[i+1] - arr[i]` for each neighbouring pair, using `zip(arr, arr[1:])`.
# EXAMPLE: `differences([1, 4, 9, 16])` -> `[3, 5, 7]`
# BIGO: O(N).
def differences(arr):
    raise NotImplementedError
# ==== END


# ==== EX 7.10 | The walrus operator | Practice
# PROMPT: Write `read_until_blank(lines)` collecting lines (stripped) until the first empty one, using `:=` inside the `while` condition with an iterator.
# EXAMPLE: `read_until_blank(["a", "b", "", "c"])` -> `['a', 'b']`
# BIGO: O(N).
def read_until_blank(lines):
    raise NotImplementedError
# ==== END
