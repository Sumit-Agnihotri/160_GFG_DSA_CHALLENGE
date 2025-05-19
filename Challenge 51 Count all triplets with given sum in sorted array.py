arr = [-3, -1, -1, 0, 1, 2]
target = -2

class Solution:
    def countTriplets(self, arr, target):
        n = len(arr)
        res = 0
        for i in range(n - 2):
            left = i + 1
            right = n - 1
            while left < right:
                sum = arr[left] + arr[right] + arr[i]
                if sum < target:
                    left += 1
                elif sum > target:
                    right -= 1
                else:
                    ele1 = arr[left]
                    ele2 = arr[right]
                    
                    count1 = 0
                    count2 = 0
                    while left <= right and arr[left] == ele1:
                        left += 1
                        count1 += 1
                    while left <= right and arr[right] == ele2:
                        right -= 1
                        count2 += 1
                    if ele1 == ele2:
                        res += (count1 * (count1 - 1)) // 2
                    else:
                        res += (count1 * count2)
        return res

s = Solution()
print(s.countTriplets(arr, target)) # Output: 4