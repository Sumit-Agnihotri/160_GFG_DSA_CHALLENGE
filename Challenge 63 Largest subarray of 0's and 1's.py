arr = [1, 0, 1, 1, 1, 0, 0]

class Solution:
    def maxLen(self, arr):
        mp = {}
        preSum = 0
        res = 0
        for i in range(len(arr)):
            preSum += -1 if arr[i] == 0 else 1
            if preSum == 0:
                res = i + 1
            if preSum in mp:
                res = max(res, i - mp[preSum])
            else:
                mp[preSum] = i
        return res

s = Solution()
print(s.maxLen(arr))  # Output: 6