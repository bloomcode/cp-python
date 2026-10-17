from ch10_sorting_bisect import (argsort, by_dept_then_age, compress, count_between, first_true, largest_number,
                                 leaderboard, min_speed, sorted_stream)


def test_ex_10_1():
    assert leaderboard([("bo", 80), ("al", 95), ("cy", 80)]) == [('al', 95), ('bo', 80), ('cy', 80)]


def test_ex_10_2():
    assert [p[0] for p in by_dept_then_age([("a", "ops", 40), ("b", "dev", 30), ("c", "ops", 25)])] == ['b', 'c', 'a']


def test_ex_10_3():
    assert largest_number([3, 30, 34, 5, 9]) == "9534330" and largest_number([0, 0]) == "0" and largest_number([10, 2]) == "210"


def test_ex_10_4():
    assert argsort([30, 10, 20]) == [1, 2, 0] and argsort([]) == []


def test_ex_10_5():
    assert count_between([1, 3, 3, 5, 8, 13], 3, 8) == 4 and count_between([1, 2], 5, 9) == 0


def test_ex_10_6():
    assert sorted_stream([5, 2, 8, 1, 9]) == [5, 2, 5, 2, 5]


def test_ex_10_7():
    assert min_speed([3, 6, 7, 11], 8) == 4 and min_speed([30, 11, 23, 4, 20], 5) == 30 and min_speed([30, 11, 23, 4, 20], 6) == 23


def test_ex_10_8():
    assert first_true(0, 100, lambda x: x * x >= 50) == 8 and first_true(0, 5, lambda x: False) == 6


def test_ex_10_9():
    assert compress([100, 5, 100, 42]) == [2, 0, 2, 1]
