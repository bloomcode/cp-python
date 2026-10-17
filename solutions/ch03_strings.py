"""Chapter 3 - Strings."""


# ==== EX 3.1 | Reverse with a slice | Core
# PROMPT: Write `reverse(s)` in one expression using a slice with a negative step.
# EXAMPLE: `reverse("python")` -> `"nohtyp"`
# BIGO: O(N); the slice builds a new string.
def reverse(s):
    raise NotImplementedError
# ==== END


# ==== EX 3.2 | Palindrome, ignoring case and spaces | Core
# PROMPT: Write `is_palindrome(s)` that keeps only letters and digits, lower-cases them, and compares with the reverse.
# EXAMPLE: `is_palindrome("Never odd or even")` -> `True`
# BIGO: O(N) time, O(N) space for the cleaned copy.
def is_palindrome(s):
    raise NotImplementedError
# ==== END


# ==== EX 3.3 | Count characters by hand | Core
# PROMPT: Write `char_counts(s)` returning a dict of character to count, using `dict.get` (no `Counter` yet).
# EXAMPLE: `char_counts("banana")` -> `{'b': 1, 'a': 3, 'n': 2}`
# BIGO: O(N).
def char_counts(s):
    raise NotImplementedError
# ==== END


# ==== EX 3.4 | Caesar shift with ord and chr | Core
# PROMPT: Write `caesar(s, k)` shifting lowercase letters by k places (wrapping z to a) and leaving everything else alone.
# EXAMPLE: `caesar("xyz abc", 3)` -> `"abc def"`
# BIGO: O(N).
# NOTE: `ord('a')` is 97. Map a letter to 0-25 with `ord(ch) - 97`, shift with `% 26`, then add 97 back.
def caesar(s, k):
    raise NotImplementedError
# ==== END


# ==== EX 3.5 | Count vowels | Core
# PROMPT: Write `count_vowels(s)` (a, e, i, o, u, either case) using a generator expression and a set.
# EXAMPLE: `count_vowels("Competitive")` -> `5`
# BIGO: O(N); set membership is O(1).
def count_vowels(s):
    raise NotImplementedError
# ==== END


# ==== EX 3.6 | Reverse the word order | Core
# PROMPT: Write `reverse_words(sentence)` that reverses the order of words and collapses extra spaces.
# EXAMPLE: `reverse_words("  the sky   is blue ")` -> `"blue is sky the"`
# BIGO: O(N).
def reverse_words(sentence):
    raise NotImplementedError
# ==== END


# ==== EX 3.7 | Build strings with join, not += | Core
# PROMPT: Write `numbers_csv(n)` returning `"1,2,...,n"`. Build a list and `join` it once; then explain why `s += str(i)` in a loop can be quadratic.
# EXAMPLE: `numbers_csv(5)` -> `"1,2,3,4,5"`
# BIGO: O(N) with join. Strings are immutable, so repeated `+=` may copy the whole string each time.
def numbers_csv(n):
    raise NotImplementedError
# ==== END


# ==== EX 3.8 | Anagram check by sorting | Core
# PROMPT: Write `is_anagram(a, b)` using `sorted`.
# EXAMPLE: `is_anagram("listen", "silent")` -> `True`
# BIGO: O(N log N). A count dict brings it to O(N) (see 11.1).
def is_anagram(a, b):
    raise NotImplementedError
# ==== END


# ==== EX 3.9 | Run-length encoding | Practice
# PROMPT: Write `rle(s)` turning runs of the same character into the character and its count.
# EXAMPLE: `rle("aaabccdddd")` -> `"a3b1c2d4"`; `rle("")` -> `""`
# BIGO: O(N).
def rle(s):
    raise NotImplementedError
# ==== END


# ==== EX 3.10 | Every position of a substring | Practice
# PROMPT: Write `find_all(s, sub)` returning every start index of `sub` in `s`, overlaps included, by calling `s.find(sub, start)` in a loop.
# EXAMPLE: `find_all("abababa", "aba")` -> `[0, 2, 4]`
# BIGO: O(N * M) worst case for the built-in search, usually much faster.
def find_all(s, sub):
    raise NotImplementedError
# ==== END
