# using python built-in function
class Solution:
    def findWordsContaining(self, words, x: str):
        n = len(words)
        res = []
        for i in range(n):
            if x in words[i]:
                res.append(i)
        
        return res

# without using built-in function
class Solution:
    def findWordsContaining(self, words, x: str):
        n = len(words)
        res = []
        for i in range(n):
            for j in range(len(words[i])):
                if words[i][j] == x:
                    res.append(i)
                    break
        
        return res