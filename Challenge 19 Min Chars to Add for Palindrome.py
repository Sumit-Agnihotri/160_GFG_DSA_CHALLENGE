class Solution:
    def minChar(self, s):
        rev_s = s[::-1]
        combined = s + "$" + rev_s
        n = len(combined)
        lps = [0] * n
        
        for i in range(1, n):
            j = lps[i - 1]
            while j > 0 and combined[i] != combined[j]:
                j = lps[j - 1]
            if combined[i] == combined[j]:
                j += 1
            lps[i] = j
        return len(s) - lps[-1]
    
s = Solution()
print(s.minChar("abc"))  # Output: 2 (add "a" and "b" to make it "abcba")