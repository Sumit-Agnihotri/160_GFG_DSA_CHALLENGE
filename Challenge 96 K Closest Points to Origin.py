points = [[1, 3], [-2, 2], [5, 8], [0, 1]]
k = 2

from heapq import nsmallest
from typing import List

class Solution:
    def k_closest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return nsmallest(k, points, key = lambda p: p[0] ** 2 + p[1] ** 2)

s = Solution()
print(s.k_closest(points, k))  # Output: [[0, 1], [-2, 2]]