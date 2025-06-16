arr = [1,4,3,2,6,5]
class Solution:
    def reverseArray(self, arr):
        left = 0
        right = len(arr) - 1
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr
s = Solution()
print(s.reverseArray(arr))
print(arr)
