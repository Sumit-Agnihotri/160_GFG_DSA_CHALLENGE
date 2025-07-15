arr = [8, 4, 2, 6, 7]
x = 4 

from collections import deque

class Solution:
    def longestSubarray(self, a, x):
        l = r = 0
        mx, mn = deque(), deque()
        res = st = 0
        while r < len(a):
            while mx and a[r] > a[mx[-1]]: mx.pop()
            while mn and a[r] < a[mn[-1]]: mn.pop()
            mx.append(r)
            mn.append(r)
            while a[mx[0]] - a[mn[0]] > x:
                l += 1
                if mx[0] < l: mx.popleft()
                if mn[0] < l: mn.popleft()
            if r - l + 1 > res: res, st = r - l + 1, l
            r += 1
        return a[st:st + res]

s = Solution()
print(s.longestSubarray(arr, x))  # Output: [4, 2, 6]