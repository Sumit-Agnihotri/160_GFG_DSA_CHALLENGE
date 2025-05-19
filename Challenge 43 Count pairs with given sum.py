arr = [1, 5, 7, -1, 5]
target = 6 

import math

class Solution:
    def countPairs(self,arr, target):
            freq = {}
            count = 0
            for i in range(len(arr)):
                if (target - arr[i]) in freq:
                    count += freq[target - arr[i]]
                freq[arr[i]] = freq.get(arr[i], 0) + 1
            return count

s = Solution()
result = s.countPairs(arr, target)
print(result) # Output: 3