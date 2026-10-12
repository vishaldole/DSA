class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = len(s)-1
        cnt = 0
        for i in range(n, -1, -1):
            if s[i] != ' ':
                cnt += 1
            elif cnt > 0:
                break
        
        return cnt