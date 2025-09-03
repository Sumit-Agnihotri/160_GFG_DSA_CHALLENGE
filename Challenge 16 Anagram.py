s1 = "geeks"
s2 = "kseeg"

class Solution:
    
    #Function is to check whether two strings are anagram of each other or not.
    def areAnagrams(self, s1, s2):
        charCount = {}
        
        for ch in s1:
            charCount[ch] = charCount.get(ch, 0) + 1
        for ch in s2:
            charCount[ch] = charCount.get(ch, 0) - 1
            
        for value in charCount.values():
            if value != 0:
                return False
        
        return True

s = Solution()
print(s.areAnagrams(s1, s2))