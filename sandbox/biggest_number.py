"""
Given a number, return the largest number by rearranging the digits.

Solved by github copilot
"""


def biggest_number(n):
    return int("".join(sorted(str(n), reverse=True)))


assert biggest_number(123) == 321
