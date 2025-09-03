txt = "abcab"
pat = "ab"

class Solution:
    def search(self, pat, txt):
        ans = []
        n, m = len(txt), len(pat)
        for i in range(n - m + 1):
            if txt[i:i+m] == pat:
                ans.append(i)
        return ans
    
s = Solution()
result = s.search(pat, txt)
print(result)  # Output: [0, 2] (the pattern "ab" is found at indices 0 and 2 in the text "abcab")