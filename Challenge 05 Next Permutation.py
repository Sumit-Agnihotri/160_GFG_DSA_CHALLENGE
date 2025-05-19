arr = [2, 4, 1, 7, 5, 0]

class Solution:
    def nextPermutation(self, nums):
        n = len(nums)
        pivot= -1
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i +1]:
                pivot = i
                break
        if pivot == -1:
            nums.reverse()
            return
        
        for i in range(n - 1, pivot, -1):
            if nums[i] > nums[pivot]:
                nums[i], nums[pivot] = nums[pivot], nums[i]
                break
        
        left, right = pivot + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        return nums
s = Solution()
result = s.nextPermutation(arr)
print(result)