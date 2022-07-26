"""
While I won't be solving this problem, I thought it
was a good exercise in recursion.

The basic premise is that if you take any starting number and apply the 
following rules:

Odd Numbers: 3n + 1
Even Numbers: n/2

The conjecture goes that the number will eventually reach a loop

4 -> 2 -> 1 -> 4 -> 2 -> 1 ...

This isn't proven for all numbers, but we will be working with small numbers anyway
Video: https://www.youtube.com/watch?v=094y1Z2wpJg

Turns out that recursion isn't the way that Copilot wanted to do this, 
but rather use a generator.
"""
from helper.util import mytime, avgtime

N = 10


def collatz(n, array: list = None):
    """my recursive solution"""
    if array is None:
        array = [n]
    n = n // 2 if n % 2 == 0 else 3 * n + 1
    array.append(n)
    if n == 1:
        return array
    return collatz(n, array)


def collatz_sequence(n):
    """copilot's generator solution"""
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        yield n
    return 1


def main():
    seq = [N] + list(collatz_sequence(N))
    print("->".join(str(x) for x in seq))


def main2():
    seq = collatz(N)
    print("->".join(str(x) for x in seq))


if __name__ == "__main__":
    avgtime(main)(run_times=10)
    avgtime(main2)(run_times=10)
