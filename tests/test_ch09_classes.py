import heapq

import pytest
from ch09_classes import Bag, Circle, Edge, Job, Point, Rect, Shape, Square, Task, lightest_edges, total_area


def test_ex_9_1():
    assert Point(0, 0).dist(Point(3, 4)) == 5.0 and repr(Point(1, 2)) == "Point(1, 2)"


def test_ex_9_2():
    assert Point(1, 2) == Point(1, 2) and Point(1, 2) != Point(2, 1) and Point(1, 2) != (1, 2)
    assert len({Point(1, 2), Point(1, 2), Point(0, 0)}) == 2


def test_ex_9_3():
    assert [t.name for t in sorted([Task(2, "b"), Task(1, "z"), Task(2, "a")])] == ['z', 'a', 'b']
    h = [Task(3, "c"), Task(1, "a")]
    heapq.heapify(h)
    assert heapq.heappop(h).name == "a"


def test_ex_9_4():
    assert Job(1, "x") < Job(2, "a") and Job(1, "x").tags == [] and Job(1, "x", ["t"]) == Job(1, "x", ["u"])
    j1, j2 = Job(1, "x"), Job(1, "y")
    j1.tags.append("t")
    assert j2.tags == []


def test_ex_9_5():
    assert lightest_edges([Edge(1, 2, 7), Edge(2, 3, 1), Edge(1, 3, 4)], 2) == [Edge(2, 3, 1), Edge(1, 3, 4)]


def test_ex_9_6():
    assert Rect(3, 4).area == 12 and Rect(3, 4).scale(2).area == 48


def test_ex_9_7():
    assert round(total_area([Circle(1), Square(2)]), 4) == 7.1416 and total_area([]) == 0
    with pytest.raises(NotImplementedError):
        Shape().area()


def test_ex_9_8():
    b = Bag()
    b.add(3)
    b.add(5)
    assert len(b) == 2 and 5 in b and 4 not in b and list(b) == [3, 5]
