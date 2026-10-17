import random

from ch16_patterns import (apply_updates, best_window, count_islands, count_subarrays, longest_unique, max_meetings,
                           pair_sum_sorted, robot, solve)


def test_ex_16_1():
    assert pair_sum_sorted([1, 3, 4, 6, 9], 10) == (0, 4) and pair_sum_sorted([1, 2], 10) is None


def test_ex_16_2():
    assert best_window([2, 1, 5, 1, 3, 2], 3) == 9


def test_ex_16_3():
    assert longest_unique("abcabcbb") == 3 and longest_unique("pwwkew") == 3 and longest_unique("") == 0 and longest_unique("abba") == 2


def test_ex_16_4():
    assert count_subarrays([1, 1, 1], 2) == 2 and count_subarrays([1, 2, 3, -3, 3], 3) == 5
    rng = random.Random(1)
    for _ in range(50):
        a = [rng.randint(-3, 3) for _ in range(12)]
        k = rng.randint(-3, 3)
        assert count_subarrays(a, k) == sum(1 for i in range(12) for j in range(i, 12) if sum(a[i:j + 1]) == k)


def test_ex_16_5():
    assert count_islands(["##..", "#..#", "...#"]) == 2 and count_islands(["...", "..."]) == 0


def test_ex_16_6():
    assert robot("UURDL") == (0, 1) and robot("") == (0, 0)


def test_ex_16_7():
    assert apply_updates(5, [(1, 3, 2), (2, 4, 3), (0, 2, -1)]) == [-1, 1, 4, 5, 3]


def test_ex_16_8():
    assert max_meetings([(1, 3), (2, 4), (3, 5), (0, 7), (5, 8)]) == 3


def test_ex_16_9():
    assert solve("2\n5\n-2 1 -3 4 -1\n3\n-5 -1 -8") == "4\n-1"
