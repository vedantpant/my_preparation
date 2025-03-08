class Node:

    def __init__(self, new_data):
        self.data = new_data
        self.next = None

def insert_at_front(head, new_data):
    new_node = Node(new_data)

    new_node.next = head

    return new_node


def print_list(head):

    curr = head

    while curr is not None:
        print(f"{curr.data}", end=" ")

        curr = curr.next

    print()

if __name__ == "__main__":
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)

    print("original linked list:", end=" ")
    print_list(head)

    print("after inserting nodes at the front:", end=" ")
    data = 1
    head = insert_at_front(head, data)

    print_list(head)