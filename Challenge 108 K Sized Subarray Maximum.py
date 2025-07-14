arr = [1, 2, 3, 1, 4, 5, 2, 3, 6]
k = 3

from collections import deque
class Solution:
    def maxOfSubarrays(self, arr, k):
        d, r = deque(), []
        for i in range(len(arr)):
            if d and d[0] <= i - k: d.popleft()
            while d and arr[d[-1]] < arr[i]: d.pop()
            d.append(i)
            if i >= k - 1: r.append(arr[d[0]])
        return r

s = Solution()
result = s.maxOfSubarrays(arr, k)
print(result)  # Output: [3, 3, 4, 5, 5, 5, 6]