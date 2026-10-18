"""Chapter 19: Concurrency."""
import queue
import threading
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ThreadPoolExecutor, TimeoutError


# ==== EX 19.1 | Start workers and wait for all | Core
# PROMPT: Write `parallel_squares(nums)` that starts one `threading.Thread` per number, each storing its number's square in its own slot of a results list, then `join`s every thread before returning the list.
# EXAMPLE: `[1, 2, 3]` -> `[1, 4, 9]`
# BIGO: O(N) work spread over N threads; each writes only its own slot, so no lock is needed.
def parallel_squares(nums):
    raise NotImplementedError
# ==== END


# ==== EX 19.2 | A producer and a consumer | Core
# PROMPT: Write `pipeline_total(nums)` with two threads joined by a `queue.Queue`: a producer thread puts each number and then `None` to say it is finished, while a consumer thread takes items until it sees `None`, adding them up. Return the consumer's total after joining both.
# EXAMPLE: `[4, 5, 6]` -> `15`
# BIGO: O(N): every value passes through the queue once; the queue does the locking and the waiting.
def pipeline_total(nums):
    raise NotImplementedError
# ==== END


# ==== EX 19.3 | A pool with a fixed number of workers | Practice
# PROMPT: Write `pool_map(fn, items, workers)` that applies `fn` to every item using at most `workers` threads at a time and returns the results in input order. Use a `ThreadPoolExecutor(max_workers=workers)` in a `with` block and its `map`.
# EXAMPLE: `lambda x: x * 10, [1, 2, 3], 2` -> `[10, 20, 30]`
# BIGO: About ceil(N / W) rounds of work for W workers; the results keep the input order however the work finishes.
def pool_map(fn, items, workers):
    raise NotImplementedError
# ==== END


# ==== EX 19.4 | A counter protected by a lock | Core
# PROMPT: Write `locked_count(threads, increments)` that starts `threads` threads, each adding 1 to a shared counter `increments` times, and returns the final count. Guard every update with one `threading.Lock` (`with lock:`), because `count += 1` is a read, an add and a write that two threads can interleave.
# EXAMPLE: `4, 1000` -> `4000`
# BIGO: O(T * K) increments; the lock makes each read-modify-write happen as one step, so none is lost.
def locked_count(threads, increments):
    raise NotImplementedError
# ==== END


# ==== EX 19.5 | Stop waiting after a timeout | Practice
# PROMPT: Write `result_within(task, seconds)` that runs `task()` on a worker thread and returns `(True, result)` if it finishes within `seconds`, or `(False, None)` otherwise, without waiting for a slow task to end. Submit it to a `ThreadPoolExecutor`, call `future.result(timeout=seconds)`, and `shutdown(wait=False)`.
# EXAMPLE: `lambda: 42, 1.0` -> `(True, 42)`; a task that sleeps 0.3 s with `0.05` -> `(False, None)`
# BIGO: Waits at most the timeout, however long the task takes.
def result_within(task, seconds):
    raise NotImplementedError
# ==== END


# ==== EX 19.6 | Split a sum across workers | Practice
# PROMPT: Write `parallel_sum(nums, workers)` that cuts `nums` into `workers` contiguous chunks of near-equal size, sums each chunk on its own thread (a `ThreadPoolExecutor`), and adds the partial sums.
# EXAMPLE: `list(range(1, 101)), 4` -> `5050`
# BIGO: O(N / W) per worker for W workers, then O(W) to combine; each worker owns one slot of the partial results.
# NOTE: In CPython, threads take turns running Python code (the GIL), so this shows the pattern rather than a speed-up; use processes for CPU-heavy work.
def parallel_sum(nums, workers):
    raise NotImplementedError
# ==== END
