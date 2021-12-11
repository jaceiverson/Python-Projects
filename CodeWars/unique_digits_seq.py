"""https://www.codewars.com/kata/599688d0e2800dda4e0001b0/train/python"""

def find_num(n):
    def split_num(num):return [int(x) for x in str(num)]

    seq = [0,1,2,3,4,5,6,7,8,9,10]
    possible_lowest = 11
    
    if n <= 10:
        return n
    
    for x in range(len(seq),n+1):
        # assign each index position
        temp_min = possible_lowest
        while True:
            # get the digits for the last number (to avoid)
            current_nums_to_avoid = split_num(seq[-1])
            # get the digits of the testing number (to check against avoid num)
            current_test_nums = split_num(temp_min)
        
            # check if test_nums are in current nums to avoid
            if not any(x in current_nums_to_avoid for x in current_test_nums) and temp_min not in seq:
                seq.append(temp_min)
                # change the possible lowest value (checking that it isn't in the seq already)
                if temp_min == possible_lowest:
                    while True:
                        possible_lowest += 1
                        if possible_lowest not in seq:
                            break
                break
            else:
                temp_min += 1

    return seq[n]

find_num(11)
find_num(20)
find_num(100)


