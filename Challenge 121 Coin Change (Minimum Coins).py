coins = [25, 10, 5]
s = 30

class Solution:
	def min_coins(self, coins, s):
		dp = [0] + [float("inf")] * s
		for i in range(1, s + 1):
			for c in coins:
				if i >= c:
					dp[i] = min(dp[i], dp[i - c] + 1)
		return -1 if dp[s] == float("inf") else dp[s]

sol = Solution()
print(sol.min_coins(coins, s))  # Output: 2