from ch08_functions import (add_item, apply_n, average, by_second, compose, depth_sum, depth_sum_iter, describe, grid_paths,
                            make_counter, memoize, power, ways)


def test_ex_8_1():
    assert power(5) == 25 and power(2, 10) == 1024 and power(exp=3, base=2) == 8


def test_ex_8_2():
    assert add_item(1) == [1] and add_item(2) == [2] and add_item(3, [0]) == [0, 3]


def test_ex_8_3():
    assert average(2, 4, 9) == 5.0 and describe(b=2, a=1) == "a=1, b=2"


def test_ex_8_4():
    assert by_second([(1, 'b'), (2, 'a'), (0, 'b')]) == [(2, 'a'), (0, 'b'), (1, 'b')]


def test_ex_8_5():
    c = make_counter()
    assert (c(), c(), c()) == (1, 2, 3)
    d = make_counter()
    assert d() == 1


def test_ex_8_6():
    assert ways(10) == 89 and ways(80) == 37889062373143906
    calls = []

    @memoize
    def square(x):
        calls.append(x)
        return x * x

    assert [square(3), square(3), square(4)] == [9, 9, 16] and calls == [3, 4]


def test_ex_8_7():
    assert grid_paths(3, 3) == 6 and grid_paths(16, 16) == 155117520


def test_ex_8_8():
    assert depth_sum(1000) == 500500 == depth_sum_iter(1000) and depth_sum_iter(100000) == 5000050000


def test_ex_8_9():
    assert compose(str, abs)(-5) == "5" and apply_n(lambda v: v * 2, 10, 1) == 1024
