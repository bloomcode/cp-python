from ch05_lists import (chunks, copies, flatten, make_grid, prefix_sums, range_sum, rotate_right, running_max, spiral,
                        transpose, unique_in_order)


def test_ex_5_1():
    g = make_grid(2, 3, 0)
    g[0][0] = 9
    assert g == [[9, 0, 0], [0, 0, 0]]
    bad = [[0] * 3] * 2  # the aliasing bug the exercise avoids
    bad[0][0] = 9
    assert bad == [[9, 0, 0], [9, 0, 0]]


def test_ex_5_2():
    assert transpose([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], [3, 6]]


def test_ex_5_3():
    assert rotate_right([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3] == rotate_right([1, 2, 3, 4, 5], 7)
    assert rotate_right([1, 2], 0) == [1, 2] and rotate_right([], 3) == []


def test_ex_5_4():
    p = prefix_sums([3, 1, 4, 1, 5])
    assert p == [0, 3, 4, 8, 9, 14]
    assert range_sum([0, 3, 4, 8, 9, 14], 1, 3) == 6 and range_sum([0, 3, 4, 8, 9, 14], 0, 4) == 14


def test_ex_5_5():
    assert unique_in_order([3, 1, 3, 2, 1]) == [3, 1, 2]


def test_ex_5_6():
    assert flatten([[1, 2], [3], [], [4, 5]]) == [1, 2, 3, 4, 5]


def test_ex_5_7():
    assert chunks([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5]]


def test_ex_5_8():
    assert running_max([2, 1, 5, 3, 7]) == [2, 2, 5, 5, 7]


def test_ex_5_9():
    grid = [[1, 2], [3, 4]]
    alias, shallow, deep = copies(grid)
    grid[0][0] = 99
    assert alias[0][0] == 99 and shallow[0][0] == 99 and deep[0][0] == 1


def test_ex_5_10():
    assert spiral([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [1, 2, 3, 6, 9, 8, 7, 4, 5]
    assert spiral([[1, 2, 3, 4], [5, 6, 7, 8]]) == [1, 2, 3, 4, 8, 7, 6, 5]
    assert spiral([[1], [2], [3]]) == [1, 2, 3] and spiral([[1, 2, 3]]) == [1, 2, 3]
