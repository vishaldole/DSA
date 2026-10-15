class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        n = len(s)
        j = 2 * k
        res = ''
        for i in range(0, n, j):
            start = i
            if i + k - 1 < n:
                end = i + k -1
            else:
                end = n-1

            while start <= end:
                res += s[end]
                end -= 1
            res += s[i+k:i+j]
        return res  

## USING PYTHON FUNCTIONALITY TO CONVERT STRING TO LIST AND AGAIN CONVERT LIST TO STRING BEFORE RETURNING THE RESULT
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)
        n = len(s)
        j = 2 * k
        for i in range(0, n, j):
            start = i
            if i + k - 1 < n:
                end = i + k -1
            else:
                end = n-1

            while start <= end:
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1
        s = ''.join(s)
        return  s