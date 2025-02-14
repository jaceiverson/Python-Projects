"""
In this puzzle we need to solve for the values of x,y,z
where x,y,z are integers 0-9 but when combined make a 3 digit number

the problem is as such

      {x}{y}{z}
    + {x}{y}{z}
    + {x}{y}{z}
    ------------
      {y}{y}{y}

in words: xyz added three times should be equal to yyy
"""

import itertools

from helper.util import avgtime


def try_it(x: int, y: int, z: int):
    return (100 * x + 10 * y + z) * 3


def deductions():
    # what we know
    # z > 4 (need to have a carryover)
    # z!=5 (need to be unique)
    # y > 0
    # x < 3 because if x=3 y=9 and 9+9+9 !=9?

    # z*3%10 = y
    # y111 = 300x+30y+3z
    # y81 = 300x+3z
    # y27 = 100x+z
    #
    # cases
    # z=0, y=0, x=0 BAD need to be unique
    # z=1, y=3, BAD y*3!=y
    # z=2, y=6 BAD y*6!=y
    # z=3 BAD
    # z=4, y=2 BAD
    # z=5 BAD unique
    # z=6, y=8
    pass


def get_total_from_z(z: int) -> int:
    # old function
    y_2 = (z * 3) % 10  # y from z
    co_2 = (z * 3) // 10  # carry over from z (pos 2)
    y_1 = ((y_2 * 3) + co_2) % 10  # y from what z said y was
    co_1 = (y_2 * 3) // 10  # carry over from y (pos 1)
    x = (y_1 - co_1) / 3
    y_0 = (x * 3) + co_2  # y_0 just equals
    return int(f"{y_0}{y_1}{y_2}")


def get_y_from_z(z: int) -> int:
    return (z * 3) % 10, (z * 3) // 10


def get_x_from_y(y: int, z_carry_over: int) -> int:
    carry_over_from_y = ((y * 3) + z_carry_over) // 10
    return int((y - carry_over_from_y) / 3)


def get_numbers(z: int) -> int:
    y, carry_over = get_y_from_z(z)
    x = get_x_from_y(y, carry_over)
    return int(f"{x}{y}{z}")


def if_z_then_y_ok(z: int) -> bool:
    """checks the values of z to see what could be possible"""
    y_from_z = (z * 3) % 10
    carry_over_1 = (z * 3) // 10
    y_from_y = ((y_from_z * 3) + carry_over_1) % 10
    if y_from_z == y_from_y and z != y_from_z:
        return z


@avgtime(100)
def brute_force():
    for x in range(10):
        for y in range(10):
            for z in range(10):
                if z != y != x and try_it(x, y, z) == 100 * y + 10 * y + y:
                    # return x, y, z
                    return int(f"{x}{y}{z}")


@avgtime(100)
def brute_force_itertools():
    for x, y, z in itertools.product(range(10), range(10), range(10)):
        if z != y != x and try_it(x, y, z) == 100 * y + 10 * y + y:
            # return x, y, z
            return int(f"{x}{y}{z}")


@avgtime(100)
def one_loop():
    for x in range(10):
        if maybe_z := if_z_then_y_ok(x):
            return get_numbers(maybe_z)


@avgtime(100)
def one_loop_no_name_expression():
    for x in range(10):
        maybe_z = if_z_then_y_ok(x)
        if maybe_z:
            return get_numbers(maybe_z)


if __name__ == "__main__":
    brute_force()
    brute_force_itertools()
    one_loop()
    one_loop_no_name_expression()
