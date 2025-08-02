arr = [6, 5, 5, 7, 4]

class Solution:  
    def findMaxSum(self,arr):
        p1 = p2 = 0
        for x in arr:
            p2, p1 = p1, max(p1, p2 + x)
        return p1

s = Solution()
print(s.findMaxSum(arr))  # Output: 15