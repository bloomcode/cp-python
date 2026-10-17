"""Chapter 1 - Input and output the contest way.

Judges feed text on standard input and read text from standard output.
Every exercise here takes the input as a string and returns the output as a
string, so it can be tested; 1.8 shows how to wire it to real stdin.
"""
import sys


# ==== EX 1.1 | Read integers from one line | Core
# PROMPT: Write `read_ints(line)` that turns a line such as `"3 -4 10"` into a list of ints, using `split` and `map`.
# EXAMPLE: `read_ints("3 -4 10\n")` -> `[3, -4, 10]`
# BIGO: O(L) for a line of L characters.
# NOTE: `split()` with no argument splits on any run of whitespace and ignores the trailing newline; `split(" ")` does not.
def read_ints(line):
    raise NotImplementedError
# ==== END


# ==== EX 1.2 | N, then N numbers | Core
# PROMPT: Write `read_array(data)`: the first line is N, the second holds N integers. Return the list.
# EXAMPLE: `read_array("4\n5 1 9 2\n")` -> `[5, 1, 9, 2]`
# BIGO: O(N).
def read_array(data):
    raise NotImplementedError
# ==== END


# ==== EX 1.3 | Read a character grid | Core
# PROMPT: Write `read_grid(data)`: the first line is `R C`, then R lines of C characters (`#` and `.`). Return a list of R lists of characters.
# EXAMPLE: `read_grid("2 3\n#.#\n..#\n")` -> `[['#', '.', '#'], ['.', '.', '#']]`
# BIGO: O(R * C).
def read_grid(data):
    raise NotImplementedError
# ==== END


# ==== EX 1.4 | T test cases | Core
# PROMPT: Write `sum_cases(data)`: the first line is T, then T lines of `a b`. Return one line per case with `a + b`.
# EXAMPLE: `sum_cases("3\n1 2\n10 -4\n0 0\n")` -> `"3\n6\n0"`
# BIGO: O(T).
# NOTE: Collect answers in a list and join once at the end; printing inside the loop is much slower in Python.
def sum_cases(data):
    raise NotImplementedError
# ==== END


# ==== EX 1.5 | Print a list on one line | Core
# PROMPT: Write `join_line(values)` that returns the values separated by single spaces, the way most judges expect.
# EXAMPLE: `join_line([3, 1, 2])` -> `"3 1 2"`
# BIGO: O(N).
# NOTE: `print(*values)` does the same on real stdout.
def join_line(values):
    raise NotImplementedError
# ==== END


# ==== EX 1.6 | Format numbers exactly | Core
# PROMPT: Write `fmt(x)` returning a float with exactly 6 decimals, and `fmt_row(name, score)` returning the name left-aligned in 10 characters and the score right-aligned in 5, using f-strings.
# EXAMPLE: `fmt(2/3)` -> `"0.666667"`; `fmt_row("ann", 42)` -> `"ann          42"`
# BIGO: O(1).
def fmt(x):
    raise NotImplementedError


def fmt_row(name, score):
    raise NotImplementedError
# ==== END


# ==== EX 1.7 | Read everything as one token stream | Core
# PROMPT: Write `pairs_from_tokens(data)`: input is N followed by N pairs `x y`, spread over any number of lines. Read all tokens with one `split()` and walk them with an iterator. Return a list of tuples.
# EXAMPLE: `pairs_from_tokens("3\n1 2 3\n4\n5 6")` -> `[(1, 2), (3, 4), (5, 6)]`
# BIGO: O(N).
# NOTE: This style ignores line breaks entirely, which protects you from judges that wrap input unexpectedly.
def pairs_from_tokens(data):
    raise NotImplementedError
# ==== END


# ==== EX 1.8 | The contest template | Core
# PROMPT: Write `solve(data)` for "print the maximum of N numbers" and a `main()` that reads all of `sys.stdin.buffer` at once, calls `solve`, and writes the result. Keep this file as your starting template.
# EXAMPLE: `solve("5\n3 9 -1 4 7")` -> `"9"`
# BIGO: O(N). Reading the whole input in one call is the fastest way to read in Python.
def solve(data):
    raise NotImplementedError


def main():
    raise NotImplementedError


if __name__ == "__main__":
    main()
# ==== END


# ==== EX 1.9 | YES or NO per query | Practice
# PROMPT: Write `even_sum_queries(data)`: first line Q, then Q lines each with a list of ints. Answer `YES` if the line's sum is even, else `NO`.
# EXAMPLE: `even_sum_queries("2\n1 3\n2 5 4")` -> `"YES\nNO"`
# BIGO: O(total numbers).
def even_sum_queries(data):
    raise NotImplementedError
# ==== END
