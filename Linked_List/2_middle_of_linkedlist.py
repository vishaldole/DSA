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

    
def traverse(ptr):
                    curr = ptr
                    print('middle of the the list starts: ')
                    while curr is not None:
                        print(f'{curr.val}->', end='')
                        curr = curr.next
                    print('None')

def middleNode(head: ListNode | None) -> ListNode | None:
            slow = head
            fast = head

            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next

            traverse(slow)
            return slow
obj = MyLinkedList()
obj.addAtHead(6)
obj.addAtHead(5)
obj.addAtHead(4)
obj.addAtHead(3)
obj.addAtHead(2)
obj.addAtHead(1)
obj.traverseLL()
middleNode(obj.head)