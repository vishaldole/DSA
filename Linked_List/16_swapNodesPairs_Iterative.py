# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    # def swapPairs(self, head: ListNode | None) -> ListNode | None:
    #     if not head or not head.next:
    #         return head
        
    #     dummy = ListNode()
    #     prev = dummy
    #     curr = head
    #     while curr and curr.next:
    #         tmp = curr.next
    #         curr.next = curr.next.next
    #         tmp.next = curr
    #         prev.next = tmp
    #         prev = curr
    #         curr = curr.next
        
    #     return dummy.next
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        dummy = ListNode()
        prev = dummy
        prev.next = head

        while prev.next and prev.next.next:
            first = prev.next
            second = first.next

            prev.next = second
            first.next = second.next
            second.next = first

            prev = first

        return dummy.next