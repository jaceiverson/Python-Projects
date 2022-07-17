from time import perf_counter_ns


def mytime(func):
    def wrapper(*args, **kwargs):
        start = perf_counter_ns()
        result = func(*args, **kwargs)
        end = perf_counter_ns()
        print(f"{func.__name__:>10} : {end-start:>10} ns")
        return result

    return wrapper
