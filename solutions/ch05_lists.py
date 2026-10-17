"""Chapter 5 - Lists."""
import copy


# ==== EX 5.1 | A 2D grid without the aliasing bug | Core
# PROMPT: Write `make_grid(r, c, fill)` returning r independent rows. Then show what goes wrong with `[[fill] * c] * r` when you change one cell.
# EXAMPLE: `g = make_grid(2, 3, 0); g[0][0] = 9` -> `[[9, 0, 0], [0, 0, 0]]`
# BIGO: O(R * C).
# NOTE: `[[0] * c] * r` repeats one inner list r times, so writing `g[0][0]` changes every row.
def make_grid(r, c, fill):
    raise NotImplementedError
# ==== END


# ==== EX 5.2 | Transpose a matrix | Core
# PROMPT: Write `transpose(m)` with `zip(*m)`, returning a list of lists.
# EXAMPLE: `transpose([[1, 2, 3], [4, 5, 6]])` -> `[[1, 4], [2, 5], [3, 6]]`
# BIGO: O(R * C).
def transpose(m):
    raise NotImplementedError
# ==== END


# ==== EX 5.3 | Rotate by k with slicing | Core
# PROMPT: Write `rotate_right(arr, k)` returning a new list rotated right by k places (k may exceed the length).
# EXAMPLE: `rotate_right([1, 2, 3, 4, 5], 2)` -> `[4, 5, 1, 2, 3]`; `k = 7` gives the same result
# BIGO: O(N).
def rotate_right(arr, k):
    raise NotImplementedError
# ==== END


# ==== EX 5.4 | Prefix sums and range queries | Core
# PROMPT: Write `prefix_sums(arr)` returning a list p of length N + 1 with p[0] = 0, and `range_sum(p, l, r)` returning the sum of arr[l..r] inclusive in O(1).
# EXAMPLE: `p = prefix_sums([3, 1, 4, 1, 5])` -> `[0, 3, 4, 8, 9, 14]`; `range_sum(p, 1, 3)` -> `6`
# BIGO: O(N) to build, O(1) per query. The single most used trick in contest problems.
def prefix_sums(arr):
    raise NotImplementedError


def range_sum(p, l, r):
    raise NotImplementedError
# ==== END


# ==== EX 5.5 | Remove duplicates, keep order | Core
# PROMPT: Write `unique_in_order(arr)` keeping the first occurrence of each value.
# EXAMPLE: `unique_in_order([3, 1, 3, 2, 1])` -> `[3, 1, 2]`
# BIGO: O(N) with a seen set. `list(dict.fromkeys(arr))` is a one-line alternative.
def unique_in_order(arr):
    raise NotImplementedError
# ==== END


# ==== EX 5.6 | Flatten one level | Core
# PROMPT: Write `flatten(rows)` with a single nested list comprehension.
# EXAMPLE: `flatten([[1, 2], [3], [], [4, 5]])` -> `[1, 2, 3, 4, 5]`
# BIGO: O(total items).
# NOTE: Read the comprehension left to right like the loops it replaces: `for row in rows` comes first, then `for x in row`.
def flatten(rows):
    raise NotImplementedError
# ==== END


# ==== EX 5.7 | Split into chunks | Core
# PROMPT: Write `chunks(arr, k)` returning consecutive pieces of size k (the last may be shorter), using `range` with a step.
# EXAMPLE: `chunks([1, 2, 3, 4, 5], 2)` -> `[[1, 2], [3, 4], [5]]`
# BIGO: O(N).
def chunks(arr, k):
    raise NotImplementedError
# ==== END


# ==== EX 5.8 | Running maximum | Core
# PROMPT: Write `running_max(arr)` where element i is the largest value among arr[0..i].
# EXAMPLE: `running_max([2, 1, 5, 3, 7])` -> `[2, 2, 5, 5, 7]`
# BIGO: O(N).
def running_max(arr):
    raise NotImplementedError
# ==== END


# ==== EX 5.9 | Copies: alias, shallow, deep | Core
# PROMPT: Write `copies(grid)` returning `(alias, shallow, deep)` made with `=`, `grid[:]` and `copy.deepcopy`. Then change `grid[0][0]` and record which of the three change with it.
# EXAMPLE: After `grid[0][0] = 99`: alias and shallow show 99, deep does not
# BIGO: Alias O(1), shallow O(R), deep O(R * C).
# NOTE: For a 2D list, `[row[:] for row in grid]` is the fast deep-enough copy contest code usually wants.
def copies(grid):
    raise NotImplementedError
# ==== END


# ==== EX 5.10 | Spiral order | Stretch
# PROMPT: Write `spiral(m)` returning a matrix's values in clockwise spiral order, starting top-left.
# EXAMPLE: `spiral([[1, 2, 3], [4, 5, 6], [7, 8, 9]])` -> `[1, 2, 3, 6, 9, 8, 7, 4, 5]`
# BIGO: O(R * C).
def spiral(m):
    raise NotImplementedError
# ==== END
