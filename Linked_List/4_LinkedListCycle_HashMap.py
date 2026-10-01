class ListNode:
    def __init__(self, val: int) -> None:
        self.val = val
        self.next = None

def hasCycle(self, head: ListNode) -> bool:
    s = set()
    curr = head

    while curr:
        if curr in s:
            return True
        else:
            s.add(curr)
            curr = curr.next
    return False