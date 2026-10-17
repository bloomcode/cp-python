import random

from ch11_collections_heapq import (LRUCache, build_graph, grid_distance, k_smallest, last_k_average, last_stone, pop_all,
                                    process_order, running_median, same_letters, top_chars)


def test_ex_11_1():
    assert top_chars("mississippi", 2) == [('i', 4), ('s', 4)] and same_letters("dusty", "study") and not same_letters("ab", "abb")


def test_ex_11_2():
    assert dict(build_graph([(1, 2), (2, 3)])) == {1: [2], 2: [1, 3], 3: [2]}


def test_ex_11_3():
    assert grid_distance(["..#", ".#.", "..."], (0, 0), (1, 2)) == 5
    assert grid_distance([".#.", "##.", "..."], (0, 0), (2, 2)) == -1


def test_ex_11_4():
    assert last_k_average([1, 10, 3, 5], 3) == [1.0, 5.5, 14 / 3, 6.0]


def test_ex_11_5():
    assert k_smallest([7, 2, 9, 1, 5], 2) == [1, 2] and pop_all([3, 1, 2]) == [1, 2, 3]


def test_ex_11_6():
    assert last_stone([2, 7, 4, 1, 8, 1]) == 1 and last_stone([2, 2]) == 0


def test_ex_11_7():
    assert process_order([(2, 0, "b"), (1, 1, "a"), (2, 2, "c")]) == ['a', 'b', 'c']


def test_ex_11_8():
    c = LRUCache(2)
    c.put(1, 1)
    c.put(2, 2)
    assert c.get(1) == 1
    c.put(3, 3)
    assert c.get(2) == -1 and c.get(3) == 3 and c.get(1) == 1


def test_ex_11_9():
    assert running_median([5, 15, 1, 3]) == [5, 10.0, 5, 4.0]
    rng = random.Random(1)
    data = [rng.randint(0, 50) for _ in range(40)]
    for i, m in enumerate(running_median(data)):
        s = sorted(data[:i + 1])
        n = len(s)
        assert m == (s[n // 2] if n % 2 else (s[n // 2 - 1] + s[n // 2]) / 2)
