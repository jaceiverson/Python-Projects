"""https://twitter.com/willmcgugan/status/1551589075106365440"""
from more_itertools import partition
from helper.util import mytime


@mytime
def partition_will(pred, values):
    if not values:
        return [], []
    if len(values) == 1:
        return ([], values) if pred(values[0]) else (values, [])
    values = sorted(values, key=pred)
    lower = 0
    upper = len(values)
    index = (lower + upper) // 2
    try:
        while index:
            value = pred(values[index])
            if pred(values[index + 1]) and not value:
                index += 1
                return values[:index], values[index:]
            if value:
                upper = index
            else:
                lower = index
            index = (lower + upper) // 2

    except IndexError:
        return values[:], []
    return [], values[:]


@mytime
def partition_docs(pred, values):
    return partition(pred, values)


def main():
    is_odd = lambda x: x % 2 == 1
    will = partition_will(is_odd, range(10))
    docs = partition_docs(is_odd, range(10))
    print(will)
    print(docs)


if __name__ == "__main__":
    main()
