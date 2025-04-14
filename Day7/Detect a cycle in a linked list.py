from selenium.webdriver.common.devtools.v131.dom import get_querying_descendants_for_container


class Listnode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def has_cycle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False

node1 = Listnode(1)
node2 = Listnode(2)
node3 = Listnode(3)
node4 = Listnode(4)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2

print(has_cycle(node1))
