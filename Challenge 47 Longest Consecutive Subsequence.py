arr = [2, 6, 1, 9, 4, 5, 3]

class Solution:
    def longestConsecutive(self,arr):
        s = set()
        ans = 0
        n = len(arr)
        for ele in arr:
            s.add(ele)
        for i in range(n):
            if (arr[i] - 1) not in s:
                j = arr[i]
                while j in s:
                    j += 1
                ans = max(ans, j - arr[i])
        return ans

s = Solution()
print(s.longestConsecutive(arr)) # Output: 6