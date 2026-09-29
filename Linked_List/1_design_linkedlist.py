class Node:
    def __init__(self, val: int) -> None:
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def addAtHead(self, val: int) -> None:
        newNode = Node(val)
        newNode.next = self.head
        self.head = newNode
        self.size += 1 

    def addAtTail(self, val: int) -> None:
        if self.head == None:
            self.head = Node(val)
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = Node(val)
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            print("addAtHead called")
            self.addAtHead(val)

        elif index == self.size:
             print("addAtTail called")
             self.addAtTail(val)

        else:
            newNode = Node(val)
            curr = self.head
            for _ in range(index-1):
                curr = curr.next

            newNode.next = curr.next
            curr.next = newNode
        
        self.size += 1

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        curr = self.head
        for _ in range(index):
            curr = curr.next
        return curr.val

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        if index == 0:
            self.head = self.head.next
        else:
            curr = self.head
            for _ in range(index-1):
                curr = curr.next
            curr.next = curr.next.next
        self.size -= 1
        
    def traverseLL(self):
        curr = self.head
        while curr is not None:
            print(f'{curr.val}->', end='')
            curr = curr.next
        print('None')

obj = MyLinkedList()
obj.addAtHead(10)
# obj.traverseLL()
obj.addAtHead(5)
obj.addAtTail(20)
obj.addAtTail(15)
obj.addAtIndex(3, 4)
obj.traverseLL()
print(f'{obj.get(-4)}')