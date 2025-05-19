arr = [2, 3, -8, 7, -1, 2, 3]

class Solution:
    def maxSubArraySum(self, arr):
        res = arr[0]
        max_ending = arr[0]
        
        for i in range(1, len(arr)):
            max_ending = max(max_ending + arr[i], arr[i])
            res = max(res, max_ending)
        return res
    
s = Solution()
print(s.maxSubArraySum(arr))  # Output: 11 Time Complexity: O(n) Space Complexity: O(1)