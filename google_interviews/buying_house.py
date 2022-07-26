"""
https://www.youtube.com/watch?v=rw4s4M3hFfs

Pretty happy with my solution here. Took me about 30 minutes to solve. 
It is not the most optimal, but it works.

How could I make it better?

Don't do brute force. 
 - Right now I am calulating the distance from each block to each building
"""

blocks = [
    {"gym": False, "school": True, "store": False},
    {"gym": True, "school": False, "store": False},
    {"gym": True, "school": True, "store": False},
    {"gym": False, "school": True, "store": False},
    {"gym": False, "school": True, "store": True},
]

my_requirements = ["gym", "school", "store"]


def find_distance(building: str) -> list:
    """finds the distance (int) from each block to the passed in building

    Args:
        building (str): name of a building on a block

    Returns:
        list: ints of distance to closest building on the block
    """
    distance = [len(blocks) for _ in blocks]
    for idx, block in enumerate(blocks):
        for idx_2, block_2 in enumerate(blocks):
            if block_2[building]:
                distance[idx] = min(distance[idx], abs(idx_2 - idx))
    return distance


def find_best_place(requirements: list) -> tuple:
    """
    given your list of requirements finds the best block to live.
    Minimizing distance walked to our required buildings
    Ties in total distance were broken by selecting the lowest maxium walking distance:
    --example--
    (0,1,1) would be better than (2,0,0) because the max of the first is 1

    Args:
        requirements (list): buildings we need to include

    Returns:
        tuple: 3 elements:
                1 - block_id of the best place
                2 - the actual block
                3 - the distances you would need to travel
    """
    distances = [find_distance(r) for r in requirements]
    low = [len(blocks)] * len(blocks[0])
    low_idx = None
    for idx, x in enumerate(zip(*distances)):
        if sum(x) <= sum(low) and max(x) < max(low):
            low, low_idx = x, idx

    return low_idx, blocks[low_idx], low


def main():
    block_id, block, walking_distance = find_best_place(my_requirements)
