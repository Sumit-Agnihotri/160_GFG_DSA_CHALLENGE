arr = [0, -1, 2, -3, 1]

import math

class Solution:
    def findTriplets(self, arr):
        resSet = set()
        n = len(arr)
        mp = {}
        for i in range(n):
            for j in range(i + 1, n):
                s = arr[i] + arr[j]
                if s not in mp:
                    mp[s] = []
                mp[s].append((i, j))
        
        for i in range(n):
            rem = -arr[i]
            if rem in mp:
                for p in mp[rem]:
                    if p[0] != i and p[1] != i:
                        curr = sorted([i, p[0], p[1]])
                        resSet.add(tuple(curr))
        
        return [list(triplet) for triplet in resSet]

s = Solution()
print(s.findTriplets(arr)) # Output: [[0, 1, 4], [2, 3, 4]]