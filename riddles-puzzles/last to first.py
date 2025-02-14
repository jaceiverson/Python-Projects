# https://www.youtube.com/watch?v=1lHDCAIsyb8&
from helper.util import avgtime, mytime


def flipNumber(num):
    if len(num) == 1:
        return num
    else:
        value = num.pop()
        num.insert(0, value)
        return num


@avgtime()
def brute_force():
    """
    I made the logic using numbers 1-100, then after I found the solution
    I put in the numbers to run faster
    """
    for x in range(105263157894736000, 105263157894737000):
        num = [int(i) for i in str(x)]
        value = flipNumber(num)
        value = int("".join(str(e) for e in value))
        if value == x * 2:
            # print(
            #     f"You have found the answer. {x:,} \nwhen last becomes first is double: {value:,}"
            # )
            return x, value


@avgtime()
def better_solution():
    # its all relative still not an efficient way to search to
    # 105 quadrillion
    for x in range(105263157894736000, 105263157894737000):
        fliped_x = int(str(x)[-1] + str(x)[:-1])
        if fliped_x == x * 2:
            return x, fliped_x


# answer is 105263157894736842
if __name__ == "__main__":
    brute_force()
    better_solution()
