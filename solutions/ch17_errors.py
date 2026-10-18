"""Chapter 17: Errors."""


# ==== EX 17.1 | Parse or report an error | Core
# PROMPT: Write `parse_port(text)` that returns the port number in `text` (spaces around it allowed). Raise `ValueError` with the message `not a number: 'text'` when it is not an integer, and `out of range: N` when it is outside 1 to 65535. Re-raise with `from None` so the caller sees your message, not the parser's.
# EXAMPLE: `parse_port(' 8080 ')` -> `8080`; `parse_port('http')` raises `ValueError("not a number: 'http'")`
# BIGO: O(L) for a string of length L.
def parse_port(text):
    raise NotImplementedError
# ==== END


# ==== EX 17.2 | A custom error type | Core
# PROMPT: Create `InsufficientFunds(needed, available)`, an `Exception` subclass that keeps both numbers as attributes and reads `needed N, available M`. Write `withdraw(balance, amount)` that returns the new balance, or raises `InsufficientFunds` when `amount` is more than `balance`. Callers can then catch this one failure and read its fields.
# EXAMPLE: `withdraw(100, 30)` -> `70`; `withdraw(20, 50)` raises `InsufficientFunds` with `needed == 50`, `available == 20`
# BIGO: O(1).
class InsufficientFunds(Exception):
    def __init__(self, needed, available):
        raise NotImplementedError


def withdraw(balance, amount):
    raise NotImplementedError
# ==== END


# ==== EX 17.3 | Wrap an error with context | Practice
# PROMPT: Create `ConfigError(Exception)`. Write `number_setting(settings, key)` that returns `int(settings[key])`, but turns a missing key (`KeyError`) or a bad number (`ValueError`) into `ConfigError("setting 'key'")` raised `from` the original, so the message says where and `__cause__` says why.
# EXAMPLE: `number_setting({'port': '80'}, 'port')` -> `80`; `number_setting({}, 'port')` raises `ConfigError` whose `__cause__` is a `KeyError`
# BIGO: O(L) to parse the value.
class ConfigError:
    pass


def number_setting(settings, key):
    raise NotImplementedError
# ==== END


# ==== EX 17.4 | Cleanup that always runs | Core
# PROMPT: Write `run_steps(steps, log)` that appends `"start"` to `log`, calls each function in `steps`, and appends `"done"` however that ends, even when a step raises (the exception still reaches the caller). Use `try` / `finally`.
# EXAMPLE: two steps that log `a` and `b` -> `log == ['start', 'a', 'b', 'done']`
# BIGO: O(S) for S steps.
def run_steps(steps, log):
    raise NotImplementedError
# ==== END


# ==== EX 17.5 | Close resources in reverse order | Practice
# PROMPT: Create `Tracked(name, log)`, a context manager whose `__enter__` appends `open name` and whose `__exit__` appends `close name` (and does not swallow exceptions). Write `use_two(log, fail)` that opens `a` then `b` in one `with` statement, appends `work`, and raises `RuntimeError` when `fail` is true. Both close, in reverse order, either way.
# EXAMPLE: `use_two(log, False)` -> `log == ['open a', 'open b', 'work', 'close b', 'close a']`
# BIGO: O(1).
class Tracked:
    def __init__(self, name, log):
        raise NotImplementedError

    def __enter__(self):
        raise NotImplementedError

    def __exit__(self, *exc):
        raise NotImplementedError


def use_two(log, fail):
    raise NotImplementedError
# ==== END


# ==== EX 17.6 | Collect every error instead of stopping | Practice
# PROMPT: Write `parse_ages(rows)` that parses each row as an age from 0 to 150 and returns `(values, problems)`: the good ages in order, and for each bad row a message `row N: not a number: text` or `row N: out of range: A` (rows count from 1, spaces trimmed). A helper raises `ValueError` for one row; the loop catches it and carries on.
# EXAMPLE: `['34', 'x', '200', ' 7 ']` -> `([34, 7], ['row 2: not a number: x', 'row 3: out of range: 200'])`
# BIGO: O(total length of the rows).
def parse_ages(rows):
    raise NotImplementedError
# ==== END
