"""testing sum time"""
from helper.util import mytime


@mytime
def s(n):
    return sum(n)


@mytime
def s1(n):
    i = 0
    for n_ in n:
        i += n_
    return i


def main():

    nums = list(range(100))
    s(nums)
    s1(nums)


if __name__ == "__main__":
    main()
