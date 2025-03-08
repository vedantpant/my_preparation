class Node:

    def __init__(self,new_data):
        self.data = new_data
        self.next = None

def search_key(head, key):

    curr = head

    while curr is not None:

        if curr.head == key:
            return True

        curr = curr.next

    return False

if __name__ == '__main__':

    head = Node(14)
    head.next = Node(21)
    head.next.next = Node(13)
    head.next.next.next = Node(30)
    head.next.next.next.next = Node(10)

    key = 14

    if search_key(head, key):
        print("Key found")
    else:
        print("key not found")

