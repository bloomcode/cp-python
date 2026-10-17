from ch07_comprehensions_builtins import (all_positive, clamp_all, closest_to_zero, differences, even_squares, first_fibs,
                                          has_duplicate, has_zero, longest_word, positive_ints, read_until_blank,
                                          sort_in_place, sorted_copy, sum_of_squares)


def test_ex_7_1():
    assert even_squares([1, 2, 3, 4]) == [4, 16]


def test_ex_7_2():
    assert clamp_all([-5, 3, 12], 0, 10) == [0, 3, 10]


def test_ex_7_3():
    assert positive_ints(["3", "-1", "0", "8"]) == [3, 8]


def test_ex_7_4():
    assert all_positive([1, 2]) and has_zero([3, 0]) and has_duplicate([1, 2, 1])
    assert all_positive([]) and not has_zero([]) and not has_duplicate([1, 2])


def test_ex_7_5():
    assert longest_word(["hi", "hello", "howdy"]) == "hello"
    assert closest_to_zero([-4, 2, -2, 5]) == 2 and closest_to_zero([-1, 3]) == -1


def test_ex_7_6():
    a = [3, 1, 2]
    assert sorted_copy(a) == [1, 2, 3] and a == [3, 1, 2]
    assert sort_in_place(a) is None and a == [3, 2, 1]


def test_ex_7_7():
    assert sum_of_squares(10) == 385


def test_ex_7_8():
    assert first_fibs(8) == [0, 1, 1, 2, 3, 5, 8, 13]


def test_ex_7_9():
    assert differences([1, 4, 9, 16]) == [3, 5, 7]


def test_ex_7_10():
    assert read_until_blank(["a", "b", "", "c"]) == ['a', 'b'] and read_until_blank(["x"]) == ['x']
