from dataclasses import dataclass

import math


def t2_lvl(i):
    return int(math.log2(i + 1)) if i > 0 else 0


def t2_i2base(i):
    # @meta  map the global idx to the local idx (ie. the idx of elem 0 in the lvl at idx @i)
    return (1 << t2_lvl(i)) - 1


def t2_l2base(l):
    # @meta  map the lvl        to the local idx (ie. the idx of elem 0 in lvl @l)
    return (1 << l) - 1


@dataclass
class BinaryTreeNode:
    data: int
    left = None
    right = None


def invert_binary_tree(root):
    """thank you github co-pilot for the solutio"""
    if root is None:
        return None
    left = invert_binary_tree(root.left)
    right = invert_binary_tree(root.right)
    root.left = right
    root.right = left
    return root


def show(tree: BinaryTreeNode):
    """
    https://stackoverflow.com/questions/34012886/print-binary-tree-level-by-level-in-python
    """
    # @meta  2-pass fn. in the 1st pass we compute the height
    if not tree:
        return
    q0 = []  # perm queue
    q1 = []  # temp queue

    # pass 0
    h = 0  # height is the number of lvls
    q0.append((tree, 0))
    q1.append((tree, 0))
    while q1:
        n, i = q1.pop(0)
        h = max(h, t2_lvl(i))
        if n.left:
            l = (n.left, 2 * i + 1)
            q0.append(l)
            q1.append(l)
        if n.right:
            r = (n.right, 2 * i + 2)
            q0.append(r)
            q1.append(r)
    h += 1  # nlvls
    N = 2**h - 1  # nelems (for a perfect tree of this height)
    W = 1  # elem width

    # pass 1
    print(f"\n\x1b[31m{h} \x1b[32m{len(q0)}\x1b[0m")
    print(f"{0:1x}\x1b[91m:\x1b[0m", end="")
    for idx, (n, i) in enumerate(q0):
        l = t2_lvl(i)  # lvl
        b = (1 << l) - 1  # base
        s0 = N // (2 ** (l + 1))
        s1 = N // (2 ** (l + 0))
        s = (
            3 + 1 + s0 + (i - b) * (s1 + 1)
        )  # absolute 1-based position (from the beginning of line)
        w = int(
            2 ** (h - l - 2)
        )  # width (around the element) (to draw the surrounding @-)

        # print(f'{i:2x} {l} {i-b}  {s0:2x} {s1:2x} {s:2x} {w:x}  {n.v:02x}')
        if 0 < idx and t2_lvl(q0[idx - 1][1]) != l:
            print(f"\n{l:1x}\x1b[91m:\x1b[0m", end="")  # new level: go to the next line
        print(f"\x1b[{s-w}G{w*'-'}\x1b[1G", end="")
        print(
            f"\x1b[{s}G{n.data:1x}\x1b[1G", end=""
        )  # `\x1b[XG` is an ANSI escape code that moves the cursor to column X
        print(f"\x1b[{s+W}G{w*'-'}\x1b[1G", end="")
    print()


def main():
    root = BinaryTreeNode(1)
    root.left = BinaryTreeNode(2)
    root.right = BinaryTreeNode(3)
    root.left.left = BinaryTreeNode(4)
    root.left.right = BinaryTreeNode(5)
    root.right.left = BinaryTreeNode(6)
    root.right.right = BinaryTreeNode(7)
    root.left.left.left = BinaryTreeNode(8)
    root.left.left.right = BinaryTreeNode(9)
    show(root)
    print("\n\nINVERTED\n\n")
    root = invert_binary_tree(root)
    show(root)
