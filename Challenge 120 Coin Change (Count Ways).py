coins = [1, 2, 3]
sum = 4

class Solution:
    def count(self, coins, sum):
        dp = [0]*(sum+1)
        dp[0]=1
        for c in coins:
            for i in range(c,sum+1):
                dp[i]+=dp[i-c]
        return dp[sum]

s = Solution()
print(s.count(coins, sum)) # Output: 4