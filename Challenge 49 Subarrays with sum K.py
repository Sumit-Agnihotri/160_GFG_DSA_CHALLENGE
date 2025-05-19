arr = [10, 2, -2, -20, 10]
k = -10

class Solution:
    def countSubarrays(self, arr, k):
        prefixSums = {}
        res = 0
        currSum = 0
        for val in arr:
            currSum += val
            if currSum == k:
                res += 1
            if currSum - k in prefixSums:
                res += prefixSums[currSum - k]
            prefixSums[currSum] = prefixSums.get(currSum, 0) + 1
        return res
    
s = Solution()
print(s.countSubarrays(arr, k)) # Output: 3