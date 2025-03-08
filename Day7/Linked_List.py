class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# def traverseList(head):
#
#     while head is not None:
#         print(head.data, end=' ')
#         head = head.next
#
#     print()

def traverseList(head):

    if head is None:
        print()
        return

    print(head.data, end=' ')
    traverseList(head.next)

def main():

    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)
    head.next.next.next = Node(40)

    traverseList(head)

if __name__ == '__main__':
    main()  