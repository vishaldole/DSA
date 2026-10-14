#using map
class Solution:
    def maxFreqSum(self, s: str) -> int:
        #store all the values with freq in a map
        mp = {} 
        for ch in s:
            mp[ch] = mp.get(ch, 0) + 1

        #find the max vowel and consonant inside the map
        vowel = 0
        consonant = 0
        for key in mp.keys():
            if key in "aeiou":
                vowel = max(vowel, mp[key])
            else:
                consonant = max(consonant, mp[key])
        
        return vowel + consonant