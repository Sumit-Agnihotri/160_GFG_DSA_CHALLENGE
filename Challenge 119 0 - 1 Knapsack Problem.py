W = 4
val = [1, 2, 3]
wt = [4, 5, 1]

class Solution:
    def knapsack(self, w_capacity, val, wt):
        n = len(val)
        dp = [0] * (w_capacity + 1)
        for i in range(n):
            for w in range(w_capacity, wt[i] - 1, -1):
                dp[w] = max(dp[w], val[i] + dp[w - wt[i]])
        return dp[w_capacity]

s = Solution()
print(s.knapsack(W, val, wt))  # Output: 3