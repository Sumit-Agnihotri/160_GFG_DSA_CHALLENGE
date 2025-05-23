arr = [4, 6, 3, 7]

class Solution:
    def countTriangles(self, arr):
        res = 0
        arr.sort()
        for i in range(2, len(arr)):
            left, right = 0, i - 1
            while left < right:
                if arr[left] + arr[right] > arr[i]:
                    res += right - left
                    right -= 1
                else:
                    left += 1
        return res

s = Solution()
print(s.countTriangles(arr)) # Output: 3