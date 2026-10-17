"""Chapter 9 - Classes and objects, just enough for contests."""
import math
from collections import namedtuple
from dataclasses import dataclass, field


# ==== EX 9.1 | A Point class | Core
# PROMPT: Write `Point(x, y)` with `__init__`, a `__repr__` that prints `Point(1, 2)`, and `dist(other)` returning the Euclidean distance.
# EXAMPLE: `Point(0, 0).dist(Point(3, 4))` -> `5.0`; `repr(Point(1, 2))` -> `"Point(1, 2)"`
# BIGO: O(1).
class Point:
    def __init__(self, x, y):
        raise NotImplementedError

    def __repr__(self):
        raise NotImplementedError

    def dist(self, other):
        raise NotImplementedError
# ==== END

    # ==== EX 9.2 | Equality and hashing | Core | class=Point
    # PROMPT: Add `__eq__` and `__hash__` to `Point` so equal points compare equal and collapse to one entry in a set.
    # EXAMPLE: `len({Point(1, 2), Point(1, 2), Point(0, 0)})` -> `2`
    # BIGO: O(1).
    # NOTE: Defining `__eq__` alone makes a class unhashable; hash the same fields you compare.
    def __eq__(self, other):
        raise NotImplementedError

    def __hash__(self):
        raise NotImplementedError
    # ==== END


# ==== EX 9.3 | Ordering with __lt__ | Core
# PROMPT: Write `Task(priority, name)` with `__lt__` comparing priority, then name, so a list of tasks can be sorted and pushed onto a heap.
# EXAMPLE: `sorted([Task(2, "b"), Task(1, "z"), Task(2, "a")])` names -> `['z', 'a', 'b']`
# BIGO: O(1) per comparison.
class Task:
    def __init__(self, priority, name):
        raise NotImplementedError

    def __lt__(self, other):
        raise NotImplementedError
# ==== END


# ==== EX 9.4 | dataclasses | Core
# PROMPT: Rewrite `Task` as `@dataclass(order=True)` named `Job` with fields `priority: int` and `name: str`, plus a `tags` list that is excluded from comparisons and defaults to empty.
# EXAMPLE: `Job(1, "x") < Job(2, "a")` -> `True`; `Job(1, "x").tags` -> `[]`
# BIGO: O(1).
# NOTE: Use `field(default_factory=list)` for mutable defaults, for the same reason as 8.2.
class Job:
    pass
# ==== END


# ==== EX 9.5 | namedtuple for records | Core
# PROMPT: Define `Edge = namedtuple("Edge", "u v w")` and write `lightest_edges(edges, k)` returning the k lightest edges sorted by weight.
# EXAMPLE: `lightest_edges([Edge(1, 2, 7), Edge(2, 3, 1), Edge(1, 3, 4)], 2)` -> `[Edge(u=2, v=3, w=1), Edge(u=1, v=3, w=4)]`
# BIGO: O(E log E).
Edge = namedtuple("Edge", "u v w")


def lightest_edges(edges, k):
    raise NotImplementedError
# ==== END


# ==== EX 9.6 | Properties | Core
# PROMPT: Write `Rect(w, h)` with an `area` property (no parentheses when read) and a `scale(f)` method that returns a new `Rect`.
# EXAMPLE: `Rect(3, 4).area` -> `12`; `Rect(3, 4).scale(2).area` -> `48`
# BIGO: O(1).
class Rect:
    def __init__(self, w, h):
        raise NotImplementedError

    @property
    def area(self):
        raise NotImplementedError

    def scale(self, f):
        raise NotImplementedError
# ==== END


# ==== EX 9.7 | Inheritance and polymorphism | Core
# PROMPT: Write a base `Shape` with `area()` raising `NotImplementedError`, and subclasses `Circle(r)` and `Square(s)`. Write `total_area(shapes)`.
# EXAMPLE: `round(total_area([Circle(1), Square(2)]), 4)` -> `7.1416`
# BIGO: O(N).
class Shape:
    def area(self):
        raise NotImplementedError


class Circle(Shape):
    def __init__(self, r):
        raise NotImplementedError

    def area(self):
        raise NotImplementedError


class Square(Shape):
    def __init__(self, s):
        raise NotImplementedError

    def area(self):
        raise NotImplementedError


def total_area(shapes):
    raise NotImplementedError
# ==== END


# ==== EX 9.8 | A container class | Practice
# PROMPT: Write `Bag` holding items in a list with `add(x)`, `__len__`, `__contains__` and `__iter__` (yielding items in insertion order), so `len`, `in` and `for` work on it.
# EXAMPLE: `b = Bag(); b.add(3); b.add(5)` -> `len(b)` is `2`, `5 in b` is `True`, `list(b)` is `[3, 5]`
# BIGO: `add` and `len` O(1); `in` O(N).
class Bag:
    def __init__(self):
        raise NotImplementedError

    def add(self, x):
        raise NotImplementedError

    def __len__(self):
        raise NotImplementedError

    def __contains__(self, x):
        raise NotImplementedError

    def __iter__(self):
        raise NotImplementedError
# ==== END
