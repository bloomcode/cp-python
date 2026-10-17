"""Chapter 6 - Tuples, sets and dictionaries."""


# ==== EX 6.1 | Tuples and unpacking | Core
# PROMPT: Write `min_max(arr)` returning a tuple, then `head_tail(arr)` using star unpacking (`first, *rest = arr`). Also swap two variables without a temporary.
# EXAMPLE: `min_max([4, 1, 9])` -> `(1, 9)`; `head_tail([4, 1, 9])` -> `(4, [1, 9])`
# BIGO: O(N).
def min_max(arr):
    raise NotImplementedError


def head_tail(arr):
    raise NotImplementedError
# ==== END


# ==== EX 6.2 | Set operations | Core
# PROMPT: Write `compare(a, b)` returning `(common, only_a, either_not_both)` as sorted lists, using `&`, `-` and `^`.
# EXAMPLE: `compare([1, 2, 3, 4], [3, 4, 5])` -> `([3, 4], [1, 2], [1, 2, 5])`
# BIGO: O(N + M).
def compare(a, b):
    raise NotImplementedError
# ==== END


# ==== EX 6.3 | Count with a dict | Core
# PROMPT: Write `word_counts(text)` returning a dict of lowercase word to count, using `d[w] = d.get(w, 0) + 1`.
# EXAMPLE: `word_counts("To be or not to be")` -> `{'to': 2, 'be': 2, 'or': 1, 'not': 1}`
# BIGO: O(N) words.
def word_counts(text):
    raise NotImplementedError
# ==== END


# ==== EX 6.4 | Invert a dictionary | Core
# PROMPT: Write `invert(d)` that swaps keys and values, assuming values are unique, with a dict comprehension.
# EXAMPLE: `invert({'a': 1, 'b': 2})` -> `{1: 'a', 2: 'b'}`
# BIGO: O(N).
def invert(d):
    raise NotImplementedError
# ==== END


# ==== EX 6.5 | Group with setdefault | Core
# PROMPT: Write `group_by_first(words)` mapping each first letter to the list of words that start with it, using `setdefault`.
# EXAMPLE: `group_by_first(["apple", "bat", "avocado"])` -> `{'a': ['apple', 'avocado'], 'b': ['bat']}`
# BIGO: O(N).
def group_by_first(words):
    raise NotImplementedError
# ==== END


# ==== EX 6.6 | Sort a dict by value, then key | Core
# PROMPT: Write `top_words(counts, k)` returning the k most frequent words, ties broken alphabetically, using `sorted(counts.items(), key=...)`.
# EXAMPLE: `top_words({'b': 2, 'a': 2, 'c': 5}, 2)` -> `['c', 'a']`
# BIGO: O(N log N).
# NOTE: A tuple key `(-count, word)` sorts by count descending and word ascending in one pass.
def top_words(counts, k):
    raise NotImplementedError
# ==== END


# ==== EX 6.7 | Tuples as dict keys | Core
# PROMPT: Write `busiest_cell(points)` returning the `(x, y)` that appears most often in a list of points, using tuples as dictionary keys. Break ties by the smallest point.
# EXAMPLE: `busiest_cell([(1, 2), (0, 0), (1, 2), (0, 0), (3, 3)])` -> `(0, 0)`
# BIGO: O(N).
# NOTE: Lists cannot be dict keys or set members because they are mutable; tuples can.
def busiest_cell(points):
    raise NotImplementedError
# ==== END


# ==== EX 6.8 | Unique pairs with a target sum | Practice
# PROMPT: Write `pairs_with_sum(nums, target)` returning the set of unordered pairs `(small, large)` that add to target.
# EXAMPLE: `pairs_with_sum([1, 5, 3, 3, 2, 4], 6)` -> `{(1, 5), (3, 3), (2, 4)}`
# BIGO: O(N).
def pairs_with_sum(nums, target):
    raise NotImplementedError
# ==== END


# ==== EX 6.9 | Dict and set comprehensions | Core
# PROMPT: Write `squares_map(n)` returning `{i: i*i}` for 1..n, and `remainders(nums, k)` returning the set of distinct `x % k`.
# EXAMPLE: `squares_map(3)` -> `{1: 1, 2: 4, 3: 9}`; `remainders([5, 7, 9, 10], 3)` -> `{0, 1, 2}`
# BIGO: O(N).
def squares_map(n):
    raise NotImplementedError


def remainders(nums, k):
    raise NotImplementedError
# ==== END


# ==== EX 6.10 | Merge two count dicts | Practice
# PROMPT: Write `merge_counts(a, b)` returning a new dict where shared keys add their values. Do not modify the inputs.
# EXAMPLE: `merge_counts({'x': 1, 'y': 2}, {'y': 5, 'z': 1})` -> `{'x': 1, 'y': 7, 'z': 1}`
# BIGO: O(N + M).
# NOTE: `a | b` (Python 3.9) merges too, but the right side wins on shared keys instead of adding.
def merge_counts(a, b):
    raise NotImplementedError
# ==== END
