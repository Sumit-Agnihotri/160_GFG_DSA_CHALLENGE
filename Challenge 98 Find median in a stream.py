arr = [5, 15, 1, 3, 2, 8]

import heapq

class Solution:
    def getMedian(self, arr):
        low, high, res = [], [], []
        for x in arr:
            if not low or x <= -low[0]:
                heapq.heappush(low, -x)
            else:
                heapq.heappush(high, x)
            if len(low) > len(high) + 1:
                heapq.heappush(high, -heapq.heappop(low))
            if len(high) > len(low):
                heapq.heappush(low, -heapq.heappop(high))
            if len(low) > len(high):
                res.append(float(-low[0]))
            else:
                res.append((-low[0] + high[0]) / 2)
        return res

s = Solution()
print(s.getMedian(arr))  # Output: [5.0, 10.0, 5.0, 4.0, 3.0, 3.5]