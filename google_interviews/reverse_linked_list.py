"""
https://youtu.be/vHKzIPwWQkg

Pretty happy with my solution on this one. I was able to get a working solution
in under an hour without any previous knowledge on the subject. 

I would change a few things, but I am overall satisfied that my solution works. 
"""


class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def get_head_node():
    n1 = LinkedList(10)
    n2 = LinkedList(12)
    n3 = LinkedList(4)
    n4 = LinkedList(7)
    n5 = LinkedList(100)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = None
    return n1


def output_linked_list(node: LinkedList) -> None:
    while node is not None:
        print(f"{node.value} -> ", end="")
        node = node.next
    print("None", end="\n\n")


def get_last_node(node: LinkedList) -> LinkedList:
    while node.next is not None:
        node = node.next
    return node


def reverse_linked_list(node: LinkedList):
    node_1 = node
    node_2 = node.next
    counter = 0
    while node_2 is not None:
        # make our transition node
        transition_node = node_2.next
        if counter == 0:
            node_1.next = None
            counter += 1
        node_2.next = node_1
        # change the values overwriting them
        node_1 = node_2
        node_2 = transition_node
    return node_1


def main():
    head_node = get_head_node()

    print("--Original List--")
    output_linked_list(head_node)

    head_node = reverse_linked_list(head_node)

    print("--Reversed List--")
    output_linked_list(head_node)


if __name__ == "__main__":
    main()
