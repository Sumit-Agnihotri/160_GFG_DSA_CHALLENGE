arr = [1, 3, 2, 3, 4]

class Solution:
    def findDuplicate(self, arr):
        return sum(arr) - (len(arr) - 1) * len(arr) // 2

s = Solution()
print(s.findDuplicate(arr)) # Output: 3