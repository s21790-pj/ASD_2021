import time


def time_measure(func, arr, p=None, r=None):
    if isinstance(p, int) and isinstance(r, int):
        start = time.perf_counter()
        func(arr, p, r)
        end = time.perf_counter()
        result = end - start
    else:
        start = time.perf_counter()
        func(arr)
        end = time.perf_counter()
        result = end - start
    return start, end, result




