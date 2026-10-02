class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    def removeElements(head, val: int):
            sentinal = ListNode()
            prev = sentinal
            prev.next = head
            # curr = head

            while prev and prev.next:
                if prev.next.val == val:
                    prev.next = prev.next.next
                else:
                    prev = prev.next
            
            return sentinal.next