W = 4
val = [1, 2, 3]
wt = [4, 5, 1]

class Solution:
    def knapsack(self, W, val, wt):
        n=len(val)
        dp=[0]*(W+1)
        for i in range(n):
            for w in range(W,wt[i]-1,-1):
                dp[w]=max(dp[w],val[i]+dp[w-wt[i]])
        return dp[W]

s = Solution()
print(s.knapsack(W, val, wt))  # Output: 3