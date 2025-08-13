s = "acbbcc"

class Solution:
    def maxPartitions(self , s):
        last = {c: i for i, c in enumerate(s)}
        ans = end = 0
        for i, c in enumerate(s):
            end = max(end, last[c])
            if i == end:
                ans += 1
        return ans

sol = Solution()
print(sol.maxPartitions(s))  # Output: 2