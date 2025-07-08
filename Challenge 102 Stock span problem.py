arr = [100, 80, 60, 70, 60, 75, 85]

class Solution:
    def calculateSpan(self, arr):
        s, r = [], []
        for i, x in enumerate(arr):
            while s and arr[s[-1]] <= x: s.pop()
            r.append(i - s[-1] if s else i + 1)
            s.append(i)
        return r

s = Solution()
print(s.calculateSpan(arr))  # Output: [1, 1, 1, 2, 1, 4, 6]