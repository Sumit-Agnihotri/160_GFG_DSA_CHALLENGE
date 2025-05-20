arr = [7, 2, 5, 3]
target = 8

import math
class Solution:
    def countPairs(self, arr, target):
        count = 0
        arr.sort()
        n = len(arr)
        l = 0
        r = n - 1
        while l < r:
            if arr[l] + arr[r] < target:
                count += (r - l)
                l += 1
            else:
                r -= 1
        return count

s = Solution()
print(s.countPairs(arr, target)) # Output: 2