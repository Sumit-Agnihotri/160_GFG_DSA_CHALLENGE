arr = [-1, 1, 5, 5, 7]
target = 6

class Solution:
    def countPairs (self, arr, target) :
        res = 0
        n = len(arr)
        left = 0
        right  = n - 1
        while left < right:
            if arr[left] + arr[right] < target:
                left += 1
            elif arr[left] + arr[right] > target:
                right -= 1
            else:
                count1 = 0
                count2 = 0
                element1 = arr[left]
                element2 = arr[right]
                while left <= right and arr[left] == element1:
                    left += 1
                    count1 += 1
                while left <= right and arr[right] == element2:
                    right -= 1
                    count2 += 1
                    
                if element1 == element2:
                    res += (count1 * (count1 - 1)) // 2
                else:
                    res += (count1 * count2)
                        
        return res

s = Solution()
print(s.countPairs(arr, target)) # Output: 3