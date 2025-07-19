s = "bbabcbcab"

class Solution:
    def longest_palin_subseq(self, s):
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n): dp[i][i] = 1
        for l in range(2, n + 1):
            for i in range(n - l + 1):
                j = i + l - 1
                if s[i] == s[j]: dp[i][j] = 2 + dp[i + 1][j - 1]
                else: dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        return dp[0][n - 1]

sol = Solution()
print(sol.longest_palin_subseq(s))  # Output: 7