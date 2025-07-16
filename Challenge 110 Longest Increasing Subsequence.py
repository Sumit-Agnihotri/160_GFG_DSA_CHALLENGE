arr = [5, 8, 3, 7, 9, 1]

from bisect import bisect_left

class Solution:
    def lis(self, arr):
        dp = []
        for x in arr:
            i = bisect_left(dp, x)
            if i == len(dp): dp.append(x)
            else: dp[i] = x
        return len(dp)

s = Solution()
print(s.lis(arr))  # Output: 3