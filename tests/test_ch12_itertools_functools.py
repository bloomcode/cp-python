from ch12_itertools_functools import (closest_subset_sum, dice_sum_counts, first_n_primes, gcd_of, interleave,
                                      k_subsets_with_sum, merge_all, numbers_from_digits, prefix, product_of,
                                      running_best, runs)


def test_ex_12_1():
    assert numbers_from_digits([1, 2, 1]) == [112, 121, 211]


def test_ex_12_2():
    assert k_subsets_with_sum([1, 2, 3, 4, 5], 2, 6) == [(1, 5), (2, 4)]


def test_ex_12_3():
    assert dice_sum_counts(2)[7] == 6 and sum(dice_sum_counts(3).values()) == 216


def test_ex_12_4():
    assert prefix([3, 1, 4]) == [0, 3, 4, 8] and running_best([2, 1, 5, 3]) == [2, 2, 5, 5]


def test_ex_12_5():
    assert runs("aaabccdddd") == [('a', 3), ('b', 1), ('c', 2), ('d', 4)] and runs("") == []


def test_ex_12_6():
    assert merge_all([[1], [2, 3], []]) == [1, 2, 3] and interleave([1, 3], [2, 4]) == [1, 2, 3, 4]


def test_ex_12_7():
    assert product_of([2, 3, 7]) == 42 and product_of([]) == 1 and gcd_of([12, 18, 30]) == 6


def test_ex_12_8():
    assert first_n_primes(6) == [2, 3, 5, 7, 11, 13]


def test_ex_12_9():
    assert closest_subset_sum([8, 3, 5, 11], 15) == 14 and closest_subset_sum([8, 3, 5, 11], 16) == 16
