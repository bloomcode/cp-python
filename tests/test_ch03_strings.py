from ch03_strings import (caesar, char_counts, count_vowels, find_all, is_anagram, is_palindrome, numbers_csv, reverse,
                          reverse_words, rle)


def test_ex_3_1():
    assert reverse("python") == "nohtyp" and reverse("") == ""


def test_ex_3_2():
    assert is_palindrome("Never odd or even") and not is_palindrome("abc")


def test_ex_3_3():
    assert char_counts("banana") == {'b': 1, 'a': 3, 'n': 2} and char_counts("") == {}


def test_ex_3_4():
    assert caesar("xyz abc", 3) == "abc def" and caesar(caesar("hello", 5), 21) == "hello"


def test_ex_3_5():
    assert count_vowels("Competitive") == 5


def test_ex_3_6():
    assert reverse_words("  the sky   is blue ") == "blue is sky the"


def test_ex_3_7():
    assert numbers_csv(5) == "1,2,3,4,5"


def test_ex_3_8():
    assert is_anagram("listen", "silent") and not is_anagram("ab", "abb")


def test_ex_3_9():
    assert rle("aaabccdddd") == "a3b1c2d4" and rle("") == ""


def test_ex_3_10():
    assert find_all("abababa", "aba") == [0, 2, 4] and find_all("abc", "z") == []
