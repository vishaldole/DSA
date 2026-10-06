class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        sentinal = ListNode()
        sentinal.next = head

        size = 0
        while head:
            size += 1
            head = head.next
        
        prev = sentinal
        prevPos = size-n
        for _ in range(prevPos):
            prev = prev.next
        
        prev.next = prev.next.next

        return sentinal.next