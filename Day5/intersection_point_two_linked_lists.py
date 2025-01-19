class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

    def getIntersectionNode(self, headA, headB):
        l1, l2 = headA, headB
        while l1 != l2:

            l1 = l1.next if l1 else headB
            l2 = l2.next if l2 else headA

        return l1