from ch01_io import even_sum_queries, fmt, fmt_row, join_line, pairs_from_tokens, read_array, read_grid, read_ints, solve, sum_cases


def test_ex_1_1():
    assert read_ints("3 -4 10\n") == [3, -4, 10] and read_ints("7") == [7]


def test_ex_1_2():
    assert read_array("4\n5 1 9 2\n") == [5, 1, 9, 2]


def test_ex_1_3():
    assert read_grid("2 3\n#.#\n..#\n") == [['#', '.', '#'], ['.', '.', '#']]


def test_ex_1_4():
    assert sum_cases("3\n1 2\n10 -4\n0 0\n") == "3\n6\n0"


def test_ex_1_5():
    assert join_line([3, 1, 2]) == "3 1 2" and join_line([]) == ""


def test_ex_1_6():
    assert fmt(2 / 3) == "0.666667" and fmt_row("ann", 42) == "ann          42"


def test_ex_1_7():
    assert pairs_from_tokens("3\n1 2 3\n4\n5 6") == [(1, 2), (3, 4), (5, 6)]


def test_ex_1_8():
    assert solve("5\n3 9 -1 4 7") == "9"


def test_ex_1_9():
    assert even_sum_queries("2\n1 3\n2 5 4") == "YES\nNO"
