"""https://www.youtube.com/watch?v=Xd760PcgfPg"""


from helper.util import mytime


def while_true(l: list) -> None:
    it = iter(l)
    while True:
        x = next(it)
        print(x)


@mytime
def while_true_catch(l: list) -> None:
    it = iter(l)
    while True:
        try:
            x = next(it)
            print(x)
        except StopIteration:
            break


@mytime
def while_true_catch_main(l: list) -> None:
    it = iter(l)
    while True:
        try:
            x = next(it)
        except StopIteration:
            break
        else:
            print(x)


@mytime
def for_loop(l: list) -> None:
    for x in l:
        print(x)


def main():
    values = [1, 2, 3, 4, 5]
    while_true_catch(values)
    while_true_catch_main(values)
    for_loop(values)


if __name__ == "__main__":
    main()
