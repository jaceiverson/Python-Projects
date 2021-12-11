"""
https://www.codewars.com/kata/52423db9add6f6fc39000354/train/python

Given a 2D array and a number of generations, compute n timesteps of Conway's Game of Life.

The rules of the game are:

Any live cell with fewer than two live neighbours dies, as if caused by underpopulation.
Any live cell with more than three live neighbours dies, as if by overcrowding.
Any live cell with two or three live neighbours lives on to the next generation.
Any dead cell with exactly three live neighbours becomes a live cell.
Each cell's neighborhood is the 8 cells immediately around it (i.e. Moore Neighborhood). The universe is infinite in both the x and y dimensions and all cells are initially dead - except for those specified in the arguments. The return value should be a 2d array cropped around all of the living cells. (If there are no living cells, then return [[]].)

For illustration purposes, 0 and 1 will be represented as ░░ and ▓▓ blocks respectively (PHP, C: plain black and white squares). You can take advantage of the htmlize function to get a text representation of the universe, e.g.:

print(htmlize(cells))
"""

def htmlize(array):
    s = []
    for row in array:
        for cell in row:
            s.append('▓▓' if cell else '░░')
        s.append('<:LF:>')
    return ''.join(s)
    
def get_generation(cells, generations):
    # create the next generation
    next_generation = [[] for x in range(len(cells))]
    
    # how many generations, iterate through them
    for iterations in range(generations):
        for rindex,row in enumerate(cells):
            for cindex,column in enumerate(row):
                # print(cells)
                neighbors = 0
                # count neighbors
                for n_rows in [-1,0,1]:
                    for n_cols in [-1,0,1]:
                        if not (n_rows == 0 and n_cols == 0):
                            # we don't need to count itself
                            try:
                                # x,y are coordinates of cell
                                x = rindex + n_rows
                                y = cindex + n_cols
                                if x >= 0 and y >= 0:
                                    # because of negative indexing, make sure 
                                    # index is >= 0
                                    # add value of cell to neighbors
                                    neighbors += cells[x][y]
                                    # print(x,y,neighbors)
                            except IndexError:
                                # print('error')
                                pass
                        
                print(f"{rindex= },{cindex= },alive:{bool(cells[rindex][cindex])},n:{neighbors}")
                #print(cells)
                # check currently alive cells
                if cells[rindex][cindex] == 1:
                    if neighbors < 2 or neighbors > 3:
                        # death conditions
                        next_generation[rindex].insert(cindex, 0)
                    else:
                        # stay alive conditions
                        next_generation[rindex].insert(cindex,1)
                # check currently dead cells
                elif cells[rindex][cindex] == 0:
                    if neighbors == 3:
                        next_generation[rindex].insert(cindex, 1)
                    else:
                        # stay dead conditions
                        next_generation[rindex].insert(cindex,0)
                
    return next_generation


start = [[1,0,0],
         [0,1,1],
         [1,1,0]]


end   = [[0,1,0],
         [0,0,1],
         [1,1,1]]

resp = get_generation(start, 1)

print("START")
print(htmlize(start))
print("MY RESULT")
print(htmlize(resp))
print("EXPECTED")
print(htmlize(end))