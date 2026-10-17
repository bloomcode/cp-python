from ch06_tuples_sets_dicts import (busiest_cell, compare, group_by_first, head_tail, invert, merge_counts, min_max,
                                    pairs_with_sum, remainders, squares_map, top_words, word_counts)


def test_ex_6_1():
    assert min_max([4, 1, 9]) == (1, 9) and head_tail([4, 1, 9]) == (4, [1, 9])


def test_ex_6_2():
    assert compare([1, 2, 3, 4], [3, 4, 5]) == ([3, 4], [1, 2], [1, 2, 5])


def test_ex_6_3():
    assert word_counts("To be or not to be") == {'to': 2, 'be': 2, 'or': 1, 'not': 1}


def test_ex_6_4():
    assert invert({'a': 1, 'b': 2}) == {1: 'a', 2: 'b'}


def test_ex_6_5():
    assert group_by_first(["apple", "bat", "avocado"]) == {'a': ['apple', 'avocado'], 'b': ['bat']}


def test_ex_6_6():
    assert top_words({'b': 2, 'a': 2, 'c': 5}, 2) == ['c', 'a']


def test_ex_6_7():
    assert busiest_cell([(1, 2), (0, 0), (1, 2), (0, 0), (3, 3)]) == (0, 0)


def test_ex_6_8():
    assert pairs_with_sum([1, 5, 3, 3, 2, 4], 6) == {(1, 5), (3, 3), (2, 4)}
    assert pairs_with_sum([3], 6) == set()


def test_ex_6_9():
    assert squares_map(3) == {1: 1, 2: 4, 3: 9} and remainders([5, 7, 9, 10], 3) == {0, 1, 2}


def test_ex_6_10():
    a, b = {'x': 1, 'y': 2}, {'y': 5, 'z': 1}
    assert merge_counts(a, b) == {'x': 1, 'y': 7, 'z': 1} and a == {'x': 1, 'y': 2}
