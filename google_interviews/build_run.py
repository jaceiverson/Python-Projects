"""
build runs

we would like to get the longest consecutive list (of lists)
that the ratio of True:False is strictly decreasing

https://www.youtube.com/watch?v=rw4s4M3hFfs&t=2380s
"""
from helper.util import mytime


build = [
    [True, True, True, False, False],
    [True, True, True, True, False],
    [True, True, True, True, True, True, False, False, False],
    [True, False, False, False, False, False],
    [True, True, True, True, True, True, True, True, True, True, True, True, False],
    [True, False],
    [True, True, True, True, False, False],
]


def get_build_percent(line_item: list) -> float:
    return sum(line_item) / len(line_item) if line_item else 0


@mytime
def process_builds(build: list) -> list:
    """
    this is my original solution after just hearing the problem
    it is good and gets the right answer but it was a little slow
    """
    # temporary output variables for storing the current longest list/idx list
    output = [build[0]]
    output_idx = [0]
    # the true longest list/idx for our build
    max_build = output
    max_idx = output_idx
    for idx, item in enumerate(build[1:], 1):
        # if the % in output is bigger, we will add the current value to the list and idx list
        if get_build_percent(output[-1]) > get_build_percent(item):
            output.append(item)
            output_idx.append(idx)
            # if the output list is larger than the max_build list, we set the max_build to that value
            if len(output) > len(max_build):
                max_build = output
                max_idx = output_idx
        # if the output is smaller, this means we increased in build %,
        # reset values and continue loop
        else:
            output = [item]
            output_idx = [idx]

    return max_build, max_idx


@mytime
def process_builds_by_index(builds: list) -> list:
    """
    after watching a little bit further I liked her idea to use pointers
    this would save some time (because I wouldn't be appending to a list
    the logic is the same, but I am just keeping track of the index instead of creating lists

    results appear to be half the time (way quicker) than my oririnal solution
    """
    temp_left, temp_right, max_left, max_right = 0, 0, 0, 0
    for idx, item in enumerate(builds[1:], 1):
        if get_build_percent(builds[idx - 1]) > get_build_percent(item):
            # if I am in here, this means there is a decreasing value
            temp_right = idx
            if max_right - max_left < temp_right - temp_left:
                max_left, max_right = temp_left, temp_right
        else:
            temp_left, temp_right = idx, idx

    return builds[max_left : max_right + 1], list(range(max_left, max_right + 1))


def output(elements, start=0):
    for idx, e in enumerate(elements, start):
        print(f"{idx:<2}: {get_build_percent(e)*100:.2f}%")


def main():
    bad_strech, bad_strech_idx = process_builds(build)
    output(bad_strech, bad_strech_idx[0])

    b, bi = process_builds_by_index(build)
    output(b, bi[0])


if __name__ == "__main__":
    main()
