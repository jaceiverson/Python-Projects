"""
https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1/train/python

Snail Sort
Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
snail(array) #=> [1,2,3,6,9,8,7,4,5]
For better understanding, please follow the numbers of the next array consecutively:

array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
snail(array) #=> [1,2,3,4,5,6,7,8,9]

NOTE: The idea is not sort the elements from the lowest value to the highest; the idea is to traverse the 2-d array in a clockwise snailshell pattern.

NOTE 2: The 0x0 (empty matrix) is represented as en empty array inside an array [[]].

"""

def snail(snail_map):
    # set up my return list
    snail_values = []
    
    while snail_map:
        try:
            # first row is added as is then removed
            [snail_values.append(x) for x in snail_map.pop(0)]

            # all right values are added then removed
            [snail_values.append(x.pop()) for x in snail_map]

            # bottom row is added reversed then removed
            [snail_values.append(x) for x in snail_map.pop()[::-1]]

            # all left values are added (reverse order -> going up) then removed
            [snail_values.append(x.pop(0)) for x in snail_map[::-1]]
            
        except IndexError:
            return snail_values
    
    return snail_values

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
expected = [1,2,3,6,9,8,7,4,5]
test.assert_equals(snail(array), expected)


array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
expected = [1,2,3,4,5,6,7,8,9]
test.assert_equals(snail(array), expected)

