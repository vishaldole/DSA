
## Approach 1 : using HashMap
def getIntersectionNode(headA, headB):
        s = set()
        curr = headB

        while curr:
            s.add(curr)
            curr = curr.next
        
        curr = headA
        while curr:
            if curr in s:
                return curr
            curr = curr.next
        return None
## Approach 1 : without using HashMap
def getIntersectionNode(headA, headB):
        #find diffence between len of two list
        lenA = 0
        currA = headA

        while currA:
            lenA += 1
            currA = currA.next
        
        lenB = 0
        currB = headB

        while currB:
            lenB += 1
            currB = currB.next
        
        diff = abs(lenA - lenB)

        # Run the diffence on longer list
        currA = headA
        currB = headB
        if lenA > lenB:
            for _ in range(diff):
                currA = currA.next
        elif lenA < lenB:
            for _ in range(diff):
                currB = currB.next
        # Now, both pointer is standing on same distance from the intersection
        # so, traverse through both list simultanously, till we find the intersection
        while currA and currB:
            if currA == currB:
                return currA
            currA = currA.next
            currB = currB.next
        return None