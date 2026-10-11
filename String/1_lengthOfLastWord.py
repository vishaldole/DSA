class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l = len(s) -1
        # trim all spaces at the end
        while l >= 0 and s[l] == ' ':
            l -= 1
        # count the character till we encounter the space
        cnt = 0
        while l >= 0 and s[l] != ' ':
            cnt += 1
            l -= 1

        return cnt