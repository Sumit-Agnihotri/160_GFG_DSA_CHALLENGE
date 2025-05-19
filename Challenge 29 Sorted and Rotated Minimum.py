arr[] = [5, 6, 1, 2, 3, 4]

class Solution:
    def findMin(self, arr):
        low, high = 0, len(arr) - 1
        while low < high:
            if arr[low] < arr[high]:
                return arr[low]
                
            mid = (low + high) // 2
            
            if arr[mid] > arr[high]:
                low = mid + 1
            else:
                high = mid
        return arr[low]
    
s = Solution()
result = s.findMin(arr)
print("Minimum element in the rotated sorted array is:", result) # Output: 1