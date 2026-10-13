#using built in function
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        n = len(stones)
        cnt = 0
        for i in range(n):
            if stones[i] in jewels:
                cnt += 1
        
        return cnt

#without using built in function , using nested loop
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        n = len(stones)
        cnt = 0
        for i in range(n):
            for j in range(len(jewels)):
                if jewels[j] == stones[i]:
                    cnt += 1
                    break
        return cnt

#using a set
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        s = set()
        cnt = 0

        for i in range(len(jewels)):
            s.add(jewels[i])

        for i in range(len(stones)):
            if stones[i] in s:
                cnt += 1
        
        return cnt
