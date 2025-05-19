arr = [2, 3, 4, 7, 11]
k = 5

from typing import List

class Solution:
    def kthMissing(self, arr, k):
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            missing = arr[mid] - (mid + 1)
            if missing < k:
                left = mid + 1
            else:
                right = mid - 1
        return left + k

s = Solution()
print(s.kthMissing(arr, k))  # Output: 9