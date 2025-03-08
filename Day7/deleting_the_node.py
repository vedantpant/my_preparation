class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


def delete_head(head):

    if head is None:
        return None

    temp = head

    head = head.next

    del temp

    return head

def print_list(curr):

    while curr:
        print(curr.data, end=" ")
        curr = curr.next

if __name__ == "__main__":
    head = Node(1)
    head.next = Node(12)
    head.next.next = Node(13)
    head.next.next.next = Node(14)
    head = delete_head(head)
    print_list(head)