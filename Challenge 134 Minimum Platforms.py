arr = [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1200, 1120, 1130, 1900, 2000]

class Solution:
    def minimumPlatform(self,arr,dep):
        arr.sort()
        dep.sort()
        i = j = plat = ans = 0
        while i < len(arr) and j < len(dep):
            if arr[i] <= dep[j]:
                plat += 1
                ans = max(ans, plat)
                i += 1
            else:
                plat -= 1
                j += 1
        return ans

s = Solution()
print(s.minimumPlatform(arr, dep)) # Output: 3