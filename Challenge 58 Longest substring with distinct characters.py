s = "geeksforgeeks"

class Solution:
    def longestUniqueSubstr(self, s):
        n = len(s)
        res = 0
        lastIndex = [-1] * 26
        start = 0
        for end in range(n):
            start = max(start, lastIndex[ord(s[end]) - ord("a")] + 1)
            res = max(res, end - start + 1)
            lastIndex[ord(s[end]) - ord("a")] = end
        return res
    
s = Solution()
print(s.longestUniqueSubstr("geeksforgeeks")) # Output: 7