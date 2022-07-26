# Generate number of '#' given an input
# input 3 -> "###"
from helper.util import mytime


@mytime
def multiply(n):
    return "#" * n


@mytime
def join(n):
    return "".join(["#" for _ in range(n)])


@mytime
def loop(n):
    s = ""
    for _ in range(n):
        s += "#"
    return s


def main():
    number = 10
    multiply(number)
    join(number)
    loop(number)


if __name__ == "__main__":
    main()
