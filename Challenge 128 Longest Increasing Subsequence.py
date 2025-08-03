arr = [5, 8, 3, 7, 9, 1]

from bisect import bisect_left
class Solution:
    def lis(self, arr):
        r = []
        for x in arr:
            i = bisect_left(r, x)
            if i == len(r): r+=[x]
            else: r[i]=x
        return len(r)

s = Solution()
print(s.lis(arr))  # Output: 3