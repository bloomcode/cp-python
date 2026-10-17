import pytest
from ch04_control_flow import (calc, collatz_steps, evens_down, first_multiple, fizzbuzz, pyramid, rank_lines,
                               sum_until_negative, times_table)


def test_ex_4_1():
    assert fizzbuzz(5) == ['1', '2', 'Fizz', '4', 'Buzz'] and fizzbuzz(15)[-1] == "FizzBuzz"


def test_ex_4_2():
    assert first_multiple([5, 7, 12, 9], 3) == 2 and first_multiple([5, 7], 3) == -1 and first_multiple([], 3) == -1


def test_ex_4_3():
    assert collatz_steps(6) == 8 and collatz_steps(1) == 0


def test_ex_4_4():
    assert times_table(3) == [[1, 2, 3], [2, 4, 6], [3, 6, 9]]


def test_ex_4_5():
    assert evens_down(7) == [6, 4, 2, 0] and evens_down(6) == [6, 4, 2, 0]


def test_ex_4_6():
    assert rank_lines(["ann", "bo"], [90, 75]) == ['1. ann: 90', '2. bo: 75']


def test_ex_4_7():
    assert pyramid(3) == ['  *', ' ***', '*****']


def test_ex_4_8():
    assert sum_until_negative([4, 0, 3, -1, 10]) == 7 and sum_until_negative([]) == 0


def test_ex_4_9():
    assert calc("*", 6, 7) == 42 and calc("/", 7, 2) == 3 and calc("-", 1, 4) == -3
    with pytest.raises(ValueError):
        calc("^", 1, 2)
