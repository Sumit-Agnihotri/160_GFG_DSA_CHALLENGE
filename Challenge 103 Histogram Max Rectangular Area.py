arr = [60, 20, 50, 40, 10, 50, 60]

class Solution:
    def getMaxArea(self,arr):
        arr.append(0)
        s, m = [-1], 0
        for i in range(len(arr)):
            while arr[s[-1]] > arr[i]:
                h = arr[s.pop()]
                w = i - s[-1] - 1
                m = max(m, h * w)
            s.append(i)
        return m

s = Solution()
print(s.getMaxArea(arr))  # Output: 100