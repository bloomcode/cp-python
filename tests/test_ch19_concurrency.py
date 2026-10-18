import time
import threading
from ch19_concurrency import locked_count, parallel_squares, parallel_sum, pipeline_total, pool_map, result_within


def test_ex_19_1():
    assert parallel_squares([1, 2, 3]) == [1, 4, 9] and parallel_squares([]) == [] and parallel_squares(list(range(50))) == [i * i for i in range(50)]


def test_ex_19_2():
    assert pipeline_total([4, 5, 6]) == 15 and pipeline_total([]) == 0 and pipeline_total(list(range(10_000))) == 49_995_000


def test_ex_19_3():
    assert pool_map(lambda x: x * 10, [1, 2, 3], 2) == [10, 20, 30] and pool_map(str, [], 3) == []
    lock, active, peak = threading.Lock(), [0], [0]

    def slow(x):
        with lock:
            active[0] += 1
            peak[0] = max(peak[0], active[0])
        time.sleep(0.01)
        with lock:
            active[0] -= 1
        return -x

    assert pool_map(slow, list(range(12)), 3) == [-x for x in range(12)] and 1 <= peak[0] <= 3


def test_ex_19_4():
    assert locked_count(4, 1000) == 4000 and locked_count(1, 0) == 0 and locked_count(8, 2500) == 20_000


def test_ex_19_5():
    assert result_within(lambda: 42, 1.0) == (True, 42)
    start = time.monotonic()
    assert result_within(lambda: time.sleep(0.3), 0.05) == (False, None) and time.monotonic() - start < 0.25


def test_ex_19_6():
    assert parallel_sum(list(range(1, 101)), 4) == 5050 and parallel_sum([], 3) == 0 and parallel_sum([5], 8) == 5
    assert parallel_sum(list(range(1000)), 7) == 499_500
