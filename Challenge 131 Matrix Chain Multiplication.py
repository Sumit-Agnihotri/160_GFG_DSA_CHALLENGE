arr = [2, 1, 3, 4]

class Solution:
    def matrixMultiplication(self, arr):
        n = len(arr)
        dp = [[0] * n for _ in range(n)]
        for l in range(2, n):
            for i in range(n-l+1):
                j = i+l-1
                dp[i][j] = min(dp[i][k] + dp[k+1][j] + arr[i-1] * arr[k] * arr[j] for k in range(i, j))
        return dp[1][n-1]

s = Solution()
print(s.matrixMultiplication(arr))  # Output: 20