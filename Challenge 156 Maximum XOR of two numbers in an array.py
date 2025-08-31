arr = [25, 10, 2, 8, 5, 3]

class Solution:
    def maxXor(self, arr):
        ans = 0
        mask = 0
        for i in range(31, -1, -1):
            mask |= 1 << i
            s = {num & mask for num in arr}
            temp = ans | (1 << i)
            if any((temp ^ p) in s for p in s):
                ans = temp
        return ans

sol = Solution()
print(sol.maxXor(arr)) # Output: 28