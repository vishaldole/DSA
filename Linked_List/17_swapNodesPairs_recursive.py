# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# class Solution:
#     def swapNodes(self, curr: ListNode | None) -> ListNode | None:
#         tmp = curr.next
#         curr.next = tmp.next
#         tmp.next = curr
        
#         return tmp

#     def swapPairs(self, head: ListNode | None) -> ListNode | None:
#         dummy = ListNode()
#         prev = dummy
#         prev.next = head

#         while prev.next and prev.next.next:
#            curr = prev.next
#            prev.next = self.swapNodes(curr)
#            prev = prev.next.next

#         return dummy.next

class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
       if not head or not head.next:
            return head

       first = head
       second = head.next

       first.next = self.swapPairs(second.next)
       second.next = first

       return second