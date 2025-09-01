arr = [1, 2, 3, 5]

class Solution:
    def missingNum(self, arr):
        return (len(arr) + 1) * (len(arr) + 2) // 2 - sum(arr)

s = Solution()
print(s.missingNum(arr))  # Output: 4