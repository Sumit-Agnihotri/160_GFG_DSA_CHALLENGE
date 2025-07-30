arr = [1, 5, 11, 5]

class Solution:
    def equalPartition(self, arr):
        sum1 = sum(arr)
        if sum1 % 2: return False
        t = {0}
        for x in arr:
            t |= {x + y for y in t}
        return sum1 // 2 in t

s = Solution()
print(s.equalPartition(arr))  # Output: True