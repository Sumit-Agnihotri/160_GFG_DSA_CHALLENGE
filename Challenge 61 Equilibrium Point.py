arr = [1, 2, 0, 3]

class Solution:
    def findEquilibrium(self, arr):
        n = len(arr)
        total_sum = sum(arr)
        left_sum = 0
        for i in range(n):
            total_sum -= arr[i]
            if left_sum == total_sum:
                return i
            else:
                left_sum += arr[i]
        return -1

s = Solution()
result = s.findEquilibrium(arr)
print(result)  # Output: 2