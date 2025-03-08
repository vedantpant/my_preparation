class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

def append(head, new_data):

    new_node = Node(new_data)

    if head is None:
        return new_node

    last = head

    while last.next:
        last = last.next

    last.next = new_node

    return head

def print_list(node):
    while node:
        print(node.data, end=' ')
        node = node.next