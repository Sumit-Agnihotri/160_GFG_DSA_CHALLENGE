arr = [2, 3, 2]

class Solution:
    def maxValue(self, arr):
        def f(a):
            x=y=0
            for n in a: x, y = y, max(y, x+n)
            return y
        return max(arr[0], f(arr[:-1]), f(arr[1:])) if len(arr) > 1 else arr[0]

s = Solution()
print(s.maxValue(arr))  # Output: 3