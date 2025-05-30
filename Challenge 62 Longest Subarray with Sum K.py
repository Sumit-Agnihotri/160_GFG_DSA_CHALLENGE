arr = [10, 5, 2, 7, 1, -10]
k = 15

class Solution:
    def longestSubarray(self, arr, k):
        mp = {}
        res = 0
        prefSum = 0
        for i in range(len(arr)):
            prefSum += arr[i]
            if prefSum == k:
                res = i + 1
            elif(prefSum - k) in mp:
                res = max(res, i - mp[prefSum - k])
            if prefSum not in mp:
                mp[prefSum] = i
        return res

s = Solution()
print(s.longestSubarray(arr, k))  # Output: 6