s = "ilike"
dictionary = ["i", "like", "gfg"]

class Solution:
    def wordBreak(self, s, dictionary):
        D, dp = set(dictionary), {}
        def f(w):
            if w in dp:return dp[w]
            if not w:return True
            dp[w] = any(w[:i] in D and f(w[i:]) for i in range(1, len(w) + 1))
            return dp[w]
        return f(s)

sol = Solution()
print(sol.wordBreak(s, dictionary))  # Output: True