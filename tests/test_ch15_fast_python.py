from ch15_fast_python import (answer_range_sums, big_sum, count_at_most, count_hits, fits, josephus, reachable,
                              squares_output)


def test_ex_15_1():
    assert fits(10**5, "nlogn") and not fits(10**5, "n2") and fits(20, "2n") and not fits(30, "2n") and fits(10**18, "logn")


def test_ex_15_2():
    assert count_hits([1, 5, 9], [9, 8, 1]) == 2


def test_ex_15_3():
    assert answer_range_sums([3, 1, 4, 1, 5], [(0, 2), (1, 4)]) == [8, 11]


def test_ex_15_4():
    assert josephus(7, 3) == [3, 6, 2, 7, 5, 1, 4] and josephus(1, 5) == [1]


def test_ex_15_5():
    assert count_at_most([5, 1, 9, 3], [0, 4, 10]) == [0, 2, 4]


def test_ex_15_6():
    assert big_sum("3\n10 20\n30") == 60


def test_ex_15_7():
    assert squares_output(3) == "1\n4\n9"


def test_ex_15_8():
    assert reachable({1: [2], 2: [3], 3: [], 4: [1]}, 1) == {1, 2, 3}
    chain = {i: [i + 1] for i in range(200000)}
    assert len(reachable(chain, 0)) == 200001
