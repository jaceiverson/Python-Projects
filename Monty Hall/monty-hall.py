import random

def monty_hall(switch=True):
    # set up doors
    # 0 will represent goats, and 1 will represent a car
    doors = [0,0,0]

    # randomly choose one to contain the "car"
    # because the index of lists starts with 0, we want either index 0,1,or2
    doors[random.randint(0,2)] = 1

    # randomly choose one to be the "user selection"
    # because the index of lists starts with 0, we want either index 0,1,or2
    user_value = doors[random.randint(0,2)]

    # the host removes a "goat" and therefore your switch option is the opposite
    # of whatever you selected first
    switch_option = 1 if user_value==0 else 0

    # if you choose to switch, assign "user_value" to the "switch_option" value
    if switch:
        user_value = switch_option

    # return user_value (1 for win, 0 for loss)
    return user_value

def main(iterations = 1000):
    # keep track of the num of wins (starting at 0) for both options
    # keep vs switch
    keep = 0
    switch = 0

    # loop through assigned the number of iterations
    for x in range(iterations):
        keep += monty_hall(False)
        switch += monty_hall()

    # print the results
    print("Likelihood of winning given that you:")
    print(f"KEEP {keep / iterations} VS SWITCH {switch / iterations}")

if __name__ == '__main__':
    main()
