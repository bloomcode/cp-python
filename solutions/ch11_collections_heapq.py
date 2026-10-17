"""Chapter 11 - collections and heapq."""
import heapq
from collections import Counter, OrderedDict, defaultdict, deque


# ==== EX 11.1 | Counter | Core
# PROMPT: Write `top_chars(s, k)` with `Counter.most_common`, and `same_letters(a, b)` comparing two Counters.
# EXAMPLE: `top_chars("mississippi", 2)` -> `[('i', 4), ('s', 4)]`; `same_letters("dusty", "study")` -> `True`
# BIGO: O(N) to count; `most_common(k)` is O(N log k).
# NOTE: Ties in `most_common` keep first-seen order: 'i' appears before 's' in "mississippi".
def top_chars(s, k):
    raise NotImplementedError


def same_letters(a, b):
    raise NotImplementedError
# ==== END


# ==== EX 11.2 | defaultdict for adjacency lists | Core
# PROMPT: Write `build_graph(edges)` returning a `defaultdict(list)` adjacency list for undirected edges `(u, v)`.
# EXAMPLE: `build_graph([(1, 2), (2, 3)])` -> `{1: [2], 2: [1, 3], 3: [2]}`
# BIGO: O(E).
def build_graph(edges):
    raise NotImplementedError
# ==== END


# ==== EX 11.3 | deque for breadth-first search | Core
# PROMPT: Write `grid_distance(grid, start, end)` returning the fewest moves (up, down, left, right) from start to end through `.` cells, or -1. Use a `deque` as the queue.
# EXAMPLE: `grid_distance(["..#", ".#.", "..."], (0, 0), (1, 2))` -> `5`
# BIGO: O(R * C). A list with `pop(0)` would make this O((R * C)^2).
def grid_distance(grid, start, end):
    raise NotImplementedError
# ==== END


# ==== EX 11.4 | deque with maxlen | Core
# PROMPT: Write `last_k_average(stream, k)` returning the average of the latest k values after each new value, using `deque(maxlen=k)` and a running sum.
# EXAMPLE: `last_k_average([1, 10, 3, 5], 3)` -> `[1.0, 5.5, 4.666666666666667, 6.0]`
# BIGO: O(1) per value.
def last_k_average(stream, k):
    raise NotImplementedError
# ==== END


# ==== EX 11.5 | heapq basics | Core
# PROMPT: Write `k_smallest(nums, k)` with `heapq.nsmallest`, and `pop_all(nums)` that heapifies a copy and pops every item in order.
# EXAMPLE: `k_smallest([7, 2, 9, 1, 5], 2)` -> `[1, 2]`; `pop_all([3, 1, 2])` -> `[1, 2, 3]`
# BIGO: heapify O(N); each push or pop O(log N).
def k_smallest(nums, k):
    raise NotImplementedError


def pop_all(nums):
    raise NotImplementedError
# ==== END


# ==== EX 11.6 | Max-heap by negation | Core
# PROMPT: Write `last_stone(stones)`: repeatedly smash the two heaviest stones; if they differ, put back the difference. Return the last weight or 0. `heapq` is a min-heap, so store negatives.
# EXAMPLE: `last_stone([2, 7, 4, 1, 8, 1])` -> `1`
# BIGO: O(N log N).
def last_stone(stones):
    raise NotImplementedError
# ==== END


# ==== EX 11.7 | Heap of tuples | Core
# PROMPT: Write `process_order(jobs)` for `(priority, arrival, name)` tuples: return names in the order a min-heap releases them (lowest priority number first, then earliest arrival).
# EXAMPLE: `process_order([(2, 0, "b"), (1, 1, "a"), (2, 2, "c")])` -> `['a', 'b', 'c']`
# BIGO: O(N log N).
# NOTE: Tuples compare item by item, so put a unique tie-breaker before anything that cannot be compared.
def process_order(jobs):
    raise NotImplementedError
# ==== END


# ==== EX 11.8 | LRU cache with OrderedDict | Practice
# PROMPT: Write `LRUCache(capacity)` with `get(key)` (returns -1 if missing) and `put(key, value)`, evicting the least recently used key. Use `move_to_end` and `popitem(last=False)`.
# EXAMPLE: capacity 2: put(1,1), put(2,2), get(1) -> `1`, put(3,3) evicts 2, get(2) -> `-1`
# BIGO: O(1) per operation.
class LRUCache:
    def __init__(self, capacity):
        raise NotImplementedError

    def get(self, key):
        raise NotImplementedError

    def put(self, key, value):
        raise NotImplementedError
# ==== END


# ==== EX 11.9 | Running median with two heaps | Stretch
# PROMPT: Write `running_median(stream)`: keep a max-heap of the lower half and a min-heap of the upper half, and return the median after each value (average the two middles for even counts).
# EXAMPLE: `running_median([5, 15, 1, 3])` -> `[5, 10.0, 5, 4.0]`
# BIGO: O(log N) per value, compared with O(N) per value for 10.6.
def running_median(stream):
    raise NotImplementedError
# ==== END
