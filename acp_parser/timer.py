import time
from si_prefix import si_format


def time_it(fn, *args, n=1, fn_output=1, **kwargs):
    """Takes a function and times how long time it takes to execute.

    Args:
        fn (function): A funtion to execute.
        n (int, optional): Number of times to execute. Defaults to 1.
        print_output (int, optional): Prints the time SI-formatted.
        *args: positional arguments of the function.
        **kwargs: keyword arguments of the function.

    Returns:
        (xreturn, float): Returns a tuple consisting of two parts:
            1. The return value of the executed function.
            2. The average time it to execute the function fn n times.
    """
    start = time.perf_counter()
    for i in range(n):
        xreturn = fn(*args, **kwargs)
    end = time.perf_counter()

    if fn_output:
        print(f"Timing function {fn.__name__}: {si_format((end - start) / n)}")

    return xreturn if fn_output else (xreturn, (end - start) / n)
