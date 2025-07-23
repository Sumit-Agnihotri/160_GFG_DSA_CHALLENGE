n = 1

class Solution:
    def count_ways(self, n):
        if n<= 2: return n
        a, b = 1, 2
        for _ in range(3, n+1):
            a, b = b, a+b
        return b

s = Solution()
print(s.count_ways(n))  # Output: 1