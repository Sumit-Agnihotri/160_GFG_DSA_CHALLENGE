arr = [3, 34, 4, 12, 5, 2]
sum = 9

class Solution:
    def isSubsetSum (self, arr, s):
        dp = {0}
        for x in arr: dp |= {x + y for y in dp}
        return s in dp

sol = Solution()
print(sol.isSubsetSum(arr, sum))  # Output: True