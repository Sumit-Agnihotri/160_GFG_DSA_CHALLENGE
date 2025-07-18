s1 = "ABCDGH"
s2 = "AEDFHR"

class Solution:
    def lcs(self, s1, s2):
        n, m = len(s1), len(s2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(n):
            for j in range(m):
                if s1[i] == s2[j]:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                else:
                    dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
        return dp[n][m]

s = Solution()
print(s.lcs(s1, s2))  # Output: 3 (LCS is "ADH")