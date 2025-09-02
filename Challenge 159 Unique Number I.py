arr = [1, 2, 1, 5, 5]

class Solution:
    def findUnique(self, arr):
        ans = 0
        for num in arr:
            ans ^= num
        return ans

s = Solution()
print(s.findUnique(arr)) # Output: 2