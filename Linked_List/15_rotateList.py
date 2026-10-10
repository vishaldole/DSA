# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
        if not head or not head.next or k == 0:
            return head
        
        #calculate len
        len  = 0
        curr = head
        while curr:
            len += 1
            curr = curr.next

        k = k % len
        s = head
        f = head
                
        for _ in range(k):
            f = f.next
        
        while f.next:
            s = s.next
            f = f.next
        
        f.next = head
        newHead = s.next
        s.next = None

        return newHead