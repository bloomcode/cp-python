"""Chapter 18: Files and Streams."""
import csv
import re


# ==== EX 18.1 | Sum the numbers in a file | Core
# PROMPT: Write `sum_file(path)` that returns the sum of the integers in a text file, one per line, skipping blank lines. Open it with `with open(path) as f` and iterate over `f`, which yields one line at a time.
# EXAMPLE: a file holding `3\n\n-1\n10\n` -> `12`
# BIGO: O(size of the file) time, O(1) extra space when read line by line.
def sum_file(path):
    raise NotImplementedError
# ==== END


# ==== EX 18.2 | Most common words in a file | Core
# PROMPT: A word is a run of letters, compared in lower case. Write `top_words(path, k)` that returns the `k` most common words in a file as `(word, count)` pairs, most frequent first and ties in alphabetical order. Count with a dictionary (or `collections.Counter`), then sort by `(-count, word)`.
# EXAMPLE: `The cat and the hat.\nThe end, and THE start!\n`, `2` -> `[('the', 4), ('and', 2)]`
# BIGO: O(size + W log W) for W distinct words: one pass to count, one sort.
def top_words(path, k):
    raise NotImplementedError
# ==== END


# ==== EX 18.3 | Write a report | Core
# PROMPT: Write `write_report(path, scores)` that writes one line `name,score` per entry of the dictionary `scores`, highest score first and ties by name, replacing any existing file, and returns how many lines it wrote. Open with mode `"w"` and write each line with `\n`.
# EXAMPLE: `{'ana': 7, 'bo': 9, 'cy': 7}` -> writes `bo,9\nana,7\ncy,7\n` and returns `3`
# BIGO: O(N log N) for the sort, O(N) to write.
def write_report(path, scores):
    raise NotImplementedError
# ==== END


# ==== EX 18.4 | Stream a large file | Practice
# PROMPT: Write `longest_line(path)` that returns the length of the longest line in a file (not counting the newline), holding only one line in memory at a time: iterate over the open file, never call `read()` or `readlines()`.
# EXAMPLE: a file with lines `ab`, `abcd`, `` -> `4`
# BIGO: O(size) time and O(longest line) memory: only one line is ever held, however big the file is.
def longest_line(path):
    raise NotImplementedError
# ==== END


# ==== EX 18.5 | Copy matching lines to another file | Practice
# PROMPT: Write `copy_matching(source, target, needle)` that writes every line of `source` containing `needle` to `target` (in order, newlines kept) and returns how many it wrote. Open both files in one `with` statement and stream from one to the other.
# EXAMPLE: lines `error: disk`, `ok`, `error: net` with needle `error` -> writes the two error lines, returns `2`
# BIGO: O(size of the input) time, O(longest line) memory: both files are streamed.
def copy_matching(source, target, needle):
    raise NotImplementedError
# ==== END


# ==== EX 18.6 | Averages from a CSV file | Practice
# PROMPT: A CSV file has the header `team,points` and one row per game. Write `average_by_team(path)` that returns a dictionary from team to its average points (a float). Read the rows with `csv.DictReader` (open the file with `newline=""`) and keep a total and a count per team.
# EXAMPLE: rows `red,10`, `blue,4`, `red,7` -> `{'red': 8.5, 'blue': 4.0}`
# BIGO: O(size of the file) time, O(T) space for T teams: keep a running total and count per team.
def average_by_team(path):
    raise NotImplementedError
# ==== END
