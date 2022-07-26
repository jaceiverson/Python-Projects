"""
https://www.youtube.com/watch?v=4tYoVx0QoN0&list=TLPQMjAwNzIwMjIr98-3uLMk6A&index=2
Given a matrix 2D list in python
remove all the island pixels from it. 
an island pixel is 1+ cells  (elements) that is no connected (touching other 1's) to the border
connections are only horizontal and vertical

0 -> white
1 -> black

"""


from copy import deepcopy
import itertools


def output(matrix):
    for row in matrix:
        print(row)


def is_border(matrix, row, col):
    return row == 0 or row == len(matrix) or col == 0 or col == len(matrix[0])


def is_island(matrix, row, col):
    matrix = deepcopy(matrix)
    try:
        for r, c in itertools.product(range(-1, 2), range(-1, 2)):
            if abs(r) != abs(c):
                if col + c < 0 or col + c > len(matrix[row]) - 1:
                    return False
                neighbor = matrix[row + r][col + c]
                if neighbor == 1:
                    matrix[row][col] = 0
                    is_island(matrix, row + r, col + c)
        return True
    except IndexError:
        return False


def remove_islands(matrix):
    for r_idx, row in enumerate(matrix[1:-1], 1):
        for c_idx, col in enumerate(row[1:-1], 1):
            # if the value is a 0, we can just continue
            if col == 0:
                continue

            if is_island(matrix, r_idx, c_idx):
                matrix[r_idx][c_idx] = 0

    return matrix


def compare_matrixes(m1, m2):
    difference = deepcopy(m1)
    for r_idx, row in enumerate(m1):
        for c_idx, col in enumerate(row):
            if col == m2[r_idx][c_idx]:
                difference[r_idx][c_idx] = ""

    return difference


def main():
    starting_input = [
        [1, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 1, 1],
        [0, 0, 1, 0, 1, 0],
        [1, 1, 0, 0, 1, 0],
        [1, 0, 1, 1, 0, 0],
        [1, 0, 0, 0, 0, 1],
    ]
    my_output = remove_islands(deepcopy(starting_input))

    comparison = compare_matrixes(starting_input, my_output)

    # output(starting_input)
    # output(my_output)
    # output(comparison)

    expected_output = [
        [1, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 1],
        [0, 0, 0, 0, 1, 0],
        [1, 1, 0, 0, 1, 0],
        [1, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 1],
    ]
    assert my_output == expected_output


if __name__ == "__main__":
    main()
