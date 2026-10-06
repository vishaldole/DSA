class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        # add sentinal node at start
        sentinal = ListNode()
        sentinal.next = head

        # move my first pointer ahead by n
        first = sentinal
        
        for _ in range(n):
            first = first.next
        
        # move both pointers until first reach the last node
        second = sentinal
        while first.next:
            second = second.next
            first = first.next

        second.next = second.next.next

        return sentinal.next