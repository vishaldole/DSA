class Solution:
    def balancedStringSplit(self, s: str) -> int:
        cnt = 0
        balStr = 0

        for i in range(len(s)):
            if s[i] == 'R':
                cnt -= 1
            else:
                cnt += 1
            
            if cnt == 0:
                balStr += 1
        
        return balStr