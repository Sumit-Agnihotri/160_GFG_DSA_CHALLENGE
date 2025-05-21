arr = [10, 30, 20, 5]
target = 25

class Solution:
    def sumClosest(self, arr, target):
        arr.sort()
        n = len(arr)
        res = []
        minDiff = float("inf")
        left = 0
        right = n - 1
        while left < right:
            sum = arr[left] + arr[right]
            if abs(sum - target) < minDiff:
                minDiff = abs(sum - target)
                res = [arr[left], arr[right]]
            elif abs(sum - target) == minDiff:
                if (arr[right] - arr[left]) > (res[1] - res[0]):
                    res = [arr[left], arr[right]]
            if sum < target:
                left += 1
            elif sum > target:
                right -= 1
            else:
                break
        return res
    
s = Solution()
result = s.sumClosest(arr, target)
print(result) # Output: [5, 20]