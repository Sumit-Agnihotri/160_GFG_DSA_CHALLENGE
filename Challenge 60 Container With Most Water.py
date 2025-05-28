arr = [1, 5, 4, 3]

class Solution:
    def maxWater(self, arr):
        left = 0
        right = len(arr) - 1
        res = 0
        while left < right:
            water = min(arr[left], arr[right]) * (right - left)
            res = max(res, water)
            if arr[left] < arr[right]:
                left += 1
            else:
                right -= 1
        return res

s = Solution()
print(s.maxWater(arr))  # Output: 6