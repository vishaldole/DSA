class ListNode:
    def __init__(self, val: int) -> None:
        self.val = val
        self.next = None

    
class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def addAtHead(self, val: int) -> None:
        newNode = ListNode(val)
        newNode.next = self.head
        self.head = newNode
        self.size += 1 

    def traverseLL(self):
                curr = self.head
                while curr is not None:
                    print(f'{curr.val}->', end='')
                    curr = curr.next
                print('None')

## Approach 1 : Using array
# def palindromeLL(head):
#     curr = head
#     arr = []
#     print('in the loop')
#     while curr:
#         arr.append(curr.val)
#         curr = curr.next

#     n = len(arr)
#     mid =  n // 2

#     for i in range(mid):
#         if arr[i] != arr[n-i-1]:
#             return False
#     return True


## Approach 2 : Without using extra space
def palindromeLL(head: ListNode | None) -> bool:
        #finding middle of the linked list
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        #reverse the 2nd half of the list
        prev = None
        curr = slow

        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        #checking the same element from both the list 
        firstList = head
        secondList = prev

        while secondList:
            if firstList.val != secondList.val:
                return False
            firstList = firstList.next
            secondList = secondList.next
        return True

obj = MyLinkedList()
obj.addAtHead(1)
obj.addAtHead(2)
obj.addAtHead(3)
obj.addAtHead(2)
# obj.addAtHead(2)
obj.addAtHead(1)
obj.traverseLL()
print(f'Given Linked List is Palindrome : {palindromeLL(obj.head)}')
    