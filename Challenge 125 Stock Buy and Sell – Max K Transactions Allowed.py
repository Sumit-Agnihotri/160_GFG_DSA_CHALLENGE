prices = [10, 22, 5, 80]
k = 2

class Solution:
    def maxProfit(self, prices, k):
        n = len(prices)
        if n == 0 or k == 0:
            return 0
        if k >= n // 2:
            return sum(max(prices[i+1] - prices[i], 0) for i in range(n-1))
        
        dp = [[0]*n for _ in range(k+1)]
        for t in range(1, k+1):
            max_diff = -prices[0]
            for d in range(1, n):
                dp[t][d] = max(dp[t][d-1], prices[d] + max_diff)
                max_diff = max(max_diff, dp[t-1][d] - prices[d])
        return dp[k][n-1]

s = Solution()
print(s.maxProfit(prices, k))  # Output: 87