from ch13_bits import (all_subsets, can_make, clear_bit, from_bits, get_bit, highest_bit_index, is_power_of_two, lonely,
                       lowest_bit, popcount_loop, popcount_str, set_bit, to_bits, toggle_bit)


def test_ex_13_1():
    x = 0b1010
    assert get_bit(x, 1) == 1 and get_bit(x, 0) == 0
    assert set_bit(x, 0) == 11 and clear_bit(x, 3) == 2 and toggle_bit(x, 2) == 14


def test_ex_13_2():
    assert popcount_loop(0b101101) == 4 == popcount_str(0b101101) and (255).bit_count() == 8
    for v in range(300):
        assert popcount_loop(v) == bin(v).count("1") == popcount_str(v)


def test_ex_13_3():
    assert is_power_of_two(64) and not is_power_of_two(96) and not is_power_of_two(0)


def test_ex_13_4():
    assert all_subsets(['a', 'b']) == [[], ['a'], ['b'], ['a', 'b']] and len(all_subsets(list(range(5)))) == 32


def test_ex_13_5():
    assert lonely([4, 1, 2, 1, 2]) == 4


def test_ex_13_6():
    assert lowest_bit(12) == 4 and highest_bit_index(12) == 3


def test_ex_13_7():
    assert to_bits(5, 8) == "00000101" and from_bits("1101") == 13


def test_ex_13_8():
    assert can_make([3, 34, 4, 12, 5, 2], 9) and not can_make([3, 34, 4], 30)
